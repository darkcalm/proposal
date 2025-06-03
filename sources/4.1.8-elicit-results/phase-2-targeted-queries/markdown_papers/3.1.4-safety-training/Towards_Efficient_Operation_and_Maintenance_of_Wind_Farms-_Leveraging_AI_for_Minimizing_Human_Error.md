# Towards Efficient Operation and Maintenance of Wind Farms- Leveraging AI for Minimizing Human Error

## Paper Metadata

- **Filename:** Towards Efficient Operation and Maintenance of Wind Farms- Leveraging AI for Minimizing Human Error.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:13.621973
- **Total Pages:** 9

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

1 
Towards Efficient Operation and Maintenance of Wind Farms: 
Leveraging AI for Minimizing Human Error 
Arvind Keprate1,2 Stine. S. Kilskar3 and Pete Andrews4 
1Grønn Met – Green Energy Lab, Department of Mechanical, Electrical and Chemical Engineering, Oslo Metropolitan 
University, Oslo, Norway 
2AI Lab, Department of Computer Science, Oslo Metropolitan University, Oslo, Norway 
3Department of Software Engineering, Safety and Security, SINTEF Digital, Trondheim, Norway 
4Echo Bolt, Alcester, UK 
arvind.keprate@oslomet.no 
 
ABSTRACT 
To effectively compete with other renewable energy 
sources, there remains a critical need to further decrease the 
Levelized Cost of Energy of Wind Farms (WFs). A 
promising way to achieve this objective is by minimizing 
the downtime of wind turbines (WTs) through effective 
Inspection 
and 
Maintenance 
(I&M) 
activities. 
Conventionally, I&M plans have predominantly relied on 
CM/SCADA data obtained from the physical components of 
turbines, with data analytics and machine learning (ML) 
techniques being employed to predict their performance and 
maintenance needs. However, statistics indicate that nearly 
40% of WT failures can be traced back to HFs. These 
include aspects such as skills, knowledge, communication, 
and even the broader organizational culture. This paper 
delves into the importance of integrating HFs in the I&M of 
WFs to optimize turbine performance, enhance safety, and 
reduce downtime. 
Firstly, we briefly discussed various Human Reliability 
Analysis (HRA) methods with special emphasis on 
Performance Shape Factors (PSFs). We then identify key 
human factors (HFs) that are vital for performing O&M 
tasks. For this, we have prepared a questionnaire to get 
qualitative input from technicians and also done a thorough 
literature review. E.g., some of the HFs that stand out 
include the ergonomics of tools and workspace designs 
tailored to technicians' needs, the cognitive load placed on 
operators during system monitoring and diagnostics, 
continuous training to handle evolving challenges, effective 
communication channels, and safety protocols designed 
with human behavior in mind. We then propose a novel 
framework for developing a computer vision-based 
recommendation system that can guide the technicians to 
perform the maintenance effectively thus minimizing the 
HE. 
1. INTRODUCTION 
The wind industry, driven by a commitment to green energy 
generation, is at the forefront of research, technological 
innovation, efficiency gains, and cost reductions. With 
turbine sizes and capacity factors having tripled, there has 
been a monumental shift in the wind energy sector. Since 
1990, generation costs have been reduced by 65% (KPMG, 
(2019)), 
underscoring 
the 
industry's 
dedication 
to 
developing sustainable and economical energy solutions for 
the future. For instance, breakthroughs in blade design and 
materials, backed by rigorous research, enable turbines to 
harness wind more proficiently, yielding higher energy 
outputs even in suboptimal wind conditions (Asim, T., 
Islam, S., Hemmati, A., & Khalid, M. (2022)). The adoption 
of various Prognostics and Health Management (PHM) 
technologies and predictive analytics has further improved 
the operation and maintenance (O&M) of (WFs), curtailing 
downtime and driving costs even lower (Haghshenas, A., 
Hasan, A., Osen, O., & Mikalsen, E. T. (2023)). 
Rinaldi et al. (Rinaldi, G., Thies, P. R., & Johanning, L. 
(2021)) performed an exhaustive survey of the latest 
strategies governing the O&M planning and CM of OWFs. 
Their review delves into the benefits and limitations of 
current practices and looks ahead to emerging trends in 
robotics, AI, and data analytics. Key opportunities 
highlighted include the integration of diverse data sources to 
refine O&M strategies, precise inventory management, 
detailed uncertainty modeling, the urgent need for 
Arvind Keprate. This is an open-access article distributed under the 
terms of the Creative Commons Attribution 3.0 United States License, 
which permits unrestricted use, distribution, and reproduction in any 
medium, provided the original author and source are credited. 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 869

---


### Page 2

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
2 
standardized open data frameworks, and the development of 
essential reference software. In a related study, Mc Morland 
et al. (Mc Morland, J., Flannigan, C., Carroll, J., Collu, M., 
Mc Millan, D., Leithead, W., & Coraddu, A. (2022)) 
highlighted the significance of various factors in O&M 
modeling for OWFs, including weather dynamics, failure, 
and degradation patterns, vessel logistics, cost estimation, 
and maintenance tactics. Besnard et al. (Besnard, F., 
Patriksson, M., Stromberg, A. B., Wojciechowski, A., & 
Bertling, 
L. 
(2009)) 
introduced 
the 
'opportunistic 
maintenance' concept for OWFs, which entails the fusion of 
multiple planned corrective and preventive maintenance 
tasks, either within a similar timeframe or even during a 
single visit. By capitalizing on wind forecasts and 
synchronizing corrective maintenance with periods of low 
power generation or unexpected failures, this approach has 
proven to yield a 43% reduction in preventive maintenance 
expenses (Fast, S., Mabee, W., Baxter, J., Christidis, T., 
Driver, L., Hill, S., Mc Murtry, J., & Tomkow, M. (2016)) 
However, as currently practiced, the PHM approach uses 
only machine-related quantitative data available from 
CM/SCADA 
systems 
to 
predict 
and 
manage 
the 
performance and maintenance needs of WFs. The biggest 
drawback of the overreliance on machine-related (MR) data 
is its inability to capture the full spectrum of operating 
conditions under which WFs function. A frequently 
undervalued metric in this context is human-related data, 
which offers additional insights into the system environment 
(Kiassat, A.C., (2013)). 
Human technicians/operators are an essential part of the 
daily O&M activities of the WFs. It is highly probable that 
Human Error (HE), in one form or another, might infiltrate 
the design, manufacturing, operation, and maintenance 
phases of WFs. Morag et al. (Morag, I. et al. (2018)), 
identified the most common HE during a maintenance 
activity described in Table 1. 
The HE may go unnoticed due to various reasons and can 
result 
in 
catastrophic 
accidents 
leading 
to 
severe 
consequences for the environment, society, and business. 
Statistics indicate, HE as one of the major factors for 
accidents across various sectors as shown in Figure 1. For 
instance, the infamous disasters within the oil and gas sector 
namely, the Piper Alpha and the BP Deepwater Horizon 
blowout occurred due to human and operational flaws. 
Likewise, the accident investigations of multiple aircraft 
crashes (such as of a Boeing 707-321C in 1977; Boeing 
747-200, in 1992; and Airbus 380-842 Qantas Flight 32 in 
2010) also point towards technical failures, HFs, and 
regulatory shortcomings as failure causes (Mathavara, K., & 
Ramachandran, G. (2022)). These statistics serve as a 
reminder that, while the hardware aspect is undoubtedly 
important, the human dimension also has a significant 
influence on the overall health and performance of the 
system. 
Table 1. Most common causes of Human Errors 
(Morag, I. et al. (2018)) 
HE Type 
Description 
Communication 
Misunderstandings among technicians and 
operators, often stemming from inadequate 
leadership and management. 
Fatigue 
Tiredness due to overwork or working in 
enclosed environments. 
Tools 
and 
equipment 
Improper use of tools and equipment can 
augment risks and compromise worker safety. 
Additionally, the lack of proper tools may 
increase HE as workers resort to using 
unsuitable machinery for specific tasks. 
Skills 
and 
expertise 
The risk of HE increases in non-routine tasks 
that 
demand 
specific 
knowledge 
when 
workers assigned are unfamiliar with the 
activities. 
Bad procedures 
HE often arises from poor information and the 
lack of standardized procedures. 
Documentation 
Poor documentation handling can increase HE 
due to its impact on task performance and 
understanding of required work. 
Procedure’s 
usage 
Lengthy procedures often lead workers to 
adopt informal methods and rely on personal 
experience to complete tasks. 
Time pressures 
Overtime and overwork often lead to more 
mistakes by workers, as they resort to 
shortcuts and simpler work methods. 
Tool 
control 
and 
housekeeping 
It concerns tracking the equipment used or 
removed from machinery. 

Figure 1. Accident percentage due to HE across various 
sectors 
 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 870

---


### Page 3

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
3 
In this paper, the authors have highlighted the importance of 
integrating HFs within O&M of WFs. Firstly, we have 
briefly discussed various Human Reliability Analysis 
(HRA) methods with special emphasis on Performance 
Shape Factors (PSFs). We then discuss two scenarios of 
performance maintenance in the yaw deck and the nacelle of 
a typical WT. Thereafter we propose a framework for 
developing a computer vision-based recommendation 
system that can guide the technicians to perform the 
maintenance effectively thus minimizing the HE. We also 
propose the use of an eye-tracking device to measure the 
stress level of technicians. 
2. HUMAN RELIABILITY ANALYSIS (HRA) 
2.1. General 
The origin of HRA is in probabilistic risk assessment 
(PRA), a discipline initially developed for understanding 
and quantifying the risks of serious accidents within the 
nuclear industry. HRA provides methods and tools for 
analyzing and assessing risks caused by operator's actions 
on a technical system, thus evaluating to operator's 
contribution to system reliability. The first fully developed 
HRA methods date back to the 1970s when systematic tools 
for analysis of the operator's contribution to risk were 
applied in the nuclear industry. There are now several HRA 
methods available for the nuclear sector, with some being 
adapted to other industries such as oil and gas, chemical, 
and aviation. Figure 2 illustrates the steps of a generic HRA 
process. 
 
Figure 2. Generic HRA Process 
 
2.2. HRA Methods 
It is common to distinguish between first and secondgeneration HRA methods (Swain, A.D. (1990), Dougherty, 
E.M. (1990)). The list of first-generation methods is 
extensive and includes amongst others Technique for 
Human Error Rate Prediction (THERP) (Swain, A.D., 
Guttman, H.E. (1983)), the Human Cognitive Reliability 
method (HCR) (Hannaman, G.W., Spurgin, A.J., Lukic, 
Y.D. (1984)), the Human Error Assessment and Reduction 
Technique (HEART) (Williams, J.C. (1985)), Accident 
Sequence Evaluation Program (ASEP) (Swain, A.D. (1987), 
and Standardized Plant Analysis Risk – Human (SPAR-H) 
reliability analysis (Gertman, D., Blackan, H.S., Marble, J., 
Byers, J., Haney, L.N., Smith, C. (2005)). 
Hollnagel (Hollnagel, E. (1998)), and Kim (Kim, I.S. 
(2001)) provide the following list of notable characteristics 
of first-generation methods: 1) Assumption that human 
reliability is similarly describable as hardware reliability. 2) 
HRA being limited to only the human actions that are 
included in the PSA event trees. 3) Binary representation of 
human action as either success or failure to carry out a given 
task. 4) Dichotomy of errors of omission (failure to perform 
an action) and errors of commission (unintended or 
unplanned action). 5) Focus on phenomenological aspects of 
human actions. 6) Little concern about the cognitive aspects 
of human actions. 7) Emphasis on quantification of human 
errors. 8) Indirect treatment of context, as the way in which 
PSFs exert their effect on performance is not described. 
Second-generation HRA methods were developed based on 
cognitive architectures to unveil the causes of errors from a 
behavioral perspective; thus, solving the main deficiency of 
the first generation. Two basic requirements proposed by 
Hollnagel (Hollnagel, E. (1998)) are that second-generation 
approach "uses enhanced PSA event trees and that it extends 
the traditional description or error modes beyond the binary 
categorization of success-failure and omission-commission" 
(p.151). He further stresses the need for a more realistic type 
of operator model, as the approach must be explicit about 
the 
way 
in 
which 
performance 
conditions 
affect 
performance. Most authors critiquing first-generation HRA 
methods agree on the necessity of incorporating a cognitive 
model into HRA "that would enable a better understanding 
of human error mechanisms that were well described by 
Reason (Reason, J. (1990))". A Technique for Human Event 
Analysis (ATHEANA) (Cooper, S.E., Ramey-Smith, A.M., 
Wreathall, J., Parry, G.W. (1996)) and Cognitive Reliability 
and Error Analysis Method (CREAM) (Hollnagel, E. 
(1998)) are examples of well-known and widely utilized 
second-generation techniques. CREAM uses the contextual 
control model (COCOM) and provides a determination of 
the reliability of a person's performance based on an error 
taxonomy that contains both error modes and error causes. 
Although addressing the main issue of first-generation HRA 
methods, one of the highlighted weaknesses of secondgeneration methods is that they do not provide sufficient 
consideration of the mutual influences between PSFs (De 
Ambroggi, M. (2011)). According to Griffith and 
Mahadevan (Griffith, C.D., Mahadevan, S. (2011)) the main 
sources of deficiencies in HRA methods include: "1) lack of 
empirical data for model development and validation, 2) 
lack of inclusion of human cognition (i.e., need for better 
human behavior 
modeling, 
3) 
large variability 
in 
implementation (i.e., HRA parameters are different 
depending on the method used), and 4) heavy reliance on 
expert judgment in selecting PSFs, and use of these PSFs to 
obtain the HEP in human reliability analysis" (p. 1444). 
HRA experts have more recently begun to look at potential 
improvements to existing methods. As an example, the 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 871

---


### Page 4

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
4 
HEART method has been used as a basis for domainspecific approaches such as Nuclear Action Reliability 
Assessment (NARA) (Kirwan, B., Gibson, H., Kennedy, R., 
Edmunds, J., Cooksley, G., Umbers, I. (2004)), Controller 
Action Reliability Assessment (CARA) (Kirwan, B., 
Gibson, H. (2008)), Railway Action Reliability Assessment 
(RARA) (Gibson, W.H., Mills, A.M., Smith, S., Kirwan, 
B.K. (2013)) and Shipboard Operations Human Reliability 
(SOHRA) (Akyuz, E., Celik, M., Cebi, S. (2016)). Another 
example is a more recent article by He et al. (He, Y., Kuai, 
N.-S., Deng, L.-M., He, X-Y. (2021)), which builds on 
CREAM by adding Human Inherent Factors (HIFs) such as 
anti-fatigue ability, concentration ability, reaction ability, 
and personality traits. 
In 2006, NASA Office of Safety and Mission Assurance 
(OSMA) published a technical report evaluating 14 HRA 
methods against a list of 17 attributes to highlight methods 
that are considered suitable for use in risk and reliability 
studies of NASA space systems and missions. The 
evaluation resulted in the selection of four methods: 
THERP, CREAM, NARA, and SPAR-H. The list of 
attributes used to compare the methods included: 
Developmental Context, Screening, Task Decomposition, 
PSF List and Causal Model, Coverage, HEP Calculation 
Procedure, Error-Specific HEPs, Task Dependencies and 
Recovery, HEP Uncertainty Bounds, Level of Knowledge 
Required, 
Validation, 
Reproducibility, 
Sensitivity, 
Experience Base, Resource Requirements, Cost and 
Availability, as well as Suitability for NASA Applications 
(Chandler, F., Chang, Y., Mosleh, A., Marble, J., Boring, 
R., Gethman, D. (2006)). Consideration of several of these 
attributes is essential when evaluating existing HRA 
methods for use in the context of O&M of WFs. 
2.3. Human Factors 
Our definition of HFs is from IEA: "Human Factors is the 
scientific discipline concerned with the understanding of 
interactions among humans and other elements of a system, 
and the profession that applies theory, principles, data, and 
other methods to design to optimize human well-being and 
overall system performance". HFs can be used either in 
accident investigations, or they can be used to enhance the 
performance of the technicians. 
The aims of using HF in general and in accident 
investigations are to: 
(1) Improve safety (i.e., reducing the risk of injury and 
death); 
(2) Improve performance in safety-critical situations (i.e., 
increase quality, productivity, and efficiency); 
(3) 
Support 
satisfaction/usability 
(i.e., 
increasing 
acceptance, comfort, and well-being). 
The details of how to use HFs for accident investigation are 
well documented in the literature, however, in this paper, we 
shall focus more on the identification of the HFs (in 
particular PSFs) that can be managed such that the I&M 
activities are performed efficiently within given time with 
minimal HE. 
2.4. Performance Shape Factors (PSFs) for OWFs 
PSFs or Performance Influencing Factors (PIFs) are defined 
by 
the 
Health 
Safety 
and 
Executive 
(HSE) 
as 
“characteristics of the job (e.g. the working environment); 
the individual (physical capability to do the work), and the 
organization (e.g. time pressure) that influence human 
performance” (HSE RR01 (2002)) 
Relevant PSFs for OWFs include environmental conditions 
(e.g., high winds, rough seas, weather variability), 
ergonomic challenges (working at heights, confined spaces, 
awkward postures), organizational aspects (training, work 
culture, resource availability), technical and mechanical 
complexity, accessibility and logistics due to remote 
locations, communication and coordination for emergency 
response, and the use of specialized tools and predictive 
maintenance technologies. On a more personal level, 
psychological stressors such as time pressure and 
distractions, as well as physiological factors like fatigue and 
hunger, can impact inspection and maintenance quality and 
error rates, especially in confined spaces like nacelles and 
hubs. 
Acknowledging PSFs and their impact on operational 
outcomes is essential for ensuring the safety, efficiency, and 
reliability of OWF’s O&M. For instance, the performance 
of technicians can significantly drop on a wet and windy 
day compared to more favorable weather conditions, 
increasing the risk of human error and injuries. Similarly, an 
overloaded technician may overlook early signs of wear, 
potentially 
causing 
unforeseen 
equipment 
failures. 
Additionally, 
a 
company 
that 
prioritizes 
proactive 
maintenance is likely to emphasize regular training, which 
can lead to fewer operational errors. 
The I&M activities and corresponding PSFs differ 
depending on the location within the WTs. For example, 
tasks on the yaw deck, such as brake maintenance and 
friction pad replacement, present unique challenges. These 
include transporting items using the nacelle crane or 
manually from inside the tower. Operations in this area 
entail inspecting the deck, handling moving parts, setting up 
the workspace, conducting maintenance, and cleaning up 
(G+ Global Offshore Wind Health & Safety Organization, 
(2021)). Challenges specific to the yaw deck include 
difficult access, particularly through ladder hatches in older 
turbines, constrained working space, and the physical strain 
of maneuvering heavy items. These conditions require 
technicians to employ specialized tools and assume 
strenuous postures, which can adversely affect their wellbeing (G+ Global Offshore Wind Health & Safety 
Organization, (2021)). 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 872

---


### Page 5

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
5 
Most service and maintenance tasks in WTs, such as routine 
inspections and part replacements, are carried out in the 
confined spaces of the nacelle and blade hub. Although 
newer, larger wind turbines provide a bit more space and 
improved accessibility, the areas remain constrained, 
frequently cluttered, and occasionally slippery due to oil 
spills. These conditions make it difficult to move safely and 
operate tools efficiently (G+ Global Offshore Wind Health 
& Safety Organization, (2021)). In the hub, accessing 
components like blade root bolts forces technicians into 
uncomfortable positions, compounded by the presence of 
grease and cramped, angled spaces. This increases the 
likelihood of injuries, equipment mishandling, and errors. 
More details regarding PSFs for working on OWT can be 
found in (G+ Global Offshore Wind Health & Safety 
Organization, (2021)). 
A questionnaire was designed to collect feedback from 
technicians, the results of which are presented in Figure 3 
(in the Appendix). The questionnaire's link is provided in 
(Questionnaire, (2024)). The responses indicate a consensus 
among technicians on most questions. For instance, 
regarding ergonomic challenges highlighted in question 3, 
one technician mentioned, "Wind turbines are often not 
ergonomically designed, lacking laydown areas for bags 
and equipment, leading to obstacles and potential hazards. 
Restricted access, working in areas with significant grease 
or oil, and maintaining a clean environment pose 
substantial challenges." Another respondent highlighted the 
absence of adequate sanitary facilities for women on WTs. 
A detailed analysis of the survey results suggests that 
conducting I&M activities on WTs is an exceptionally 
challenging 
task, 
which 
significantly 
increases 
the 
likelihood of HE. Moreover, the lack of real-time 
supervision at inspection sites reduces the opportunities to 
correct such errors. Consequently, the following section 
introduces a novel framework for a Computer Vision 
supervisory agent designed to monitor technicians during 
inspections and capable of raising an alarm if there is a risk 
of HE 
3. COMPUTER VISION-BASED RECOMMENDATION AGENT 
The steps involved in the framework that integrates multimodal inputs like videos and images consist of the 
following steps: 
1. Data Collection: Using high-resolution cameras, we 
will gather a comprehensive dataset of videos and 
images capturing expert technicians performing WT 
inspections. 
2. Data Preprocessing: We will apply techniques like 
frame 
extraction, 
noise 
reduction, 
and 
image 
stabilization to the recorded videos and images to 
prepare the data for analysis. Next, we will manually 
annotate them with labels indicating correct and 
incorrect actions, focusing on key inspection points and 
common errors. Finally, we will augment the data using 
techniques such as rotation, scaling, and mirroring to 
increase the dataset's robustness against variations in 
real-world scenarios. 
3. Model Development: We will use convolutional neural 
networks (CNNs) to extract features from images and 
video frames, and employ Long Short-Term Memory 
(LSTM) networks to analyze temporal dependencies in 
video data. We will then implement a fusion technique 
to 
effectively 
integrate 
features 
from 
different 
modalities, capturing a comprehensive profile of 
inspection activities. Lastly, we will develop a 
classification system using machine learning to 
distinguish between correct and incorrect inspection 
behaviors based on the labeled data. 
4. Real-Time Monitoring System: We will install a 
monitoring device at strategic locations around the 
wind turbine. Each device will be equipped with a highresolution camera and a speaker system. The camera 
will continuously capture video of the technician’s 
activities, allowing the system to visually monitor the 
inspection process from multiple angles. We will use 
edge 
computing 
devices 
integrated 
within 
the 
monitoring systems to process the data in real-time, 
significantly reducing latency and ensuring that any 
deviations or anomalies are promptly detected. The 
speaker will provide immediate audio feedback and 
recommendations to the technician based on the realtime analysis, including alerts about potential errors, 
reminders of inspection steps, or safety warnings. 
5. Feedback Loop: We will integrate a feedback system 
where the model learns from new inspection videos 
over time, adapting to new techniques and evolving 
standards in turbine maintenance. We will regularly 
evaluate the system’s accuracy and reliability in 
detecting deviations and making iterative improvements 
based on real-world performance and feedback from 
technicians 
and 
supervisors. 
Furthermore, 
the 
technicians will also be able to interact with the system 
using voice commands. They will be able to respond to 
the audio cues by confirming receipt of messages or 
asking for further clarification. They will also be able to 
report issues, fetch information, or even tag certain 
observations without having to stop their work or 
remove their gloves, which can be particularly useful in 
harsh weather conditions. 
The deployment of such a framework has the potential to 
lower the HE significantly within WT maintenance and it 
also aligns with the broader goals of the wind industry to 
reduce costs and improve the reliability and efficiency of 
green energy production. As the industry continues to 
evolve, the continuous refinement and adoption of such 
integrated frameworks will be essential for sustaining 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 873

---


### Page 6

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
6 
growth and ensuring the safety and well-being of the human 
technicians at the heart of these operations. 
4. CONCLUSION 
This paper laid out the critical importance of integrating 
HFs into the O&M of WFs, with a particular focus on the 
potential to enhance safety and efficiency through advanced 
technologies and methodologies. We discussed various 
approaches that have been used in the past for performing 
HRA to estimate HEP. The important PSFs for 
maintenance activity on WFs, include environmental 
conditions, ergonomic challenges, organizational aspects, 
accessibility and logistics due to remote locations, 
communication and coordination for emergency response, 
the use of specialized tools, and psychological stressors. A 
questionnaire was designed to collect feedback on PSFs 
from WT technicians. For example, all the technicians 
agreed that the awkward positions required for accessing 
components like blade root bolts not only increase the risk 
of injury but also elevate the likelihood of mishandling 
equipment and making errors. 
To address these issues, we proposed a computer visionbased supervisory agent capable of real-time monitoring. 
This system, which utilizes multi-modal inputs from highresolution cameras and provides audio feedback, represents 
a significant leap forward in reducing HE. By continuously 
capturing and analyzing the technician's actions, the system 
offers corrective feedback and actionable recommendations, 
thereby ensuring adherence to best practices and enhancing 
overall safety. 
REFERENCES 
1. KPMG, 
2019. 
https://assets.kpmg.com/content/dam/kpmg/dk/pdf/DK2019/11/The-socioeconomic-impacts-of-windenergy_compressed.pdf 
2. Asim, T., Islam, S., Hemmati, A., & Khalid, M. (2022, 
January 14). A Review of Recent Advancements in 
Offshore Wind Turbine Technology. Energies, 15(2), 
579. 
3. Haghshenas, A., Hasan, A., Osen, O., & Mikalsen, E. 
T. (2023, January 25). Predictive digital twin for 
offshore wind farms. Energy Informatics, 6(1). 
4. Rinaldi, G., Thies, P. R., & Johanning, L. (2021, April 
27). Current Status and Future Trends in the Operation 
and Maintenance of Offshore Wind Turbines: A 
Review. Energies, 14(9), 2484. 
5. Mc Morland, J., Flannigan, C., Carroll, J., Collu, M., 
Mc Millan, D., Leithead, W., & Coraddu, A. (2022, 
September). A review of operations and maintenance 
modelling with considerations for novel wind turbine 
concepts. Renewable and Sustainable Energy Reviews, 
165, 112581. 
6. Besnard, F., Patriksson, M., Stromberg, A. B., 
Wojciechowski, A., & Bertling, L. (2009, June). An 
optimization framework for opportunistic maintenance 
of offshore wind power system. 2009 IEEE Bucharest 
Power Tech. 
7. Fast, S., Mabee, W., Baxter, J., Christidis, T., Driver, 
L., Hill, S., Mc Murtry, J., & Tomkow, M. (2016, 
January 25). Lessons learned from Ontario wind energy 
disputes. Nature Energy; Nature Portfolio. 
8. Kiassat, A.C., 2013. System Performance Analysis 
Considering Human-related Factors. 
Ph D Thesis. University of Toronto. 
9. Morag, I. et al. (2018) ‘Identifying the causes of human 
error in maintenance work in developing countries’, 
International Journal of Industrial Ergonomics, 68, pp. 
222–230. 
10. Mathavara, K., & Ramachandran, G. (2022). Role of 
Human Factors in Preventing Aviation Accidents: An 
Insight. Intech Open. doi: 10.5772/intechopen.106899. 
11. Swain, A.D. (1990). Human reliability analysis: need, 
status, trends and limitations. Reliability Engineering 
and System Safety 29(3), 301-313. 
12. Dougherty, E.M. (1990). Human reliability analysis – 
where should thou turn? Reliability Engineering and 
System Safety 29(3), 283-299. 
13. Swain, A.D., Guttman, H.E. (1983). Handbook of 
human reliability analysis with emphasis on nuclear 
power plant applications. Final report. NUREG/CR1278. Washington, DC: US Nuclear Regulatory 
Commission. 
14. Hannaman, G.W., Spurgin, A.J., Lukic, Y.D. (1984). 
Human Cognitive Reliability Model for PRA Analysis. 
Draft Report NUS-4531, EPRI Project RP2170-3. 
Electric Power and Research Institute, Palo Alto, CA. 
15. Williams, J.C. (1985), HEART A proposed method for 
achieving high reliability in process operation by means 
of 
human 
factors 
engineering 
technology, 
in 
Proceeding of a symposium on the achievement of 
reliability in operating plant, Safety and Reliability 
Society, 16 September 1985. 
16. Swain, A.D. (1987). Evaluation of Human Reliability 
on the Basis of Operational Experience, in Economics 
and Social Science. The Munich Technical University. 
17. Gertman, D., Blackan, H.S., Marble, J., Byers, J., 
Haney, L.N., Smith, C. (2005). The SPAR-H Human 
Reliability Analysis Method. U.S. Nuclear Regulatory 
Commission. NUREG/CR-6883, Washington DC. 
18. Hollnagel, E. (1998). Cognitive Reliability and Error 
Analysis Method CREAM. 1. Ed., Elsevier. 
19. Kim, I.S. (2001). Human Reliability analysis in the 
man-machine interface design review. Annals of 
Nuclear Energy 28(11), 1069-1081. 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 874

---


### Page 7

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
7 
20. Reason, J. (1990). Human Error. Cambridge University 
Press, Cabridge, UK. 
21. Cooper, S.E., Ramey-Smith, A.M., Wreathall, J., Parry, 
G.W. (1996). A technique for human error analysis 
(ATHEANA). Technical basis and methodology 
description. USNRC; 1996. No. Nureg/CR-6350. 
22. De Ambroggi, M. (2011). Modelling and assessment of 
dependent 
performance 
shaping 
factors 
through 
Analytic Network Process. Reliability Engineering and 
System Safety 96(7), 849-860. 
23. Griffith, C.D., Mahadevan, S. (2011). Inclusion of 
fatigue effects in human reliability analysis. Reliability 
Engineering and System Safety 96(11), 1437-1447. 
24. Kirwan, B., Gibson, H., Kennedy, R., Edmunds, J., 
Cooksley, G., Umbers, I. (2004). Nuclear action 
reliability assessment (NARA): a data-based HRA tool. 
In: Probabilistic safety assessment and management. 
Springer, p. 1206-1211. 
25. Kirwan, B., Gibson, H. (2008). CARA: a human 
reliability assessment tool for air traffic safety 
management – technical basis and preliminary 
architecture. In: The safety of systems. Springer, p. 197214. 
26. Gibson, W.H., Mills, A.M., Smith, S., Kirwan, B.K. 
(2013). Railway action reliability assessment, a 
railway-specific 
approach 
to 
human 
error 
quantification. In: Proceedings of the Australian system 
safety conference, 7 p. 
27. Akyuz, E., Celik, M., Cebi, S. (2016). A phase of 
comprehensive research to determine marine-specific 
EPC values in human error assessment and reduction 
technique. Safety Science 87, 108-122. 
28. He, Y., Kuai, N.-S., Deng, L.-M., He, X-Y. (2021). A 
method for assessing Human Error Probability through 
physiological and psychological factors tests based on 
CREAM and its applications. Reliability Engineering 
and System Safety 215 (2021) 107884, 12 p. 
29. Chandler, F., Chang, Y., Mosleh, A., Marble, J., 
Boring, R., Gethman, D. (2006). Human Reliability 
Analysis Methods: Selection Guidance for NASA. 
NASA Office of Safety and Mission Assurance, 
Washington, DC (2006), 123 p. 
30. HSE RR01 (2002). Human factors integration: 
Implementation in the onshore and offshore industries. 
31. G+ 
Global 
Offshore 
Wind 
Health 
& 
Safety 
Organization, 2021 incident report. Energy Institute, 
UK. 
32. Questionnaire,2024.https://forms.office.com/Pages/Shar
e Form Page.aspx?id=Eh_I_o Zi UEWJEf RG_Nr6Hw UV
r L3Fu U9Gk TQNYRKR5FURTFNWDgx SEJSQ0U5T
E5IVlo3TDRRTVZPSy4u&sharetoken=4i Zz38x8ISIt U
Px LNw XM 
BIOGRAPHIES 
Arvind Keprate received his B. Tech in Mechanical 
Engineering (2007) from Himachal Pradesh University, 
M.Sc. in Marine & Subsea Technology (2014), and Ph D 
(2017), in Offshore Engineering from the University of 
Stavanger, Norway. He is currently a Professor at Oslo 
Metropolitan University where he teaches Design related 
courses to Mechanical Engineering students. Besides this, 
he also teaches Machine Learning, Probability & Statistics 
at Kristiania University College in Oslo. He has been a 
visiting researcher at the Prognostics Center of Excellence, 
NASA Ames Research Center, USA. Currently, his research 
is focused on Digital Twins and PHM of complex SocioEcological-Technical Energy Systems such as Wind Farms. 
Stine Skaufel Kilskar has an M.Sc. in Industrial 
Economics and Technology Management (2014) from the 
Norwegian University of Science and Technology, Norway, 
with a focus on strategic change management. She is 
currently a Research Scientist at SINTEF Digital in 
Trondheim. She has ten years’ experience of working in 
safety-related research projects within various industries, 
such as construction, maritime, oil & gas, and energy. The 
research is mainly focused on safety management and 
human factors. 
Pete Andrews qualified from the University of Sheffield 
with a Masters degree in Aerospace Engineering in 2005. 
Working within the power industry for the last 19 years he 
has delivered operational, engineering and leadership roles 
across a broad range of power generation assets and 
technologies. Previously he delivered a number of roles 
within leading utilities including Commercial Manager 
supporting major asset divestments and managing offshore 
wind services and Plant Manager accountable for a large 
offshore wind farm. Recognizing that the pace of innovation 
in offshore wind operations and maintenance was lagging 
compared to the rate of development in other aspects of the 
sector he founded Echo Bolt, an organisation dedicated to 
deploying 
advanced 
technologies 
to 
improve 
the 
management of structural integrity of wind turbines.

Appendix 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 875

---


### Page 8

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
8 
Fig 3. Response of Questionnaire 
 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 876

---


### Page 9

ANNUAL CONFERENCE OF THE EUROPEAN PROGNOSTICS AND HEALTH MANAGEMENT SOCIETY 2024 
9 
 
Proceedings of the 8th European Conference of the Prognostics and Health Management Society 2024 - ISBN – 978-1-936263-40-0
Page 877

---
