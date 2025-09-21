

---

Page 1

---

He et al. 
Chinese Journal of Mechanical Engineering            (2024) 37:9  
https://doi.org/10.1186/s10033-024-00998-7
REVIEW
Open Access
© The Author(s) 2024. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which 
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this 
licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
Chinese Journal of Mechanical Engineering
From Digital Human Modeling to Human 
Digital Twin: Framework and Perspectives 
in Human Factors
Qiqi He1,2†, Li Li3†, Dai Li1,2, Tao Peng1,2*   , Xiangying Zhang1,2, Yincheng Cai1,2, Xujun Zhang2,4 and 
Renzhong Tang1,2 
Abstract 
The human digital twin (HDT) emerges as a promising human-centric technology in Industry 5.0, but challenges 
remain in human modeling and simulation. Digital human modeling (DHM) provides solutions for modeling and sim-
ulating human physical and cognitive aspects to support ergonomic analysis. However, it has limitations in real-time 
data usage, personalized services, and timely interaction. The emerging HDT concept offers new possibilities by inte-
grating multi-source data and artificial intelligence for continuous monitoring and assessment. Hence, this paper 
reviews the evolution from DHM to HDT and proposes a unified HDT framework from a human factors perspective. 
The framework comprises the physical twin, the virtual twin, and the linkage between these two. The virtual twin 
integrates human modeling and AI engines to enable model-data-hybrid-enabled simulation. HDT can potentially 
upgrade traditional ergonomic methods to intelligent services through real-time analysis, timely feedback, and bidi-
rectional interactions. Finally, the future perspectives of HDT for industrial applications as well as technical and social 
challenges are discussed. In general, this study outlines a human factors perspective on HDT for the first time, which 
is useful for cross-disciplinary research and human factors innovation to enhance the development of HDT in industry.
Keywords  Human digital twin, Digital human modeling, Human factors, Human-centric technology
1  Introduction
The symbiotic relationship between humans and emerg-
ing technologies is crucial in the social-technical trans-
formation toward Industry 5.0, given the significant 
value that humans hold in future industrial workplaces 
[1, 2]. Human-cyber-physical systems (HCPS) [3] and 
cyber-physical-social systems (CPSS) [4] are emerg-
ing paradigms that incorporate human factors into 
cyber-physical systems. Basic human needs like safety, 
health, and well-being attract great attention, especially 
in human-centric smart manufacturing [5]. As such, 
human-centric techniques play an important role to put 
core human needs at the center of the production process 
[6].
Industry 5.0 identified digital twins (DT) as one of the 
enabling technologies that are better to merge the physi-
cal and virtual worlds [1]. The success of DT technology 
in physical systems (e.g., machines and devices) has moti-
vated the exploration of DT in humans [7]. The human 
digital twin (HDT) emerges as a promising human-cen-
tric technology that has drawn attention from academia 
and industry [3, 8]. For instance, in the past three years, 
some concepts relevant to HDT (e.g., digital human and 
†Qiqi He and Li Li have contributed equally to this work and should be 
considered co-first authors.
*Correspondence:
Tao Peng
tao_peng@zju.edu.cn
1 State Key Laboratory of Fluid Power Components and Mechatronic 
Systems, Zhejiang University, Hangzhou 310027, China
2 ZJU‑Sunon Joint Research Center for Smart Furniture, Zhejiang 
University, Hangzhou 310027, China
3 PICO‑Lab, Bytedance Inc., Shanghai 200233, China
4 Sunon Technology Co., Ltd., Hangzhou 311215, China


---

Page 2

---

Page 2 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
digital twin of person) have appeared in Gartner’s hype 
cycle for emerging technologies, experiencing upward 
growth in the innovation trigger phase (see Figure  1). 
Consequently, both Wang et al. [3, 9] and Sparrow et al. 
[10] regarded HDT as an enabling technology for HCPS 
with a bright future, which brings humans and physical 
systems together in a virtual space.
The majority of current HDT research is in the fields of 
healthcare and medicine, such as the DT of the human 
body for managing athletes’ fitness [7] and patients’ 
health [11], or the DT of organs for medical services 
[12]. For instance, Dassault Systèmes has developed a DT 
heart that uses magnetic resonance imaging and electro-
cardiogram (ECG) to visualize the difficult-to-see anat-
omy in the real world [13]. This kind of HDT seems to 
have a strong correlation with human lives and anatomy. 
In comparison, there are fewer studies on HDT in the 
manufacturing industry. Nevertheless, frameworks and 
concepts are only briefly described in a few HDT studies. 
Wang et al. [8] proposed the HDT-driven HCPS frame-
work that has the potential to enhance human-robot col-
laboration (HRC). Hafez et al. [14] introduced the HDT 
concept for monitoring the human-machine state.
In the industrial fields, little in-depth research has 
been conducted on the DT of workers because human 
needs have not received as much attention as produc-
tion efficiency and product quality of production from 
a techno-economic perspective [6]. More and more 
researchers have argued that humans are irreplaceable 
for flexibility, creativity, and problem-solving capabili-
ties in manufacturing [3]. However, human modeling 
and simulation remain a challenge in HDT because 
humans are a far more complex system than machines 
and other devices, and also because human behav-
ior is unpredictable [3]. To build a human model, sev-
eral researchers have combined finite element models 
(FEM) with computed tomography (CT) [7]. But there 
are numerous physiological parameters, which result in 
huge computational costs [7]. Human factors—rather 
than specifics of human anatomy—are what human-
centric manufacturing systems are concerned with to 
improve human well-being and overall system perfor-
mance [15]. Therefore, an easier and more practical 
method is needed for human modeling and simulation 
in HDT.
The human factors, often known as ergonomics, con-
siders different aspects of humanity from an interdis-
ciplinary viewpoint, including physical, psychological 
(affective and cognitive), and social [16]. Digital human 
modeling (DHM) provides digital solutions for mod-
eling and simulating the physical and cognitive aspects 
of humans, and bridges computer-aided engineering and 
human factors engineering [17, 18]. For instance, DHM 
tools could generate biomechanical models using anthro-
pometric data, enabling the analysis of muscle forces 
and spine loads during manual material handling [19]. 
Additionally, models of DHM have been constructed 
and validated with professional/domain knowledge from 
disciplines like anatomy, biomechanics, and psychology 
[20]. For these reasons, the DHM is taken as a break-
through in this research and has the potential to enhance 
HDT modeling and simulation.
To the best of our knowledge, there is no discussion 
about the relationship between DHM and HDT. Paul 
et  al. [21] first suggested that a core element of Ergo-
nomics 4.0 is the transition of DHM into DT, which is 
distinguished from each other by real-time and person-
alization. The former concentrates on the biomechani-
cal and cognitive models of human manikins [18], while 
the latter primarily tackles the cyber-physical integration 
of physical entities [22]. However, it can be difficult for 
DHM to represent real-world human conditions accu-
rately. Although DHM uses anatomy information to 
build highly realistic and accurate generic human body 
models, DHM often involves scaling the generic model 
to reflect the statistical body dimensions of the end-user 
population [21]. In addition, DHM applies inverse kin-
ematic techniques with precise kinematics and dynam-
ics data, which may not be suitable for all simulation 
situations. It is challenging for DHM to reflect how the 
human body interacts with realistic environments. In 
contrast, HDT takes into account real-time data, simula-
tion data, and the fusion of physical and virtual data to 
meet the needs for personalization and responsiveness 
[22]. Based on abundant data and models, HDT is able 
to construct multi-scale human body models to fit differ-
ent application scenarios and needs for fidelity. From the 
perspective of human factors, HDT could be the future 
trend for human modeling in DHM, but this is still worth 
discussing.
Figure 1  Emerging technologies relevant to HDT in Gartner’s hype 
cycle


---

Page 3

---

Page 3 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
	
According to recent studies, the current trend in 
human factors is to implement real-time assessments 
and interventions in the production process [21, 23]. 
However, DHM is often used during the design phase 
since the manikins must be manually adjusted and the 
lab sensors are chunky and expensive [24]. In recent 
years, a growing number of studies have been combing 
human factors with advanced digital technologies like 
the Internet of Things (IoT), artificial intelligence (AI), 
and eXtended reality (XR) to respond to the development 
trends [21, 25]. For instance, advanced, unobtrusive, and 
body-worn sensors are utilized for on-site measurement 
enabling biomechanical analysis during work, such as 
inertial measurement units (IMUs) and wireless wearable 
electromyography (EMG) [26, 27]. These innovations 
help to rapidly provide accurate data for the virtual-real 
mapping of human throughout production or service 
stages [28]. In the human factors perspective, HDT is a 
digital representation of the human body that integrates 
modeling, simulation, and digital technologies to assess 
the condition of human factors and provide feedback to 
the system. It is essential to give a holistic view between 
DHM and HDT and to investigate a unified HDT frame-
work to integrate human factors and digital technologies.
In response, this study seeks to answer the following 
three research questions:
•	 What are the distinguishing features and evolution-
ary shifts involved in transitioning from DHM to 
HDT?
•	 From a human factors perspective, what technical 
details should be available regarding the HDT frame-
work?
•	 What are the future industry applications and chal-
lenges associated with HDT?
The rest of this paper is organized as follows: In Sec-
tion2, the current state of the art in DHM and HDT is 
reviewed; in Section 3, the evolutionary shifts involved in 
transitioning from DHM to HDT are introduced; in Sec-
tion 4, the HDT framework is elaborated in detail; and 
in Section 5, the future perspectives are highlighted with 
open discussions.
2  Overview of DHM and HDT
2.1  Brief Review of DHM
DHM is defined as the simulation of human anthropo-
metric, biomechanical, and perceptual-cognitive attrib-
utes in a computerized environment [18, 28]. With DHM, 
people can make proactive ergonomics designs and eco-
nomically simulate and test a diverse variety of underly-
ing hypotheses about human behavior [18].
The literature review for DHM is focused on mod-
eling and simulating human behaviors and cognition in 
science, not in the arts. Since the 1960s, there has been 
a gradual evolution of scientific DHM, accompanied by 
rising needs and technological advancements. The evolu-
tion of DHM from 1960s is represented in Figure 2.
Based on the functionality, DHM models can be 
broadly divided into three main branches: anthropomet-
ric models, biomechanical models, and perceptual-cog-
nitive models [28]. The functions, applications, and tools 
corresponding to these three types are summarized in 
Table 1.
The first type is anthropometric models, which involve 
describing the geometric dimension of human body 
measurements with physical properties [38]. These mod-
els provide insights for product or space design consider-
ing the geometric constraints of the human body, such as 
workplace or cockpit design in terms of reachability anal-
ysis, visibility analysis, and ergonomic assessment (e.g., 
OWAS and RULA). Representative tools include JACK 
[29], RAMSIS [30], and SANTOS [31], etc.
The second type focuses on the biomechanical prop-
erties of human body, realizing multibody mechanics of 
the human musculoskeletal system [39]. Musculoskeletal 
modeling is usually driven by kinematics and kinetics 
principles, such as Lagrange’s equation [28]. With these, 
musculoskeletal forces and loading calculation, gait anal-
ysis, postures and dynamics prediction can be reached. 
Typical tools include AnyBody [32], OpemSim [33], 
and 3DSSPP [34], etc. Also, SANTOS and JACK added 
biomechanical modules in their later versions. Though 
it is rarely studied, biomechanical models can also be 
developed using finite element analysis [28, 40].
The third type deals with the perceptual-cognitive 
aspect of humans. It aims to simulate how people per-
ceive, process, and memorize information and how 
Figure 2  Main development lines of DHM (Adapted and modified 
from Ref. [28])


---

Page 4

---

Page 4 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
decisions are made so that the cognitive state and perfor-
mance of humans can be predicted [41]. Some research-
ers also referred to it as human performance modeling 
[42]. This type is less studied compared with the other 
two, as modeling the cognitive aspect of a human is more 
challenging. Most underlying theories are conceptual or 
empirical, so the context of use is limited. Typical models 
like ACT-R [35], QN-MHP [36], and SOAR [37], etc.
It is worth noting that the distinction between the three 
types is not absolute. Sometimes, anthropometric mod-
els are the prerequisite of complex movements measure-
ment in biomechanical models coinciding with the length 
of limb segments, location of mass centers, and so on [37, 
43, 44].
Currently, many DHM tools have been commercial-
ized and widely used in different industries [32, 45]. 
Some DHM software tools make an effort to synchro-
nize motion and physiological data acquired from sen-
sors at the same time by integrating multiple modules 
and providing functional modules or interfaces [45, 46]. 
For example, biomechanical analysis and monitoring are 
achieved by the integration of musculoskeletal models 
with synchronized EMG, forces, and motion data [47, 
48]. Although DHM tools have worked on data synchro-
nization, there are several limitations:  (1) scenarios that 
can only be used in a lab setting for short-term monitor-
ing, (2) model parameters that are fixed by offline learn-
ing, and (3) lack of attention to historical behavior and 
contextual information about the individuals.
2.2  Brief Review of HDT
With increasing applications of DT in many fields, 
research on HDT is gradually emerging. The state-of-the-
art of HDT is presented in terms of both human health 
and performance.
In terms of human health, some researchers suggested 
that HDT technology can be used to monitor and predict 
an individual’s health status. As a related standard, the 
development and use of ISO/IEEE 11073 makes it easier 
to use the gathered health data [49], laying the founda-
tion for the implementation of HDT. El Saddik et al. [50] 
developed an ecosystem of the DT to promote health and 
well-being in a data-driven manner, which lacks mecha-
nism models (e.g., biomechanical models of humans). 
Okegbile et  al. [51] proposed the framework of HDT 
for personalized healthcare services and highlighted 
its key technologies, challenges, and future directions. 
Ferdousi et  al. [52] compared the well-being DT with 
product DT and gave attention to the mental health and 
social aspects of human beings. Moreover, HDT focusing 
on certain scenarios or human organs has also aroused 
a wide range of discussion. Barricelli et  al. [7] studied 
HDTs of a sports team, which could monitor and man-
age athletes by collecting measurements describing their 
behavior. Cardio twin, a DT of the human heart running 
on the edge based on the ecosystem [50] mentioned, was 
presented to detect, prevent and reduce the risk of suffer-
ing heart diseases [12]. He et al. [53] proposed a method 
for constructing a shape-performance integrated DT of 
the lumbar spine to predict the real-time biomechan-
ics of the lumbar spine during human movement. These 
studies have greatly promoted the development of HDT, 
but there are still certain limitations in scalability and 
universality.
In terms of human performance, there is no recog-
nized standard or framework for HDT due to the wide 
range of application scenarios involved. The main topic 
of relevant studies is how HDT can be used to enhance 
human performance or play better human roles in vari-
ous scenarios. Bilberg et al. [54] proposed a DT-driven 
HRC assembly system for dynamic skill-based task 
allocation between humans and robots, task sequenc-
ing, and real-time control of flexible assembly cells. 
Fan et  al. [55] explored a vision-based HDT mode-
ling approach for three human statuses, including 3D 
human posture, action intention, and ergonomic risk 
in an HRC scenario. According to Graessler et al. [56], 
the development of an HDT that can represent employ-
ees enables user feedback to be generated instantly and 
used to support decision-making in the production 
system. In the human-centered application scenario, 
some studies focus on creating a more lifelike twin 
of humans to improve the interactive experience by 
combining interaction and visualization technologies. 
Table 1  Functions, applications, and common tools in DHM
Categories
Anthropometric models
Biomechanical models
Perceptual-cognitive models
Function
Simulating the distribution of physi-
cal dimensions of human body
Simulating human musculoskeletal system
Simulating human
perceptual-cognitive state and decision-making 
behavior
Application
Product, workplace or cockpit design
Posture prediction, gait analysis, and dynamics 
prediction
Human cognitive state and performance predic-
tion
Tool
JACK [29], RAMSIS [30], SANTOS [31]
AnyBody [32], OpenSim [33], 3DSSPP [34], JACK, 
SANTOS
ACT-R [35], QN-MHP [36], SOAR [37]


---

Page 5

---

Page 5 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
	
Orts-Escolano et al. [57] proposed an end-to-end sys-
tem for Augmented Reality/Virtual Reality (AR/VR) 
telepresence to realize real-time 3D reconstructions of 
people, furniture, and objects; and transmitted them 
to remote users in real-time. Chen et al. [58] used AR 
technology to deliver interactive, holistic, whole-body 
visual information to create a virtual human body, 
and conducted safe work posture training. Meanwhile, 
Wang et  al. [9] presented a comprehensive discussion 
on definition, architecture, enabling technologies, and 
applications from an Industry 5.0 perspective.
Currently, although the studies on HDT reflect the 
key features of DT like interoperability, real-time, and 
fidelity, the implementation of HDT is still in its early 
stage [51]. Most studies focus more on a specific organ, 
function, or aspect of life, lacking a holistic descrip-
tion of the human, body, and having poor applicability 
in other scenarios like manufacturing. Compared with 
DHM, HDT includes real-time information detection 
and an AI-inference module [12], which can address 
the limitations of DHM to some extent, such as no real-
time data import and parameters derived from offline 
learning. Moreover, HDT is applied not only for simu-
lating but also for monitoring and intervention.
2.3  Comparison of DHM and HDT
Based on the reviews above, Table 2 presents a summa-
rized comparison of key features of DHM and HDT. Both 
technologies use digital representations to demonstrate 
human behavior. DHM is used to simulate and predict 
the physical and cognitive behavior of humans, grounded 
in underlying mathematical models and theoretical prin-
ciples. But, it is rarely utilized to track real-time human 
performance or physical safety [42]. In contrast, HDT 
relies on computation resources and real-time data from 
the physical world to maintain continuous high-fidelity 
monitoring, prediction, and proactive interactions. As 
a result, DHM is a valuable approach for understanding 
human behavior. It provides strong interpretability based 
on well-established scientific knowledge. On the other 
hand, HDT promotes an attention to time-effectiveness 
and personalized services.
3  Moving from DHM to HDT
Simulating and modeling are essential steps in the crea-
tion of an HDT model. The literature review indicates 
that HDT integrates a variety of technologies that will 
provide efficient ways to address the limitations of DHM. 
Furthermore, DHM provides a strong theoretical foun-
dation for modeling and simulating of humans in the 
aspects of physical, physiology, and psychology [59]. 
This indicates that the transition from DHM to HDT is 
worth being better tracked to further the development of 
human factors. As shown in Figure 3, industry systems 
now contain diverse elements, which increase the com-
plexity of interaction between humans and systems. This 
increase has led to a gradual change of human factors 
Table 2  Comparison of DHM vs. HDT in key features
Features
DHM
HDT
Theory-based
High
Medium
Data-based
Medium
High
Interpretability
High
Medium-high
Real-time
Low
High
Simulation-supporting
High
Medium-high
Monitoring-supporting
Medium-Low
High
Prediction-supporting
High
High
Interaction-supporting
Low
High
Figure 3  Major advances of human factors in the industry


---

Page 6

---

Page 6 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
from observation-based techniques, such as time-and-
motion studies, to techniques based on multi-sensors 
and intelligent algorithms [60]. From the perspective 
of human factors, the evolution of DHM into HDT will 
embrace three characteristics: model-data-hybrid-ena-
bled, online learning, and timely interaction.
3.1  From Model‑Enabled to Model‑Data‑Hybrid‑Enabled
The model-driven approach known as DHM generates 
posture and motion based on anthropometric databases, 
inverse kinematics and motion capture (MoCap) systems, 
etc. [61]. There is a lack of diversity in personal charac-
teristics and environmental conditions [62], despite the 
fact that model-enabled approaches provide a strong 
theoretical foundation. Data-driven approaches may be 
able to bridge the gap. For instance, by combining the 
anthropometric model with data-based body size varia-
tion, new motions for humans in and out of vehicles can 
be generated without MoCap [62]. Additionally, data-
driven methods are in high demand due to personaliza-
tion, continuous monitoring, and evaluation, whereas 
model-enabled solutions are generally theoretical or 
hypothetical [25, 63]. For example, a musculoskeletal 
model can reveal a lot of information about muscular 
dynamics, but it is complex enough that requires lots 
of computing resources [64]. A hybrid model that com-
bines a musculoskeletal model with a predictive skeletal 
model could significantly reduce the use of experimental 
data and increase calculation efficiency [64]. As a result, 
our objective is to develop a model-data-hybrid-enabled 
HDT framework that involves different DHM models 
and multi-modal data sources.
3.2  From Offline to Online Learning Paradigm
HDT is anticipated to be a technique used in realistic 
scenarios to monitor and evaluate the health status of 
workers and system performance [12], as well as to pro-
vide two-way feedback between humans and machines/
robots [3]. Therefore, it is crucial to implement real-time 
feedback and an online learning paradigm [65]. How-
ever, common DHM tools have some limitations in real-
time, such as the needs for short-term data recording and 
offline post-analysis in a lab setting, and the fixed form 
of some model parameters (e.g., mechanical properties 
of muscle fiber) [62]. Thus, a data-driven module for AI-
inference would be essential in the HDT framework to 
fill the gaps. On the one hand, machine learning (ML) 
methods could be used to evaluate performance [66] and 
ergonomics risk [67] based on data from non-intrusive 
devices (e.g., Kinect and IMUs). For example, Luka et al. 
[68] used ML to estimate muscle fatigue online in real-
time based on data from offline biomechanical models. 
On the other hand, deep learning (DL) [66] methods have 
better accuracy in time series data, like recurrent neural 
networks (RNN) [69], enabling the analysis of motion 
history and context information.
3.3  From Pre‑Design to Timely Interaction
A proactive ergonomics method called DHM is used to 
pre-design products, workstations, and tasks [70]. While 
HDT focuses on real-time monitoring and intervention, 
it places more emphasis on perceptibility and timely 
interaction. Perceptibility is the ability to perceive human 
behavior and reactions, and it is related to advances in 
wireless and sensor technologies [71]. A timely interac-
tion helps to ensure the operators’ health and safety and 
enhances user experiences [25]. In specific, prompt feed-
back to individuals is essential for proactive musculo-
skeletal disorders prevention, action training guidance, 
decision support, etc. [72] For example, timely interac-
tion between humans and robots in the HRC scenarios 
could improve accuracy and safety in complex and flex-
ible co-tasks [71, 72]. In addition, HDT will be efficient to 
update robotic controls strategies quickly by monitoring 
operators and timely intervention, e.g., planning a trajec-
tory without collisions [73–75]. In general, a modularized 
user interface (UI) in HDT that is flexible and replace-
able for the new is essential to ensure timeliness as new 
modes of interaction (e.g., gestures and voice) emerge.
4  Framework of HDT in Human Factors
Based on the above analysis, a unified HDT framework 
is being proposed to integrate human factors and digi-
tal techniques to deal with complex and dynamic situ-
ations in reality. As shown in Figure  4, the proposed 
HDT framework is composed of the Physical Twin (PT), 
the Virtual Twin (VT), and the linkage between the PT 
and VT. It is designed based on a common connotation 
of digital twin (DT) according to [76, 77] and follows a 
widely consensual HDT framework for health and well-
being in Ref. [50], which has been applied to the DT of 
the human heart [12]. These studies provide a solid 
theoretical foundation for the HDT framework. How-
ever, the current HDT framework is not suitable for our 
application scenarios and goals from a human factors 
perspective.
The HDT is a model-data-hybrid-enabled method that 
can proactive ergonomic design to intelligent ergonomic 
services. It combines human modeling methods with 
AI techniques to build multi-scale human models based 
on abundant data from the PT. Then, iterative and self-
updating models can be enabled by continuous data and 
information in a feedback loop, allowing real-time analy-
sis and timely interaction between the PT and VT.
In this section, the proposed HDT framework is 
presented in detail. The content of the three main 


---

Page 7

---

Page 7 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
	
components—data source, digital engine, and interface—
has been tailored to meet the technical requirements of 
human factors analysis. Firstly, this framework prioritizes 
the twin of work-related human factors, such as body 
movements and cognitive status, rather than high-fidelity 
anatomical representations. Additionally, it integrates 
ergonomic methods like biomechanical modeling with 
AI-interface methods. These ensure model timeliness as 
well as model accuracy, efficiency, and personalization 
with iteration. Furthermore, it offers multi-scale human 
body models adaptable to different fidelity needs. For 
instance, the HDT model for an operator incorporates 
varying levels of detail. High-detail hand models are nec-
essary for assembly workers collaborating with robots 
to enable real-time adjustments in robot path planning 
based on their gestures. Manual laborers need low-detail 
musculoskeletal with an emphasis on general work pos-
tures to prevent musculoskeletal disorders (MSDs).
4.1  Data Source
Multi-modal data from multiple sources need to be 
obtained by smart sensors in order to characterize the 
physical human being from a comprehensive perspec-
tive, involving physical, psychological, and social aspects. 
It is important to note that the acquisition of such data 
in daily work should preferably follow the following prin-
ciples: non-interference, non-intrusiveness, and non-
infringement of privacy.
There are four types of data sources according to differ-
ent sources and usages. (1) Physiological signals, includ-
ing existing electrophysiological signals such as EMG, 
ECG, Electroencephalogram (EEG), which measure the 
electrical signals emitted by skeletal muscles, brain, and 
heart, respectively [78]. As well as data on vital signs like 
the heart beat and blood pressure from wearable sensors 
and devices. (2) Motion data, from Kinect, optical or 
IMU-based MoCap system, used to measure the real 
body movements; and sensing data from pressure and 
infrared sensors to identify human posture and activi-
ties. (3) Other data from the social network and environ-
ment to capture the social environment and contextual 
information. (4) Demographics data of the subjects such 
as age, gender, BMI, years, which are crucial to model 
personalization.
All data seem to be relevant to the study of human fac-
tors that improve performance, well-being, and health, 
and the majority of the data will be collected, stored, and 
transmitted in a synchronized manner [66]. For instance, 
wearable IMU and EMG sensors have proved that they 
can be utilized to capture motion and muscular activity 
in real-time, enabling online MSDs assessment by offer-
ing reliable and objective measurements [27]. Besides, 
EEG signals are broadly used in conjunction with big data 
analytics and AI algorithms for emotion recognition [79] 
and mental fatigue detection [80].
There are undoubtedly technical challenges during 
collection, storage, and transmission. On the one hand, 
flexible and nonintrusive sensors should be developed to 
collect data with the minimal possibility of discomfort 
and disruption to daily tasks. On the other hand, data 
transmission and synchronization mechanisms should 
be ensured due to the daily upload of a large volume 
of data to the server. For instance, if a huge volume of 
instant video stream data is required, a rapid and efficient 
communication system is a major guarantee of the data 
transmission capabilities. Additionally, adopting an edge-
cloud IoT architecture can increase the capacity of data 
storage, processing, and computing, and edge devices 
may make it possible to respond to massive amounts of 
data more rapidly and in real-time.
Figure 4  Framework of HDT from a human factors perspective


---

Page 8

---

Page 8 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
4.2  Digital Engine
The digital engine serves as the trunk or brain of the VT 
in the proposed framework. The digital engine is com-
posed of two parts: a human modeling engine and an AI-
inference engine. For real-time monitoring, assessment, 
prediction, and optimization, the digital engine plays an 
important role in model-data-hybrid-enabled simulation 
and intelligent analysis to extract behavioral and contex-
tual information.
The human modeling engine is a model-enabled mod-
ule. To give a comprehensive description of the human 
body, it should consider health, cognition, and bio-
mechanics models by using physiological signal data, 
motion data, contextual information, etc. Health mod-
eling mainly considers mental health and physical health. 
For mental health, models focus on cognitive load meas-
urements to address mental stress from the workplace 
[81]. For physical health, relevant mathematical models 
include static endurance time models and dynamic mus-
cle fatigue models [82]. In terms of cognitive modeling, 
perceptual-cognitive models are used to evaluate opera-
tors’ capacity and ability for conducting mental tasks 
(e.g., perception, awareness, and memory) [81, 83]. On 
the side of biomechanics, 3D biomechanical models of 
the musculoskeletal system are built via motion data and 
an anthropometry database. Kinematics and kinetics cal-
culations are used to simulate movements for examining 
joint loads and muscle force [84].
Notably, twinning of cognitive abilities is most chal-
lenging. Since human brains’ structure and function are 
intricate, not to mention cognitive mechanisms, it is 
thereby hard to establish an accurate model of cognitive 
performance for now. While non-invasive neuroimag-
ing techniques, such as EEG, are used to facilitate brain-
computer interfaces and enhance safety within symbiotic 
HRC scenarios according to Wang et al. [85]. These tech-
nologies hold the potential to reflect cognitive activities 
and the brain’s functional states in support of HDT. How-
ever, this neural information is constrained by accuracy, 
resolution, and latency limits [85].
The AI-inference engine is a data-enabled module that 
includes data pre-processing, feature extraction and rep-
resentation, data analytics and inference, and decision-
making. Data pre-processing is in charge of filtering the 
raw data acquired, synchronization with timestamps, and 
normalization. Based on the pre-processed data, feature 
extraction is conducted to develop a feature set that rep-
resents the physiological trait, which is helpful to reduce 
redundant data from the dataset. Data analytics and 
inference are the next crucial step. Popular AI algorithms 
like ML and DL can provide a range of solutions for vari-
ous objects, including recognition, monitoring, assess-
ment, and prediction [86–88]. And the outputs, such as 
MSDs risk assessment, action safety guidance, health 
state inferences, can support decision-making. When it 
comes to AI inference, what needs to be treated with cau-
tion is the modalities of input data and the computational 
resources.
Additionally, since both the human modeling engine 
and the AI-interface engine have advantages and dis-
advantages, it is sometimes better to combine the two 
technologies to ensure real-time efficiency and person-
alization. For instance, a vision-based DL algorithm 
extracts a human 2D skeletal pose in real-time; skeletal 
models can be used to predict the kinematics and kinet-
ics of human motions; as a result, muscle forces and joint 
loads can be estimated after importing the reconstructed 
posture data into musculoskeletal models. This method 
is computationally efficient since the hybrid model com-
bines the skeletal model’s rapid motion prediction with 
muscular dynamics assessment [64]. In terms of person-
alization, physical activity levels, preferences, and behav-
ior patterns vary widely among individuals. The general 
approach of the human modeling engine is effective in 
developing generalized human models with unified char-
acteristics (e.g., BMI and gender) but limited in a statical 
population level. Hence, the AI-inference engine emerges 
as an essential tool in building personalized models. 
The AI module combines data from the generic model 
with real-world data, including individual features and 
contextual information. It learns about individual pref-
erences and behavioral patterns using this integrated 
data. Furthermore, it enables dynamical updating of the 
parameters of HDT models. For example, Liao et al. [88] 
developed DT models of drivers to predict personalized 
lane change behavior online, considering their prefer-
ences. Additionally, Moztarzadeh et al. [89] increased the 
usefulness of DTs for cancer prediction by dynamically 
modifying decision trees based on dynamic data.
However, creating an iterative and self-updating model 
requires a technological breakthrough due to the real-
time and high-frequency motion data needed. Therefore, 
data transmission interoperability, data normalization, 
and communication are essential when building a large-
scale multidisciplinary HDT model.
4.3  Interface
Owing to the AI-inference engine working, HDT can 
learn the users’ behavior and preferences through a 
complex interaction with the real environment. And the 
interface plays a central role in virtual-reality interaction, 
which supports the immersive interaction of digital and 
physical humans using different interaction techniques. 
In this framework, HDT can finally represent and visu-
alize the physical and cognitive status of human digitally 
and send feedback to the corresponding physical human 


---

Page 9

---

Page 9 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
	
based on the modeling and analysis results. As shown in 
Figure  4, the interface, functioning as the skin appear-
ance of VT, includes three modules: function, visualiza-
tion, and multimodal interaction.
The function module has the following purposes: 
monitoring, assessment, prediction, and recognition. 
Some of the functions are widely applied in human fac-
tors, including performance analysis and prediction, 
ergonomics assessment, health monitoring, and occu-
pational risk monitoring, as well as intention and action 
recognition. In addition, a digital representation of the 
physical human is also made available to create an end-
to-end immersive twin that can be displayed livelier 
on terminal devices. To this end, this HDT framework 
concentrates more on accurate virtual-real mapping of 
essential human factors, such as body movements, work-
ing postures, and physical and cognitive status, rather 
than a high-fidelity representation of human anatomy. 
Finally, the digital avatar must interact with both physical 
humans and other VTs through multi-modal interaction. 
Advanced technologies like AR/VR, wearables, and high-
performance computing help to create an all-around 
and immersive interactive experience with sight, sound, 
touch, and smell. For example, AR is used to generate 
virtual objects in the same environment through precise 
spatial and temporal mapping. Wearable UI may become 
a trend that enables users to easily interact with small 
wearable devices with touchscreen displays and receive 
timely feedback (e.g., vibration alerts or message notifi-
cations) [7]. High-performance computing is also neces-
sary for better synchronization and a more user-friendly 
experience.
5  Future Perspectives
5.1  Industrial Application Trends
The widespread adoption of DT technology across all 
areas of our lives and work has promoted the develop-
ment of HDT in the medical and sports fields. However, 
HDT is still in its infancy in the industrial field because 
human needs are not prioritized in the technological-
centered period; instead, there is an ongoing pursuit of 
the quality and efficiency of production. In light of the 
growing emphasis on the human factors in Industry 5.0 
and the HCPS paradigm, our research has found that 
HDT has the potential to provide intelligent services 
including data visualization, monitoring, prediction, and 
immersive interaction, by considering the human fac-
tors throughout the product lifecycle. Furthermore, a few 
leading companies have shown interests and a trend of 
application towards HDT in the industrial field, including 
the clothing, manufacturing, and metaverse industries 
(see Figure 5). Meanwhile, multi-scale human body mod-
els can be utilized to adapt different application needs.
With customization and personalization prevalent over 
the years, anthropometric measurement is a key technol-
ogy in clothing customization so that clothing sizes can 
fit every customer. In the past, personal tailoring required 
taking a precise tape measurement getting the client’s 
individual measurements. Currently, Magic Weaver Inc. 
is trending to become a representative HDT application 
in clothing customization, as it proves the feasibility of 
AI body digitalization and measuring solutions to cloth-
ing companies, including smart size recommendations 
and tailor-made services [90]. The best-fit sizes of indi-
vidual customers are computed based on their photos 
through 3D human body modeling technologies. It also 
reduced the return and exchange rate by 70% for some 
customers and invalid inventory of clothing companies 
by generating realistic human body models. In the future, 
vision-based recognized methods for whole-body meas-
urements can be used to generate HDT models at an 
anthropometric level.
In the manufacturing industry, humans and robots are 
working closely together. Collaboration is becoming a hot 
topic in HRC scenarios. They share the same workspace 
for flexible automation, with robots handling physically 
demanding, repetitive, and tedious tasks. HDT is condu-
cive to monitoring human body and providing real-time 
information about the environment for worker safety 
in HRC. As a typical application, KUKA’s collaborative, 
sensitive robots can work more effectively with opera-
tors compared to conventional robots [91]. Indeed, one 
of the key reasons is that the motions of humans and 
robots may be monitored with sensors and predicted dig-
itally so that humans and robots interact extremely close 
with efficient precision, and safety. Therefore, cognitive 
modeling of HDT using monitoring data will enhance 
Figure 5  Representative HDT application trends in industries


---

Page 10

---

Page 10 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
communication between humans and robots for flexible 
task coordination.
In addition, occupational health and safety issues have 
always attracted attention in the manufacturing field [92]. 
As technology advances, industrial exoskeletons are inte-
grated with AI, sensors, and other technologies to aug-
ment human capabilities and reduce fatigue [93]. With 
this, multi-scale HDT models can combine with exoskel-
etons to improve the physiological state of workers by 
giving wearable tools and ergonomics data. For instance, 
German Bionic Inc. developed wearable exoskeleton 
devices with software platforms for real-time monitor-
ing and posture risk identification [94]. Ekso Bionics Inc. 
offered lightweight exoskeletons with 3D body visualiza-
tion for assembly workers [95]. Furthermore, Cyberdyne 
Inc. created the ­HAL® exoskeleton to enhance user phys-
ical functions according to user intentions via biometric 
sensors [96]. In the future, wearable exoskeletons com-
bined with more bio-electric sensors may develop higher-
fidelity HDT models to monitor workers’ health risk 
factors and provide adaptive external support.
In the emerging metaverse industry, many companies 
are devoted to improving user-virtual world connection 
using VR/AR technologies to create a complete loop of 
human-machine interaction. A touch glove developed 
by Meta (Facebook) Reality Labs reflects a wide range of 
minor sensations, including pressure, texture, and vibra-
tion, giving users the sense that they are physically touch-
ing virtual objects [97]. Pebble Feel, a wearable device 
that enables VR users to perceive the temperature in a 
virtual environment, was unveiled by Shifrall, a Pana-
sonic subsidiary [98]. In the future, metaverse needs a 
socially interactive, immersive interaction network envi-
ronment within the HDT framework as a multi-user 
platform.
5.2  Challenges
In this work, a comprehensive overview and characteris-
tics of the shift from DHM to HDT were discussed. Then, 
a proposed HDT framework was introduced, combining 
human factors with advanced digital techniques to meet 
the needs of modern industry. Meanwhile, the promising 
future of HDT for industrial applications were also high-
lighted. However, HDT still has a long way to go in terms 
of theories, technologies, and implementation with pub-
lic attention. Several technical and social challenges must 
be addressed to fully realize its potential.
•	 Multidisciplinary cooperation. As human mod-
eling in the HDT framework has considered mul-
tiple aspects, knowledge from various disciplines 
is needed, such as brain science, psychology, and 
biomechanics. For instance, a finite element model 
was constructed by combining a digital twin of the 
lumbar spine with AI, data analytics, and biome-
chanics to predict real-time biomechanics during 
human movement [53]. This requires investigating 
the combination of multidisciplinary methodologies, 
theories, or models, as even creating a high-fidelity 
dynamic visualization of a small part of the lumbar 
spine is complex.
•	 Privacy-preserving. The HDT utilizes various data to 
identify and assess the states of users, raising privacy 
and security concerns [99]. There are three consider-
ations in this regard. Firstly, user privacy is a critical 
concern and is influenced by how data is acquired. 
For example, the motion data used to provide action 
guidance in HDT can be obtained through cameras, 
wearable devices, or ambient sensors. The level of 
user acceptance of these data acquisition meth-
ods will depend on the degree of intrusiveness and 
obtrusiveness associated with daily usage. Secondly, 
user privacy concerns vary based on the type of data 
source. Personal information should be used and 
transmitted prudently with the user’s consent. The 
accessibility of this data for specific tasks requires 
discussion. Finally, the central processing of user data 
by third parties can raise privacy concerns because 
users are concerned about their data being mali-
ciously leaked or attacked. Edge computing and fed-
erated learning can help process sensitive data more 
securely. Further exploration is needed to determine 
the scenario applicability of general authentication 
approaches and encryption mechanisms in edge 
computing.
•	 Multimodal data fusion. The selection of sensing 
devices and sensors determines the usability and 
variety of HDT applications. The multi-source heter-
ogeneous data in HDT require an integration of valu-
able information from each modality and neglects the 
redundant features. For instance, how to deal with 
body movements, heart rate, and working context 
data to recognize a worker’s stress level. Multimodal 
sensory data fusion can compensate for inconsistent 
measurements from individual sensors [78].
•	 High-fidelity issue. The ML and DL approaches 
place a greater emphasis on correlation rather than 
causality, which can result in a lack of interpretabil-
ity. However, an explainable model is significant in 
gaining user trust and contributing to its applica-
tions. For instance, if a high risk of MSDs is pre-
dicted, would this prediction be trusted and utilized 
to develop follow-up measures without explana-
tion? Therefore, there are still some challenges to 
be addressed in evaluating the model-data-hybrid-
enable technologies in HDT with high-fidelity. The 


---

Page 11

---

Page 11 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
	
growing field of eXplainable Artificial Intelligence 
(XAI) can assist in the development of models with 
interpretability [100].
•	 Autonomy. The cyber twin of the HDT can per-
form data analysis and decision-making. How-
ever, it should be careful to determine the level of 
automation for these decisions because they may 
be made based on incomplete information. As a 
result, the distribution of privileges between the 
user and the system requires further investigation. 
To advance the development and implementation 
of HDT, related policy, legislation, and ethical con-
siderations must be considered.
•	 Regulatory Compliance. The ability of HDT to 
accurately and timely capture and reflect changes 
in individual characteristics may give rise to privacy 
and data regulatory issues. Data related to individu-
als, such as facial data, should be their own [101]. 
The owner’s informed consent is essential to ensure 
the legal use of data. This is critical in domains 
like medical treatments. Strict laws and guidelines 
should govern HDT ownership and data security, 
with regulatory mechanisms tailored to the sen-
sitivity of information in each industry. Through 
technological innovation, legal regulation, and ethi-
cal guidance, the potential and risks of HDT for a 
positive impact on individuals and society can be 
balanced.
It is hoped that this effort will lead to more open dis-
cussions among practitioners and researchers, and moti-
vate cross-disciplinary ideas, which continuously enrich 
the theories and technologies for the future of HDT.
Acknowledgements
The authors sincerely thanks to the researchers at the Institute of Industrial 
Engineering, Zhejiang University for their critical discussion and feedback dur-
ing manuscript preparation.
Authors’ Contributions
QH: methodology; formal analysis; visualization; writing - original draft. LL: 
methodology; writing - original draft. DL: investigation; formal analysis; writing 
- review & editing. TP: conceptualization; methodology; writing - review & edit-
ing; supervision. XZ: formal analysis; writing - review & editing. YC: investiga-
tion; visualization. XZ: resources; project administration. RT: resources; funding 
acquisition; supervision. All authors read and approved the final manuscript.
Funding
Supported by National Natural Science Foundation of China (Grant No. 
72071179), and ZJU-Sunon Joint Research Center of Smart Furniture, Zhejiang 
University, China.
Data availability
The data are available from the corresponding author on reasonable request.
Declarations
Competing Interests
The authors declare no competing financial interests.
Received: 23 February 2023   Revised: 13 September 2023   Accepted: 19 
January 2024
References
	 [1]	 X Xu, Y Q Lu, B Vogel-Heuser, et al. Industry 4.0 and Industry 5.0—Incep-
tion, conception and perception. Journal of Manufacturing Systems, 
2000, 61: 530–535.
	 [2]	 S Grabowska, S Saniuk, and B Gajdzik, et al. Industry 5.0: Improving 
humanization and sustainability of Industry 4.0. Scientometrics, 2022, 
127(6): 3117–3144.
	 [3]	 B C Wang, P Zheng, Y Yin, et al. Toward human-centric smart manufac-
turing: A human-cyber-physical systems (HCPS) perspective. Journal of 
Manufacturing Systems, 2022, 63: 471–490.
	 [4]	 Y C Zhou, F R. Yu, J Chen, et al. Cyber-physical-social systems: A state-
of-the-art survey, challenges and opportunities. IEEE Commun. Surv. 
Tutorials, 2019, 22(1): 389–425.
	 [5]	 Y Q Lu, H Zheng, S Chand, et al. Outlook on human-centric manufactur-
ing towards Industry 5.0. Journal of Manufacturing Systems, 2022, 62: 
612–627.
	 [6]	 M Breque, N L De, A Petridis. Industry 5.0: Towards a sustainable, 
human-centric and resilient European industry. Luxembourg, LU: Euro-
pean Commission, Directorate-General for Research and Innovation, 
2021.
	 [7]	 B R Barricelli, E Casiraghi, J Gliozzo, et al. Human digital twin for fitness 
management. IEEE Access, 2020, 8: 26637–26664.
	 [8]	 B C Wang, H Zhou, G Yang, et al. Human digital twin (HDT) driven 
human-cyber-physical systems: Key technologies and applications. 
Chinese Journal of Mechanical Engineering, 2022, 35: 11.
	 [9]	 B C Wang, H Y Zhou, X Y Li, et al. Human Digital Twin in the context of 
Industry 5.0. Robotics and Computer-Integrated Manufacturing, 2024, 85: 
102626.
	 [10]	 D Sparrow, K Kruger, A Basson. Human digital twin for integrating 
human workers in Industry 4.0. International Conference on Competitive 
Manufacturing, Stellenbosch, South Africa, January 30–February 1, 2019.
	 [11]	 Y Liu, L Zhang, Y Yang, et al. A novel cloud-based framework for the 
elderly healthcare services using digital twin. IEEE Access, 2019, 7: 
49088–49101.
	 [12]	 R Martinez-Velazquez, R Gamez, A El Saddik. Cardio twin: A digital twin 
of the human heart running on the edge. 2019 IEEE International Sym-
posium on Medical Measurements and Applications (MeMeA), Istanbul, 
Turkey, June 26–28, 2019: 1–6.
	 [13]	 Virtual human modeling and the living heart - Science in the age of 
experience. https://​ifwe.​3ds.​com/​life-​scien​ces-​healt​hcare/​access-​to-​
scien​ce-​techn​ology-​break​throu​ghs. 2023–09–05.
	 [14]	 W Hafez. Human digital twin: Enabling human-multi smart machines 
collaboration. 2019 Intelligent Systems Conference (IntelliSys), London, UK, 
September 5–6, 2019: 981–993.
	 [15]	 J W Leng, W N Sha, B C Wang, et al. Industry 5.0: Prospect and retro-
spect. Journal of Manufacturing Systems, 2022, 65: 279–295.
	 [16]	 J Dul, R Bruder, P Buckle, et al. A strategy for human factors/ergonom-
ics: Developing the discipline and profession. Ergonomics, 2012, 55(4): 
377–395.
	 [17]	 A Naumann, M Rötting. Digital human modeling for design and evalua-
tion of human-machine systems. MMI-Interaktiv, 2007, 12: 27–35.
	 [18]	 D B Chaffin. Digital human modeling for workspace design. Reviews of 
Human Factors and Ergonomics, 2008, 4(1): 41–74.
	 [19]	 K Gomez-Bull, G Ibarra-Mejia, J L Hernandez-Arellano. Biomechanical 
analysis of a manual materials handling task in a local manufactur-
ing company. 1st Annual World Conference of the Society for Industrial 


---

Page 12

---

Page 12 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
and Systems Engineering, Washington, DC, USA, October 16–18, 2012: 
386–390.
	 [20]	 S Hignett, E L Jones, D Miller, et al. Human factors and ergonomics 
and quality improvement science: integrating approaches for safety in 
healthcare. BMJ Quality Safety, 2015, 24(4): 250–254.
	 [21]	 G Paul, N D Abele, K Kluth. A review and qualitative meta-analysis of 
digital human modeling and cyber-physical-systems in Ergonomics 4.0. 
IISE Transactions on Occupational Ergonomics and Human Factors, 2021, 
9(3–4): 111–123.
	 [22]	 F Tao, H Zhang, A Liu, et al. Digital twin in industry: State-of-the-art. IEEE 
Transactions on Industrial Informatics, 2018, 15(4): 2405–2415.
	 [23]	 E Rauch, C Linder, P Dallasega. Anthropocentric perspective of produc-
tion before and within Industry 4.0. Computers & Industrial Engineer-
ing, 2020, 139: 105644.
	 [24]	 J A Cort, D Devries. Accuracy of postures predicted using a digital 
human model during four manual exertion tasks, and implications 
for ergonomic assessments. IISE Transactions on Occupational Ergo-
nomics and Human Factors, 2019, 7(1): 43–58.
	 [25]	 B A Kadir, O Broberg, C S da Conceição. Current research and future 
perspectives on human factors and ergonomics in Industry 4.0. 
Computers & Industrial Engineering, 2019, 137: 106004.
	 [26]	 V C H Chan, G B Ross, A L Clouthier, et al. The role of machine 
learning in the primary prevention of work-related musculoskeletal 
disorders: A scoping review. Applied Ergonomics, 2022, 98: 103574.
	 [27]	 P Giannini, G Bassani, C A Avizzano, et al. Wearable sensor network for 
biomechanical overload assessment in manual material handling. 
Sensors, 2020, 20(14): 1–29.
	 [28]	 H Bubb. Why do we need digital human models. In: DHM and Posturog-
raphy. S Scataglini, G Paul. London: Academic Press, 2019: 7–32.
	 [29]	 N I Badler, C B Phillips, B L Webber. Simulating humans: Computer graph-
ics animation and control. New York: Oxford University Press, 1993.
	 [30]	 A Seidl. RAMSIS – A new CAD-tool for ergonomic analysis of vehicles 
developed for the German automotive industry. SAE Technical Paper, 
1997, 1233: 51–57.
	 [31]	 K Abdel-Malek, J Z Yang, J H Kim, et al. Development of the virtual-
human Santos TM. 1st International Conference on Digital Human 
Modeling, Beijing, China, July 22–27, 2007: 490–499.
	 [32]	 M Damsgaard, J Rasmussen, S T Christensen, et al. Analysis of mus-
culoskeletal systems in the AnyBody modeling system. Simulation 
Modelling Practice and Theory, 2006, 14(8): 1100–1111.
	 [33]	 S L Delp, F C Anderson, A S Arnold, et al. OpenSim: Open-source soft-
ware to create and analyze dynamic simulations of movement. IEEE 
Transactions on Biomedical Engineering, 2007, 54(11): 1940–1950.
	 [34]	 R Feyen, Y L Liu, D Chaffin, et al. New software tools improve workplace 
design. Ergonomics in Design, 1999, 7(2): 24–30.
	 [35]	 J R Anderson, D Bothell, C Lebiere, et al. An integrated theory of list 
memory. Journal of Memory and Language, 1998, 38(4): 341–380.
	 [36]	 Y L Liu, R Feyen, O Tsimhoni. Queueing network-model human 
processor (QN-MHP): A computational architecture for multitask 
performance in human-machine systems. ACM Transactions on 
Computer-Human Interaction (TOCHI), 2006, 13(1): 37–70.
	 [37]	 A Newell. SOAR as a unified theory of cognition: Issues and explana-
tions. Behavioral and Brain Sciences, 1992, 15(3): 464–492.
	 [38]	 A Wolf, J Miehling, S Wartzack. Challenges in interaction modelling with 
digital human models – A systematic literature review of interaction 
modelling approaches. Ergonomics, 2020, 63(11): 1442–1458.
	 [39]	 X Y Yu, Y Shi, H Yu, et al. Digital human modeling and its applications: 
Review and future prospects. Journal of X-Ray Science and Technology, 
2015, 23(3): 385–400.
	 [40]	 G F Wei, F Tian, C T Wang. Study on human musculoskeletal biomechan-
ics based on China digital human project. Applied Mechanics and 
Materials, 2012, 110: 5131–5135.
	 [41]	 J Yang, B Howard. Prediction of initial and final postures for motion 
planning in human manual manipulation tasks based on cognitive 
decision making. Journal of Computing and Information Science in 
Engineering, 2020, 20 (1): 011007.
	 [42]	 R G Feyen. Bridging the gap: Exploring interactions between digital 
human models and cognitive models. 1st International Conference on 
Digital Human Modeling, Beijing, China, July 22–27, 2007: 382–391.
	 [43]	 J Rasmussen, M E Lund, R P Waagepetersen. Data-based parametric 
biomechanical models for cyclic motions. 6th International Digital 
Human Modeling Symposium, Skövde, Sweden, August 31–Septem-
ber 2, 2020, 11: 372–379.
	 [44]	 G Rao, D Amarantini, E Berton, et al. Influence of body segments’ param-
eters estimation models on inverse dynamics solutions during gait. 
Journal of Biomechanics, 2006, 39(8): 1531–1536.
	 [45]	 L Ma, D Chablat, F Bennis, et al. A new muscle fatigue and recovery 
model and its ergonomics application in human simulation. Virtual and 
Physical Prototyping, 2010, 5(3): 123–137.
	 [46]	 H O Demirel, V G Duffy. Impact of force feedback on computer aided 
ergonomic analyses. 2nd International Conference on Digital Human 
Modeling, San Diego, CA, USA, July 19–24, 2009: 608–613.
	 [47]	 D Panariello, S Grazioso, T Caporaso, et al. Biomechanical analysis of the 
upper body during overhead industrial tasks using electromyography 
and motion capture integrated with digital human models. Interna-
tional Journal on Interactive Design and Manufacturing (IJIDeM), 2022, 
16(2): 733–752.
	 [48]	 Z Karimi, A Mazloumi, A Sharifnezhad, et al. Determining the interac-
tions between postural variability structure and discomfort develop-
ment using nonlinear analysis techniques during prolonged standing 
work. Applied Ergonomics, 2021, 96: 103489.
	 [49]	 H F Badawi, F Laamarti, A El Saddik. ISO/IEEE 11073 personal health 
device (X73-PHD) standards compliant systems: A systematic literature 
review. IEEE Access, 2019, 7: 3062–3073.
	 [50]	 A El Saddik, H F Badawi, R Martinez, et al. Dtwins: A digital twins eco-
system for health and well-being. IEEE COMSOC MMTC Communications 
- Frontiers, 2019, 14: 39–46.
	 [51]	 S D Okegbile, J Cai, C Yi, et al. Human digital twin for personalized 
healthcare: Vision, architecture and future directions. IEEE Network, 2022: 
1–7.
	 [52]	 R Ferdousi, F Laamarti, M A Hossain, et al. Digital twins for well-being: 
An overview. Digital Twin, 2022, 1(7): 7.
	 [53]	 X He, Y Qiu, X Lai, et al. Towards a shape-performance integrated digital 
twin for lumbar spine analysis. Digital Twin, 2021, 1(8): 8.
	 [54]	 A Bilberg, A A Malik. Digital twin driven human–robot collaborative 
assembly. CIRP Annals, 2019, 68(1): 499–502.
	 [55]	 J M Fan, P Zheng, C K M Lee. A vision-based human digital twin 
modeling approach for adaptive human–robot collaboration. Journal of 
Manufacturing Science and Engineering, 2023, 145(12): 121002.
	 [56]	 I Graessler, A Pöhler. Integration of a digital twin as human representa-
tion in a scheduling procedure of a cyber-physical production system. 
IEEE International Conference on Industrial Engineering and Engineering 
Management (IEEM), Singapore, December 10–13, 2017: 289–293.
	 [57]	 S Orts-Escolano, C Rhemann, S Fanello, et al. Holoportation: Virtual 3d 
teleportation in real-time. 29th Annual Symposium on User Interface 
Software and Technology, Tokyo, Japan, October 16–19, 2016: 741–754.
	 [58]	 K Chen, G Perera, L Li, et al. Develop and evaluate an augmented reality 
posture training tool to promote work safety. Human Factors and Ergo-
nomics Society Annual Meeting, Sage CA: Los Angeles, December, 2020, 
64(1): 2051–2055.
	 [59]	 M C Schall, N B Fethke, V Roemig. Digital human modeling in the occu-
pational safety and health process: An application in manufacturing. 
IISE Transactions on Occupational Ergonomics and Human Factors, 2018, 
6(2): 64–75.
	 [60]	 Q H Wang, Y X Wang.Theoretical framework, intension and methods of 
smart human-robot ergonomics. Technology and Innovation Manage-
ment. 2022, 43(1): 55–62.(in Chinese)
	 [61]	 N Rego-Monteil, M Suriano, D C Pereira, et al. A data collection method-
ology to perform DHMS-based ergonomic analysis of manufacturing 
tasks. Proceedings of the 12th International Conference on Modelling and 
Applied Simulation, Athens, Greece, September 25–27, 2013: 114–121.
	 [62]	 M Mochimaru. Digital human models for human-centered design. 
Journal of Robotics and Mechatronics, 2017, 29(5): 783–789.
	 [63]	 L X Tsao, L F Li, L Ma. Human work and status evaluation based on 
wearable sensors in human factors and ergonomics: A review. IEEE 
Transactions on Human-Machine Systems, 2019, 49(1): 72–84.
	 [64]	 R Zaman, Y Xiang, R Rakshit, et al. Hybrid predictive model for lifting 
by integrating skeletal motion prediction with an OpenSim musculo-
skeletal model. IEEE Transactions on Biomedical Engineering, 2022, 69(3): 
1111–1122.


---

Page 13

---

Page 13 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
	
	 [65]	 X Z Yan, H Li, A R Li, et al. Wearable IMU-based real-time motion warn-
ing system for construction workers’ musculoskeletal disorders preven-
tion. Automation in Construction, 2017, 74: 2–11.
	 [66]	 L X Tsao, M A Nussbaum, S Kim, et al. Modelling performance dur-
ing repetitive precision tasks using wearable sensors: A data-driven 
approach. Ergonomics, 2020, 63(7): 831–849.
	 [67]	 M M Fernández, J Á Fernández, J M Bajo, et al. Ergonomic risk assess-
ment based on computer vision and machine learning. Computers & 
Industrial Engineering, 2020, 149: 106816.
	 [68]	 L Peternel, C Fang, N Tsagarakis, et al. A selective muscle fatigue man-
agement approach to ergonomic human-robot co-manipulation. 
Robotics and Computer-Integrated Manufacturing, 2019, 58: 69–79.
	 [69]	 A Nasr, S Bell, J Y He, et al. MuscleNET: Mapping electromyography to 
kinematic and dynamic biomechanical variables by machine learn-
ing. Journal of Neural Engineering, 2021, 18(4): 1–20.
	 [70]	 D B Chaffin. Human motion simulation for vehicle and workplace 
design. Human Factors and Ergonomics in Manufacturing & Service 
Industries, 2007, 17(5): 475–484.
	 [71]	 M N Liu, S L Fang, H Y Dong, et al. Review of digital twin about con-
cepts, technologies, and industrial applications. Journal of Manufac-
turing Systems, 2021, 58: 346–361.
	 [72]	 J Q Zhao, E Obonyo, S G Bilén. Wearable inertial measurement unit 
sensing system for musculoskeletal disorders prevention in construc-
tion. Sensors, 2021, 21(4): 1–28.
	 [73]	 Q B Lv, R Zhang, X M Sun, et al. A digital twin-driven human-robot 
collaborative assembly approach in the wake of COVID-19. Journal of 
Manufacturing Systems, 2021, 60: 837–851.
	 [74]	 D Riedelbauch, D Luthardt-Bergmann, D Henrich, et al. A cognitive 
human model for virtual commissioning of dynamic human-robot 
teams. 2021 5th IEEE International Conference on Robotic Computing 
(IRC), Taichung, Taiwan, China, July 15–19, 2021: 27–34.
	 [75]	 L X He, P Glogowski, K Lemmerz, et al. Method to integrate human 
simulation into Gazebo for human-robot collaboration. IOP Confer-
ence Series: Materials Science and Engineering, 2020, 825(1): 012006.
	 [76]	 F Tao, F Y Sui, A Liu, et al. Digital twin-driven product design framework. 
International Journal of Production Research, 2019, 57(12): 3935–3953.
	 [77]	 E Glaessgen, D Stargel. The digital twin paradigm for future NASA and 
US air force vehicles. 53rd AIAA/ASME/ASCE/AHS/ASC Structures, Struc-
tural Dynamics and Materials Conference, Honolulu, Hawaii, USA, April 
23–26, 2012: 1818.
	 [78]	 G Schirner, D Erdogmus, K Chowdhury, et al. The future of human-in-
the-loop cyber-physical systems. Computer, 2013, 46(1): 36–45.
	 [79]	 J W Li, S Barma, P U Mak, et al. Single-channel selection for EEG-based 
emotion recognition using brain rhythm sequencing. IEEE Journal of 
Biomedical and Health Informatics, 2022, 26(6): 2493–2503.
	 [80]	 I Mehmood, H Li, W Umer, et al. Multimodal integration for data-driven 
classification of mental fatigue during construction equipment 
operations: Incorporating electroencephalography, electrodermal 
activity, and video signals. Developments in the Built Environment, 
2023, 15: 100198.
	 [81]	 D Romero, P Bernus, O Noran, et al. The Operator 4.0: Human cyber-
physical systems & adaptive automation towards human-automation 
symbiosis work systems. International IFIP WG 5.7 Conference on 
Advances in Production Management Systems, Iguassu Falls, Brazil, 
September 3–7, 2016, 2: 677–686.
	 [82]	 L Ma, D Chablat, F Bennis, et al. A new simple dynamic muscle fatigue 
model and its validation. International Journal of Industrial Ergonom-
ics, 2009, 39(1): 211–220.
	 [83]	 B Robbins, D Carruth, A Morais. Bridging the gap between HCI and 
DHM: The modeling of spatial awareness within a cognitive archi-
tecture. 2nd International Conference on Digital Human Modeling, San 
Diego, CA, USA, July 19–24, 2009: 295–304.
	 [84]	 A Nérot, W Skalli, X Wang. An assessment of the realism of digital 
human manikins used for simulation in ergonomics. Ergonomics, 
2015, 58(11): 1897–1909.
	 [85]	 S C Liu, L H Wang, R X Gao. Cognitive neuroscience and robot-
ics: Advancements and future research directions. Robotics and 
Computer-Integrated Manufacturing, 2024, 85: 102610.
	 [86]	 M J Zhang, H X Li, S C Tian. Visual analysis of machine learning methods 
in the field of ergonomics—Based on Cite Space V. International 
Journal of Industrial Ergonomics, 2023, 93: 103395.
	 [87]	 J Oyekan, Y Chen, C Turner, et al. Applying a fusion of wearable sensors 
and a cognitive inspired architecture to real-time ergonomics analy-
sis of manual assembly tasks. Journal of Manufacturing Systems, 2021, 
61: 391–405.
	 [88]	 X S Liao, X P Zhao, Z R Wang, et al. Driver digital twin for online predic-
tion of personalized lane-change behavior. IEEE Internet of Things 
Journal, 2023, 10(15): 13235–13246.
	 [89]	 O Moztarzadeh, M Jamshidi, S Sargolzaei, et al. Metaverse and health-
care: Machine learning-enabled digital twins of cancer. Bioengineer-
ing, 2023, 10(4): 455.
	 [90]	 AI body digitization & measuring. https://​www.​magic​weaver.​com/. 
2023–09–05.
	 [91]	 Human-robot collaboration: Welcome, fellow robot! https://​www.​
kuka.​com/​en-​cn/​future-​produ​ction/​human-​robot-​colla​borat​ion. 
2023–09–05.
	 [92]	 R Bavaresco, H Arruda, E Rocha, et al. Internet of things and occupa-
tional well-being in Industry 4.0: A systematic mapping study and 
taxonomy. Computers & Industrial Engineering, 2021, 161: 107670.
	 [93]	 C Constantinescu, R Rus, C-A Rusu, et al.Digital twins of exoskeleton-
centered workplaces: Challenges and development methodology. 
Procedia Manufacturing, 2019, 39: 58–65.
	 [94]	 Exoskeleton tools. https://​germa​nbion​ic.​com/​en/​solut​ions/​exosk​eleto​
ns/ . 2023–09–05.
	 [95]	 Ekso empowers manufacturing. https://​eksob​ionics.​com/​manuf​actur​
ing/ . 2023–09–05.
	 [96]	 What’s HAL? https://​www.​cyber​dyne.​jp/​engli​sh/​produ​cts/​HAL/. 
2023–09–05.
	 [97]	 Inside reality labs research: Meet the team that’s working to bring touch 
to the digital world. https://​tech.​fb.​com/​ar-​vr/​2021/​11/​inside-​reali​
ty-​labs-​meet-​the-​team-​thats-​bring​ing-​touch-​to-​the-​digit​al-​world/. 
2023–09–05.
	 [98]	 Pebble feel. https://​ja.​shift​all.​net/​produ​cts/​pebbl​efeel. 2023–09–05.
	 [99]	 G Sirigu, B Carminati, E Ferrari. Privacy and security issues for human 
digital twins. 2022 IEEE 4th International Conference on Trust, Privacy 
and Security in Intelligent Systems, and Applications (TPS-ISA), Atlanta, 
GA, USA, December 14–17, 2022: 1–9.
	[100]	 A Holzinger. From machine learning to explainable AI. 2018 World 
Symposium on Digital Intelligence for Systems and Machines (DISA), 
Kosice, Slovakia, August 23–25, 2018: 55–66.
	[101]	 L J Kish, E J Topol. Unpatients—Why patients should own their medi-
cal data. Nature Biotechnology, 2015, 33(9): 921–924.
Qiqi He  born in 1995, is currently a Ph.D. candidate at State Key Lab-
oratory of Fluid Power Components and Mechatronic Systems, Zhejiang 
University, China. Her research interests include human factors and 
smart office toward employee health promotion. E-mail: he_qiqi@zju.
edu.cn
Li Li  born in 1995, is currently working as human factors research 
scientist at PICO-Lab, Bytedance Inc., China. He acquired his doctoral 
degree in industrial engineering from North Carolina State University, 
United States. His research focuses on XR-enabled human factors, 
ergonomics, and biomechanics. E-mail: lilidavid@foxmail.com
Dai Li  born in 1998, is currently a master degree candidate at State 
Key Laboratory of Fluid Power Components and Mechatronic Systems, 
Zhejiang University, China. Her research interests include big data ana-
lytics and smart office toward employee health promotion. E-mail: 
li_dai@zju.edu.cn
Tao Peng  born in 1984, is currently an Associate Professor at 
State Key Laboratory of Fluid Power Components and Mechatronic 
Systems, Zhejiang University, China. He received his bachelor and 
master degrees from Xi’an Jiaotong University, China, and doctoral 
degree from University of Auckland, New Zealand. His research inter-
ests include innovative smart technologies for manufacturing and 
services, big data-driven production management, and cognitive 


---

Page 14

---

Page 14 of 14
He et al. Chinese Journal of Mechanical Engineering            (2024) 37:9 
intelligence-enabled design, manufacturing and supply chains. Tel: 
+86-571-87952048; E-mail: tao_peng@zju.edu.cn
Xiangying Zhang  born in 1996,  acquired her doctoral degree 
in industrial engineering from Zhejiang University, China. She was a 
joint Ph.D. candidate at the Hong Kong Polytechnic University, China. 
Her research interests include physical activity recognition and smart 
office toward employee health promotion. E-mail: xiangyingzhang@
zju.edu.cn
Yincheng Cai  born in 1998, is currently a master degree candidate 
at State Key Laboratory of Fluid Power Components and Mechatronic 
Systems, Zhejiang University, China. His research interests include 
smart office toward employee health promotion. E-mail: cai-
yincheng@zju.edu.cn
Xujun Zhang  born in 1977, is currently the Director of Sunon 
Technology Co., Ltd., China, the General Manager of Sunon Research 
Institute,  China, and the Deputy Director of the ZJU-Sunon Joint 
Research Center for Smart Furniture, China. He serves as an advisor of 
ZJU-Sunon Joint Graduate Training Base of Zhejiang Province, and his 
main research interests are development and management of smart 
health-oriented office furniture products. E-mail: xujun.zhang@isu-
non.com
Renzhong Tang  born in 1961, is currently a Full Professor at State 
Key Laboratory of Fluid Power Components and Mechatronic Sys-
tems, Zhejiang University, China. He received his doctoral degree in 
mechanical manufacture from Zhejiang University, China. He serves 
as the Director of ZJU-Sunon Joint Research Center for Smart Furniture, 
China. His research interests include smart service for office staff, 
smart manufacturing systems, lean thinking and lean production, 
low-carbon manufacturing. E-mail: tangrz@zju.edu.cn
