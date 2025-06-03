# Agarwal2024 PREDICTIVE MAINTENANCE UNLEASHING APPLICATIONS OF MACHINE LEARNING  A COMPREHENSIVE EXPLORATION

## Paper Metadata

- **Filename:** Agarwal2024_PREDICTIVE_MAINTENANCE_UNLEASHING_APPLICATIONS_OF_MACHINE_LEARNING__A_COMPREHENSIVE_EXPLORATION_DOI_10-30780_specialissue-iset-2024_009.pdf
- **DOI:** 10.30780/specialissue.iset.2024/009
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:10.055821
- **Total Pages:** 5

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

International Journal of Technical Research & Science ISSN:2454-2024 
 ____________________________________________ 
___________________________________________________________________________ 
DOI Number: https://doi.org/10.30780/ specialissue-ISET-2024/009 
 
 pg. 50 
Paper Id: IJTRS-ISET-24-009 

 www.ijtrs.com, www.ijtrs.org 
All Right Reserved @ IJTRS 
PREDICTIVE MAINTENANCE 
UNLEASHING APPLICATIONS OF 
MACHINE LEARNING: A 
COMPREHENSIVE EXPLORATION 
Vishnu Agarwal, Mohammad Sabir, Surbhi Mishra, Rahul Sen 
E-Mail Id: vishnuagarwal.p@gmail.com, sabii.sankhla@gmail.com, 
surbhiudr27@gmail.com, rahul.sen1422@gmail.com 
Geetanjali Institute of Technical Studies, Udaipur, Rajasthan, India 
Abstract- The integration of industrial artificial intelligence (AI), smart sensing, and the Internet of Things 
(Io T) has revolutionized data utilization in various sectors. Predictive maintenance (PDM) emerges as a pivotal 
strategy, leveraging data from diverse manufacturing and sensing sources to anticipate equipment failures. This 
paper presents a comprehensive overview of the application of machine learning (ML) techniques in PDM, 
categorizing advancements based on ML algorithms and data acquisition equipment. Through highlighting 
significant contributions and ongoing pilot projects, this review provides valuable insights for optimizing 
maintenance strategies and enhancing equipment performance and longevity. 
Keywords: Machine learning, predictive maintenance. 
1. INTRODUCTION 
Effective maintenance is vital for success in manufacturing settings. Neglected equipment can cause unexpected 
downtime and reduced productivity, resulting in operational delays, increased waste, and lower product quality, 
among other negative impacts on business performance. 
Various organizations adopt diverse maintenance strategies based on factors like maintenance objectives, 
equipment characteristics, operational processes, and work environment. These strategies typically fall into 
categories such as corrective maintenance (CM), preventive maintenance (PM), predictive maintenance (PDM), 
and proactive maintenance. PDM specifically targets timely maintenance decisions through real-time fault 
detection, component diagnosis, degradation monitoring, and failure prediction, thereby minimizing uncertainty 
in maintenance tasks. 
The advancement of IT infrastructure in the era of Industry 4.0 has facilitated the integration of smart sensing, 
Internet of Things (Io T), big data collection, and analytics tools, empowering companies to harness the full 
potential of their data. This data-driven approach enables informed decision-making through analysis of 
historical patterns and trends. However, managing complex equipment with vast data sets poses significant 
challenges for manual processing and analysis by humans. Human-dependent scenarios, where individuals 
monitor equipment and make manual decisions, suffer from drawbacks. The expertise level of specialists 
significantly influences performance, as less experienced professionals are prone to higher rates of false 
diagnostic decisions compared to their more experienced counterparts. Industries lacking well-trained and 
experienced specialists face exacerbated challenges in maintaining consistent diagnostic accuracy. Studies 
comparing diagnostic decisions among specialists highlight the variability in outcomes, underscoring the 
limitations of human-dependent processes in critical decision-making scenarios. 
 
Fig. 1.1 Machine Learning is a Subset of Artificial Intelligence 
Machine learning (ML) is a subset of artificial intelligence (AI) characterized by algorithms or programs

---


### Page 2

International Journal of Technical Research & Science ISSN:2454-2024 
 ____________________________________________ 
___________________________________________________________________________ 
DOI Number: https://doi.org/10.30780/ specialissue-ISET-2024/009 
 
 pg. 51 
Paper Id: IJTRS-ISET-24-009 

 www.ijtrs.com, www.ijtrs.org 
All Right Reserved @ IJTRS 
capable of independent learning with minimal human intervention. ML offers solutions to complex human 
challenges like image processing, big data analysis, robotics, and speech recognition. Its application in 
monitoring and analyzing equipment health enhances operational and maintenance efficiency, leading to 
improved equipment performance and reduced breakdown occurrences. For instance, Roosefert et al. 
demonstrated an 84% reduction in breakdown time and an 88% decrease in breakdown frequency using an MLbased predictive maintenance (PDM) approach compared to traditional Industry 3.0 methods. This approach 
also enhances equipment availability, reliability, and reduces operational risks, thereby enhancing corporate 
competitiveness. 
Recent advancements in ML techniques have spurred numerous studies showcasing its potential. Akram et al. 
achieved 93.02% accuracy in fault detection of photovoltaic cell defects using convolutional neural networks 
(CNNs). Ren et al. employed region-based CNNs (R-CNN) for real-time object detection training, while Cha et 
al. applied R-CNN for detecting structural surface damages on bridges with a mean average precision (m AP) of 
87.8%. However, selecting the most suitable, simple, and effective ML algorithm for specific problems remains 
a challenge, often requiring extensive data acquisition on failure scenarios and system operating states for model 
training. 
2. THE PROGRESSION OF MAINTENANCE STRATEGIES 
The initial maintenance approach, known as corrective maintenance (CM) or "run to failure," is depicted in 
Figure 2. In CM, maintenance activities are reactive, triggered only after equipment breakdowns occur. This 
approach lacks scheduled routine maintenance, making it challenging to optimize equipment performance 
economically or in terms of reliability. Consequently, equipment availability and reliability may suffer. Despite 
its limitations, CM remains in use due to its low implementation costs, making it suitable for equipment with 
limited budgets for repair or replacement. Companies often employ CM for equipment that has minimal impact 
on overall production operations. 
 
Fig. 2.1 Evolution of maintenance approaches [3] 
The evolution of maintenance strategies progresses to preventive maintenance (PM). PM adopts a proactive, 
time-based approach where regular inspections and maintenance tasks are scheduled and executed before 
potential failures occur. The goal is to prevent system failures during operation, particularly those that could be 
costly or pose risks. 
Advancing further in maintenance strategy evolution is condition-based maintenance (CBM), along with its 
refined form known as predictive maintenance (PDM). PDM employs sophisticated analytics techniques to 
anticipate faults or failures in a degrading system. By continuously monitoring equipment operating conditions 
and performance metrics, PDM aims to detect early signs of wear or deterioration that could lead to component 
failure. Beyond basic condition monitoring, PDM's primary objective is to forecast the remaining useful life of 
machinery using historical data. This predictive aspect holds promise for significant maintenance optimization 
and cost reductions. 
4. 
LEVERAGING 
MACHINE 
LEARNING 
(ML) 
FOR 
PREDICTIVE 
MAINTENANCE (PDM) 
In the predictive maintenance (PDM) strategy, there's ongoing real-time monitoring and analysis of equipment 
health. Lei et al. [20] outline the machinery health diagnosis process into four key steps: data acquisition, 
constructing health indicators, segmenting health stages, and predicting remaining useful life. 
4.1 Data Acquisition 
Acquiring data is fundamental for subsequent processing and analysis, particularly in addressing predictive

---


### Page 3

International Journal of Technical Research & Science ISSN:2454-2024 
 ____________________________________________ 
___________________________________________________________________________ 
DOI Number: https://doi.org/10.30780/ specialissue-ISET-2024/009 
 
 pg. 52 
Paper Id: IJTRS-ISET-24-009 

 www.ijtrs.com, www.ijtrs.org 
All Right Reserved @ IJTRS 
maintenance (PDM) challenges. This process entails designing and configuring an appropriate system 
architecture to capture and store various sensor data from the equipment. A typical data acquisition system 
includes sensors, data transmission components, and storage devices. Depending on the equipment's nature, a 
combination of sensors such as accelerometers, acoustic emission sensors, infrared thermometers, and others 
may be employed to comprehensively reflect machinery degradation processes. 
4.2 Health Indicator Construction 
Following feature extraction, the subsequent phase involves establishing the health indicator (HI). This indicator 
serves as a real-time representation of machinery health, integrating various condition monitoring signals like 
vibration, current, and acoustic emissions. The construction of the health indicator is pivotal in the context of 
predictive maintenance (PDM), as it provides crucial insights into equipment health status. 
4.3 Health Stage Division 
The next phase involves categorizing machine operations into stages based on the determined health indicator 
(HI). However, this task can be challenging, especially when the machine operates with a consistent HI 
throughout its operation, lacking distinct stages. In such instances, the machines operational state changes 
uniformly at a steady pace [21]. Nevertheless, this step remains crucial in predictive maintenance (PDM) 
applications. For certain mechanical devices like journal bearings, the equipment's operational state can be 
divided into multiple stages. In the healthy stage, HI readings remain relatively constant, providing limited 
information about the device's failure trend. As a result, accurately forecasting the Remaining Useful Life 
(RUL) during this stage is neither essential nor precise. 
4.4 Remaining useful life Prediction 
Forecasting the Remaining Useful Life (RUL) of machinery stands as a pivotal challenge within the realm of 
predictive maintenance (PDM). RUL is defined as the duration remaining until the end of a machine's useful life 
[23]. The core objective of RUL prediction is to estimate the time remaining before the machinery becomes 
inoperable, leveraging condition monitoring data. This task serves as the final technical step and ultimate 
objective of machinery prognostics. Approaches to RUL prediction can be classified into physical model-based 
methods, statistical model-based techniques, and artificial intelligence (AI) approaches. 
4.5 Challenges for PDM using ML in Vietnam 
Essentially, every machine encompasses various failure modes, necessitating comprehensive laboratory testing 
to generate standardized datasets. Obtaining such data during routine operations proves challenging, often 
limited to specific failure modes. Additionally, aggregating data across similar machines is crucial but difficult 
due to the scarcity of machines in many organizations. Collaboration and data sharing among oil and gas 
companies, particularly in Vietnam, are essential to bolster the advancement and research of predictive 
maintenance (PDM) by facilitating access to vital machinery data. 
CONCLUSION 
Predictive maintenance (PDM) is gaining popularity across various industries due to its effectiveness in 
reducing unnecessary maintenance tasks and enhancing machinery reliability. With the rise of Industry 4.0, 
machine learning (ML) has become a key player in PDM, aiding in data processing, continuous equipment 
monitoring, and health analysis. This paper examines PDM practices and reviews the application of advanced 
AI techniques in this field, specifically focusing on the four main technical steps of machinery health 
prognostics: data acquisition, health indicator construction, health stage division, and remaining useful life 
prediction. 
At BIENDONG POC, there is a strategic initiative to implement PDM solutions using ML modeling to monitor, 
maintain, and track equipment reliability and performance within a plant environment. The ability to monitor 
equipment health and quickly identify potential failures supports informed decision-making and maintenance 
planning. This approach emphasizes continuous performance improvement and proactive management of 
equipment health, with a focus on identifying performance degradation as an early warning sign of potential 
issues. Therefore, staying updated with research developments and trends in PDM is crucial for evaluating the 
current state and guiding future research directions at BIENDONG POC. 
REFERENCES 
[1] 
BS EN 1336:2017, "Maintenance–Maintenance terminology", 2017. 
[2] 
Raghu Raj, “How preventive maintenance can backfire and harm your assets”, 2020. [Online]. Available: 
[3] 
Tomasz Nowakowski, Agnieszka Tubis, and Sylwia Werbińska-Wojciechowska, "Evolution of technical 
systems maintenance approaches-review and a case study", International Conference on Intelligent 
Systems in Production Engineering and Maintenance. Springer, 2018, pp. 161 - 174. 
[4] 
Tran Vu Tung, Tran Ngoc Trung, Ngo Huu Hai, and Nguyen Thanh Tinh, "Digital transformation in oil 
and gas companies - A case study of Bien Dong POC", Petrovietnam Journal, Vol. 10, pp. 67 - 78, 2020.

---


### Page 4

International Journal of Technical Research & Science ISSN:2454-2024 
 ____________________________________________ 
___________________________________________________________________________ 
DOI Number: https://doi.org/10.30780/ specialissue-ISET-2024/009 
 
 pg. 53 
Paper Id: IJTRS-ISET-24-009 

 www.ijtrs.com, www.ijtrs.org 
All Right Reserved @ IJTRS 
DOI: 10.47800/ PVJ.2020.10-07. 
[5] 
Trần Ngọc Trung, Trần Vũ Tùng, Hoàng Kỳ Sơn, Ngô Hữu Hải và Đào Quang Khoa, "Thực tiễn triển 
khai nền tảng số hóa tập trung tại mỏ Hải Thạch - Mộc Tinh”, Tạp chí Dầu khí, Số 12, trang 47 - 56, 
2020. DOI: 10.47800/ PVJ.2020.12-06. 
[6] 
Rebecca Smith-Bindman, Philip Chu, Diana Lynn Miglioretti, Chris Quale, Robert Daniel Rosenberg, 
Gary Cutter, Berta Geller, Peter Bacchetti, Edward A. Sickles, and Karla Kerlikowske, "Physician 
predictors of mammographic accuracy", Journal of the National Cancer Institute, Vol. 97, No. 5, pp. 358 - 
367, 2005. DOI: 10.1093/ jnci/dji060. 
[7] 
Varun Gulshan, Lily Peng, Marc Coram, Martin C. Stumpe, Derek Wu, Arunachalam Narayanaswamy, 
Subhashini Venugopalan, Kasumi Widner, Tom Madams, Jorge Cuadros, Ramasamy Kim, Rajiv Raman, 
Philip C. Nelson, Jessica L. Mega, and Dale R. Webster, "Development and validation of a deep learning 
algorithm for detection of diabetic retinopathy in retinal fundus photographs", JAMA, Vol. 316, No. 22, 
pp. 2402 - 2410, 2016. DOI: 10.1001/jama.2016.17216. 
[8] 
Bruce I. Reiner and Elizabeth Krupinski, "The insidious problem of fatigue in medical imaging practice", 
Journal of Digital Imaging, Vol. 25, No. 1, pp. 3 - 6, 2012. DOI: 10.1007/s10278-011-9436-4. 
[9] 
Roosefert Mohan T., Preetha Roselyn J., Annie Uthra R., Devaraj D., and Umachandran K., “Intelligent 
machine learning based total productive maintenance approach for achieving zero downtime in industrial 
machinery”, Computer & Industrial Engineering, Vol. 157, 2021. 
[10] M.Waqar Akramad, Guiqiang Li, Yi Jin, Xiao Chen, Changan Zhu, Xudong Zhao, Abdul Khaliq, 
M.Faheem, and Ashfaq Ahmad, "CNN based automatic detection of photovoltaic cell defects in 
electroluminescence images", Energy, Vol. 189, 2019. DOI: 10.1016/j.energy.2019.116319. 
[11] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun, "Faster R-CNN: Towards real-time object 
detection with region proposal networks", IEEE Transactions on Pattern Analysis and Machine 
Intelligence, Vol. 39, pp. 1137- 1149, 2017. DOI: 10.1109/TPAMI.2016.2577031. 
[12] Young-Jin Cha, Wooram Choi, Gahyun Suh, Sadegh Mahmoudkhani, and Oral Büyüköztürk, 
"Autonomous structural visual inspection using regionbased deep learning for detecting multiple damage 
types", Computer-Aided Civil and Infrastructure Engineering, Vol. 33, No. 9, pp. 731 - 747, 2018. DOI: 
doi/10.1111/ mice.12334. 
[13] Wenbin Wang, Matthew J. Carr, Tommy Wai Shing Chow, and Michael G. Pecht, "A two-level 
inspection model with technological insertions", IEEE Transactions on Reliability, Vol. 61, pp. 479 - 490, 
2012. DOI: 10.1109/ TR.2012.2183911. 
[14] Sule Selcuk, "Predictive maintenance, its implementation and latest trends", Journal of Engineering 
Manufacture, Vol. 231, No. 9, pp. 1670 - 1679, 2017. DOI: 10.1177/0954405415601640. 
[15] R. Keith Mobley, Lindley R. Higgins, and Darrin J. Wikoff, Maintenance engineering handbook, 7th 
edition. Mc Graw-Hill Education, 2008. 
[16] Pw C, “Predictive maintenance 4.0 - Beyond the hype: PDM 4.0 delivers results”, 2018. [Online]. 
Available: https://www.pwc.de/de/industrielle-produktion/pwcpredictive-maintenance-4-0.pdf. 
[17] Valerio Dilda, Lapo Mori, Olivier Noterdaeme, and Christoph Schmitz, “Manufacturing: Analytics 
unleashes 
Productivity 
and 
profitability”, 
2017. 
[Online]. 
Available: 
https://www.mckinsey.com/businessfunctions/operations/our-insights/manufacturinganalytics-unleashesproductivity-and-profitability. 
[18] Knud Lasse Lueth, “Predictive maintenance initiatives saved organizations $17B in 2018, as the number 
of vendors surges”, 2019. [Online]. Available: https://iot-analytics.com/numbers-of-predictivemaintenancevendors-surges/. 
[19] Vyas, M., Kumar, V., Vyas, S., Swami, R.K. (2023). Grid-Connected DFIG-Based Wind Energy 
Conversion System with ANFIS Neuro-Fuzzy Controller. In: Namrata, K., Priyadarshi, N., Bansal, R.C., 
Kumar, J. (eds) Smart Energy and Advancement in Power Technologies. Lecture Notes in Electrical 
Engineering, vol 927. Springer, Singapore. https://doi.org/10.1007/978-981-19-4975-3_48 
[20] Vyas, S., Joshi, R.R., Kumar, V. (2022). An Intelligent Technique to Mitigate the Transient Effect on 
Circuit Breaker Due to the Occurrence of Various Types of Faults. In: Bansal, R.C., Zemmari, A., 
Sharma, K.G., Gajrani, J. (eds) Proceedings of International Conference on Computational Intelligence 
and 
Emerging 
Power 
System. 
Algorithms 
for 
Intelligent 
Systems. 
Springer, 
Singapore. 
https://doi.org/10.1007/978-981-16-4103-9_21 
[21] S. V. et. al., “Life Extension of Transformer Mineral Oil Using AI-Based Strategy for Reduction Of 
Oxidative Products”, TURCOMAT, vol. 12, no. 11, pp. 264–271, May 2021. 
[22] D Paliwal, A Choudhur, T Govandhan, “Identification of faults through wavelet transform vis-à-vis fast 
Fourier transform of noisy vibration signals emanated from defective rolling element bearings”, Frontiers 
of Mechanical Engineering 9, 130-141. 
[23] Pankaj Malhotra, Lovekesh Vig, Gautam Shroff, and Puneet Agarwal, “Long short-term memory 
networksfor anomaly detection in time series”, 23rd European Symposium on Artificial Neural Networks, 
Computational Intelligence and Machine Learning (ESANN), Bruges, Belgium, 2015.

---


### Page 5

International Journal of Technical Research & Science ISSN:2454-2024 
 ____________________________________________ 
___________________________________________________________________________ 
DOI Number: https://doi.org/10.30780/ specialissue-ISET-2024/009 
 
 pg. 54 
Paper Id: IJTRS-ISET-24-009 

 www.ijtrs.com, www.ijtrs.org 
All Right Reserved @ IJTRS 
[24] Pankaj Malhotra, Anusha Ramakrishnan, Gaurangi Anand, Lovekesh Vig, Puneet Agarwal, and Gautam 
Shroff, "LSTM-based encoder-decoder for multisensory anomaly detection", 2016. [Online]. Available: 
https://arxiv.org/pdf/1607.00148.pdf. 
[25] H. Kumawat et al., “Using AI Techniques to Improve the Power Quality of Standalone Hybrid Renewable 
Energy Systems”, Crafting a Sustainable Future Through Education and Sustainable Development, IGI 
Global, Pages 219-228, 2023. 
[26] Achmad Widodo and Bo-Suk Yang, "Application of relevance vector machine and survival probability to 
machine degradation assessment", Expert Systems with Applications, Vol. 38, No. 3, pp. 2592 - 2599, 
2011. DOI: 10.1016/j.eswa.2010.08.049.

---
