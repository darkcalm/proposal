

---

Page 1

---

NREL is a national laboratory of the U.S. Department of Energy 
Office of Energy Efficiency & Renewable Energy 
Operated by the Alliance for Sustainable Energy, LLC 
This report is available at no cost from the National Renewable Energy 
Laboratory (NREL) at www.nrel.gov/publications. 
 
 
Contract No. DE-AC36-08GO28308 
 
 
Technical Report 
NREL/TP-6A20-72102 
April 2019 
An Overview of Distributed Energy 
Resource (DER) Interconnection: 
Current Practices and Emerging 
Solutions 
Kelsey Horowitz,1 Zac Peterson,1 Michael Coddington,1 
Fei Ding,1 Ben Sigrin,1 Danish Saleem,1,  
Sara E. Baldwin,2 Brian Lydic,2 Sky C. Stanfield,2  
Nadav Enbar,3 Steven Coley,3 Aditya Sundararajan,4 
and Chris Schroeder5 
1 National Renewable Energy Laboratory 
2 Interstate Renewable Energy Council (IREC) 
3 Electric Power Research Institute (EPRI) 
4 Florida International University (FIU) 
5 Smart Electric Power Alliance (SEPA) 


---

Page 2

---

NREL is a national laboratory of the U.S. Department of Energy 
Office of Energy Efficiency & Renewable Energy 
Operated by the Alliance for Sustainable Energy, LLC 
This report is available at no cost from the National Renewable Energy 
Laboratory (NREL) at www.nrel.gov/publications. 
Contract No. DE-AC36-08GO28308 
National Renewable Energy Laboratory 
15013 Denver West Parkway 
Golden, CO 80401 
303-275-3000 • www.nrel.gov 
Technical Report 
NREL/TP-6A20-72102 
April 2019 
An Overview of Distributed Energy 
Resource (DER) Interconnection: 
Current Practices and Emerging 
Solutions
Kelsey Horowitz,1 Zac Peterson,1 Michael Coddington,1 
Fei Ding,1 Ben Sigrin,1 Danish Saleem,1,  
Sara E. Baldwin,2 Brian Lydic,2 Sky C. Stanfield,2  
Nadav Enbar,3 Steven Coley,3 Aditya Sundararajan,4 
and Chris Schroeder5
1 National Renewable Energy Laboratory 
2 Interstate Renewable Energy Council (IREC)
3 Electric Power Research Institute (EPRI) 
4 Florida International University (FIU) 
5 Smart Electric Power Alliance (SEPA) 
Prepared as part of the Distributed Generation Interconnection Collaborative (DGIC) 
Suggested Citation 
Horowitz, Kelsey, Zac Peterson, Michael Coddington, Fei Ding, Ben Sigrin, Danish Saleem, 
Sara E. Baldwin, et al. 2019. An Overview of Distributed Energy Resource 
(DER) Interconnection: Current Practices and Emerging Solutions. Golden, CO: National 
Renewable Energy Laboratory. NREL/TP-6A20-72102. 
https://www.nrel.gov/docs/fy19osti/72102.pdf.


---

Page 3

---

 
 
NOTICE 
This work was authored in part by the National Renewable Energy Laboratory, operated by Alliance for Sustainable 
Energy, LLC, for the U.S. Department of Energy (DOE) under Contract No. DE-AC36-08GO28308. Funding 
provided by the U.S. Department of Energy Office of Energy Efficiency and Renewable Energy Solar Energy 
Technologies Office. The views expressed herein do not necessarily represent the views of the DOE or the U.S. 
Government. 
This report is available at no cost from the National Renewable 
Energy Laboratory (NREL) at www.nrel.gov/publications. 
U.S. Department of Energy (DOE) reports produced after 1991 
and a growing number of pre-1991 documents are available  
free via www.OSTI.gov. 
Cover Photos by Dennis Schroeder: (clockwise, left to right) NREL 51934, NREL 45897, NREL 42160, NREL 45891, NREL 48097,  
NREL 46526. 
NREL prints on paper that contains recycled content. 


---

Page 4

---

iii 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Acknowledgments 
This report was produced as part of the activities of the Distributed Generation Interconnection 
Collaborative (DGIC). The authors would like to thank the U.S. Department of Energy (DOE) 
Office of Energy Efficiency and Renewable Energy’s Solar Energy Technologies Office for its 
sponsorship and support. 
We would like to thank the members of the advisory board for this guidebook, which include (in 
no particular order):  
1. Joel Hornburg of Arizona Public Service (APS) 
2. Nadav Enbar and Steven Coley of the Electric Power Research Institute (EPRI) 
3. Patrick Dalton of Xcel Energy (reviewed only the technical content of the report)  
4. Steve Steffel of PEPCO Holdings Inc. (PHI) and Exelon  
5. John Sterling previously of the Smart Electric Power Alliance (SEPA), now of First Solar 
6. Chris Schroeder of the SEPA 
7. Sara Baldwin from the Interstate Renewable Energy Council (IREC) 
8. Jan Ahlen from the National Rural Electric Cooperative Association (NRECA) 
We would also like to acknowledge the following people and organizations for insightful review 
and discussion on this guidebook: 
• Kristen Ardani (NREL) 
• Lori Bird (NREL) 
This work was authored by Alliance for Sustainable Energy, LLC, the manager and operator of 
the National Renewable Energy Laboratory for DOE under Contract No. DE-AC36-08GO28308. 
Funding provided by the DOE Office of Energy Efficiency and Renewable Energy Solar Energy 
Technologies Office. The views expressed in the article do not necessarily represent the views of 
DOE or the U.S. Government. 


---

Page 5

---

iv 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
List of Acronyms and Abbreviations 
3V0 
ground fault (zero sequence) overvoltage protection 
AC 
alternating current 
ADMS 
advanced distribution management system 
AHJ 
authorities having jurisdiction 
AMI 
advanced metering infrastructure 
ANM 
active network management 
ANSI 
American National Standards Institute 
APS 
Arizona Public Service 
BTM 
behind-the-meter 
C2M2 
Cybersecurity Capability Maturity Model 
 
CIP 
critical infrastructure protection 
co-op 
electric cooperative 
CVR 
conservative voltage reduction 
DC 
direct current 
DER 
distributed energy resource 
DERMS 
distributed energy resource management system 
DG 
distributed generation 
DGIC 
Distributed Generation Interconnection Collaborative 
DOE 
U.S. Department of Energy 
DPV 
distributed photovoltaics 
D-STATCOM 
distribution static synchronous compensators 
D-SVC 
distribution static var compensators 
DTT 
direct transfer trip 
EPACT 
Energy Policy Act 
EPRI 
Electric Power Research Institute 
EPS 
electric power systems 
FAQ 
frequently asked question 
FERC 
U.S. Federal Energy Regulatory Commission 
FICS 
flexible interconnect capacity solution 
FTM 
front-of-the-meter 
HECO 
Hawaiian Electric Companies 
IEC 
International Electrotechnical Commission 
IEEE 
Institute of Electrical and Electronics Engineers 
IOU 
investor-owned utility 
IP 
Internet protocol 
IREC 
Interstate Renewable Energy Council 
IT 
information technology 
LREC 
Lake Region Electric Cooperative 
LTC 
load tap changer 
muni 
municipal utility 
NARUC 
National Association of Regulatory Utility Commissioners 
NEC 
National Electrical Code 
NEM 
net energy metering 
NERC 
North American Electric Reliability Corporation 
NIST 
National Institute of Standards and Technology 


---

Page 6

---

v 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
NREL 
National Renewable Energy Laboratory 
OMS 
outage management system 
OT 
operational technology 
PCC 
point of common coupling 
PF  
power factor 
PG&E 
Pacific Gas & Electric 
PHI 
Pepco Holdings Inc. 
POA 
principles of access 
 
PoC 
point of [DER] connection 
P 
real power 
p.u. 
per unit 
PUC 
public utility commission 
PV 
photovoltaic 
Q 
reactive power 
SCADA 
supervisory control and data acquisition 
SDG&E 
San Diego Gas & Electric 
SEPA  
Smart Electric Power Alliance 
SGIP 
Small Generator Interconnection Procedures 
Solar ABCs 
Solar American Board for Codes and Standards 
SunSpec 
SunSpec Alliance 
TCP 
transmission control protocol 
TLS 
transport layer security 
UK 
United Kingdom 
var 
volt-ampere reactive 


---

Page 7

---

vi 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Table of Contents 
Introduction ................................................................................................................................................. 1 
Motivation, Purpose, and Intended Use ................................................................................................. 1 
Scope ...................................................................................................................................................... 2 
Interconnection Considerations and Their Relation to the Guidebook Chapters ................................... 3 
1 
Interconnection Application Procedures and Management ............................................................ 5 
1.1 
State of Development .................................................................................................................... 5 
1.2 
Current Practices and Emerging Solutions .................................................................................... 5 
1.2.1 
Central Information Webpage .......................................................................................... 5 
1.2.2 
Process Improvements ...................................................................................................... 6 
1.2.3 
Online Application Systems ............................................................................................. 8 
1.2.4 
Implementation Considerations ........................................................................................ 9 
2 
Technical Screens for DER Interconnection ................................................................................... 12 
2.1 
State of Development .................................................................................................................. 12 
2.2 
Current Practices and Emerging Solutions .................................................................................. 12 
2.2.1 
FERC Technical Screens ................................................................................................ 12 
2.2.2. 
Emerging Solutions ........................................................................................................ 19 
3 
Advanced Inverters ............................................................................................................................ 21 
3.1 
State of Development .................................................................................................................. 21 
3.2 
Current Practices and Emerging Solutions .................................................................................. 22 
3.2.1 
Advanced Inverters for Voltage Regulation ................................................................... 22 
3.2.2 
Real Power Reduction or Curtailment Using Autonomous Advanced Inverter Functions
 ........................................................................................................................................ 25 
3.2.3 
Overarching Notes about Using Advanced Inverters for Mitigating Voltage and/or 
Thermal Violations ......................................................................................................... 26 
4 
IEEE 1547 Standard (2003–2018) ...................................................................................................... 28 
4.1 
State of Development .................................................................................................................. 28 
4.1.1 
Changes in IEEE 1547-2018 .......................................................................................... 29 
4.1.2 
IEEE 1547.X Family of Standards ................................................................................. 31 
4.2 
State Rules and Adoption of IEEE 1547 ..................................................................................... 32 
5 
Strategies and Upgrades for Mitigating the Distribution System Impacts of DERs .................... 33 
5.1 
Current Practices and Emerging Solutions .................................................................................. 33 
5.1.1 
Current Typical Strategies and Upgrades for Mitigating DER Impacts on Distribution 33 
5.1.2 
Preemptive Upgrades ..................................................................................................... 35 
5.1.3 
Emerging Mitigation Strategies ..................................................................................... 35 
5.2 
Looking Ahead: Key Considerations and Implementation Issues............................................... 37 
6 
Cost Allocation ................................................................................................................................... 39 
6.1 
State of Development .................................................................................................................. 39 
6.1.1 
The Conventional Cost-Causer-Pays Approach ............................................................. 40 
6.2 
Emerging Solutions ..................................................................................................................... 40 
6.2.1 
Group Study/Group Cost Allocation .............................................................................. 40 
6.2.2 
Post-Upgrade Allocation ................................................................................................ 41 
6.2.3 
Preemptive Upgrade Cost-Sharing Allocation ............................................................... 42 
6.3 
Potential Future Directions .......................................................................................................... 43 
7 
Predicting Future DER Growth .......................................................................................................... 44 
7.1 
State of Development .................................................................................................................. 45 
7.2 
Current Practices and Emerging Solutions .................................................................................. 46 
8 
Cybersecurity ...................................................................................................................................... 47 
8.1 
State of Development .................................................................................................................. 47 
8.2 
Current Practices ......................................................................................................................... 49 
8.3 
Considerations and Emerging Practices ...................................................................................... 50 


---

Page 8

---

vii 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
9 
Storage and Solar + Storage Interconnection ................................................................................. 53 
9.1 
State of Development .................................................................................................................. 54 
9.2 
Considerations and Emerging Practices ...................................................................................... 54 
10 Pulling it All Together: The Interconnection Maturity Model ......................................................... 59 
10.1 Interconnection Approaches at Low DER Penetrations .............................................................. 59 
10.2 Interconnection Approaches at Moderate to High DER Penetrations ......................................... 62 
10.3 Key Ongoing Interconnection Challenges .................................................................................. 62 
11 Summary and Conclusion ................................................................................................................. 64 
References ................................................................................................................................................. 67 
 
 
 


---

Page 9

---

viii 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
List of Figures 
Figure 1. Examples of rapidly accelerating DPV deployment on some U.S. systems: Missouri’s Empire 
District Electric Company and South Carolina Electric & Gas Company (EIA 2017) ............ 1 
Figure 2. Typical utility interconnection process; systems above a certain size may skip the Fast Track 
Screening Process and go straight to more detailed impact studies ......................................... 3 
Figure 3. Application processing times: manual processes versus online .................................................... 8 
Figure 4. Mapping of different tools for identifying potential interconnection locations and 
interconnection application activities, from Xcel (2018) ....................................................... 11 
Figure 5. FERC SGIP technical screens summary, including the additional considerations for PV (yellow 
box) from Coddington (2012) ................................................................................................ 15 
Figure 6. PHI process for automated DPV screening using power-flow modeling (Bank 2017) ............... 20 
Figure 7. Smart inverter functional categories ............................................................................................ 22 
Figure 8. DPV hosting capacity of three test feeders with various advanced inverter functions ................ 23 
Figure 9. Example volt-var curve ............................................................................................................... 24 
Figure 10. Two examples of volt-watt curves, generating active power only (left), both generating and 
absorbing active power (right) ............................................................................................... 25 
Figure 11. Example active power-reactive power curve ............................................................................. 25 
Figure 12. Timeline of changes to the IEEE 1547 standard ....................................................................... 29 
Figure 13. Application of IEEE 1547-2018 performance categories (EPRI 2017) .................................... 31 
Figure 14. Overview of the IEEE 1547 family of interconnection standards (IEEE 2015) ........................ 32 
Figure 15. U.S. annual energy storage deployment history (2012–2017) and forecast (2018–2023), in 
MW, from GTM Research (2018) ......................................................................................... 53 
Figure 16. Characteristics of utilities interviewed by SEPA about interconnection practices .................... 59 
Figure 17. Online interconnection platform status for utilities interviewed by SEPA in July 2018 ........... 61 
 
List of Tables 
Table 1. Typical Solutions Used Today to Mitigate Effects of DER on Distribution Systems .................. 34 
Table 2. Methods Used for DER Adoption Forecasting ............................................................................. 45 
Table 3. Basic and Advanced Security Controls Guidelines ...................................................................... 51 
Table 4. Summary of the Maturity of Knowledge and Standards for Interconnection Aspects Covered in 
this Report .............................................................................................................................. 64 
 


---

Page 10

---

1 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Introduction 
Motivation, Purpose, and Intended Use  
Deployment of distributed energy resources (DERs), in particular distributed photovoltaics 
(DPV), has increased in recent years and is anticipated to continue increasing in the future (GTM 
2017, Labastida 2017). The increase has been particularly significant on certain systems. Figure 
1 shows an example of a rapid rise in the number and capacity of DER with net-energy metering 
(NEM) for two different systems in Missouri and South Carolina. 
 
 
Figure 1. Examples of rapidly accelerating DPV deployment on some U.S. systems: Missouri’s 
Empire District Electric Company and South Carolina Electric & Gas Company (EIA 2017) 
As DER deployment grows, there is a need for utilities and regulators to understand 
considerations for interconnecting these resources to their systems as well as different solutions 
that may be suitable given their DER penetration levels, system characteristics, capabilities, and 
organizational structures. 
This report from the Distributed Generation Interconnection Collaborative (DGIC) was 
commissioned based on the need—identified through DGIC—for a central document 
summarizing considerations, practices, and emerging solutions across a broad set of topics 
related to DER interconnection. The report is targeted at a high-level, strategic-planning 
audience at utilities who are seeking an overview of DER interconnection issues and approaches 
and looking to understand how these may relate to their own situations. The audience includes a 
broad set of utilities and situations, including investor-owned utilities (IOUs), municipal utilities 
(munis), and cooperatives (co-ops) with a range of current DER penetration levels. 
This report complements existing resources, including more detailed research reports on specific 
interconnection-related topics (e.g., Coddington et al. 2012b; Parks, Woerner, and Ardani 2014), 
in-depth handbooks or reports on a specific interconnection-related topic (Seguin et al. 2016), as 
well as the recently published “New Approaches to Distributed PV Interconnection: 
Implementation Considerations for Addressing Emerging Issues” (McAllister forthcoming), 
which is geared more at a policymaker audience and provides a more detailed review of 
interconnection practices at utilities and states. It also provides a broader perspective and some 
forward-looking information not contained in interconnection handbooks or guidebooks 


---

Page 11

---

2 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
provided by some utilities (e.g., PG&E 2017b), which provide details of current interconnection 
policies and procedures of individual utilities relevant to interconnection applicants.  
Although some areas of interconnection have established standards, many are still nascent with 
no clear or accepted best practice. Additionally, the practice most suitable for a given situation 
will vary depending on the level of DER penetration; the utility, customer, and developer 
characteristics and preferences; the attributes of the electrical power system; and other factors. 
This report does not seek to recommend or dictate practices in any of these areas, but rather 
provides an overview of the status of different aspects of interconnection, existing standards, and 
emerging solutions currently being explored that can inform utility planning and decisions. Some 
of this information may also be useful to regulators, policymakers, and DER developers seeking 
to understand barriers to interconnection, potential solutions currently being explored, and ways 
to work with utilities on interconnection policies.  
Scope 
DERs are resources connected to the distribution system close to the load, such as DPV, wind, 
combined heat and power, microgrids, energy storage, microturbines, and diesel generators. 
Energy efficiency, demand response, and electric vehicles are also sometimes considered DERs. 
These resources may be deployed individually, co-located, or aggregated and in some cases 
jointly controlled. According to the National Association of Regulatory Utility Commissioners 
(NARUC), these resources “can either reduce demand (such as energy efficiency) or provide 
supply to satisfy the energy, capacity, or ancillary service needs of the distribution grid” 
(NARUC 2016). DPV, wind, and energy storage may be behind-the-meter (BTM) or in front-of-
the-meter (FTM) and utility owned, customer owned, or third-party owned, although very little 
BTM wind and energy storage capacity is installed to-date. Some states, like Hawaii, have been 
dominated by deployment of small residential and 
commercial rooftop DPV systems (typically 1–200 
kW in size), while others, like North Carolina, 
have seen more large, ground-mounted DPV 
systems ranging in size from several hundred kW 
to several MW that are not primarily sited to serve 
a given load or co-located with a load. 
This report covers interconnection issues that 
apply broadly to distributed generation (DG), 
regardless of technology or type. The advanced 
inverter chapter applies specifically to inverter-
based DERs. Special considerations are needed for 
energy storage, which can act as a load or a generator. Because of this, we include a separate 
chapter covering some of the unique aspects of storage interconnection. Although some of the 
practices in this report may be relevant to microgrids, we do not explicitly consider all the unique 
aspects related to this technology, including interconnection and operating practices for 
microgrids in interconnected or islanded modes. We cover interconnection of both BTM and 
FTM systems connected to the distribution system. The distribution system consists of medium- 
and low-voltage circuits, typically between 4 kV and 46 kV. We do not cover energy efficiency, 
DER types covered in this guidebook: 
 
• 
DG, including BTM and FTM systems 
connected to distribution systems 
• 
Distributed energy storage 
 
DER types not covered: 
 
• 
Energy efficiency 
• 
Demand response 
• 
Electric vehicles 


---

Page 12

---

3 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
demand response, or electric vehicles, because these resources do not go through an 
interconnection process.  
Interconnection Considerations and Their Relation to the Guidebook 
Chapters 
Figure 2 shows the typical interconnection process for DERs. First, an application for 
interconnection is submitted; processing and management of these applications is discussed in 
Chapter 1. If the project is below a specified size threshold, the utility then conducts a series of 
technical screens to evaluate the potential impact of the PV on its system. The number and type 
of screens a given project undergoes depend on the characteristics of the project. Technical 
screens and studies for DER interconnection are discussed in Chapter 2. If any negative system 
impacts—for example on voltage, power quality, or protection—are identified during the 
screening process, strategies for mitigating those impacts are identified by the utility. There is a 
variety of options for mitigating these impacts, including, but not limited to, downsizing the PV 
system, using advanced inverter functions (for inverter-based DERs), or upgrading the 
distribution network. We discuss how advanced inverters can be used to mitigate violations in 
Chapter 3. The ability of inverters to provide advanced functionality is constrained by the 
capabilities of the inverters and the ability to exercise those capabilities, which is defined by 
standards. The Institute of Electrical and Electronics Engineers (IEEE) 1547 family of 
standards is the critical foundation for DER interconnection, and it establishes criteria and 
requirements related to performance, operation, testing, safety, and maintenance on the grid. This 
standard is discussed in Chapter 4. Other important interconnection standards and codes, and 
their relationship to the IEEE 1547 standard, are also mentioned in this guidebook. 
 
Figure 2. Typical utility interconnection process; systems above a certain size may skip the Fast 
Track Screening Process and go straight to more detailed impact studies 
Different distribution system upgrades that can alternatively, or in combination with advanced 
inverters, be used to mitigate impacts are discussed in Chapter 5. If a project triggers upgrades, 
individual customers—or in some cases a small group of developers applying for interconnection 
at a similar time—are then responsible for the cost of these upgrades. However, these traditional 


---

Page 13

---

4 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
cost-allocation approaches can be problematic. Different emerging cost-allocation schemes are 
discussed in Chapter 6. 
System upgrades that might otherwise be triggered by DERs may also be avoided—to the benefit 
of developers, utilities, and rate payers—if systems can be guided into low-cost, low-impact 
locations. One possible way to do this is through hosting-capacity maps, which provide 
information on locations where DERs could be located without negatively impacting the system. 
We provide information on hosting-capacity maps and how they might relate to different 
components of the interconnection application, technical screening, and planning 
processes. 
Today, the interconnection process shown in Figure 2 is typically undertaken on a system-by-
system basis without considering future deployment of other DERs. However, several aspects of 
interconnection depend on the deployment of other DERs. For example, different distribution 
system upgrades may be preferred depending on the DER penetration levels that are anticipated 
in the future. The ability to predict the amount of DERs that might be interconnected to a 
particular circuit is also important for evaluating the potential risks and viability of different cost-
allocation approaches. With this in mind, we provide an overview of different approaches for and 
current understanding around forecasting DER deployment in Chapter 7. 
Another important consideration during the interconnection process is cybersecurity. 
Cybersecurity has become an increasing concern for society as a whole, affecting a wide range of 
critical systems, including banking and medical records systems, among many others. In electric 
power systems, concerns extend from bulk power plants, to the transmission network, to the 
distribution network. The deployment of DERs on the distribution network poses new questions 
including how to balance the growing need for increased information sharing and grid 
transparency with the need for ensuring sufficient protections and privacy. Standards for 
cybersecurity are still being developed. We discuss the current state of understanding and 
emerging practices related to cybersecurity and the interconnection of DERs in Chapter 8. 
Finally, Figure 2 shows the general DG interconnection process, but there are special 
considerations for storage systems, which can act both as generation and load. Chapter 9 
discusses issues related to storage and solar plus storage interconnection. 
In Chapter 10, we synthesize information from the other chapters and loosely map it onto what 
we term an “interconnection maturity model,” which conceptualizes evolving interconnection 
processes and needs as a function of DER penetration and utility characteristics. Chapter 11 
provides a report summary and conclusions. 


---

Page 14

---

5 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
1 Interconnection Application Procedures and 
Management 
In areas with active DER markets, spikes in application volume can overburden existing utility 
interconnection procedures, resulting in increased costs and backed-up interconnection queues. 
In addition to the financial consequences of these spikes, delayed interconnection processing 
timelines may degrade customer relationships or result in regulatory consequences. Utilities such 
as Pacific Gas and Electric (PG&E) and San Diego Gas and Electric (SDG&E) have taken active 
steps to streamline application-management processes to mitigate these impacts with great 
success (Ardani and Margolis 2015; Parks, Woerner, and Ardani 2014). In addition to alleviating 
the burden of applications on utilities, improved interconnection application procedures and 
management processes can help ensure that customer expectations around fairness, transparency, 
communication, and efficiency are met. The following sections provide an overview of good 
practices and considerations identified for improving interconnection processes. Although the 
full application process includes technical screening, this chapter focuses on the administrative 
aspects of application management. Chapter 2 discusses the technical screening aspects.  
1.1 State of Development 
The methods used to process interconnection applications are unique to every utility. Some 
utilities still rely on hard-copy forms submitted via mail or in-person and carried through the 
application process manually. Others have web-based platforms integrated with existing 
operations systems that fully automate application processing and aid in technical screening. The 
systems used by different companies are influenced by a number of factors, such as the amount 
of resources dedicated to interconnection, regulatory standards, and business preferences. 
Although there will continue to be different solutions suited for specific utilities and situations, 
some overarching good practices have emerged. 
1.2 Current Practices and Emerging Solutions  
 Central Information Webpage 
An important component typically used to provide transparency and promote applicant self-
sufficiency is a website dedicated to providing interested stakeholders with the relevant 
information for interconnecting DERs to the utility’s system. These sites should be easily 
navigable and include clear information about the interconnection process, application forms, 
and reference materials. The following are key elements typically found on these websites:  
• Application forms—Utilities may have a variety of application forms depending on 
project characteristics, screening processes, etc. The website can act as a guide to direct 
users to the appropriate forms. The page should be updated periodically to ensure out-of-
date forms are no longer available. Online application systems may act as the application 
forms directly, in which case access to these portals should be clearly provided. 
• Application checklist—This is a customer-facing document that delineates each step in 
the application process while noting the timeline for major milestones, requirements, and 
associated fees. This document can outline the entire process from initial steps, such as 
requesting a pre-application report, to construction of upgrades and meter installations at 


---

Page 15

---

6 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
the tail end of the process. A clear description of required fees (i.e., application, study, 
and upgrade fees) should also be included.  
• Contact information—Providing a single point of contact for all interconnection-related 
questions helps limit confusion about who fields what questions. The contact information 
may include an email address, phone number, or live-chat option. On the utility end, it is 
helpful to identify a single point of contact or dedicated team to answer all 
interconnection-related questions. 
• Reference materials—Resources such as example application documents (e.g., one-line 
drawings) or instructional videos will aid in educating customers and reducing the 
number of questions utility staff must respond to. This may also include links to a 
frequently asked questions (FAQs) page, incentive program information, interconnection 
rules, or a list of local developers. Some utilities host trainings and webinars for 
developers and customers to explain the process or recent changes to regulations and 
procedures.  
• Dispute-resolution processes—These processes provide a clear pathway for resolving 
disputes in a timely manner. This may include negotiations or mediations, involving a 
utility or public utility commission (PUC) ombudsperson, third-party technical expert 
(IREC 2017, Bird et al. 2018), or both. Transparency of interconnection processes, 
requirements, and fees can reduce the need for dispute-resolution mechanisms. 
 Process Improvements 
Many states have standardized interconnection forms and requirements in an effort to improve 
the interconnection process. Consistent forms and requirements among the utilities within a state 
can improve interconnection processes in several ways, for example, by reducing the number of 
questions a utility receives or increasing the amount of applications submitted correctly without 
missing information. Below, we discuss additional process improvements that can be 
implemented by individual utilities or through state regulatory requirements. 
Pre-application reports—These reports use readily available information to provide detailed 
technical information about a point of interconnection. The information provided by the utility 
allows prospective applicants to identify potential interconnection limitations early in the process 
at a relatively low cost. Doing so may help utilities reduce the number of speculative applications 
received, thus reducing the total volume of applications to be processed. The U.S. Federal 
Energy Regulatory Commission (FERC) Small Generator Interconnection Procedures (SGIP), 
which can be used as a template for pre-application processes, identifies information to be 
provided in the report, fees, and timelines (FERC 2013). 
Application clarity—A study by EQ Research found that application forms are sometimes 
perceived to be confusing and consequently require clarification from the utility (Barnes et al. 
2016). Reviewing application forms to improve their clarity may reduce resources spent 
responding to customer questions. One aspect of this is ensuring applications explicitly denote 
what information is required for a field to be complete. For example, if an application simply 
requests the “Customer Name” but actually requires the exact name on the account, this should 
be stated. Doing so can avoid mistakes such as an employee entering their name when it is not 
officially associated with the account. Resources such as an FAQ page or sample application 
forms can be referenced as well for additional clarification. For example, in Minnesota, Xcel 


---

Page 16

---

7 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Energy provides example drawings that customers can reference (Xcel Energy Minnesota 2018). 
Application forms posted online can be formatted as fillable electronic documents that clearly 
identify required information. 
Workflow efficiency—Redundant requests for information are another issue identified by 
installers in EQ Research’s study (Barnes et al. 2016). Evaluating the application documents may 
expose opportunities to simplify the forms and workflows to remove unnecessary steps and 
redundant data requests. For example, while overhauling its interconnection workflows in the 
early 2010s, PG&E flagged the request for “proof of 24/7 meter access” as an unnecessary 
requirement and consequently removed it (Ardani and Margolis 2015). Developing an internal 
application review checklist can aid in improving coordination and accountability by detailing 
the actions and personnel needed to complete each step of the application process (EPRI 2017a). 
This may help reduce duplicative efforts by the utility (Ardani and Margolis 2015).  
Signatures and payment—Collecting signatures and processing payment are two distinct areas 
that cause delays and difficulty (Barnes et al. 2016). Online payment options in addition to, or as 
an alternative to, cash or check payment can reduce the time needed to complete the transaction 
and the risk that payment is lost in transit. Similarly, removing requirements for wet signatures 
and allowing electronic signatures can reduce the time it takes to process an application (Barnes 
et al. 2016). 
Communication—Utilities and customers interact multiple times throughout the interconnection 
process. Internal application review checklists for utility use and external checklists for 
developers (National Grid RI 2018, National Grid MA 2018) can help streamline 
communications with customers by creating a clear directive for what information is shared, how 
it is shared, and when. Such checklists may also specify internal communications processes, for 
instance, designating a point of contact to coordinate communications between the different 
parties in the utility and the customer. Many utilities designate a single point of contact or team 
to handle interconnection-related requests and questions. 
Application tracking—A common customer expectation is a clear method for tracking the 
application status once the application has been submitted. Some utilities instruct applicants to 
do so by reaching out directly via phone, email, or in-person. Five of the six utilities the Electric 
Power Research Institute (EPRI 2017a) interviewed relied on this method and justified this 
practice based on the low volumes of interconnection applications. Another method is for the 
utility to post a public queue containing application status information that is periodically 
updated. California’s Rule 21 requires IOUs to post interconnection queue information publicly 
for certain projects (Bird et al. 2018). Online application systems typically provide a more 
versatile solution, allowing applicants to check the application’s real-time status at their 
convenience through the web portal.  
Automation and integration—Automation helps minimize the number of steps that must be 
manually completed, thus reducing the time utility staff must spend on processing applications. 
EPRI found that tasks such as document generation (e.g., meter exchange orders), workflow 
reminders, and application status updates all provide opportunities for automation (EPRI 2017a). 
Integrating interconnection application data with mapping or analysis tools also provides 
opportunities to improve efficiency and reduce labor. 


---

Page 17

---

8 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 Online Application Systems 
Online application systems are a significant improvement over legacy application-management 
methods for utilities with increasing or high volumes of interconnection applications. These 
systems provide customers, installers, and other stakeholders such as local permitting authorities 
with a central location to interact with applications. The portals provide an interface that can 
guide users through the application process step-by-step, prompting for information as needed. 
They are typically used to coordinate communications among the stakeholder groups and can 
send internal and external automated status reports and workflow reminders. Further, online 
systems can be used to coordinate electronic payment, manage forms, and transfer data to 
internal databases. 
Through these services, online application systems can facilitate all of the improvements 
discussed in Section 1.2.2. Online systems automate much of the process, reducing the time 
customers and utility staff need to complete each application. Automation can help with flagging 
incomplete information and providing status updates or workflow reminders. Integrating these 
online systems with existing business systems can expand their functionality and value. By 
linking to additional data streams, the platforms can perform tasks like auto-populating and 
verifying information submitted by users to reduce input errors. Advanced implementations can 
be used to aid in technical screening and initial engineering reviews. 
Automation with online application systems has helped several utilities reduce application 
processing times and costs. Utilities have developed successful in-house tools, and third-party 
solutions are also used throughout the industry. PG&E and SDG&E were both early adopters of 
online application systems, and they realized significant cost savings from the systems with 
nearly immediate payback. The Smart Electric Power Alliance (SEPA) found that more than 
50% of utilities with online application systems were able to process applications in less than 2 
weeks, compared to less than 20% of utilities without online systems (Figure 3) (Makhyoun, 
Campbell, and Taylor 2014). 
 
Figure 3. Application processing times: manual processes versus online 
Figure reproduced with permission from (Makhyoun, Campbell, and Taylor 2014) 
The benefits of implementing an online system may not outweigh the cost in all cases, 
particularly in areas with low interconnection activity. These systems are a significant 
undertaking in terms of time and resources. Utilities must also consider how they are 
implemented. Some utilities have developed online application systems in-house, while others 
have purchased off-the-shelf products. Major benefits of off-the-shelf products include the speed 
of deployment and flexibility. For example, PG&E initially developed a successful online system 
in-house but eventually transitioned to an off-the-shelf solution that could adapt to regulatory 


---

Page 18

---

9 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
changes more efficiently. Integrating these systems with existing business systems and data 
streams introduces cybersecurity risk that must be mitigated. 
 Implementation Considerations 
A number of factors may impact whether a certain improvement is feasible or if it is the right fit 
for a utility. The following are a few factors a utility may need to consider before implementing 
improvements to application-management procedures: 
• Regulation—In states with standardized interconnection forms and processes, the utility 
may require approval from regulators prior to making any changes to application 
documents or processes. In this case, the utility may need to engage with regulators to 
discuss issues with the current methods and evaluate the process more formally. In some 
cases, regulators may initiate changes to application process. For example, regulators in 
New York established a requirement for all IOUs to deploy an online application system 
(NYPSC n.d.).  
• Resource availability—Availability of staff or operational funds may dictate what 
improvements are feasible. Utilities with limited resources may consider deploying 
improvements in phases, targeting low-cost, high-return opportunities first, or using more 
off-the-shelf tools. Assessing Opportunities and Challenges for Streamlining 
Interconnection Processes discusses several layers of interconnection improvements 
categorized by general resource intensity (EPRI 2017a). 
• Interconnection activity—Although fully automated application systems have proven 
their worth in highly active DER markets, these systems may be unnecessary in areas 
with very low levels of current and expected interconnection activity. Evaluating the 
level of interconnection activity and projected growth rate is an important first step in 
identifying whether improvements are needed. If increased interconnection activity 
causes issues like delayed processing time and increased cost, utilities may need to 
consider improving their systems.  
• Operational preferences—A utility’s values and operational preferences may drive 
decisions about which improvements are attractive investments. For instance, EPRI found 
that Lake Region Electric Cooperative (LREC), a rural co-op in Minnesota, prefers 
manual processes because it highly values the person-to-person interaction with its 
customers. Thus, it is hesitant to adopt automated processes that might lessen its personal 
relationships with customers. With a low level of interconnection activity, LREC may be 
able to maintain these processes. 


---

Page 19

---

10 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Side Box 1: The Importance of Data 
Data play an important role in many aspects of DER interconnection. Collecting and managing data 
are important to improving interconnection. Ensuring and verifying data integrity are critical and can 
be challenging. Importantly, data incoming from new systems—for example, advanced metering 
infrastructure (AMI)—should not always be assumed to be accurate.  
Key data issues related to different parts of interconnection are highlighted below. A few good 
practices across-the-board include: 
• Work towards machine-readable, standard data formats whenever possible. 
• Use clear and consistent data field definitions and include metadata with data sets. 
• When collecting data, provide example forms or responses. 
• Consider investing in dedicated resources to coordinate and manage data that may be 
dispersed across multiple business units within a utility 
It may also be useful to implement systems to record information observed or collected during the 
course of regular utility operations in a database, to build up data sets that can be used in the future. 
One possible example is recording data about settings on voltage-regulating devices in a central 
system when these settings are adjusted by workers in the field. The particular collected data that 
should be stored and managed will vary depending on the goals and needs of a particular utility. 
 
Application Processing
•Collect and store 
data on application 
forms that can be 
used to evaluate the 
effectiveness of 
different policies, 
programs, and 
systems/tools.
•Provide data to 
customers about the 
system that can help 
guide DERs into low-
cost/high-value 
locations.
•Provide customers 
and regulators with 
data on timelines 
and processing steps 
for interconnection.
Technical Screening
•Advanced technical 
screening using 
power-flow analysis 
requires data on 
load, grid device 
settings (e.g., 
capacitors and 
voltage regulators), 
and DER output or 
behavior. 
•Coordinate between 
departments so 
groups running this 
analysis can 
leverage data 
collected through 
different utility 
systems (e.g., OMS, 
ADMS) as relevant.
DER Deployment Forecasting
•Forecasters can 
utilize data sets 
from multiple 
sources, including 
utility and non-
utility data sources 
(e.g., census data, 
county data).
•Collect and maintain 
data sets that can be 
used to understand 
how policy and rate 
changes influence 
customer adoption 
to improve models 
in the future.


---

Page 20

---

11 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Side Box 2: Toward Streamlined Interconnection: The Relationship Between 
Different Tools and Application Activities  
Clearly defining the use cases up front for different tools and data sets in collaboration with 
multiple stakeholders—as well as using transparent, vetted tools and processes when possible—
can help ensure that these systems are designed effectively for the intended use and that they are 
actually utilized by utilities, developers, and/or PUCs. Providing easily findable information or 
materials on how different utility resources, data, and tools can be used by developers during 
interconnection is also beneficial. Xcel Energy’s “How to Interconnect” webpage gives one 
example of how these relationships can be illustrated (Figure 4). 
 
Figure 4. Mapping of different tools for identifying potential interconnection locations and 
interconnection application activities, from Xcel (2018) 
According to an Interstate Renewable Energy Council (IREC) report, early efforts to implement 
pre-application reports and hosting-capacity maps, for example in Hawaii and California, appear 
to be reducing the number of non-viable projects that seek to interconnect and positively 
redirecting projects (IREC 2017). In addition to being tools for identifying good locations for 
DER interconnection, hosting-capacity maps can be used as part of the application-screening and 
engineering-study processes, as outlined in Chapter 2. 


---

Page 21

---

12 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
2 Technical Screens for DER Interconnection 
Technical screening of systems that apply for interconnection is important for ensuring safe, 
reliable, and cost-effective interconnection. Once a utility receives a complete interconnection 
application, screens can be applied (as a series of quick-check questions), and the approval may 
be granted immediately. If the application does not pass this test, many states allow it to undergo 
a supplementary review to determine the need for a detailed impact study involving modeling 
and mitigation (Figure 2). The supplemental review1 process is discussed more below.  
2.1 State of Development 
Most technical screens used in utility interconnection procedures have not changed since 2005 
when FERC first published the SGIP (FERC 2005, FERC 2013). Many states have adopted or 
encouraged use of the FERC SGIP as part of their rules for regulated utilities, and most utilities 
that engage in DER interconnection have adopted all or most of the FERC-recommended 
technical screens. The FERC procedures involve a series of 10 initial review screens, which we 
discuss in more detail in this chapter of the report. If any of these technical screens are triggered 
(or tripped or failed), the DER interconnection application may be required to go through 
supplemental screens, as specified in FERC Order No. 792 in 2013. However, only a few states 
have adopted these supplemental screens to date, including California, Massachusetts, New 
York, Minnesota, Ohio, Illinois, and Iowa. 
At the time of publication, the screens associated with FERC SGIP were considered sound 
technical guidance for catching DER systems that might have negative impacts on the grid. The 
National Renewable Energy Laboratory (NREL) published a report with input from IREC in 
2012 that examined potential updates for the FERC SGIP (many of which were adopted), and it 
offers still-relevant suggestions on improving the technical screens used across the United States 
(Coddington et al. 2012a). Several of the SGIP screens are evaluated in detail, and suggestions 
are raised for consideration. This report was published prior to the FERC SGIP workshops, and 
thus some of the recommendations were incorporated into FERC Order No. 792 (FERC 2013). 
2.2 Current Practices and Emerging Solutions 
 FERC Technical Screens 
In this section, we detail the original technical screens published in FERC Order No. 2006 
(SGIP), explain the purpose of each screen, and note research on potential relevance to and 
accuracy for evaluating DER impacts. Although these screens may not fully capture potential 
DER impacts, they are used to flag possible impacts as part of the FERC SGIP, they are used in 
many state interconnection rules, and they are often part of the interconnection procedures at 
                                                 
1 If an interconnection applicant fails one or more of the Fast Track screens, many states’ procedures 
allow it to undergo “supplemental review” or “additional review” to determine whether it could interconnect without 
full study. In its most recent revision to SGIP, FERC integrated a more transparent supplemental review process that 
relies on three screens, including a penetration screen (Screen 1), set at 100% of minimum load. In most cases, if the 
proposed generation facility is below 100% of the minimum load measured at the time the generator will be online, 
then the risk of power back feeding beyond the substation is minimal, and there is a good possibility that power 
quality, voltage control, and other safety and reliability concerns may be addressed without the need for a full study. 
The other two screens allow utilities to evaluate any potential voltage and power quality (Screen 2) and/or safety and 
reliability impacts (Screen 3). 


---

Page 22

---

13 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
electric utilities. Each screen is referenced by the number used in FERC Order No. 2006 and 
again in FERC Order No. 792 (2013). Figure 5 provides a graphical overview of the 10 screens.  
2.2.1.1  
The proposed Small Generating Facility’s Point of Interconnection must be on a portion of the 
Transmission Provider’s Distribution System that is subject to the Tariff. (Note: “Transmission 
Provider” in this case is the electric utility that operates the distribution system). 
Explanation and comments—The interconnection application must be on the utility’s 
distribution system. This screen is used to direct projects connecting to networked transmission 
systems to the study process, because the remaining screens were not designed to evaluate 
transmission system impacts. 
2.2.1.2  
For interconnection of a proposed Small Generating Facility to a radial distribution circuit, the 
aggregated generation, including the proposed Small Generating Facility, on the circuit shall 
not exceed 15% of the line section annual peak load as most recently measured at the substation. 
A line section is that portion of a Transmission Provider’s2 electric system connected to a 
customer bounded by automatic sectionalizing devices or the end of the distribution line. 
Explanation and comments—Also known as the “Penetration Screen” or the “15% Screen,” 
this screen requires supplemental review or detailed impact studies when the circuit contains a 
sum of DER nameplate capacity that is equal to or greater than 15% of the peak demand on that 
feeder or line section. However, it is well understood that certain circuits have hosting capacities 
far below 15% of peak load, while others have hosting capacities far greater than 15% of peak 
load (Reno 2015). 
NREL led the writing and publication of a report on the 15% rule in 2013 that focused on 
alternatives to this screen (Coddington et al. 2012b). Some of these alternatives were 
incorporated into the supplemental screens of the first revision of FERC SGIP in 2013.  
2.2.1.3 
For interconnection of a proposed Small Generating Facility to the load side of spot network 
protectors, the proposed Small Generating Facility must utilize an inverter-based equipment 
package and, together with the aggregated other inverter-based generation, shall not exceed the 
smaller of 5% of a spot network's maximum load or 50 kW. 
Explanation and comments—This screen was developed prior to any other standards and codes 
that address DER on secondary networks, whether they be spot networks or area networks. IEEE 
1547-2018 as well as IEEE 1547.6 offer guidance for DER systems that would interconnect onto 
a secondary spot network distribution system or an area network distribution system. The first 
IEEE 1547-2003 barely addressed spot network interconnections, and completely left area 
networks for future standards to address. All secondary network distribution systems utilize 
“network protectors,” which include a relay function that trips on reverse power flow (intended 
to maintain the reliability of the network in the case of a fault). Preventing reverse power flow 
                                                 
2 See note above. “Transmission Provider” in this case is the electric utility that operates the distribution system.  


---

Page 23

---

14 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
onto secondary networks can be done, and there are numerous examples of successful DER 
interconnection onto secondary networks. However, it may be inappropriate to receive fast-track 
interconnection approval in this case, and thus this screen requires either supplemental review or 
a detailed impact study of the proposed DER. For very small DERs, fast-track approvals may be 
granted by the local utility if the risk of reverse power flow is minimal, or “de minimus” as noted 
in IEEE 1547.6, the recommended practice for interconnection onto secondary networks. 
2.2.1.4 
The proposed Small Generating Facility, in aggregation with other generation on the 
distribution circuit, shall not contribute more than 10% to the distribution circuit's maximum 
fault current at the point on the high voltage (primary) level nearest the proposed point of 
change of ownership. 
Explanation and comments—This screen is seeking to compare the contribution of fault 
current onto a circuit from DER and the utility system because of concern over protection of 
utility equipment and the coordination of the protection system. An alternative, effective screen 
for protection and protection-coordination issues has not yet been identified. 


---

Page 24

---

15 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Figure 5. FERC SGIP technical screens summary, including the additional considerations for PV 
(yellow box) from Coddington 2012) 
2.2.1.5 
The proposed Small Generating Facility, in aggregate with other generation on the distribution 
circuit, shall not cause any distribution protective devices and equipment (including, but not 
limited to, substation breakers, fuse cutouts, and line reclosers), or Interconnection Customer 
equipment on the system to exceed 87.5% of the short circuit interrupting capability; nor shall 
the interconnection proposed for a circuit that already exceeds 87.5% of the short circuit 
interrupting capability. 
Explanation and comments—This screen is evaluating the total fault current on a circuit to 
ensure that the utility source(s) and the DERs do not, in combination, exceed 87.5% of the short-
circuit equipment rating on the circuit. Many modern inverters, when tied to a faulted line 
section, have fault durations that are typically shorter than the durations of synchronous 
machines or the utility system, and they typically drop offline more quickly than traditional 
synchronous machines (Keller and Kroposki 2010). 
 
 


---

Page 25

---

16 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
2.2.1.6 
Using the table below, determine the type of interconnection to a primary distribution line. This 
screen includes a review of the type of electrical service provided to the Interconnecting 
Customer, including line configuration and the transformer connection to limit the potential for 
creating over-voltages on the Transmission Provider's3 electric power system due to a loss of 
ground during the operating time of any anti-islanding function.” 
Primary Distribution Line 
Type 
Type of Interconnection to Primary Distribution 
Line 
Result/Criteria 
Three-phase, three wire 
(Note: delta typ.) 
Three-phase or single-phase, phase-to-phase 
Pass screen 
Three-phase, four wire 
(Note: Gnd. Wye typ.) 
Effectively-grounded three-phase or single-phase, 
line-neutral 
Pass screen 
Explanation and comments—This screen is designed to flag any DERs that do not integrate 
well with the primary electrical system where several potential problems may arise for the utility 
system if improperly tied to the grid. If the primary distribution line serving the generating 
facility’s distribution transformer is single-phase and connected to a line-to-neutral 
configuration, then there is no concern about over-voltages to distribution provider’s, or other 
customer’s, equipment caused by loss of system-neutral grounding during the operating time of 
the non-islanding protective function. 
2.2.1.7 
If the proposed Small Generating Facility is to be interconnected on single-phase shared 
secondary, the aggregate generation capacity on the shared secondary, including the proposed 
Small Generating Facility, shall not exceed 20 kW. 
Explanation and comments—This screen is based on a typical secondary circuit in North 
America, and it may be an inappropriate value for many utilities that design and build their 
secondary services differently than other utilities. Many U.S. utilities continue to use 25-kVA 
transformers for residential use and single-phase services, and the FERC 20-kW rating specified 
in this screen was likely designed around typical services. Of course, some utilities have 
transformers and secondary wiring that would easily accommodate more than 20 kW, and some 
utilities would have problems with some systems that are smaller than 20 kW. In 2010, the Solar 
American Board for Codes and Standards (Solar ABCs) reported that, of the 32 subject-matter 
experts who responded to questions about the FERC screens, 26 suggested that this screen 
should be updated, because the 20-kW threshold seemed inappropriate for various reasons 
(Sheehan and Cleveland 2010). Ultimately this screen is meant to flag DERs that may cause 
overloads or voltage imbalances on the secondary conductors or the transformer windings, or at 
the customer/DER system point of common coupling (PCC). 
2.2.1.8 
If the proposed Small Generating Facility is single-phase and is to be interconnected on a center 
tap neutral of a 240 volt service, its addition shall not create an imbalance between the two sides 
of the 240 volt service of more than 20% of the nameplate rating of the service transformer. 
                                                 
3 See note above. “Transmission Provider” in this case is the electric utility that operates the distribution system. 


---

Page 26

---

17 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Explanation and comments—The vast majority of U.S. homes are served by 120/240-volt 
services that have a center tap neutral, and thus having any imbalance is unlikely because most 
inverters for residential use are rated for 240 volts. Early DER systems used a greater number of 
systems that operated at 120 volts, while most DER systems installed on residential rooftops 
today operate at the U.S. standard of 240 volts. Although it is acceptable to install a DER on a 
residential (or small commercial 120/240-volt system) rooftop with an inverter operating at 120 
volts, it is highly unusual today (based on discussions with inverter manufacturers, utility 
engineers, and UL standard technical panel members). Ultimately, inverters that produce power 
at 120 volts should probably not be connected to 240-volt electric service, because voltage 
imbalance is much more likely (a 240-volt inverter or DER should be used with 240-volt electric 
service), but it may occur and is allowed. 
2.2.1.9 
The Small Generating Facility, in aggregate with other generation interconnected to the 
transmission side of a substation transformer feeding the circuit where the Small Generating 
Facility proposes to interconnect shall not exceed 10 MW in an area where there are known, or 
posted, transient stability limitations to generating units located in the general electrical vicinity 
(e.g., three or four transmission busses from the point of interconnection). 
Explanation and comments—This screen points to the possibility that a utility may have 
known transient stability limitations. If a substation or utility area has posted transient stability 
limitations, this would generally require detailed impact studies that may include transmission-
level transient and dynamic studies. The 10-MW limit is a fairly high threshold, and a system of 
that size would likely trip other screens before this one (thus requiring detailed impact study). 
For many, this screen is of limited usefulness, and many utilities are not sure how to apply it or 
do not have information about known conditions. Solar ABCs reported that 24 of 33 subject-
matter experts suggested this screen be modified or removed because it is vague and 
misunderstood (Sheehan and Cleveland 2010). 
2.2.1.10 
No construction of facilities by the Transmission Provider4 on its own system shall be required 
to accommodate the Small Generating Facility. 
Explanation and comments—This screen is passed if there are no known needs to update the 
electric system for the distribution/transmission utility. This screen has been problematic in some 
places where it is applied strictly to include interconnection facilities or other minor changes 
(such as a fuse) that could easily be identified through the screening process and do not warrant a 
full-scale study process. Some subject-matter experts have observed that this screen can be very 
easily tripped, while others have noted that it is very difficult to suggest that construction is 
necessary without a detailed impact study. Alternative approaches have been developed in 
various jurisdictions, and this screen is often removed now. 
                                                 
4 See note above. “Transmission Provider” in this case is the electric utility that operates the distribution system. 


---

Page 27

---

18 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Supplemental Screens 
FERC SGIP also provides a Supplemental Review process for generators that do not pass the 10 
Fast Track screens discussed above. FERC Order No. 792 improved upon the original 
Supplemental Review process by adding timelines, screens, and fees following a model first 
developed in California and Massachusetts. The purpose of Supplemental Review is to provide 
utilities with additional time and resources to identify whether any of the issues identified by the 
failure of Fast Track screens can be resolved with limited additional review and thereby avoid 
the need for a full study process. Because the Fast Track screens are necessarily conservative, 
Supplemental Review has become a critical method for increasing the efficiency of the 
interconnection process for customers and utilities as higher penetrations of DG arise in a state. 
In particular, as DG penetration increases, the 15% of peak load screen (screen 2.2.1.2) will be 
failed frequently, and the Supplemental Review screens allow a utility the time to identify 
whether there are particular issues that would prevent a project from connecting safely and 
reliably if the aggregate generation on the circuit does not exceed the minimum load. 
The Supplemental Review screens are defined, but flexible. This makes the process clear enough 
that interconnection customers can determine whether it makes sense to go through the 
Supplemental Review process and to understand its intent and results, while allowing the utility 
sufficient flexibility to conduct the appropriate review before approving an interconnection. As 
long as the utility can articulate the technical concerns identified when providing the 
Supplemental Review results, it can require a system to proceed to full study where warranted. 
New York has recently taken steps to create more definitive screens that clarify, for customers 
and utilities, how the Supplemental Review analysis is to be conducted and eliminate some of the 
ambiguity and potential for disputes that arise with more open-ended screens.5 
FERC maintains that the actual cost of conducting these Supplemental Review screens should be 
borne by the interconnection customer, while some states use a flat fee approach. 
2.2.1.11 – Minimum Load Screen 
Where 12 months of line section minimum load data (including onsite load but not station 
service load served by the proposed Small Generating Facility) are available, can be calculated, 
can be estimated from existing data, or determined from a power flow model, the aggregate 
Generating Facility capacity on the line section is less than 100% of the minimum load for all 
line sections bounded by automatic sectionalizing devices upstream of the proposed Small 
Generating Facility. 
Explanation and comments—This screen evaluates whether the aggregate generating capacity 
on the line section, including the proposed generator, exceeds 100% of the line section’s 
minimum load. If so, the proposed generator must go on to full study. If the aggregate generating 
capacity is below 100% of minimum load, however, the utility applies the following two screens 
to ensure the generator can be interconnected safely and reliably. 
2.2.1.12 – Voltage and Power-Quality Screen 
In aggregate with existing generation on the line section: (1) the voltage regulation on the line 
section can be maintained in compliance with relevant requirements under all system conditions; 
                                                 
5 See Appendix G in NYPSC (2018).  


---

Page 28

---

19 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
(2) the voltage fluctuation is within acceptable limits as defined by Institute of Electrical and 
Electronics Engineers (IEEE) Standard 1453, or utility practice similar to IEEE Standard 1453; 
and (3) the harmonic levels meet IEEE Standard 519 limits. 
Explanation and comments—This screen identifies the key technical standards for voltage 
regulation and requires compliance with those standards for the screen to be passed. The screen 
verifies whether voltage is maintained within steady-state limitations and evaluates compliance 
with flicker, rapid voltage chance, and harmonics standards. 
2.2.1.13 – Safety and Reliability Screen 
The location of the proposed Small Generating Facility and the aggregate generation capacity 
on the line section do not create impacts to safety or reliability that cannot be adequately 
addressed without application of the Study Process. 
This screen then identifies a list of relevant factors that can be considered and allows the utility 
to consider other factors it deems appropriate, to determine potential impacts to safety and 
reliability in applying this screen. 
Explanation and comments—This screen gives utilities flexibility to identify a full range of 
possible technical considerations in the proposed interconnection. The screen provides a list of 
typical factors the utility might consider, which allows applicants to better understand the review 
process, but it does not require that each factor be applied in every circumstance. 
Since FERC adopted the updated Supplemental Review process in Order 792, numerous states 
have also moved ahead with this approach, including Illinois and Minnesota. It is expected that 
Supplemental Review will become a critical component of the review process in most states as 
they start to reach penetrations of 50% of minimum load on many circuits. 
 Emerging Solutions 
Because the impacts on the system can vary so significantly depending on the characteristics of 
the network and DER applying for interconnection, it can be hard to accurately capture potential 
system effects using technical screens based on rules of thumb. The use of supplemental 
screening, discussed above, can provide a more accurate sense of system impacts in some cases, 
but it can be more expensive and time consuming. Power flow modeling or hosting capacity 
analyses could also be used as an alternative to technical screens that may provide more accurate 
information about system impacts (see Side Box 3). However, such approaches require a 
significant amount of data and in-house modeling capabilities at utilities, and they may not be 
appropriate for all companies or all DER penetration levels. The potential appropriateness of 
different solutions for different situations is further discussed in Chapter 10. 


---

Page 29

---

20 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Side Box 3: Advanced Screening Approaches: Power Flow Analysis and Hosting 
Capacity Maps 
Power flow modeling may be used in lieu of technical screening to more precisely indicate potential 
DER impacts on the system. Power flow modeling can also be used for calculating hosting capacity and 
creating hosting-capacity maps, depending on the method used. Several different hosting-capacity 
analysis methods are available, each of which has pros and cons (Stanfield et al. 2017).  
Pepco Holdings Inc. (PHI) is one utility that has begun using power-flow modeling for evaluating PV 
applications in collaboration with Electrical Distribution Design (EDD). Its automated process for 
screening DPV applications is illustrated in Figure 6. However, this approach requires significant data 
and modeling capabilities as well as integration between different utility systems. This approach may 
become more viable for a larger number of utilities in the future.  
 
Figure 6. PHI process for automated DPV screening using power-flow modeling (Bank 2017) 
Step 1
• PV applications are submitted through PHI's online customer work request portal.
Step 2
• Once application is ready, it is identified for review by the automated PV Evaluation Service.
• PV Evaluation Service includes a screen based on state requirements and feeder restrictions anticipated by PHI.
Step 3
•The feeder model is retrieved, and all component settings are attached.
•Preexisting PV sites, preceding PV sites in the application queue, AMI load data, and Clear Sky PV output estimates 
are attached to the model.
Step 4
•A full set of engineering studies, including power-flow modeling, protection analysis, and other secondary network 
checks, are automatically executed to evalute the new PV application.
•All PV engineering studies are generally completed within 5 minutes once the application has been flagged for 
evaluation.


---

Page 30

---

21 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
3 Advanced Inverters 
Many DERs generate power as direct current (DC) and need a method to convert DC to the 
alternating current (AC) used on the grid and in homes and businesses. Inverters convert DC to 
AC and allow PV, battery, and other DC sources to supply local loads. For most PV systems, 
inverters also tie in to the grid and match the local voltage and frequency. These inverters are 
power-electronics based and were once very problematic for grid connection, with high levels of 
harmonics and other power-quality challenges. However, today’s inverters are much improved, 
and the advent of “smart” or “advanced” inverters promises additional capabilities.  
3.1 State of Development 
Most inverters tied to the North American grid since 2003 (grid-tied inverters) have been listed 
under UL 1741, “Standard for Inverters, Converters, Controllers and Interconnection System 
Equipment for Use with Distributed Energy Resources.” UL 1741 was first harmonized with 
IEEE 1547.1 and IEEE 1547 so that interconnection requirements are in sync across these 
standards (see Side Box 4 for more information on the coverage and relationship between 
different standards). UL 1741 is intended for use with both standalone (not grid-tied) and grid-
tied power systems. Grid-tied inverters can serve local loads and, if there is excess power and 
energy, can export to the electric utility system. 
IEEE 1547-2003 required that inverters drop offline during a grid disturbance and wait until at 
least 5 minutes after the grid returns to normal operating conditions before resuming operation. 
This approach caused several notable cascading trips and blackouts in Germany—which had 
significant penetrations of renewables. This resulted in changes to standards for inverter 
behavior. In North America, inverters will soon be required to be capable of supporting the grid 
and riding through disturbances, just like bulk power generators are required to do. Advanced 
inverters can be used to support these functions. UL 1741 SA listed and labeled inverters are 
fully capable of meeting the voltage and frequency ride-through provisions.  
Inverters can be programmed 
to specify how they respond 
to external commands or to 
the status of the grid. First-
generation inverters (those 
harmonized with IEEE 1547-
2003) are still available 
commercially as of 2018 and 
are programmed to drop off 
the grid when there are 
voltage or frequency 
disturbances. These types of 
inverters likely will continue to be installed for several years, until states update their 
interconnection rules to align with the updated IEEE 1547-2018 standard and updated UL 1741 
standards (such as UL 1741 SA or future versions). 
In addition to voltage and frequency ride-through, advanced inverters can provide an array of 
other functions. From 2009 to 2012, a working group defined a set of smart inverter capabilities 
(EPRI 2014). UL 1741 SA—the standard now required in California, Hawaii, and Massachusetts 
Advanced inverters can also be used to achieve other goals as 
part of broader grid modernization or improvement efforts. 
For example, through the integrated use of advanced 
inverters and other legacy voltage-control devices, 
distribution utilities can regulate entire-feeder voltage and 
reduce energy consumption. One study shows the use of 
advanced inverters can help increase conservative voltage 
reduction (CVR) energy savings based on the simulation 
analysis of two utility distribution systems (Ding et al. 2016). 


---

Page 31

---

22 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
(and perhaps other states and territories)—includes seven required tests and two optional tests for 
advanced inverter functionality (UL 2018). Some of these functions, like improved voltage and 
frequency ride-through, are not optional. However, other capabilities, including active voltage 
support, are available functions in UL 1741 SA listed inverters, but they are not turned on or 
used in practice unless required by the utility. Additional advanced inverter functions may be 
used beyond those specified by UL 1741 SA (EPRI 2014). Even if inverters are UL 1741 SA 
listed, their settings specified by state standards (e.g., in California and Hawaii) can differ from 
the default settings in UL 1741 SA or IEEE 1547-2018. 
Adjusting advanced inverter settings and coordinating inverter operation can help avoid issues 
related to oscillatory behavior (inverter hunting). For example, combining local or autonomous 
control at fast time scales (seconds and sub-seconds) with control signals sent from a central 
operator at a slower time scale (e.g., minutes) could help coordinate between devices or better 
achieve certain objectives. Distributed energy resource management systems (DERMS) and/or 
ADMS may be able to aid in this effort. With proposed DERMS capabilities (Grid Management 
Working Group 2017), DERMS could modify inverter power factor (PF) and settings as well as 
dispatch or broadcast randomized response times for inverters, which would support these 
functions. 
 
Figure 7. Smart inverter functional categories 
Advanced inverters can be customer owned and controlled or owned and controlled by the utility 
to provide supported functionality. For example, pilots with utility-controlled inverters have been 
implemented by Arizona Public Service (APS) (Adhikari 2015), the Salt River Project, and the 
PG&E Electric Program Investment Charge (EPIC) project (PG&E n.d.). 
3.2 Current Practices and Emerging Solutions 
 Advanced Inverters for Voltage Regulation  
Advanced inverters can help regulate distribution by providing active and reactive power 
support. Advanced inverters may inject or absorb reactive power or vars. Injecting reactive 
• Inverters autonomously respond to local signals without input from a 
remote operator.
• Examples include volt-var and volt-watt functions.
Autonomous 
Functions
• Require direct interaction with an operator and fall into basic functions and 
direct control subcategories.
• A basic function example is remote disconnection from the grid. 
• A direct control example is a request to change PF of the inverter.
• IEEE 1547-2018 provides standards for interoperability between DER 
inverters and utility systems relevant to this mode.
Functions 
Driven by an 
Operator


---

Page 32

---

23 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
power increases the local voltage, while absorbing reactive power decreases the local voltage. 
This can provide an alternative to, or be used in combination with, other potentially expensive 
distribution upgrades for mitigating DER voltage impacts (see Chapter 5). For example, 
advanced inverters can help address over-voltage issues that are commonly observed as a first 
concern on U.S. circuits. Figure 8 shows that using advanced inverters with a lagging PF can 
mitigate this issue and significantly expand DPV hosting capacity, although the extent of 
expansion depends on circuit characteristics and DPV location on the feeder. Reactive power 
capabilities have been available in many inverters listed under UL 1741 and harmonized with 
IEEE 1547-2003 and successfully deployed in many DER systems. In general, if reactive power 
capabilities are used, the inverter is set at a specific PF or volt-ampere reactive (var). However, 
active voltage regulation was specifically forbidden in the previously IEEE 1547 standard, IEEE 
1547-2003. 
 
Figure 8. DPV hosting capacity of three test feeders with various advanced inverter functions 
Constant PF mode, voltage and reactive power control, and voltage and active power control are 
the three most commonly used advanced inverter voltage-regulation functions. Voltage and 
active power control is typically only used as a backup function for temporary abnormal 
conditions—for example, if voltage excursions outside of the American National Standards 
Institute (ANSI) Range B voltage limits occur—rather than the primary voltage-regulation mode 
under normal conditions. This is done to minimize real power curtailment and associated effects 
on DER project economics, as discussed below. 
According to IEEE 1547-2018, other functions including active power-reactive power mode and 
constant reactive power mode are also required as normal DER operating performance categories 
(see Chapter 4 and Figure 13). Other than these functions, some advanced inverters can also 
accept direct real and reactive power (P/Q) setpoints from an operator (Figure 7), which may be 
sent or updated at different time frequencies and using various approaches to determine the 
setpoints. 
Constant PF mode—In this mode, the inverter operates at a constant PF, which is typically not 
lower than 0.90 so the reactive power does not exceed 44% of the nameplate apparent power 
rating. Constant PF mode with a PF = 1 (unity PF) setting is usually the default mode of the 
installed DER as well as the default mode in standards. The disadvantage of this mode compared 


---

Page 33

---

24 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
with volt-var, volt-watt, or volt-var plus volt-watt (discussed below) is that vars are provided 
even when the voltage is normal, introducing unnecessary reactive power flows into the system 
and potentially reducing the real power output of the DER unnecessarily (see Section 3.2.2). 
Voltage and reactive power control (volt-var control)—Using this function, the inverter can 
actively control its reactive power output as a function of voltage following a voltage-reactive 
power piecewise linear characteristic (volt-var curve, Figure 9). For most practical applications, 
the volt-var curve is predefined, and the advanced inverter operates in an autonomous mode.  
 
Figure 9. Example volt-var curve 
In Figure 9, Vref specifies the reference voltage considered “normal” or desirable. The location 
of the inverter on the circuit (e.g., whether it is near the substation or a voltage regulator) can 
influence the appropriate Vref value. Vref can also be adjusted based on the application of the 
smart inverter control. For example, during normal operation, the voltage should be kept near the 
nominal value: Vref = 1.0 per unit (p.u.). For other applications, a different Vref may be 
desirable. For example, implementation of CVR, which lowers the distribution voltage to reduce 
energy consumption, may use a lower Vref such as 0.96 p.u. In addition, some commercial 
ADMS products can compute optimal voltage setpoints for Vref, so smart inverters can adjust 
their power output accordingly. Disadvantages of volt-var control include the potential for 
control interactions or oscillatory behavior, which can have control interactions and may provide 
or consume vars unnecessarily at locations where the voltage with not be affected (e.g., feeder 
head-end). 
Voltage and active power control (volt-watt control)—In this mode, the inverter can actively 
control its active power output as a function of voltage following a voltage-active power 
piecewise linear characteristic (volt-watt curve, Figure 10). As with volt-var control, most 
practical applications operate advanced inverters under volt-watt control in an autonomous 
manner. Volt-watt is also commonly used, although typically in combination with other 
functions as an “emergency backup”; for example, volt-var or constant PF are used for regulation 
unless the voltage moves into an abnormal range, in which case volt-watt control activates. In the 
IEEE 1547-2018 standard, the lowest allowable threshold for use of volt-watt is the threshold 
between ANSI Range A and ANSI Range B, with the default setting at 1.06 p.u.. This approach 
is used to avoid excessive or unnecessary real power curtailment from the DER, which impacts 
project economics and can be problematic for developers. 


---

Page 34

---

25 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Figure 10. Two examples of volt-watt curves, generating active power only (left), both generating 
and absorbing active power (right) 
Active power-reactive power mode—Under this mode, the advanced inverter actively controls 
its reactive power output as a function of the active power output following a target piecewise 
linear active power-reactive power characteristic (Figure 11). This mode can help manage the 
system PF within a certain range without injecting/absorbing substantial var/reactive power, as 
may occur with other modes. However, it can be challenging to define a very 
effective active power-reactive power curve to solve voltage problems, because under this mode 
the inverter is not responding directly to voltage or frequency measurement. Currently, this mode 
is rarely used in practice. 
 
 
Figure 11. Example active power-reactive power curve 
Constant reactive power mode—In this mode, the inverter maintains a constant reactive power 
output (injection or absorption). This is similar to constant PF mode in that vars may be provided 
when voltage is normal, and they are not required. However, it is also relatively simple to 
implement. 
 Real Power Reduction or Curtailment Using Autonomous Advanced 
Inverter Functions 
The total amount of reactive power that can be provided without reducing or curtailing the real 
power output of a DPV system is constrained by the fact that the square of the apparent power 
(in kVA) is equal to the sum of the square of real power output and the square of reactive power 


---

Page 35

---

26 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
output. Inverters can be oversized, with the inverter kVA rating exceeding the DPV system 
rating, allowing for headroom to provide reactive power without reducing real power output. In 
previous practice, however, inverters have typically been undersized when installed compared to 
the array size, owing to the overall DPV system cost structure (Fu et al. 2017). Even with an 
inverter that is not oversized, however, the inverter may be able to provide reactive power during 
certain times without reducing real power output, because the actual real power output of the 
array is sufficiently below the rated power of the array. This may occur, for example, if the 
inverters are installed in a location and time (e.g., winter, or during cloudy days) where the 
irradiance is below that at which PV panels are rated (1,000 W/m2). 
In some cases, however, supplying reactive power will limit the real power output of the system. 
Research conducted on the Hawaiian Electric Companies’ (HECO’s) system provided 
information on how real power output may be curtailed in volt-var and volt-watt modes 
(Giraldez et al. 2017). Even with very high DPV penetrations, 87% of customers with volt-
var/volt-watt hybrid controls (where volt-watt is activated only once the voltage goes outside of 
ANSI Range A limits) experienced annual energy curtailment of 1% or less, 11% experienced 
curtailment of 1%–5%, and the other 2% experienced curtailment of 5%–10%. In the HECO 
study, curtailment was less than 0.5% for 95% of DPV customers and less than 5% for the 
remaining customers for lower penetration levels (Giraldez et al. 2017). European studies have 
found similarly low levels of curtailment required when using advanced inverters to mitigate 
voltage violations on distribution systems and expand the hosting capacity (Etherden and Bollen 
2011, Luhmann et al. 2015). 
 Overarching Notes about Using Advanced Inverters for Mitigating Voltage 
Violations 
There are overarching good practices for selecting the settings of advanced inverters. For 
example, certain parameter settings are known to cause undesirable behavior like hunting. These 
include the use of a very steep slope for volt-var or volt-watt curves, extremely fast response 
times, or intentional delays in the control system. It is also possible to create instability when 
using volt-var combined with volt-watt if the volt-var is in “active power priority mode,” 
meaning that active power output is prioritized over reactive power supply. IEEE 1547-2018 
takes both issues into account by defining reasonably slow default response times and 
eliminating “active power priority mode.”  


---

Page 36

---

27 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Side Box 4: Important Interconnection Standards and Codes 
A strong foundation of codes and standards is important for achieving safe, reliable, and affordable DER 
interconnection. Every electric utility should have an interconnection application and approval process that 
DG developers can follow, and every jurisdiction should have a building permit process for ensuring that 
DG systems are installed safely and properly. 
The following four standards and codes have been important for the rapid pace of U.S. DPV system 
deployment. There is a strong connection among these standards, because they are all typically codified in 
state rules for DER interconnection, although not all states have these rules at present. 
IEEE 1547 
The IEEE 1547 family of standards provides the critical foundation for interconnecting DERs to electric 
utility distribution grids. It establishes criteria and requirements for interconnecting DERs with electric 
power systems (EPS). It provides requirements relevant to the performance, operation, testing, safety, and 
maintenance of interconnected systems. 
UL 1741 
In the United States, UL 1741 is the standard to which all inverters and converters must be listed, and UL 
1741 is harmonized with IEEE 1547 and IEEE 1547.1 (the testing standard). This standard ensures that 
every inverter is manufactured, programmed, and tested to adhere to the interconnection standard, and 
generally inverters without the proper “UL 1741” label are not permitted to be connected to or operated on 
the distribution system. Any inverters that are not UL listed would require extensive study and testing 
through the steps laid out in IEEE 1547-2018 and IEEE 1547.1. Products listed under the UL 1741 family of 
standards are intended to be installed in accordance with the National Electrical Code (NEC), NFPA 70.  
UL 1741 SA refers to Supplement SA of the standard, which, in addition to UL 1741, allows for limited 
testing of advanced functions ahead of the 1547.1 revision. The requirements for functionality under UL 
1741 SA are set in a “Source Requirements Document,” e.g., California Rule 21 or HECO Rule 14H 
requirements.  
NEC 
The NEC is the electrical building code to which most DPV and other DG systems should be designed, 
built, and operated.1 All DPV systems should be designed to follow NEC requirements, and, when the 
systems are completed, they should be inspected to ensure that all NEC requirements have been followed. 
The NEC contains articles specific to DPV and other DG systems, but also contains many articles specific to 
the design of the non-inverter electrical system such as conductors and conduits, fuses and other protection, 
and grounding. 
ANSI C84.1 
The ANSI C84.1 standard is adhered to by most electrical utilities, and it is used to set guidelines for 
maintaining voltage levels within tolerances that will support the integrity of the utilization equipment 
served by the EPS. The ANSI C84.1 “Range A” is most often used to set the parameters to be “nominal 
voltage +/- 5%.” Equipment will perform best when operated inside Range A, and it may be damaged if 
operated outside that range for an extended time (see ANSI C84.1 for specifics). DPV systems can impact 
voltage levels, typically causing higher voltages, and ANSI C84.1 helps define the range for proper 
operation of all utilization equipment and DG. 
1Some large, ground-mount DPV may use other codes (e.g., National Electrical Safety Code, NESC) instead of NEC. 


---

Page 37

---

28 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
4 IEEE 1547 Standard (2003–2018) 
4.1 State of Development 
IEEE 1547 has been the de-facto standard for DER interconnection in the United States since the 
standard was published in 2003, updated to IEEE 1547a, and recently updated to the latest 
version IEEE 1547-2018. IEEE 1547 applies only to the PCC or local DER interface, in general, 
and that is typically at the main point of utility service. The revised standard covers other 
important system criteria such as the point of connection (PoC), which may be a significant 
distance from the PCC.  
IEEE 1547-2003 was considered a critical piece of the interconnection puzzle after passage of 
the 1978 Public Utility Regulatory Policies Act (PURPA) (Maloney 2016). The U.S. federal 
Energy Policy Act of 2005 (EPACT 2005) called for state PUCs to “consider” certain standards 
for electric utilities. Under Section 1254 of the act, “Interconnection services shall be offered 
based upon the standards developed by the Institute of Electrical and Electronics Engineers: 
IEEE Standard 1547 for Interconnecting Distributed Resources with Electric Power Systems, as 
they may be amended from time to time.” Thus, adoption of the standard was strongly suggested, 
although not mandated, by EPACT 2005.  
Most U.S. states have adopted IEEE 1547-2003, along with a handful of relevant standards and 
codes, as the legal requirement for interconnecting DERs to electric distribution systems owned 
and operated by electric utilities (Area Electric Power Systems or EPS). IEEE 1547-2003 was 
developed by an IEEE working group as the primary standard for interconnection in North 
America. It was generally seen as a “low-penetration standard,” and few members of the working 
group felt that DERs would play a prominent role in the future of grid generation. Because there 
was very limited experience with DG in large quantities, the original standard was designed to 
require the DG to drop offline during even minimal disturbances.  
As PV system costs dropped 
dramatically, there was a 
tremendous rise in the number 
and capacity of installed DPV 
systems around 2006–2010, 
which has continued through 
the present. Within a few years 
of the publication of IEEE 1547-2003, there was realization that the “low-penetration standard” 
would need to be significantly revised to accommodate the tremendous growth of DPV and other 
DERs. The revision efforts began in 2013 and have involved approximately 250 stakeholders. 
IEEE 1547 was amended in 2014 with IEEE 1547a, which contained three specific required 
capabilities for DERs—voltage ride-through, frequency ride-through, and active voltage 
support—that the working group considered as steps toward full revision of the standard, which 
occurred in 2018. Reflecting the increased penetration levels and complexity of DERs, IEEE 
1547-2018 is 136 pages long, compared with 16 pages for IEEE 1547-2003. Figure 12 shows the 
timeline of IEEE 1547 changes. 
The original terminology in the IEEE 1547 standard, 
“distributed resources,” was changed in the 2018 revision 
to “distributed energy resources.” The acronym was 
changed from DR to DER, which reduced confusion with 
demand response. 


---

Page 38

---

29 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Figure 12. Timeline of changes to the IEEE 1547 standard 
 Changes in IEEE 1547-2018 
The 2018 standard includes substantial changes from the original 2003 standard, including the 
following (not listed in any particular order based on importance or other factors): 
• DER size limitations—Elimination of the 10-MW cap on the standard’s applicability. It 
now covers any generation connected to distribution systems, and any reference to power 
is in volt-amps (a utility industry standard is kVA or MVA, rather than kW or MW). 
• Reactive power support—Requirements for DER to have leading and lagging reactive 
power capability, and several reactive control functionalities to be employed when 
coordinated with the local utility (and assuming the DER has the capability, such as with 
smart inverters). This reactive power capability will primarily be leveraged to support the 
local voltage conditions on the utility system, and it must be carefully coordinated with 
the utility while meeting all jurisdictional rules. 
• Ride-through requirements—Mandatory voltage and frequency disturbance ride-
through capabilities that vary depending on the type of technology. Three categories (I–
III) are described in the standard (and in Figure 13) depending on the technology and the 
location of the DER (some island systems may require category III, for example). 
Because of this capability, DERs can provide additional support to the bulk power grid 
during abnormal voltage or frequency conditions. Ride-through requirements and their 
necessity for supporting system stability and reliability are also discussed in Chapter 3. 
These updates were considered a key part of the revision from the 2003 standard. 
• Bulk system support—Primary frequency-response functionality to allow DERs to help 
mitigate frequency disturbances on the bulk power system, similar to bulk power 
generator requirements. 
• Protection coordination—Clarification for the need to coordinate DERs with feeder 
reclosing to prevent reclosing into unintentional island conditions or phase differences. 
2003
IEEE-1547 first 
published
2014
IEEE 1547a (Amendent 1) 
published, adding three important 
provisions: voltage ride-through, 
frequency ride-through, and active 
voltage response
April 2018
Full revision of the 
IEEE 1547 standard 
approved and 
published. 


---

Page 39

---

30 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
• Power quality—Updated power-quality requirements that address the power-electronic 
technology (smart inverters) available with many types of DERs. The power-quality 
clause in the standard includes significantly greater detail and updated references to 
power-quality standards. 
• Interoperability requirements—Interoperability requirements that will allow DERs to 
be integrated into distribution systems with automated controls and updated switching 
and reclosing schemes. 
• Testing and modeling—Testing that will characterize short-circuit current 
characteristics of inverters and other technologies. This will also improve modeling 
programs that seek improved DER models for various applications.  
• Secondary network distribution systems—Greater capability to interconnect to 
secondary network distribution systems (networks). Both “spot networks” and “area 
networks” are now addressed in Clause 9 of the standard.  
• Function prioritization—Capability to specify the priority of various DER functions. 
• Open phases—Capability to detect open-phase conditions for DER systems. 
• Default and adjustability—DER control and trip settings with both default settings and 
a wide range of adjustability for many technologies. 
• Communication standards—Communications interfaces with a standardized, non-
proprietary design. 
• Anti-island prevention—Improved anti-islanding detection. However, the detection and 
trip time of 2 seconds (or less) remains as in the original standard. 
Figure 13 illustrates two important concepts within the new IEEE 1547-2018. Category A and B 
settings for voltage regulation help support the grid during normal conditions and allow utilities 
and DER vendors to leverage the technical capabilities of smart inverters to help regulate 
distribution voltages, an important function for all electric utilities. Category A is required of all 
DER systems, while Category B would require wider regulation capabilities and would likely be 
applied to advanced inverter technologies. 
Categories I, II, and III are specific to voltage and frequency ride-through capabilities during 
abnormal conditions. Similar to the logic differentiating Categories A and B, Category I provides 
the most essential bulk system needs and applies to all state-of-the-art DER technologies, 
whereas Category II provides for all bulk system stability/reliability needs, avoids tripping for a 
wider range of disturbances, and considers fault-induced delayed voltage recovery. Category III 
provides the broadest set of capabilities, including additional capability for addressing 
distribution system reliability and power-quality needs and coordinating with existing 
requirements for very high DER penetrations (e.g., California Rule 21 and HECO Rule 14). 
Category III could be applicable, for example, to certain grids such as microgrids and islands 
(e.g., the Hawaiian Islands) that may see more voltage and frequency disturbances. 


---

Page 40

---

31 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Figure 13. Application of IEEE 1547-2018 performance categories (EPRI 2017b) 
 IEEE 1547.X Family of Standards 
Figure 14 illustrates several of the standards closely related to IEEE 1547. Some of these 
standards have language such as “must” and “shall,” while others are guides or recommended 
practices. Guides and recommended practices are generally not adopted as requirements in state 
rules and requirements, because they do not prescribe the requirements for DER installations and 
operations. 


---

Page 41

---

32 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
 
Figure 14. Overview of the IEEE 1547 family of interconnection standards (IEEE 2015) 
4.2 State Rules and Adoption of IEEE 1547 
Many states are now working to understand IEEE 1547-2018, and a few states are actively 
updating their standards to reflect it. Utility commissions, utilities, and other stakeholders will 
need to work together to ensure a common understanding of the standard and its implications for 
interconnection. For example, the Minnesota PUC formed a DER working group in 2016 to 
address interconnection, and Phase II (started in late 2017) has focused on the adoption of IEEE 
1547-2018 (the Minnesota PUC anticipated approval of the standard prior to the final IEEE 
balloting process and publication). 
State PUCs and non-
regulated utilities will 
need to review the 
existing state 
interconnection rules. 
The impacts that the 
revised standard may 
have on those rules, and the operations parameters of each utility, will need to be considered. 
Ensuring that all inverters comply with IEEE 1547-2018, via UL 
1741, is critical for helping to maintain system stability (e.g., 
because of voltage and frequency ride-through capability), 
minimize harmonics, and allow for use of alternative set points 
without the need for expensive retrofits as DER penetration 
levels increase. 


---

Page 42

---

33 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
5 Strategies and Upgrades for Mitigating the 
Distribution System Impacts of DERs 
As discussed in Chapter 2, DERs can impact the voltage, power quality, and protection 
coordination on distribution networks. If negative impacts are anticipated or observed, action is 
required to mitigate these effects. These mitigation measures may include the use of advanced 
inverter functionality (discussed in Chapter 3), changing the settings of existing devices on the 
distribution network, or upgrading or installing new equipment on feeders or at substations. This 
chapter provides an overview of approaches to mitigating distribution-level impacts. However, 
coordinating across transmission and distribution systems may be required at high DER 
penetrations to handle back feed at the substation. 
DERs do not always trigger distribution system upgrades. Individual small residential and 
commercial systems typically do not require upgrades, although clusters or aggregations of 
systems may, and even large systems do not always cause problems (Bird et al. 2018; Sena, 
Quiroz, and Broderick 2014). The impacts depend significantly on the location, type, and control 
modes of the DER, in addition to the characteristics of the distribution system. In some 
scenarios, DER can actually help to defer distribution and/or transmission system upgrades that 
would otherwise be required. Several efforts are underway (Pathways to an Open Grid: O’ahu 
2017) to develop frameworks for estimating this deferral value, but there is currently no 
consensus best practice. Current approaches often involve identifying specific substations and 
feeders with planned upgrades and doing a detailed, temporal assessment on potential for 
different DERs to defer those upgrades. Additional discussion on upgrade deferrals and 
understanding of locational value of DERs is included in McAllister (forthcoming). 
5.1 Current Practices and Emerging Solutions 
 Current Typical Strategies and Upgrades for Mitigating DER Impacts on 
Distribution 
Table 1 describes mitigation strategies and upgrades typically used today to address different 
system violations that may occur owing to DER deployment. Mitigation strategies or upgrades 
are typically determined during the interconnection study process. The last system triggering the 
upgrade is typically responsible for these costs. Issues around allocation of costs for these 
upgrades are discussed in Chapter 6. 
Although some of these solutions are novel, they largely rely on traditional types of distribution 
network equipment. Which solutions are most appropriate depends strongly on the specific 
characteristics of the feeder (e.g., network or radial, electrical properties, existing equipment), 
the type and operating mode of the DER, and the location of the DER. More discussion of 
system impacts and these mitigation solutions can be found in Seguin et al. (2016). In addition to 
mitigation via traditional utility network equipment, PV inverters with alternative PF set points 
can be used to provide reactive and active power control and significantly expand hosting 
capacity, as discussed in Chapter 3. 


---

Page 43

---

34 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Table 1. Typical Solutions Used Today to Mitigate Effects of DER on Distribution Systems 
Mitigation Solution 
Applicable Violations 
Key Considerations and Notes 
Use alternative PF set 
points for the DER, for 
example, non-unity PF or 
advanced inverter functions 
for var and watt control  
• High or low voltage 
• Voltage flicker at PCC 
• Low to no cost if set at install. 
• Ability to mitigate voltage problems 
depends on the fraction of advanced 
inverters on the system. Retrofits of 
old inverters are typically 
prohibitively expensive. 
• At high penetrations, advanced 
inverters may need to be used in 
concert with other voltage-regulation 
solutions to fully mitigate DER 
impacts. 
• Legal and commercial constraints 
should be considered. 
• Utility ownership and/or control of 
advanced inverters is possible, 
being piloted. 
Modify capacitor and/or 
voltage-regulator controls 
• Reverse power flow 
• High or low voltage  
• Voltage flicker at the device 
• Excessive device movement 
• Bidirectional or co-generation mode 
for desired operation with reverse 
power flow. 
• Modifying device bandwidth may 
help with voltage flicker. 
 
Move voltage-regulating 
devices 
• Voltage flicker at the device 
• High or low voltage 
• Need to balance high- and low-
voltage conditions.  
 
Install new voltage 
regulators 
• High or low voltage 
• If adding new regulators, include 
bidirectional functionality.  
Modify load tap changer 
(LTC) tap set point 
• High or low voltage 
• Excessive device movement 
• Need to balance high- and low-
voltage conditions.  
 
Install LTC at the 
substation 
• High or low voltage 
 
Direct transfer trip (DTT) 
• Anti-islanding 
• Voltage supervisory reclosing 
relaying 
 
• UL1741 inverters pass anti-islanding 
tests, but interaction between 
inverters may not be tested. 
• DTT is required by utilities under 
certain circumstances, but not 
universally. 
Reconductoring 
• Thermal overload 
• Voltage flicker 
 
Upgrade protection 
coordination schemes 
• Protection 
 
Move protective devices 
• Protection 
 


---

Page 44

---

35 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Thermal violations are often the most expensive to mitigate. In a survey of PV interconnections 
in the western United States, the average cost of thermal upgrades was over $1.2 million, most 
often because of costly reconductoring in the face of line overloads (Bird et al. 2018). In cases 
where thermal violations occur, alternative emerging solutions—including the use of battery 
energy storage or dynamic real power curtailment—may be more cost effective and warrant 
further exploration. Similarly, substation upgrades can be expensive, so alternative, advanced 
solutions, where technically feasible, may be economically viable. Providing data to developers 
on existing substation equipment (e.g., presence of 3V06, on-load tap changer), thermal ratings 
of the conductor, and distance to three-phase networks may also help guide systems into 
locations where thermal violations and substation upgrades are less likely to occur. 
In addition to the solutions listed in Table 1, the size of individual DER units can be limited as an 
alternative to upgrades. Whether downsizing is an acceptable solution will depend on the 
upgrade costs relative to the expected revenue loss for the developer. Additionally, the DER can 
be installed at an alternative site with available hosting capacity or tolerable costs to mitigate any 
violations. As discussed in Chapter 1, providing initial data about which circuits have available 
hosting capacity or are unlikely to trigger expensive violations during the interconnection 
process may help guide DER to low-cost locations. 
 Preemptive Upgrades 
Upgrades that expand the hosting capacity may be undertaken preemptively, rather than in 
reaction to interconnection of specific systems. These are upgrades that benefit the entire system 
and not only a single installation. Examples of upgrades that fall into this category are installing 
3V0 at the substation, upgrading substation transformers (including installation of a new, larger 
transformer, adding an LTC, or otherwise upgrading transformer controls), upgrading voltage-
regulating devices to have bidirectional controls, and making certain protection coordination 
upgrades. This type of forward-looking or preemptive upgrade approach relies on the ability to 
forecast DER deployment (see Chapter 7), and it can be difficult to determine and target these 
investments to provide the greatest value to all customers. Preemptive upgrades are further 
discussed in Chapter 6.  
 Emerging Mitigation Strategies  
Several emerging solutions present attractive alternatives to traditional upgrades in certain 
circumstances: 
Battery energy storage—Batteries are a DER and can cause system violations themselves in 
certain modes of operation. However, batteries can also be used as a mitigation strategy, either 
standing alone or in combination with other upgrades. They can provide a wide range of 
functionality, and costs are decreasing rapidly. New York has suggested that batteries may be a 
good option to deploy at flexible interconnection sites to decrease curtailment risk (REV 
Connect 2018). HECO has found that using BTM storage to avoid export from PV systems can 
significantly decrease the cost of distribution system upgrades as penetration levels grow, 
although the batteries themselves come at a cost for the customer. In fact, if batteries are used 
without export, this alleviates all distribution violations and negates the needs for upgrades but 
can also significantly reduce load and impact utility revenues. In addition to operation focused 
                                                 
6 3V0 is ground fault (zero-sequence) overvoltage protection 


---

Page 45

---

36 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
on mitigating distribution interconnection constraints, operating modes can include operation as 
an energy and/or reserve resource, energy regulation, customer islanding, or market participation 
and/or value stacking as part of a larger DERMS system. The ability of a battery to alleviate 
distribution interconnection constraints will compete with these different uses, so examining and 
incentivizing this operating mode is critical if the battery will be relied on for this purpose. 
PG&E outlines some of its experience using batteries for transmission and distribution cost 
reduction (PG&E 2017a). Xcel Energy has a pilot on the use of storage deployed both on the 
distribution feeder and BTM for voltage regulation and peak shaving (Chacon 2017). APS has a 
similar pilot with storage deployed at the neighborhood level (Adhikari 2015). Results and best 
practices from these pilots are still emerging. 
D-STATCOM and D-SVC—Static synchronous compensators (STATCOM) and static var 
compensators (SVC) have been used to provide reactive power support on transmission systems, 
and they are now being applied to distribution systems, where they are referred to as D-
STATCOM and D-SVC. These technologies can be used to provide or absorb reactive power 
and mitigate voltage violations. This includes use to provide fast-acting reactive power and 
mitigate flicker or transient over-voltages. Ergon Energy (in Australia), which has experienced 
very high penetrations of DPV, has deployed several D-STATCOM systems, either standing 
alone or in combination with advanced inverters (Codon 2016). Ergon Energy found that D-
STATCOM can regulate voltage and is less expensive than traditional approaches for mitigating 
voltage violations, and the utility provides insights on good practices for siting these systems. 
Flexible interconnection/active network management—Flexible interconnection refers to the 
ability of a developer to avoid upgrades by accepting that its system may have real power 
curtailed as necessary to avoid system violations. This option has been explored extensively for 
interconnection of variable renewable energy resources in the United Kingdom (UK), where it is 
typically referred to as active network management (ANM). This can also be referred to or 
included in DERMS functionality. A good-practices guide for ANM based on these experiences 
has been developed (Energy Networks Association 2015). Although the UK distribution system 
is different than the U.S. system, many good practices from this guide may be applicable to or 
adapted for the United States. New York is piloting flexible interconnection called flexible 
interconnect capacity solution (FICS) with two DER projects—one 2-MW PV plant and one 
450-kW farm waste digestor—but no results are yet available (REV Connect 2018). 
Flexible interconnection can be acceptable when the expected curtailment risk is lower than the 
cost of system upgrades that would otherwise be required. One option is to offer the developer an 
option of flexible or firm interconnection (traditional system upgrades are used and there is no 
curtailment), because the preferred option will vary depending on the characteristics of the 
project, site, and developer. Principles of access (POA)—the rules for which generators are 
curtailed when and for how much—are critical for enabling developers to assess their 
curtailment risk and ensure the viability of this alternative. Both in the UK and in New York, 
last-in first-off (last generator interconnected is the first to be curtailed, with a fixed maximum 
curtailment level for each generator dictated by when it was interconnected), pro-rata (evenly 
distributed curtailment), or a combination of these approaches with generators placed in tranches 
with different levels of maximum curtailment according to when they interconnected have 
previously been the most acceptable POA. Experiences with different POA and associated issues 
are detailed in Baringa Partners and UK Power Networks (2012) and Kane and Ault (2014). 


---

Page 46

---

37 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Establishing a transparent method for curtailment risk calculations that is acceptable to all 
stakeholders is also critical when implementing this solution. 
Although FICS allows for avoiding traditional distribution system upgrades, there is a minimum 
investment required to be able to implement this solution at a utility, and a marginal cost per 
system associated with deploying an ANM platform. There are limited data on ANM or DERMS 
costs that could define this floor, and the costs can vary; some data are provided in NREL’s 
Distribution Grid Integration Unit Cost Database.7 
Advanced communication and control schemes—More integrated and advanced 
communication and distribution control schemes, for example ADMS and/or DERMS, can also 
be used to mitigate multiple impacts on the grid. In some cases, new grid equipment must still be 
installed (e.g., bidirectional voltage-regulator controls), and upgrades to the communication 
systems may be required depending on the architecture used and existing utility communications 
infrastructure. Requirements for the 
communications systems vary 
depending on the functionality, but 
HECO cites the following 
requirements for DER and storage 
management applications: 20 
milliseconds – 14 seconds latency, 
9.6–56 kilobits per second 
bandwidth, 90%–100% coverage, 
99%–99.99% reliability, 1-hour 
backup (Hawaiian Electric 
Companies 2014). High security is 
required for all communications 
infrastructures and applications (see Chapter 8). Interoperability can be a challenge for these 
systems, so implementing interoperable solutions early and holding vendors to certain 
requirements are important. Although there are several ongoing DERMS and ADMS pilots, best 
practices have not yet been developed for how to use these systems as an alternative to 
traditional upgrades, and their cost-benefit proposition compared to alternative integration or 
interconnection approaches as a function of penetration level is not yet fully understood. This 
will likely depend on the existing systems and resources of the utility as well as other goals that 
could increase the benefit of these systems. As with batteries, consideration must be given to the 
ability of DERMS or ADMS to alleviate system violations if competing with other objectives 
that may conflict.  
5.2 Looking Ahead: Key Considerations and Implementation Issues 
Today, the distribution infrastructure upgrades required for mitigating negative system impacts 
are typically evaluated as individual DPV systems apply for interconnection through the review 
and impact study processes. Systems triggering an upgrade are typically responsible for the 
associated cost (see Chapter 6). In the future, as the number of system interconnection 
applications grows, there is value in a more forward-looking, integrated assessment of 
distribution infrastructure upgrade needs across multiple systems or as a function of penetration 
                                                 
7 https://www.nrel.gov/solar/distribution-grid-integration-unit-cost-database.html  
DERMS functionality is still being defined. SEPA and the 
Grid Management Working Group recently published a 
document outlining proposed DERMS requirements 
(Grid Management Working Group 2017). DERMS may 
be usable in the implementation of FICS or to support 
more sophisticated advanced inverter controls. DERMS 
and ADMS could also be used in concert to optimize 
performance. Integrated consideration of different 
schemes and systems during the planning process could 
help ensure maximum benefit from these solutions. 


---

Page 47

---

38 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
level. For example, some mitigation options, including system-wide upgrades, may have a higher 
upfront cost but can be more effective at expanding hosting capacity, resulting in a lower overall 
cost per watt for interconnection upgrades. Additionally, particularly at higher penetration levels, 
one upgrade may not resolve all violations, so a suite of mitigation strategies is required. 
A few key changes are needed to transition to this forward-looking approach. Understanding 
whether certain system-wide upgrades (or even more focused preemptive upgrades, for example, 
3V0 at the substation) make sense requires the ability to estimate future DER deployment levels 
(see Chapter 7). Additionally, distribution planning and analysis tools must be developed that 
can effectively evaluate such a suite of solutions working in concert with legacy assets. These 
tools should also be able to accurately model the behavior of different types of DERs and their 
interactions. Finally, modeling that considers time-series behavior of DERs and time-dependent 
grid impacts can much more accurately evaluate the potential impact and effectiveness of 
different emerging solutions for mitigating system violations. However, this greatly increases 
analysis demands associated with interconnection or integration; leveraging existing tools, 
increasing data collection, and collaborating across organizations will likely be key to the 
feasibility of this approach, along with evaluating the required model resolution and time periods 
included in the model to achieve desired objectives. 
In addition to specific network characteristics, the costs of program design, development, and 
execution; modeled revenue expectations; the existing systems and capabilities of the utility; and 
utility preference/risk tolerance with respect to third-party or customer ownership or control will 
also come into play when determining which upgrade options are best for a given circumstance. 
Certain system upgrades, like ADMS, may be useful for mitigating the impact of DERs, but they 
also can be justified as part of achieving broader utility objectives. For emerging technologies—
such as batteries, D-STATCOM, or DERMS—declining technology costs should also be 
considered when making investment decisions. 
 


---

Page 48

---

39 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
6 Cost Allocation 
An important and longstanding issue for utilities and their regulators is how to allocate utility 
costs efficiently and equitably among customers. Many challenges arise when seeking 
approaches for allocating the costs of mitigating DER impacts in ways that can both increase the 
efficiency of the interconnection process and allocate costs in fairly and equitably. The process 
of assessing and assigning costs often leads to disputes and delays for larger DG projects. 
Stakeholder interests conflict, with each stakeholder vying to reduce its individual exposures to 
cost and risk. The following are two key questions related to DER interconnection cost 
allocation: 
1. How can the benefits that different stakeholders realize from grid upgrades be identified? 
2. How can upgrade costs be allocated efficiently and equitably to beneficiaries? 
DER interconnection cost-allocation approaches vary across the United States, because each 
utility is governed by different regulatory and legal rulings.  
6.1 State of Development 
Although allocation is an emerging issue for distribution system costs related to rising DER 
penetrations, practices for allocating transmission system costs have long been debated among 
stakeholders. Guiding principles for allocation of transmission system costs have emerged 
through rulemakings and court rulings, and these can inform DER interconnection cost allocation 
practices at the distribution level. 
A key principle is “cost 
causation,” such that “all 
approved rates [must] reflect to 
some degree the costs actually 
caused by the customer who 
must pay them” (K N Energy 
Inc. v. FERC 1992). Another 
expression of this principle is 
that those who benefit from a 
facility should pay for the 
facility. The Seventh Circuit 
Court of Appeals has 
commented on this concept in 
public utility ratemaking, stating 
that “to the extent that a 
[customer] benefits from the costs of new facilities, it may be said to have ‘caused’ a part of 
those costs to be incurred, as without the expectation of its contributions the facilities might not 
have been built, or might have been delayed” (ICC v. FERC 2009).  
One of the biggest challenges with cost allocation for DERs is estimating cost causation, 
including trying to isolate costs necessitated by serving DER customers compared to costs 
caused by other factors. For example, substation equipment or primary three-phase conductor 
This chapter focuses on issues around allocation of costs for 
upgrades required to interconnect DER without adverse grid 
impacts. Other interconnection costs required solely for a 
specific generator interconnect that cannot be used to serve 
utilities’ general customer population are not considered. 
Allocation of these costs is much more straightforward, and 
these are often covered by interconnection fees. They may 
include administrative processing, distribution engineering, 
metering, meter change, field inspection, and 
interconnection facilities (protection devices, transformers, 
and metering equipment required for a system to safely 
connect physically and electrically to the grid).  


---

Page 49

---

40 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
upgrades add headroom that later serves growth in customer loads or growth of future DER, but 
this can be difficult to calculate or predict. 
 The Conventional Cost-Causer-Pays Approach 
The conventional approach to allocating upgrade costs is commonly referred to as the “cost 
causer pays” method. Under this arrangement, the DER applicant is required to pay for all costs, 
including the full cost of distribution system upgrades deemed necessary to accommodate the 
project. Benefits of this method include the following: 
• It follows the principle of cost causation.  
• It provides a location-based signal that can discourage projects in locations with high 
upgrade costs, but not penalize those with low upgrade costs, thus lowering overall 
integration costs.  
• It is simple in execution. 
However, this approach has shortcomings that are causing many jurisdictions to consider 
alternative approaches. The main shortcoming stems from situations in which future projects also 
benefit from the newly upgraded circuit yet are not incurring any associated costs, putting the 
burden of paying for network upgrades entirely on the first DER applicant to trigger the need for 
a new facility (the cost causer). This is commonly referred to as a “free-rider” problem, when an 
entity or group can use a resource without paying for it. Beyond concerns of fairness, this can 
lead to other adverse implications considering the sequential order in which upgrade costs are 
allocated to projects in the interconnection queue: 
• Procedural delays—Applicants trying to evade upgrade costs may grind the 
interconnection queue to a halt for that circuit until a solution is found or the applicant 
drops out. The next applicant repeats the process until somebody eventually pays. 
• Project termination—Smaller projects may be unable to shoulder the financial burden of 
high upgrade costs, while larger projects may balk at the altered project economics. This 
may result in upgrades never being done, because they are not economic for any 
individual project, although they could be economic if the costs were spread across a 
group of projects.  
6.2 Emerging Solutions  
Here we review several alternative options for cost allocation that are currently being explored 
by some U.S. utilities. These approaches are still in their early phases, and clear best practices 
have not yet emerged. Developing interconnection procedures and cost-recovery rules that 
balance the tradeoffs between transaction efficiency and allocation equity will likely remain an 
ongoing challenge. Successfully addressing the challenge will depend on defining and 
prioritizing the primary objectives governing interconnection. Differences in solutions among 
utilities are likely to remain owing to differences in rulings among the many state regulatory 
commissions, municipalities, and electric co-ops that have legal jurisdiction over distribution 
system costs. 
 Group Study/Group Cost Allocation 
This method spreads upfront interconnection costs among a group of DER applications being 
evaluated at the same time. Multiple applicants are studied as a group, and identified upgrade 


---

Page 50

---

41 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
costs are spread across all projects within the group according to their relative contributions 
toward requiring the upgrade. This approach borrows from the cluster study process applied to 
transmission-level interconnections such as those conducted by the California Independent 
System Operator and other independent system operators and regional transmission 
organizations, through wholesale interconnection tariffs. 
Several states have implemented this method for projects under different tariff regimes, with 
Massachusetts being a notable example. In California, projects larger than 1 MW must pay for 
distribution system upgrades that are needed to accommodate their interconnection, and, under 
the electric Rule 21 tariff, projects that fail an “interdependency test” are put into a group process 
that studies the impact of multiple projects at the same time. Any costs for interconnection 
studies or upgrades are then charged proportionally to all the projects in the group.  
However, experience with the group study process remains limited. The core challenge 
associated with this process is that every applicant in the group must stick through the entire 
group-study process. This can slow the interconnection process as projects change their designs 
or applicants drop out. Studies may need to be repeated and costs reallocated among the 
remaining applicants, which could increase costs, add more time to the process, and cause more 
headaches for utilities and DER applicants. 
 Post-Upgrade Allocation  
This approach involves a single entity paying for the upfront costs of an upgraded facility. As 
new systems connect and use the upgraded facility, the entity that originally paid for the upgrade 
is reimbursed. Two variations of this method are currently being explored: 
Cost-causer post-upgrade cost-sharing allocation—In this method, the initial cost causer pays 
for the entirety of the upgrades caused by their request for interconnection. The original cost 
causer is then reimbursed by future projects that interconnect to the upgraded circuit. A 2017 
order by the New York Public Service Commission issued a “limited mandatory cost-sharing 
rule” for substation-level upgrades in excess of $250,000 that allocates the costs of qualifying 
upgrades to projects above 200 kWAC in size (NYPSC 2017). Under the order, the developer 
whose project causes a violation pays 100% of the qualifying upgrade costs. The original 
developer’s eligible costs are then defrayed by future projects that interconnect and benefit from 
the upgraded circuit. Costs are reimbursed by future developers through payments to the utility, 
which then redistributes costs to prior developer(s). The prorated share for each project is based 
on the fraction of each MW project size compared to the total size of aggregated projects 
benefiting from the upgrade. The order notes that this is an interim approach while a more 
comprehensive method for cost causation and allocation is developed. 
Utility prorated cost-sharing allocation—The other variant of the post-upgrade cost-allocation 
method is similar to the preemptive upgrade approach being piloted by National Grid (see 
Section 6.2.3) in that the utility pays the upfront costs of the upgrade. The difference is that, 
instead of pre-selecting locations for upgrades and marketing the new available capacity, the 
utility waits until a developer interconnection request triggers a needed upgrade. HECO 
previously used a group-study process (similar to that described above) under older DG feed-in-
tariff regimes. However, HECO found that the group-study process was difficult to implement 
efficiently and slowed the interconnection process for the many small residential DPV systems 


---

Page 51

---

42 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
that have been the primary driver of DG growth in Hawaii. The utility has since switched to a 
model that prorates the cost of required common-system upgrades for some projects on a $/kW 
basis dependent on the future available capacity freed up by that upgrade. This typically applies 
only to smaller projects—less than about 100 kW, which is the threshold for many of the DG 
programs—and to those that are not on HECO’s customer self-supply tariff. For larger projects 
that do not participate in a DG program, HECO follows the conventional cost-causer-pays 
model. 
 
 Preemptive Upgrade Cost-Sharing Allocation 
Although the post-upgrade allocation approach helps to fix the free-rider problem, challenges 
remain for smaller systems that may be first in line in the interconnection queue and may not 
have the upfront capital to support the upgrade cost, potentially delaying the interconnection 
process for future projects. To combat these issues, a New York Reforming the Energy Vision 
(NY REV) pilot being run by National Grid is examining a preemptive upgrade and cost-sharing 
approach (National Grid 2017). 
Side Box 5: Summary of Different Cost-Allocation Schemes in Use Today 
Several processes are being explored to alter the conventional cost-causer-pays model, each 
with its own advantages and disadvantages:
 
• Follows cost-causation principle, except when future DER customers 
benefit from prior upgrades without paying for costs. 
• Can slow down the interconnection process.
Cost-Causer Pays (Traditional approach)
• Fair sharing of upgrade costs, but slow and inefficient for many small 
projects.
Group Study/Group Cost Allocation
• Fair sharing of upgrade costs.
• Disadvantages small projects that are first in the queue and cannot afford 
upgrade costs.
• In New York, this is seen as an interim approach while a more 
comprehensive method for cost causation and allocation is developed. 
Cost-Causer Post-Upgrade Cost Sharing
• More efficient for smaller projects but can raise concerns about equity in 
cost allocation if there are not enough future DG projects.
Utility Prorated Cost Sharing
• More efficient for DG interconnection processes.
• Involves cost-recovery risks for the utility if there are not enough future 
DG projects.
Preemptive Upgrade Cost Sharing


---

Page 52

---

43 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
In this pilot, the utility pays for the initial investment in 3V0 ground-fault protection needed with 
higher penetrations of DG. Future projects that are larger than 50 kW and interconnect to the 
upgraded substation pay the utility a one-time prorated fee to cover the total cost of the 3V0 
upgrade. The prorated fee is evenly divided among projects by kW size. Costs are allocated 
based on common system upgrades and adjusted by a factor to represent the substation 
transformer’s capacity, which in part allows for a portion of the capacity to be used free of 
charge by DG projects of less than 50 kW. Although this approach helps reduce the burden on 
the first causer, it could shift the cost-recovery risk to other distribution customers if the fees 
from future DG projects do not cover the upgrade costs. To mitigate this risk, the utility is 
engaging in a marketing initiative to recruit DG developers to connect in the area.  
6.3 Potential Future Directions 
Moving toward an integrated distribution-planning paradigm may help achieve the desired 
balance between interconnection efficiency and equity in DER interconnection cost allocation. 
Several initiatives highlighted below may aid in this effort: 
• Improving interconnection cost estimations—This could help developers plan and 
execute PV installations more efficiently. It includes two key aspects: 
o Estimating future impacts and mitigation needs—Distribution system hosting-
capacity analysis and accompanying maps could improve the screening and 
interconnection study process by proactively informing future DG developers of 
estimated system impacts and potential mitigation solutions for a given DG 
deployment.  
o Improving cost certainty—Cost-certainty policies are being explored in many 
states to improve cost-estimation processes and reduce the risk of actual 
interconnection costs being significantly above initial cost estimates.  
• Exploring alternative mitigation measures—As discussed in Chapter 5, in lieu of 
costly upgrades to accommodate DG growth, some utilities are considering flexible 
interconnection arrangements that would curtail DG output to prevent system violations. 
This flexible interconnection solution could help avoid issues of upgrade cost allocation, 
but risks associated with long-term curtailment must be better understood and resolved, 
considering changes to the grid, connected loads, and other DG systems. 
• Improving DER adoption forecasts—More granular, robust, and accurate DER 
forecasts may help reduce the risk of future cost recovery given the uncertainty in future 
DER growth. Current approaches for predicting DER growth are discussed in the next 
chapter.  
Another possible form of cost allocation is rate-basing NEM upgrades and thus allocating 
upgrade costs to all customers. One example of this has occurred as part of NEM 2.0 in 
California, which added the requirement for an interconnection fee to recover costs for 
interconnection facilities. Although this approach can facilitate interconnection, its fairness and 
effectiveness is still under evaluation, and there is little experience with such solutions to date.  


---

Page 53

---

44 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
7 Predicting Future DER Growth 
Failing to incorporate accurate DER forecasts into long-term distribution and transmission 
planning can lead to wide-ranging consequences. In the case of over-forecasting, additional bulk 
generation resources may not be built owing to the predicted DER contribution to resource 
adequacy, leading to a less reliable and resilient system. In the case of under-forecasting, 
unnecessary generation resources and infrastructure could be added, resulting in an overbuilt, 
cost-inefficient system. Additionally, poor forecasts of DER deployment on specific circuits may 
lead to suboptimal distribution upgrades and potentially put the ratepayers or developers at risk 
for bearing high upgrade costs under the cost-allocation schemes discussed in Chapter 6. 
There are two categories of approaches to estimating future DER deployment (Table 2). Top-
down methods have historically been popular but are less precise. Bottom-up methods provide a 
step-change in data and methodological sophistication. 
Top-down methods are premised on the idea that modeling individual consumers is not 
necessary (or feasible) for forecasting territory-wide DER adoption. This assumption facilitates 
easier data collection, specification of relationships of interest, and model execution. At least 
three classes of top-down models have been used to forecast DER adoption: time series, 
econometric, and Bass diffusion. Time-series models extrapolate historical, cyclic data to future 
outcomes (Dong, Sigrin, and Brinkman 2017). They are probably the simplest forecasting model 
to use because, at minimum, they only require observations of historical deployment. 
Econometric models apply statistical methods to explain observed data and thus can be specified 
in many ways (Davidson et al. 2014; Bernards, Morren, and Slootweg 2018; Dharshing 2017). 
These models are typically intended to explain the historical impact of different factors on 
adoption, with less emphasis on prediction. Nevertheless, there are well-known methods for 
improving the predictive ability of econometric models, such as cross-folding (i.e., out-of-sample 
prediction). Data requirements are generally modest, but depend on the specification (e.g., 
historical independent and dependent variables for each region of interest). Bass diffusion 
models are currently the most frequently used method to forecast DER adoption (Wang, Yu, and 
Johnson 2017; Guidolin and Mortarino 2010). These methods are popular because they are easy 
to specify and are intended to represent the growth patterns of a new product. The Bass model 
follows a sigmoidal “S” shape of diffusion, where a new technology is adopted by a mixture of 
technology innovators (those that first uptake a new product) and imitators (those whose 
probability of adopting is proportional to the existing base of adopters). 
Bottom-up modeling seeks to model each consumer in the utility territory and the influence of 
their unique characteristics on adoption (Sigrin et. al. 2016; Adepetu and Keshav 2016; Agarwal 
et al. 2015; Mittal, Huang, and Krejci 2017; Rai and Robinson 2015; Zhang et al. 2015). These 
consumers, or “agents,” are allowed to evaluate DER (or not) based on their individual 
characteristics. The main characteristics needed include the agent’s electrical consumption, 
building and roof profile, and applicable retail tariffs as well as any other agent-level attributes 
that are known. The likelihood of adoption and relevant characteristics can be inferred by 
training the model on prior DER adoption. Data-driven techniques excel with big data and may 
break down with low sample-size situations, for example, creating bias in the model (over-
fitting) when training is done based on a small number of adopters who do not represent the 
population. 


---

Page 54

---

45 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Table 2. Methods Used for DER Adoption Forecasting 
 
Top-down 
Bottom-up 
 Time Series 
Econometric 
Bass Diffusion 
Pros 
Simple, easy to estimate 
and validate. 
High familiarity and use 
in other domains, 
explanatory value. 
Easy to specify, 
intended to model 
new technology 
adoption.  
Excels at 
spatial 
predictions, 
models unique 
attributes of 
consumers. 
Cons 
Does not represent 
inherent technical limits 
to adoption, for instance, 
that there are a finite 
number of households. 
Does not capture 
changes over time to 
adoption likelihood (e.g., 
decreasing capital 
costs). 
Better suited to predict 
aggregate adoption than 
individual or feeder-
level. Based on 
population central 
tendencies, which can 
fail to capture outliers or 
early adopters. 
Easy to overfit and 
can be sensitive to 
transient market 
effects. Relatively 
inflexible to add 
additional 
explanatory 
variables. 
Requires 
significant 
investment in 
data and 
computing 
resources. 
Data 
required 
At minimum, only 
requires observations of 
aggregate historical 
deployment over time. 
 
Very flexible in data 
used; modelers can 
incorporate nearly any 
data available that might 
explain observations. 
However, modelers 
should use standard 
statistics test to avoid 
overfitting. 
In its simplest 
formulation, only 
needs historical 
time series of 
adoption. Further 
specifications can 
incorporate impact 
of product prices, 
advertisement, or 
other time-varying 
features 
Modelers can 
incorporate 
nearly any data 
available at 
agent level: 
electrical 
consumption, 
building and 
roof profile, 
applicable retail 
tariffs, etc. 
Example 
use case 
Projecting adoption to fit 
an exogenous policy, 
such as a DPV carve-
out in a state 
Renewable Portfolio 
Standard. 
 
Understanding factors 
that explain historical 
adoption of DPV. 
Forecasting 
aggregate-level 
adoption in a utility’s 
territory. 
Generating 
household-level 
adoption 
probabilities for 
use in 
distribution 
planning or 
hosting-
capacity 
analysis. 
7.1 State of Development 
Top-down methods have been used extensively in the past, but they are increasingly being 
replaced by bottom-up methods, which offer two important improvements. First, top-down 
methods often struggle to distinguish between different types of customers, essentially treating 
everyone as the average. Of course, this is not realistic—some customers are more likely to 
adopt a novel technology, some care more about being environmentally friendly, some may be 
unable to afford rooftop PV, and others may see economic benefits. Second, top-down models 
are often “theory-driven,” meaning the modeler necessarily imposes the relationships between 


---

Page 55

---

46 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
the data available based on a given a priori theory of human behavior. A data-driven approach 
can be more agnostic, as the model seeks to uncover latent relationships in the data that better 
predict the variable of interest. Data-driven modeling is fundamental to the field of machine 
learning, which is widely understood to have superior predictive ability over theory-driven 
modeling. 
An emerging class of models seeks to combine the simplicity of top-down methods with the 
spatial precision of bottom-up methods. For instance, IOUs in California first forecast the 
territory-wide expected deployment and then disaggregate the forecasted quantity to individual 
distribution feeders (DRPWG 2018). Disaggregation methods can range widely from simplistic 
(proportional to population), to moderate complexity (weighted disaggregation based on 
demographics), to a data-driven approach. 
7.2 Current Practices and Emerging Solutions 
Bottom-up DER adoption models require significant investments in data and computing 
resources, so their uptake in industry has been slow. As the cost of developing analytics 
decreases, and vendor options increase, the prevalence of these models may increase. From their 
customer-billing data, utilities are already well positioned to populate these analytic platforms 
and may choose to populate additional fields over time. Suitability of customer rooftops is likely 
not well known to utilities, although it can be inferred through satellite data (Sigrin and Mooney 
2018, Gagnon et al. 2016) that are available in various forms through a variety of publicly 
available tools and data sets, such as GRiD8 and Google Sunroof.9 Finally, utilities may also 
choose to license demographic and market segmentation data from third parties. 
Utilities and other practitioners that use technology-adoption forecasts should acknowledge the 
inherent uncertainty of such analyses. Economic uncertainty relates to the techno-economic 
factors that impact model projections. Future capital costs, fuel costs, and policy mandates entail 
uncertainty, and they significantly affect results. Modeling uncertainty relates to the modeling 
choices made. Lack of available data or experience with emerging technologies might limit 
modeling choices. In all circumstances, modelers should run multiple scenarios, question their 
assumptions, consider sources of uncertainty, and consider interactive effects. 
The choice of a DER-adoption model for specific analyses is not always obvious and is still a 
topic of research. One clear finding, however, is that DER adoption should be accounted for in 
transmission and distribution plans. For instance, a recent NREL publication estimated that poor 
DER-adoption forecasts could cost utilities as much as $7/MWh of served load (roughly one 
quarter of current wholesale electricity prices) from suboptimal asset investments (Gagnon et al. 
2018). At low levels of DER penetration, top-down methods are likely acceptable—they are less 
costly to use, and their results may be accurate enough for this case. However, as DER adoption 
grows, utilities should consider investing in data collection and storage as well as in building an 
analytics platform around the data. Seen this way, DER-adoption models can be considered as 
strategic assets that allow the utility to develop better real-time business intelligence. 
                                                 
8 See https://griduc.rsgis.erdc.dren.mil/griduc. 
9 See https://www.google.com/get/sunroof/data-explorer/. 


---

Page 56

---

47 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
8 Cybersecurity 
The deployment of DERs increases the number of devices that are owned and controlled by 
consumers and third parties. To enable utility features such as remote access and remote control, 
grid-edge devices such as DERs are often also equipped with digital communications and control 
interfaces that pose an exploitable cyberattack surface. These types of cybersecurity concerns are 
not unique to DERs or the energy space—they increasingly arise in other sectors and for other 
technologies—but they warrant consideration as utilities interconnect these resources. 
Cybersecurity should be considered at the business process and network layers of the grid’s 
devices, communication channels, and higher-level applications. 
Typically, the cybersecurity risks associated with DERs on the distribution grid manifest in 
different forms: 
• At the operational level, smart inverters, weather sensors, and production meters are 
some of the devices that constitute DERs. The ubiquitous bidirectional communications 
capabilities of these DER devices increase exposure to potential cybersecurity risks that 
impact not only the traditional tenets of security—confidentiality, integrity, and 
availability—but also others, such as usefulness, accountability, and non-repudiation 
(Pender-Bey 2013). The standardized interoperability interface for DERs will offer the 
primary point of entry, and security measures must be taken to protect this interface from 
local or remote intrusion. 
• NEM DERs present the opportunity for manipulation for (predominantly) financial 
reasons (Wei 2017). This can be achieved physically by tampering with the devices or by 
attempting to intercept, modify, and/or destroy the data being logged by the devices and 
the onsite data-acquisition systems. 
• For utility use cases that enable remote DER control features such as microgrid 
controllers or smart inverters for active/reactive power control, volt/var optimization, and 
dynamic inverter operating mode configurations, the communication protocols used for 
such purposes might also be vulnerable to attacks that attempt interception, modification, 
and/or corruption of the control signal packets. 
• Higher numbers of third-party devices associated with DER deployment can also increase 
cybersecurity risk exposure if the devices are not sufficiently secure. Increased third-
party access to devices connected on the grid could also increase the risk of insider 
threats (Qi et al. 2016, Advanced Energy Economy 2017, Stamber et al. 2017). 
8.1 State of Development 
The best practices and standards for addressing these cybersecurity aspects of DER 
interconnections are still being developed. However, several industry standards and guidelines 
cover the cybersecurity challenges faced by DERs. These include the North American Electric 
Reliability Corporation (NERC) critical infrastructure protection (CIP), National Institute of 
Standards and Technology (NIST) 800-53 and NIST Cybersecurity Framework (CSF), 
International Electrotechnical Commission (IEC) 62351, and the Cybersecurity Capability 
Maturity Model (C2M2) by the U.S. Department of Energy (DOE). Some of these are explained 
below. 


---

Page 57

---

48 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
NIST—NIST has developed multiple standards to address cybersecurity in different 
applications. Standards germane to DER security include the following: 
• NISTIR 7628, Guidelines for Smart Grid Cybersecurity—This three-volume report 
provides an analytical framework for having effective cybersecurity strategies within an 
organization (Pillitteri and Brewer 2014) and includes coverage of related interoperability 
issues.  
• NIST SP 800-82, Guide to Industrial Control Systems Security—This guide provides 
instruction on important concepts and considerations for securing industrial control 
systems (NIST 2015). The second revision of this standard encompasses the supervisory 
control and data acquisition (SCADA) and distributed control systems (DCS) as well. 
• NIST Framework for Improving Critical Infrastructure Cybersecurity—This 
framework provides a general guide for how an organization may develop processes to 
manage cyber risk (NIST 2014). It consists of three parts: the Framework Core is a set of 
cybersecurity activities, outcomes, and informative references common across different 
critical infrastructures; the Elements of the Core detail the guidance to develop individual 
organizational profiles; and Profiles help an organization align and prioritize its 
cybersecurity activities with mission requirements, risks, and resources. 
• The other standards include NIST SP 1108, the NIST Framework and Roadmap for 
Smart Grid Interoperability Standards, Release 3.0; NIST SP 800-12, an Introduction to 
Computer Security: the NIST Handbook; and NIST SP 800-53, the Security and Privacy 
Controls for Federal Information Systems and Organizations. 
IEC: The IEC developed IEC 62351 to provide security for information exchange in power 
systems. This cybersecurity standard is intended to cover gaps in the other communication 
protocols or standards (Fries 2017, Cleveland 2012) and end-to-end security issues, including the 
following: 
• Communications network and systems security including transmission control 
protocol/Internet protocol (TCP/IP) – IEC 62351-3 
• Data and communications security including Manufacturing Message Specification 
(MMS) – IEC 62351-4  
• Data and communications security for IEC 61850 – IEC 62351-6  
• Data and communications security for network and system management – IEC 62351-7 
• Role-based access controls – IEC 62351-7 
• IEC 62443 is a family of standards to secure industrial automation and control systems, 
and it builds upon the IEC/ISO 27000 series. 
IEEE—The IEEE standard 1547-2018 states that it does not mandate specific cybersecurity 
requirements and that the requirements are based on mutual agreements specific to deployments 
and subject to regulatory restrictions of the corresponding jurisdiction. Specifically, IEEE 1547-
2018 does not mandate any specific cybersecurity requirements around front panel security, 
network security, or security for the DER local communication interface. However, it recognizes, 
at a higher level, that cybersecurity is a critical issue for DER deployments in terms of broader 
monitoring and control communications networks, and it includes some insights related to issues 
in system architecture and flexibility as well as testing. An example of a potential option for 
cybersecurity is to have the local DER communications interface disabled by default and to only 


---

Page 58

---

49 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
enable it through a password-protected front panel interface. This would prohibit access through 
the local DER communications interface until a secure network device is attached. 
Other IEEE standards that cover different aspects of cybersecurity include the following: 
• IEEE 1547.3—IEEE Standard for Interconnecting Distributed Resources with Electric 
Power Systems 
• IEEE C37.240—IEEE Standard Cybersecurity Requirements for Substation Automation, 
Protection, and Control Systems 
• IEEE 1686—IEEE Standard for Intelligent Electronic Devices Cybersecurity 
Capabilities 
• IEEE C118 series of standards—Data management and protection of synchrophasors 
• IEEE 1711—IEEE Standard for Serial SCADA Protection Protocol for Substation Serial 
Link Cybersecurity  
UL—UL is also working to develop standards for DER cybersecurity in collaboration with 
national laboratories, utilities, vendors, and manufacturers. Some of these efforts are currently 
under development, although some have been published.10  
DOE—DOE published two key documents to emphasize the need for cybersecurity in the 
domain of power:  
• DOE/DHS ES-C2M2—The electricity subsector cybersecurity capability maturity model 
• DOE/NIST/NERC RMP—The electricity subsector cybersecurity risk management 
process guideline 
These documents provide cybersecurity benchmarks for utilities and provide guidance on 
effective risk-management processes with consideration of specific organizational requirements 
and constraints. 
NERC—NERC has standards related to cybersecurity issues on the bulk power system. These 
existing standards do not directly relate to DERs, which are connected to distribution systems, 
but some best practices may be adapted from the NERC CIP series in developing approaches 
suitable for cybersecurity associated with DERs and distribution systems (NERC 2016). 
8.2 Current Practices 
Several widely accepted general cybersecurity frameworks have been applied to utility systems 
as a whole, including the integration of DERs. Defense-in-depth and defense-in-breadth are two 
examples. Defense-in-depth secures a domain by integrating protection tools into each layer, 
such that even if one layer is compromised, the subsequent layers are not readily exposed (Holl 
2003). The security for each layer comes from different vendors to avoid the same exploit 
breaking all layers. It has been applied to all seven logical layers of the Open Systems 
Interconnect (OSI) model (Small 2011, SANS 2001, Shamim 2014, Anzalchi 2018). Defense-in-
breadth leverages the knowledge about the breadth of the attack surface to offer protection. Its 
objective is to deploy asset- and protocol-specific protection tools at each logical layer of the 
enterprise to mitigate attacks that could originate from protected/unprotected networks, 
                                                 
10 See https://industries.ul.com/cybersecurity/ul-2900-standards-process. 


---

Page 59

---

50 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
trusted/untrusted devices, aware/unaware users, connected/isolated controls, and open-
source/proprietary protocols and interfaces (ECI 2017). A variety of other layered security 
models and methods are also in use today (Strom 2017, Sundararajan et al. 2018). Some current 
efforts in cybersecurity of industrial control systems generally, which also apply to DER, simply 
involve addressing known flaws in information technology (IT) – operational technology (OT) 
(IT-OT) network segmentation, passwords that can be cracked using dictionary attacks, and 
obsolete firmware versions. 
8.3 Considerations and Emerging Practices 
The following are key considerations for utilities looking to manage cybersecurity related to 
DER interconnection: 
• It is important to understand each device’s security requirements, identify the gaps in the 
existing security infrastructure, and then secure the highest-priority gaps through 
extensive testing prior to system integration. Once system integration is complete, 
periodic performance checks should also be conducted.  
• Data tagging, integrity validation, and anomaly detection are critical for data protection.  
• Anomaly-detection tools are needed to discover subtle data breaches by sophisticated 
attackers today, and this will help utilities ensure effective situation awareness, incident 
response, information sharing, and communications across their IT/OT infrastructure. 
These algorithm-based intrusion-detection tools will be implemented at the enterprise 
level (e.g., at the utility command and control center) where the data from field devices 
such as telemetry will be processed and checked for data quality before being subject to 
anomaly detection. Such processing can also happen on-the-fly through stream 
processing models, incorporated again at the central level of the utility.  
• Having uniform standards and enforcing them for vendors before connecting devices, 
rather than lowering requirements according to current vendor capabilities, is critical for 
minimizing cybersecurity risk.  
Although still in a nascent stage, standards, guidelines, and procedures around different aspects 
of cybersecurity are being actively developed, and some information is becoming available. The 
SunSpec Alliance (SunSpec) has been convening a cybersecurity working group that includes 
subgroups focusing on DER devices and server security, secure network architecture, access 
controls, and communication and protocol security. Testing procedures to secure the data and 
communications of DERs on the distribution grid developed through this working group are 
available on the SunSpec DER Cybersecurity website (SunSpec 2018). These procedures will 
eventually be translated into UL standards that could help utilities ensure that their multi-vendor 
environments have products that meet a minimum level of security. 
Table 3 shows a set of basic and advanced guidelines for cybersecurity of the networks 
interacting with DERs (not individual DER devices). These were developed based on a review of 
protocol-level DER vulnerabilities, the potential attacks that can exploit those vulnerabilities, 
and the available solutions to counter those threats (Sundararajan et al. 2018). The advanced 
security controls align with the emerging standards discussed above.  
 


---

Page 60

---

51 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Table 3. Basic and Advanced Security Controls Guidelines 
Basic Security Controls 
Advanced Security Controls 
• 
Network segmentation—By segmenting IT, OT, and management 
networks with access-control lists that avoid broadcast storms and 
establish hyper-quiet data links for effective intrusion detection, 
damage can be contained if one of the networks is compromised. 
• 
Systemic security—Secure the network systemically by 
implementing context- and signature-based intrusion detection and 
intrusion prevention systems as well as inline blocking tools. 
• 
Inline-blocking devices—To protect critical nodes from 
unauthorized access in a SCADA system within the OT network, 
inline blocking tools with transport layer token authentication and 
data diodes with hardware layer filtering of Modbus TCP messages 
can be used. 
• 
Intrusion-detection systems—Use context-based and signature-
based ID/IPS for network-based anomaly detection and business 
process security. 
• 
Selective encryption—Encryption creates an overhead for 
resource-constrained device communications where latency might 
also be critical. Therefore, selective encryption of the data will help 
utilities to minimize the processing overhead and application latency. 
Use of public key infrastructure (PKI) and digital certificates is 
preferred to guarantee a chain of trust using software and hardware 
policies. 
• 
Role-based access controls (RBAC)—Use access-control lists on 
networking switches with strict restrictions on the traffic based on the 
need to minimize unauthorized access of network devices, power 
systems appliances, and IT servers. 
• 
Port security—All used ports should be locked in by the media 
access control (MAC) addresses of authorized devices with initial 
connection to avoid device swapping for cyberattacks launched from 
inside the trusted networks of the organization. Also, disabling all 
unused ports on the firewalls and switches to eliminate unauthorized 
access is a sound practice. 
• 
Patching—Any out-of-date critical infrastructure creates 
vulnerabilities that can be exploited. By making periodic updates of 
software security patches, cyber-risks from known vulnerabilities of 
older software versions can be mitigated. 
• 
Least privilege—Give users access only to those applications they 
need to perform assigned tasks. 
• 
Visualization—Real-time monitoring dashboards that interactively 
visualize system events and logs ingested from heterogeneous 
devices in the DER ecosystem provide situational awareness. 
• 
Multi-factor authentication—Two-factor authentication gives users 
an added layer of security. 
• 
Strong usernames and passwords—All networked devices must 
be capable of avoiding brute force and dictionary attacks from 
hackers both outside and inside the network, which can be enforced 
using strong username-password combinations.  
• 
Activate transport 
layer security (TLS) in 
DER devices such as 
smart inverters and 
microgrid controller 
systems. 
• 
Implement session 
resumption when the 
session is severed for 
a time less than the 
TLS session 
resumption time by 
using a secret session 
key. 
• 
Implement session 
negotiation when the 
session is severed for 
a time more than the 
TLS session 
renegotiation time. 
• 
Use a message 
authentication code. 
• 
Support multiple 
certification 
authorities. 
• 
Terminate the session 
if a revoked certificate 
is used to establish 
the connection; this is 
done using a 
certification-revocation 
list. 
• 
Identify and terminate 
the session if an 
expired certificate is 
used to establish the 
connection. 
 


---

Page 61

---

52 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
These guidelines provide a roadmap for utilities to achieve improved cybersecurity for DERs. 
Additional consideration may be warranted in the future as increasing smart grid features may be 
implemented that could expose the component devices of the grid to potential cyber-physical 
attacks (INL 2016; Otuoze, Mustafa, and Larik 2018; Eder-Neuhauser et al. 2017; Ozgur et al. 
2017). 
 


---

Page 62

---

53 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
9 Storage and Solar + Storage Interconnection 
The amount of advanced energy storage, including batteries and flywheels but not pumped-hydro 
or large-scale thermal storage, currently connected to the grid is relatively small but growing 
quickly. As of the second quarter of 2018, the U.S. energy storage market grew 60% year-over-
year in deployed MW; in MWh, the market grew 200% year-over-year. The BTM storage market 
accounted for 75% of MW deployments during the second quarter of 2018, and nearly two thirds 
of MWh deployments. The total estimated storage deployment in 2018 is 393 MW, nearly half of 
which is connected to the distribution system (for both residential and non-residential 
customers). Energy storage deployment is anticipated to accelerate as costs continue to decline, 
favorable rate structures are adopted, and interest in diverse storage applications increases. GTM 
Research (2018) projects nearly 1 GW will be installed in 2019, rising to nearly 4 GW in 2023 
(Figure 15). As energy storage markets grow, transparent and non-discriminatory interconnection 
standards for storage—whether standalone or BTM energy storage systems paired with DPV 
(“solar + storage”)—can help ensure a timely, cost-effective, and efficient process for 
developers, customers, and utilities. 
 
 
Figure 15. U.S. annual energy storage deployment history (2012–2017) and forecast (2018–2023), 
in MW, from GTM Research (2018)  
Reproduced with permission from GTM 


---

Page 63

---

54 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
9.1 State of Development 
Best practices for storage 
interconnection are still emerging and 
evolving. Although some utilities can 
transfer lessons learned from 
interconnection of other types of 
DERs, storage has unique 
characteristics that must be 
considered for it to be effectively 
integrated into existing 
interconnection rules. First, energy 
storage can act as both generation (by 
injecting stored electricity onto the 
grid) and load (during its charging 
state). Second, energy storage can be 
controlled so it operates only when 
intended and with controllable power 
levels. Several states have begun 
exploring interconnection processes 
tailored to these unique 
characteristics. This section reviews the lessons learned and emerging good practices for 
interconnection specifically related to the characteristics of storage systems. 
9.2 Considerations and Emerging Practices  
Below are the key considerations that have been identified for adapting the interconnection 
process for energy storage specifically: 
• Include energy storage as part of state interconnection standards—The definition of 
“generating facilities” in interconnection standards often omits mention of energy 
storage, which can create ambiguity about the ability of a storage system to apply under 
the rules. FERC set an example for how to address this issue in 2013, when it revised the 
definition of “small generating facilities” in its SGIP (see Chapter 2) to explicitly include 
energy storage systems. This change resolved ambiguity regarding the applicability of the 
rules to storage systems (FERC 2013). 
• Include provisions to address different energy storage configurations and clarify 
what level of review each type of system will undergo—Energy storage technologies 
can be deployed under different configurations, which impacts the level of review 
required to ensure safe interconnection to the grid. For example, in the case of a BTM 
solar + storage system, the storage device’s role may be simply to capture electricity 
generated by the solar system during the day for use onsite after the sun goes down, 
rather than injecting it back onto the grid (i.e., “non-exporting”). Or it may be designed to 
export power back onto the grid for sale to the utility under net metering or other 
applicable tariffs. 
 
Energy storage systems can use control technologies to limit export to the grid under 
defined conditions, which can affect the review for potential system impacts in certain 
States (in green) taking steps to explicitly address energy 
storage in interconnection rules 
 


---

Page 64

---

55 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
states. Control technologies, along with contractual provisions in the interconnection 
agreement, can be used together to establish appropriate parameters for review. State 
interconnection standards are beginning to clarify the process for different potential 
configurations based on the expected function of the system, with specific clauses to 
reference different scenarios and provide clarity around how these systems are to be 
handled in the review and study process. States are addressing this with the inclusion of 
the following provisions in rules:  
 
o Addressing non-exporting and limited-exporting systems—Solar + storage 
systems primarily designed to serve onsite customer load may never or rarely 
export energy onto the grid (i.e., “non-exporting”). They may also be designed to 
never or rarely export energy beyond a certain limited power level (i.e., “limited 
export”). Recognizing that non- and limited-export systems have different impacts 
on the system than do full-export systems enables states to craft a more 
appropriate study process that looks only at the impacts that could actually be 
realized. For utilities to study non- and limited-export projects in different ways, 
however, they must be provided adequate assurances that the devices being used 
to control export have been tested to perform accordingly. States—including 
California, Hawaii, Nevada, New York, and North Carolina—are beginning to 
address these technical issues in their interconnection rules, putting parameters 
and limitations around these system configurations and providing more specificity 
about how these systems should be reviewed and studied. There is also an effort 
underway to define UL testing and certification procedures for these functions. 
o Addressing what generating capacity will be evaluated—When an applicant 
seeks to interconnect a standalone energy storage system or one co-located with a 
generating facility at a single site, most interconnection standards evaluate the 
request on the basis of the facilities’ aggregate, or maximum, nameplate capacity. 
However, this approach does not often reflect the operational characteristics of 
many energy storage systems. For example, a BTM solar + storage system 
designed to primarily serve onsite customer load may export far less energy onto 
the grid than suggested by the aggregate nameplate capacity of the system, and 
the system controls may prevent the system from exporting onto the grid 
altogether, or from having the storage and solar systems export simultaneously. 
Thus, in this instance, the aggregate nameplate capacity approach represents a 
“worst-case scenario,” versus the actual operational profile of the system. In 
recognition of this, some states and utilities are permitting the evaluation of 
interconnection requests based on net system capacity (versus aggregate system 
capacity) in combination with proposed use provisions that allow the applicant to 
define how the system will be used. Nevada’s Rule 15, for example, clarifies that 
the size of storage-coupled systems for the purposes of interconnection review is 
based on the net system generating capacity, as limited by the use of an inverter-
based or other control system (net nameplate rating). FERC’s interconnection 
process, for example, directs utilities to assume less than the maximum capacity if 
the applicant can demonstrate that it can limit the export so as not to “adversely 
affect” the safety and reliability of the electric system (FERC 2013). States that 
have taken a similar approach, to varying degrees, include North Carolina, South 


---

Page 65

---

56 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Carolina, and Minnesota. More concrete language may be necessary, however, to 
make clear how that determination may be made and to require the utilities to 
consider those limitations. 
o Addressing inadvertent export—Although energy storage system controls can 
avoid export onto the grid, there are times when non-exporting or limited-export 
systems will inadvertently export limited amounts of power for very short 
durations due to transient mismatch between system output and load consumption 
(when unanticipated load fluctuations occur). This can occur for customers whose 
systems are sized to closely match their load, or those with larger loads that may 
abruptly turn off while being supplied by the storage system. Importantly, 
inadvertent export is different from “islanding,” and distributed energy storage 
devices, like PV systems, are equipped with UL listed and certified inverters with 
automatic anti-islanding functionality that do not allow energy to be exported 
when the distribution system is deenergized (to protect utility personnel and 
anyone else that may come into contact with the distribution system). California, 
Hawaii, Colorado, and Nevada have addressed this issue by incorporating 
inadvertent export into their standards (SCE 2016, Hawaiian Public Utilities 
Commission 2015, Xcel 2017a, Xcel 2017b, Xcel 2017c). The rules have allowed 
up to 30 seconds of maximum export for any single event, with provisions to 
ensure total inadvertent exports remain within an acceptable kWh limit (which 
may be monitored by the utility), and to ensure that the system enters a “safe” 
mode if control system failures occur. Because these specific requirements are not 
fully addressed in IEEE 1547-2018, state rules and developing UL testing 
requirements must address them. 
o Specifying the most appropriate level of review, based on system design 
configuration and operational controls—In addition to incorporating the above 
definitions and technical parameters into rules, state interconnection standards are 
specifying how and if certain systems can interconnect and which level of review 
they should undergo. Ideally, the level of review reflects the system design, 
intended operational characteristics, and system controls. For example, non-
exporting storage systems could be reviewed in a more expedited manner by not 
applying the technical screens in the Fast Track process that relate to the amount 
of electricity sent onto the grid (IREC 2017). Interconnection rules in California, 
for example, clarify the appropriate review screen(s) for systems that are non-
exporting—and somewhat clarify screens for limited-exporting systems and/or 
those with certain inadvertent exports—within defined parameters. In California, 
non-exporting systems can currently skip the 15% of peak load screen (screen M) 
and the transmission dependency and stability test (screen L).  
o Providing transparent screen and study results to allow for reasonable 
system modifications to address technical concerns, if needed—Certain 
modifications to energy storage system design and operation may reduce or avoid 
the need for grid upgrades, to the extent any system impacts or concerns are 
identified in the Fast Track, Supplemental Review, or System Impact Study 
processes. By providing sufficient and transparent information to the 
interconnection customer with respect to the screen or study results, some states 


---

Page 66

---

57 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
and utilities are enabling applicants to alter their system design to address 
concerns, rather than requiring a new interconnection application. Although this 
practice benefits all technology types, it is particularly relevant for storage 
systems, which are highly controllable. 
• Clarify rules to account for the generation and load aspects of energy storage—
Although the utility technical review processes for determining electric-system impacts 
from conventional generation and load sources seeking to interconnect are similar, these 
processes are typically governed by two different sets of rules (thus requiring separate 
applications and review processes). Because energy storage systems can act as both 
generation and load, the same upgrades might be triggered by either function. For 
example, a customer’s service entrance may need to be upgraded to accommodate greater 
load and export, or the size of a service transformer may need to be upgraded. In 
addition, there is often ambiguity about when an energy storage system would trigger the 
need for two sets of processes and utility reviews—one for load and one for generation. 
To avoid confusion around this point, state interconnection rules for new sources of 
generation are being clarified with regard to how they interact with rules governing new 
load. Some states are clarifying the review processes for load and generation such that 
both processes can be consolidated for energy storage customers. Additional information 
on how states are starting to handle this issue can be found in McAllister (forthcoming). 
 
Beyond the technical requirements, it is also important to clarify what cost-allocation 
rules are applicable to energy storage systems. For example, the same upgrade may be 
identified for both the charging and discharging functions, but the rules governing new or 
modified load may have a different set of cost-allocation principles than would apply 
under the interconnection rules for new generators. Thus, it is important to clarify which 
cost-allocation rules would apply where the upgrade may be needed both for the charge 
and discharge functions. California has clarified that the cost-allocation rules under the 
load rules would be applied first when an upgrade is triggered owing to both functions. 
This issue is an area for further exploration, to identify applicable best practices as more 
systems are deployed. 
• Revise interconnection applications, agreements, and associated documents to 
correctly obtain information about storage systems—In addition to revising the 
process and technical standards in interconnection rules to accommodate energy storage, 
interconnection application materials require revision to reflect these changes and collect 
additional relevant information. These updates might be required by states and could be 
incorporated during other updates to interconnection documents required in nearly all 
states after certain timespans. 
• Ensure appropriateness of charging and discharging for BTM solar + storage 
systems for other renewable energy policy compliance—Some states are addressing 
the need to ensure BTM solar + storage systems operate in compliance with applicable 
state renewable energy policies, such as NEM. Specifically, for BTM solar + storage 
projects configured to primarily serve customer load, but that may export excess PV 
energy onto the grid—and thus would be eligible to receive customer bill credits via 
NEM—there is a need to guarantee that the excess generation provided to the grid is 
generated by the NEM-eligible renewable energy. This is not technically an 
interconnection question in that it does not directly relate to the safety and reliability of 


---

Page 67

---

58 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
the system, but in some states metering requirements for revenue tracking are included as 
part of the interconnection rules. Ensuring compliance with NEM policies requires an 
ability to track the energy used to charge the energy storage systems and the discharge of 
that energy onto the grid, to guarantee that the energy receiving NEM credits is from an 
eligible source. Although some system controls can track this information, initially more 
data, experience, and/or verification measures may be needed to assure NEM integrity is 
not compromised. Challenges exist in obtaining DER system monitoring information and 
integrating those data with the utility metering systems. Measurement accuracy testing 
and time correlation are two such challenges that may keep utilities from effectively 
using the data currently. Information on specific efforts being undertaken by different 
states in this area is included in McAllister (forthcoming). 
 
Whether or not energy monitoring is used to ensure NEM compliance, most storage 
systems can use controls that ensure very little, if any, non-renewable energy is 
discharged to the grid. Although the mechanism by which this is achieved may differ 
between DC-coupled and AC-coupled storage, both types of systems generally can either 
charge only from the PV system (or other renewable resource) or ensure that the storage 
only discharges up to an output level equal to the local load demand. UL is currently 
developing certification rules that will ensure these controls function as intended. 
This is not an exhaustive list of issues that may arise when addressing energy storage 
interconnections, and other issues may need to be dealt with more explicitly as more systems are 
deployed. As states and utilities gain more experience with energy storage systems, best 
practices will continue to emerge and evolve. 
 


---

Page 68

---

59 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
10 Pulling it All Together: The Interconnection 
Maturity Model 
In the chapters above, we reviewed key issues associated with DER interconnection. In this 
chapter, we discuss solutions to address DER interconnection that may apply to utilities 
experiencing different DER penetration levels and having different characteristics or resources—
a mapping we refer to as the “Interconnection Maturity Model.” This model is meant to provide 
high-level guidance on when different approaches might be considered, rather than suggest best 
practices, which are generally still being established. Improved understanding of best practices 
will continue to develop as experience with DERs increases. 
The discussion in this chapter is derived from: 
1. A synthesis of insights from the individual chapters in this guidebook, which draw from 
prior studies, utility interviews, and experiences of the authors.  
2. Feedback provided by the advisory board for this report (advisory board members are 
listed in the Acknowledgments). 
3. Additional targeted interviews of 10 U.S. utilities conducted in July 2018 by SEPA on 
behalf of DGIC. The characteristics of the utilities interviewed by SEPA are shown in 
Figure 16. 
The resulting information covers utilities with a diversity of size, type, and geography and 
provides useful insights around interconnection practices that may be suitable for utilities at 
different points along the Interconnection Maturity Model. 
 
 
 
Figure 16. Characteristics of utilities interviewed by SEPA about interconnection practices  
10.1 Interconnection Approaches at Low DER Penetrations 
Utilities with low penetrations of DER may be able to use legacy interconnection approaches 
involving more manual labor as well as reactive, system-by-system screening and upgrade 
selection. They may not require additional coordination between divisions or significant new 
resources dedicated to DER planning. However, as discussed in this report, deployment of 
DERs—particularly PV and storage—can increase rapidly. We have seen many examples of this 
increase across the United States as well as in other countries, particularly in Germany and 


---

Page 69

---

60 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Australia. Utilities can take certain actions even before they have significant DER penetrations 
that can help to minimize the cost, risk, and stress associated with possible future increases in 
deployment, including the following: 
• Adopt the IEEE 1547-2018 standard—As discussed in Chapters 3 and 4, this new 
standard provides functionality, including voltage and frequency ride-through, that allows 
inverters to minimize impact on the grid. In Germany, the installation of significant 
amounts of DER without these functions resulted in system stability issues and expensive 
retrofits to installed systems. Adopting the IEEE 1547-2018 standard early can help 
minimize future risks and costs in case penetration increases.  
• Use application templates—The use of application templates with clearly defined fields 
requires minimal effort and can improve the interconnection process for utilities and 
customers, even at low DER penetrations. Providing “canned” one-line diagrams for 
eligible system configurations, allowing a contractor to select the appropriate diagram 
and then complete the system information, has been useful for some utilities. 
Additionally, asking for installation photos in the template, especially of the safety 
disconnect(s), has allowed many applications that would fail inspection to be identified 
before rolling a truck at utilities interviewed, saving the utility and developer time and 
money. 
• Designate a point of contact—Designate a point of contact for interconnection 
applications as well as a clear way to communicate application status.  
• Coordinate inspection—Working with metering teams and/or authorities having 
jurisdiction (AHJ) to conduct necessary inspections with the fewest number of truck rolls 
can save time and money for all parties.  
• Collect and maintain data sets—Collecting and maintaining data sets about 
interconnected systems, incentives and programs, and system characteristics can be 
helpful for evaluating the effectiveness of different approaches to interconnection and 
improving processes and programs. Although some data collection and maintenance 
efforts may be burdensome and unnecessary at low penetration levels, others may be 
feasible and could provide significant benefit. 
• Provide system information to applicants as possible during the interconnection 
process—Providing system information to applicants can help to guide DERs to low-
cost/high-value locations. DERs can have significant distribution system impacts even at 
low penetration if larger systems are installed in poor locations, depending on the 
characteristics of the distribution system, so this can be valuable at any penetration level. 
The amount and type of system information will vary depending on the utility and state. 
For example, implementing and updating complete hosting-capacity maps may be 
difficult or hard to justify for some utilities at low penetration levels (today, these are 
resource-intensive to maintain), but using pre-application reports or even just providing 
basic system information (e.g., whether or not 3V0 is present at the substation) to 
applicants would be feasible and would improve the interconnection process. Utilities we 
interviewed have recommended that any information be easy for applicants to find and 
that clear guidance be provided on how different information is intended to be used in 
order to maximize benefit. 
• Provide vendor outreach and training— Utilities reported that vendor or DER 
applicant outreach and training (provided by the utilities) can help to streamline the 


---

Page 70

---

61 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
interconnection process. The appropriate degree and type (e.g., in-person, provision of 
materials online) of outreach and training will vary depending on the specific utility and 
vendor characteristics, capabilities, and preferences.  
• Implement online application platforms—Although they may not be necessary at very 
low penetration levels, utilities may still want to consider online application platforms 
relatively early. Figure 17 shows the status of implementing an online interconnection 
platform for the utilities interviewed by SEPA: all utilities with more than 250 
interconnection applications per year (or with annual application volumes exceeding 
0.2% of the customer base) are using, installing, or evaluating online application 
platforms to help manage and process applications. Online application platforms have 
been shown to measurably reduce staffing requirements, interconnection timelines, and 
the frequency of incomplete applications, while improving customer service (see Chapter 
1). SEPA’s interviews indicated that online platforms also increased visibility and 
reporting of interconnection information within the organization, including among system 
planners, customer service personnel, and executives. This may help to lay the 
groundwork for further collaboration between departments that could be useful at high 
penetration levels.  
• Improve cost allocation—Cost-allocation schemes may largely follow traditional 
models at low penetration levels, but utilities could start implementing approaches like 
group-study processes, preemptive upgrades, or post-upgrade reimbursement for circuits 
where higher DER penetrations are anticipated. Different cost-allocation approaches are 
still being evaluated, and the appropriateness of specific approaches may vary by 
scenario.  
It may also be beneficial to develop in-house capabilities or work with consultants or other 
partners to improve understanding of DER forecasting. An estimate of future DER adoption 
could suggest which solutions are appropriate at low penetration levels. Overall, different 
interconnection solutions will make sense for different utilities based on utility characteristics, 
location, and status in terms of grid-modernization efforts. 
 
Figure 17. Online interconnection platform status for utilities interviewed by SEPA in July 2018 


---

Page 71

---

62 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
10.2  Interconnection Approaches at Moderate to High DER 
Penetrations 
As DER penetration levels and the number of interconnection applications increase, investments 
in streamlining and improving the interconnection process can yield higher returns. Online 
interconnection platforms will likely be essential for managing the application process under 
most moderate- to high-penetration scenarios. Adopting the IEEE 1547-2018 standard likewise 
becomes more important, as does considering how to implement the standard. 
More sophisticated and accurate technical screens may also make sense at high penetrations. 
These could include, for example, the use of power-flow modeling, depending on the capability, 
resources, and other characteristics (e.g., whether the utility is using ADMS, or has sufficient 
data to perform accurate power-flow modeling) of a specific utility. Existing, simpler screens 
may also continue to evolve and improve as recent research and development are translated into 
practice and new research becomes available. For penetration levels at which significant back 
feed to transmission is anticipated or there is a desire to export more DER energy to the 
transmission system, it will become necessary to consider combined transmission and 
distribution DER effects during screening or the study process. More data will likely need to be 
collected from developers and provided to them during the application process. As data become 
available, more sophisticated power-flow modeling and DER adoption forecasting may be 
possible. Hosting capacity maps and engagement with applicants around their use may be 
increasingly feasible and valuable. 
Overall, as DER penetration reaches high levels, it may be useful or necessary to move toward 
more forward-looking and proactive approaches to interconnection, shifting toward a DER-
integration mindset rather than considering individual interconnection applications in isolation. 
This may also include additional analysis or consideration of DPV, energy storage, managed 
electrical vehicle charging, and other flexible loads or demand response under different control 
regimes, depending on the needs and resources of a given utility. Moving toward an integration-
oriented approach may also involve increasing collaboration across departments—e.g., 
geographic information systems, billing and customer service, outage management systems 
(OMS), distribution management systems, transmission planning, distribution planning, 
protection, secondary system design—and integrating with broader grid-modernization efforts. 
The ability to implement more proactive upgrade approaches effectively relies on having 
reasonable confidence in DER deployment forecasts. Thus, additional resources to improve 
forecasting techniques may be warranted. 
10.3 Key Ongoing Interconnection Challenges  
There are still many open questions about what constitutes best practices for interconnection. In 
addition to the issues discussed throughout this report, other key challenges identified for the 
future include the following: 
• Maintaining system and organizational flexibility in the face of continued technological 
change as well as policy and market uncertainty.  


---

Page 72

---

63 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
• Challenges around generation metering, including the cost of a second or potentially third 
generation meter, issues with the billing system configuration, and customer site 
aesthetics.  
• Issues with data integrity and availability, including the lack of reliable data from DPV 
inverters and in some cases other utility systems. Additionally, many utilities have 
minimal distribution system data.  
• In general, new issues arising around concentrations of smaller DER systems and 
associated changes in their system impacts, including DPV on new housing developments 
or third-party owned DER aggregations. 
• Cybersecurity issues and personally identifiable information with online application-
processing systems as well as the increasing collection and management of data. 
• Need for continued development of cybersecurity standards for distribution and DERs.  
• Questions around storage interconnection, including:  
o A lack of interconnection standards. 
o The variety of possible control, connection, and operational configurations 
possible for energy storage. 
o The lack of clarity with AHJ and inspection/process requirements. 
o NEM requirements. 
o Metering/billing system integration. 
 


---

Page 73

---

64 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
11 Summary and Conclusion  
As DER penetration levels increase, it is important to understand the key issues involved in 
interconnection and how interconnection processes can be tailored to adapt to this new paradigm. 
This document provides an overview of these issues—targeted at a utility audience—including 
current understanding and future needs as well as how the solutions may relate to DER 
penetration level and utility characteristics. It presents standards or best practices where 
established, while acknowledging that best practices are still unknown and under development 
for many aspects of interconnection. Table 4 summarizes the maturity of knowledge and 
standards development for different interconnection aspects covered in this report. 
Interconnection approaches will continue to evolve in these areas, with ongoing standards 
development and increased understanding of good practices as pilots and studies are completed. 
This is a rapidly changing space, and updates to the information in this document will be 
required. Table 4 also lists some living resources and projects related to interconnection that may 
facilitate tracking of these topics. 
Table 4. Summary of the Maturity of Knowledge and Standards for Interconnection Aspects 
Covered in this Report 
Chapter  Topic 
Standards or Established 
Good Practices 
State of Knowledge and 
Key Unknowns 
Additional 
Resources  
1 
Application 
Procedures 
and 
Management 
Online processes reduce 
application-processing times, 
but at very low penetrations 
the investment may not be 
justified. There are several 
other established good 
practices, e.g., application 
clarity.  
Some practices do not have 
publicly available cost-
benefit analyses, and the 
solutions most suitable for a 
given utility will depend on 
the circumstances.  
 
2 
Technical 
Screens 
FERC SGIP screens are 
typically used. The screens 
do not fully capture DER 
effects, but they have 
provided rules of thumb to 
safely connect DER in the 
past. Impacts vary on a case-
by-case basis and are 
evaluated for individual 
systems. 
Unknowns include the best 
screening approaches to 
use, tradeoffs between data 
and computational 
intensity/study cost, and 
accuracy of the screens.  
 
 
https://www
.ferc.gov/in
dustries/ele
ctric/indus-
act/gi/small
-gen.asp 
 
3 
Advanced 
Inverters 
Capabilities required for 
inverters are specified in 
IEEE 1547-2018. California 
Rule 21 and Hawaii Rule 14H 
have specifications for 
inverters in those regions. 
 
Some studies and pilots 
showing the potential for 
advanced inverters to 
facilitate DPV interconnection 
Research is ongoing about 
the ability of advanced 
inverters to mitigate issues 
associated with DERs in 
different scenarios. 
 
Understanding of how to 
implement IEEE 1547-2018 
with respect to advanced 
inverters is still being 
developed.  
 
https://stan
dards.ieee.
org/standar
d/1547-
2018.html 
 
http://www.
cpuc.ca.go
v/Rule21/  


---

Page 74

---

65 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
have been completed; others 
are ongoing.  
Relative tradeoffs in cost 
and risk for developers 
interconnecting with different 
advanced inverter settings 
are still being studied. 
4 
IEEE 1547 
IEEE 1547-2018 is the 
current, active standard. 
Questions include how the 
standard will be 
implemented in different 
states.  
https://stan
dards.ieee.
org/standar
d/1547-
2018.html 
5 
Distribution 
System 
Upgrades 
The best upgrade strategy is 
determined on a case-by-
case, system-by-system 
basis. There is no 
generalizable set of best 
upgrades. 
 
In some cases, changing 
voltage regulator or capacitor 
set points can help mitigate 
impacts. Changing the PF on 
the DER can also represent a 
low-cost integration option, 
but it depends on the relative 
costs and risks to the 
developer and developer-
utility-regulator preferences.  
Uncertainties include costs 
vs. benefits for utilities, DER 
developers, and customers; 
risks of emerging upgrades; 
how to select forward-
looking integration options; 
and which upgrades may be 
most effective if anticipating 
very high DER penetration 
levels.  
 
6 
Cost Allocation 
There is no established 
standard or best practice. 
Cost-causer pays is current 
typical practice, but it can 
result in challenges around 
fairness in contributing to 
upgrades. 
Several new cost-allocation 
approaches are currently 
being piloted, and they can 
be analyzed in the future to 
determine their impacts, 
effectiveness, and potential 
issues. 
 
7 
Forecasting 
DER 
Deployment 
There is no established best 
forecasting tool. Determining 
which tool is most 
appropriate is still a subject of 
research and will depend on 
the resources, data 
availability, and needs of a 
given utility. 
 
However, a need to forecast 
DER growth has been 
recognized from a distribution 
and bulk system perspective.  
Validation is still required to 
vet the accuracy of different 
emerging models. 
 
Tradeoffs between different 
models in terms of accuracy 
and requirements at different 
penetration levels is still a 
topic of research.  
https://drpw
g.org/growt
h-
scenarios/  
8 
Cybersecurity 
No standard for DER 
cybersecurity exists, but 
there are some established 
good practices related to 
Standards for DER 
cybersecurity are currently in 
development.  
https://suns
pec.org/sun
spec-
cybersecuri


---

Page 75

---

66 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
maintaining cybersecurity of 
the utility’s network. 
ty-
workgroup/ 
9 
Storage and 
Solar + Storage 
Interconnection 
There is no established best 
practice or standard. Several 
states are exploring different 
options in their 
interconnection processes.  
 
There is a recognized need 
to treat storage differently 
than DG in interconnection 
standards and study 
processes, accounting for 
different configurations of 
storage and solar + storage.  
Pilots and standard 
development are still in the 
early stages. 
 
It is unknown how best to 
account for operational 
diversity and potential 
changes in storage behavior 
over system lifetimes to 
meet utility and developer 
needs. 
https://www
.epri.com/#/
pages/sa/e
pri_energy_
storage_int
egration_co
uncil_esic?l
ang=en-US  
10 
Interconnection 
Maturity Model 
At high DER penetrations, 
utilities need a more 
automated and streamlined 
interconnection process, and 
may benefit from integrating 
DER planning with other 
planning processes.  
When it makes sense to 
implement different 
interconnection solutions 
depends on the specific 
scenario and utility, and 
limited data demonstrate 
which solutions are most 
appropriate for different 
scenarios. 
 
 
 


---

Page 76

---

67 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
References  
Adepetu, A., and S. Keshav. 2016. “Understanding Solar PV and Battery Adoption in Ontario: 
An Agent-Based Approach.” In Proceedings of the Seventh International Conference on Future 
Energy Systems (e-Energy '16). New York: ACM. 
Adhikari, S. 2015. “APS Solar Partner Program.” Presented at the Integrating PV in Distribution 
Grids: Solutions and Technologies Workshop, Golden, CO, October 22-23, 2015. 
https://www.nrel.gov/esif/assets/pdfs/highpenworkshop_adhikari.pdf.  
Advanced Energy Economy. 2017. Access to Data: Bringing the Electricity Grid into the 
Information Age. San Francisco: Advanced Energy Economy. 
https://info.aee.net/hubfs/PDF/Access-to-data.pdf. 
Agarwal, A., D. Cai, S. Shah, M. Chandy, and R. Sherick. 2015. “A Model for Residential 
Adoption of Photovoltaic Systems.” Presented at the 2015 IEEE Power & Energy Society 
General Meeting, Denver, CO. doi: 10.1109/PESGM.2015.7286226.  
Anzalchi, A., A. Sundararajan, L. Wei, A. Moghadasi, M.M. Pour, and A.I. Sarwat. 2018. 
“Future Directions to the Application of Distributed Fog Computing in Smart Grid 
Systems.”  In Smart Grid Analytics for Sustainability and Urbanization, ed. Zbigniew H. Gontar, 
162-195. Accessed September 20, 2018. https://doi:10.4018/978-1-5225-3996-4.ch006.  
 
Ardani, K., and R. Margolis. 2015. Decreasing Soft Costs for Solar Photovoltaics by Improving 
the Interconnection Process: A Case Study of Pacific Gas and Electric. NREL/TP-7A40-65066. 
Golden, CO: National Renewable Energy Laboratory. 
https://www.nrel.gov/docs/fy15osti/65066.pdf.  
Bank, J. 2017. “DEW-ISM Implementation at PEPCO: A Model and Data Driven Approach to 
Automating PV Interconnection Studies.” Presented at IEEE PES, July 20, 2017. 
http://www.edd-us.com/wp-content/uploads/2017/07/IEEE-PES-GM-2017-Pres-jbank.pdf.  
Baringa Partners and UK Power Networks. 2012. Flexible Plug and Play: Principles of Access 
Report. London: UK Power Networks. 
https://www.ukpowernetworks.co.uk/internet/asset/dac8de6d-1243-4689-b5b5-
a8285a2553fO/Principles_of_Access_report_FINAL.pdf. 
Barnes, C., J. Barnes, B. Elder, and B. Inskeep. 2016. Comparing Utility Interconnection 
Timelines for Small-Scale Solar PV, 2nd Edition. Cary, NC: EQ Research. http://www.eq-
research.com/. 
Bernards, R., J. Morren, and H. Slootweg. 2018 “Development and Implementation of Statistical 
Models for Estimating Diversified Adoption of Energy Transition Technologies.” IEEE 
Transactions on Sustainable Energy PP (99): 1. doi: 10.1109/TSTE.2018.2794579. 
Bird, L.A., F. Flores-Espino, C.M. Volpi, K.B. Ardani, D. Manning, and R. McAllister. 2018. 
Review of Interconnection Practices and Costs in the Western States. NREL/TP-6A20-71232. 
Golden, CO: National Renewable Energy Laboratory. https://doi.org/10.2172/1435904. 


---

Page 77

---

68 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Chacon, B. 2017. “Xcel Energy Investigates Use of Battery Storage.” T&D World, January 24, 
2017. https://www.tdworld.com/renewables/xcel-energy-investigates-use-battery-storage.  
Cleveland, F. 2012. IEC TC57 WG15: IEC 62351 Security Standards for the Power System 
Information Infrastructure. White Paper. Geneva: International Electrotechnical Commission.  
Coddington, M., B. Mather, B. Kroposki, K. Lynn, A. Razon, A. Ellis, R. Hill, T. Key, K. 
Nicole, and J. Smith. 2012. Updating Interconnection Screens for PV System Integration. 
NREL/TP-5500-54063. Golden, CO: National Renewable Energy Laboratory. 
https://doi.org/10.2172/1036038. 
Condon, D., D. McPhail, and D. Ingram. 2016. “Application of Low Voltage Statcom to Correct 
Voltage Issues Caused by Inverter Energy Systems” Presented at the Australasian Universities 
Power Engineering Conference (AUPEC), Brisbane, Australia, September 25-28, 2016. doi: 
10.1109/AUPEC.2016.7749332. 
Davidson, C., E. Drury, A. Lopez, R. Elmore, and R. Margolis. 2014. “Modeling Photovoltaic 
Diffusion: An Analysis of Geospatial Datasets.” Environmental Research Letters 9 (7): 074009. 
http://dx.doi.org/10.1088/1748-9326/9/7/074009. 
Dharshing, S. 2017. “Household Dynamics of Technology Adoption: A Spatial Econometric 
Analysis of Residential Solar Photovoltaic (PV) Systems in Germany.” Energy Research & 
Social Science 23: 113–124. https://doi.org/10.1016/j.erss.2016.10.012. 
Ding, F., A. Nagarajan, S. Chakraborty, M. Baggu, A. Nguyen, S. Walinga, M. McCarty, and F. 
Bell. 2016. Photovoltaic Impact Assessment of Smart Inverter Volt-VAR Control on Distribution 
System Conservation Voltage Reduction and Power Quality. NREL/TP-5D00-67296. Golden, 
CO: National Renewable Energy Laboratory. https://www.nrel.gov/docs/fy17osti/67296.pdf 
Dong, C., B. Sigrin, and G. Brinkman. 2017. “Forecasting Residential Solar Photovoltaic 
Deployment in California.” Technological Forecasting and Social Change 117: 251–265. 
ECI. 2017. “A Layered Approach to Cybersecurity.” EzeCastle Integration (ECI) Technical 
Report. 
Eder-Neuhauser, P., T. Zseby, J. Fabini, and G. Vormayr. 2017. “Cyber Attack Models for Smart 
Grid Environments.” Sustainable Energy, Grids and Networks December: 10–29. 
EIA (U.S. Energy Information Administration). “Form EIA-851M (Formerly EIA-826) Detailed 
Data.” Accessed April 19, 2017. https://www.eia.gov/electricity/data/eia861m/.  
Energy Networks Association. 2015. Active Network Management Good Practice Guide. 
London: Energy Networks Association. 
http://www.energynetworks.org/assets/files/news/publications/1500205_ENA_ANM_report_A
W_online.pdf.  
EPACT (Energy Policy Act) of 2005. 2005. Public Law 109–58.109th Congress. 
https://www.ferc.gov/enforcement/enforce-res/EPAct2005.pdf. 


---

Page 78

---

69 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
EPRI (Electric Power Research Institute). 2014. Common Functions for Smart Inverters. Report 
3002002233. Palo Alto, CA: EPRI. 
https://www.epri.com/#/pages/product/3002002233/?lang=en. 
EPRI (Electric Power Research Institute). 2017a. Assessing Opportunities and Challenges for 
Streamlining Interconnection Processes. Minnesota Department of Commerce and the 
Minnesota Solar Pathways Project. 
EPRI (Electric Power Research Institute). 2017b. IEEE 1547: New Interconnection 
Requirements for Distributed Energy Resources. Factsheet 3002011346. Palo Alto, CA: EPRI. 
https://www.epri.com/#/pages/product/3002011346/?lang=en   
Etherden, N., and M.H.J. Bollen. 2011. “Increasing the Hosting Capacity of Distribution 
Networks by Curtailment of Renewable Energy Resources.” Presented at 2011 IEEE Trondheim 
PowerTech. doi:10.1109/PTC.2011.6019292. 
FERC (U.S. Federal Energy Regulatory Commission). 2005. Standardization of Small Generator 
Interconnection Agreements and Procedures. Docket No. RM02-12-000; Order No. 2006. 
Washington, DC: FERC. https://www.ferc.gov/EventCalendar/Files/20050512110357-
order2006.pdf. 
FERC (U.S. Federal Energy Regulatory Commission). 2013. Small Generator Interconnection 
Agreements and Procedures. RM13-2-000; Order No. 792. Washington, DC: FERC. 
https://www.ferc.gov/whats-new/comm-meet/2013/112113/E-1.pdf.Fu, R., D. Feldman, R. 
Margolis, M. Woodhouse, and K. Ardani. 2017. U.S. Solar Photovoltaic System Cost 
Benchmark: Q1 2017. Golden, CO: National Renewable Energy Laboratory. 
https://www.nrel.gov/docs/fy17osti/68925.pdf. 
Fries, S. 2017. “Security in Power System Automation: Status and Application of IEC 62351.” 
Siemens Corporate Technology Presentation. June 13, 2017. 
http://iectc57.ucaiug.org/wg15public/Public%20Documents/Overview%20of%20IEC%2062351
%20standards.pdf.  
 
Gagnon, P., G. Barbose, B. Stoll, A. Ehlen, J. Zuboy, T. Mai, and A. Mills. 2018. Estimating the 
Value of Improved Distributed Photovoltaic Adoption Forecasts for Utility Resource Planning. 
NREL/TP-6A20-71042. Golden, CO: National Renewable Energy Laboratory; Berkeley, CA: 
Lawrence Berkeley National Laboratory. 
Gagnon, P., R. Margolis, J. Melius, C. Phillips, and R. Elmore. 2016. Rooftop Solar Photovoltaic 
Technical Potential in the United States: A Detailed Assessment. NREL/TP-6A20-65298. 
Golden, CO: National Renewable Energy Laboratory. 
https://www.nrel.gov/docs/fy16osti/65298.pdf. 
Giraldez, J., A. Nagarajan, P. Gotseff, V. Krishnan, A. Hoke, R. Ueda, J. Shindo, M. Asano, and 
E. Ifuku. 2017. Simulation of Hawaiian Electric Companies Feeder Operations with Advanced 
Inverters and Analysis of Annual Photovoltaic Energy Curtailment. NREL/TP-5D00-68681. 
Golden, CO: National Renewable Energy Laboratory. 
https://www.nrel.gov/docs/fy17osti/68681.pdf 


---

Page 79

---

70 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Grid Management Working Group. 2017. “DERMS Requirements.” Accessed November 13, 
2017. https://sepapower.org/derms-requirements/ 
GTM Research and SEIA. 2017. Q2 2017 U.S. Solar Market Insight Report. Boston: GTM 
Research.  
GTM Research. 2018. Q3 2018 U.S. Energy Storage Monitor. Boston: GTM Research.  
Guidolin, M., and C. Mortarino. 2010. “Cross-Country Diffusion of Photovoltaic Systems: 
Modelling Choices and Forecasts for National Adoption Patterns.” Technological Forecasting 
and Social Change 77 (2): 279–296. http://dx.doi.org/10.1016/j.techfore.2009.07.003. 
Hawaiian Electric Companies. 2014. Distributed Generation Interconnection Plan (DGIP), 
Response to Hawaii Public Utilities Commission Order No. 32053. Honolulu: Hawaiian Electric 
Companies. 
http://files.hawaii.gov/puc/4_Book%201%20(transmittal%20ltr_DGIP_Attachments%20A-
1%20to%20A-5).pdf.  
Hawaiian Public Utilities Commission. 2015. Decision and Order No. 33258, Dkt. No. 2014-
0192, p. 85, October 12, 2015. 
Holl, K. 2003. “OSI Defense in Depth to Increase Application Security.” SANS Security 
Essentials GSEC Practical Assignment Version 1.4b. https://www.giac.org/paper/gsec/2868/osi-
defense-in-depth-increase-application-security/104841.  
ICC v. FERC. 2009. 576 F 3d at 476. 
https://www.dwt.com/files/uploads/Documents/Advisories/Illinois%20Commerce%20v%20FER
C.pdf. 
IEEE (Institute of Electrical and Electronics Engineers). 2015. IEEE 1547 Series of 
Interconnection Standards. IEEE Standards Association. 
http://grouper.ieee.org/groups/scc21/1547_series/1547_series_index.html. 
INL (Idaho National Laboratory). 2016. Cyber Threat and Vulnerability Analysis of the U.S. 
Electric Sector. Mission Support Center Analysis Report. Idaho Falls: INL. 
IREC (Interstate Renewable Energy Council). 2017. Priority Considerations for Interconnection 
Standards: A Quick Reference Guide for Utility Regulators. Latham, NY: IREC. 
http://www.irecusa.org/wp-content/uploads/2017/08/IREC-Interconnection-2017_8-10-
17.pdf.Kane, L., and G. Ault. 2014. “A Review and Analysis of Renewable Energy Curtailment 
Schemes and Principles of Access: Transitioning Towards Business as Usual.” Energy Policy 72: 
67–77. 
Keller, J., and B. Kroposki. 2010. Understanding Fault Characteristics of Inverter-Based 
Distributed Energy Resources. NREL/TP-550-46698. Golden, CO: National Renewable Energy 
Laboratory. http://research.iaun.ac.ir/pd/bahador.fani/pdfs/UploadFile_9423.pdf 
K N Energy, Inc. v. FERC. 1992. 968 F.2d 1295, 1300 (D.C. Cir. 1992). 


---

Page 80

---

71 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Labastida, R. R. and D. Gauntlett. 2017. Q1 2017 Market Data: Global Distributed Solar PV. 
Navigant Research. 
Luhmann, T., E. Wieben, R. Treydel, M. Stadler, and T. Kumm. 2015. “An Approach for Cost-
Efficient Grid Integration of Distributed Renewable Energy Sources.” Engineering 1: 447–452. 
doi:10.15302/J-ENG-2015099. 
Makhyoun, M., B. Campbell, and M. Taylor. 2014. Distributed Solar Interconnection 
Challenges and Best Practices. Washington, DC: Solar Electric Power Association. 
https://www.growsolar.org/wp-content/uploads/2014/10/SEPA-Interconnection-Report-1014-
email.pdf. 
Maloney, P. 2016. “PURPA’s Puzzle: FERC Workshop Revisits 1978 Law, Embattled as Ever.” 
Utility Dive, July 28, 2016. https://www.utilitydive.com/news/purpas-puzzle-ferc-workshop-
revisits-1978-law-embattled-as-ever/423005/. 
McAllister, R., D. Manning, L. Bird, M. Coddington, and C. Volpi. Forthcoming. New 
Approaches to Distributed PV Interconnection: Implementation Considerations for Addressing 
Emerging Issues. Golden, CO: National Renewable Energy Laboratory.  
Mittal, A., W. Huang, and C. Krejci. 2017. “Consumer-adoption Modeling of Distributed Solar 
Using an Agent-based Approach.” Computational Social Sciences. 
http://works.bepress.com/anuj-mittal/11/. 
NARUC (National Association of Regulatory Utility Commissioners). 2016. Distributed Energy 
Resources Rate Design and Compensation. Washington, DC: NARUC. 
https://pubs.naruc.org/pub.cfm?id=19FDF48B-AA57-5160-DBA1-BE2E9C2F7EA0. 
National Grid. 2017. National Grid DG Interconnection REV Demo Project. Case 14-M-0101, 
Proceeding on Motion of the Commission in Regard to Reforming the Energy Vision (REV). 
Niagara Mohawk Power Corporation d/b/a National Grid. 
http://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId={6B0377EF-F949-
4DAA-A164-AB8ABB019E5B}. 
National Grid RI. 2018. “Interconnection Process.” Accessed September 14, 2018. 
https://www9.nationalgridus.com/narragansett/business/energyeff/4_interconnection-process.asp. 
National Grid MA. 2018. “Completion Documentation.” Accessed September 14, 2018. 
https://www9.nationalgridus.com/Masselectric/home/energyeff/4_completion-
documentation.asp. 
NERC (North American Electric Reliability Corporation). 2016. CIP Standards. Atlanta: NERC. 
http://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx.  
NIST (National Institute of Standards and Technology). 2014. Framework for Improving Critical 
Infrastructure Cybersecurity, Version 1.0. Gaithersburg, MD: NIST.  


---

Page 81

---

72 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
NIST (National Institute of Standards and Technology). 2015. Guide to Industrial Control 
Systems (ICS) Security. NIST Special Publication 800-82, Revision 2. Gaithersburg, MD: NIST. 
NYPSC (New York Public Service Commission). n.d. “New York Interconnection Online 
Application Portal Functional Requirements.” Accessed July 16, 2018. 
http://www3.dps.ny.gov/W/PSCWeb.nsf/96f0fec0b45a3c6485257688006a701a/dcf68efca391ad
6085257687006f396b/$FILE/EPRI%20Task%201%20Memo%20Report_Final%209-9-16.pdf. 
NYPSC (New York Public Service Commission). 2017. Order Adopting Interconnection 
Management Plan and Cost Allocation Mechanism, and Making Other Findings. Case 16-E-
0560 - Joint Petition for Modifications to the New York State Standardized Interconnection 
Requirements and Application Process for New Distributed Generators 5 MW or Less Connected 
in Parallel with Utility Distribution Systems. Albany: NYPSC. 
http://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7b22BEAB22-7F9F-
45B8-89FD-0E8AD84692B4%7d. 
NYPSC (New York Public Service Commission). 2018. New York State Standardized 
Interconnection Requirements and Application Process for New Distributed Generators and 
Energy Storage Systems 5 MW or Less Connected in Parallel with Utility Distribution Systems. 
Albany: NYPSC. 
http://www3.dps.ny.gov/W/PSCWeb.nsf/96f0fec0b45a3c6485257688006a701a/dcf68efca391ad
6085257687006f396b/$FILE/October%20SIR%20Appendix%20A%20-%20Final%2010-3-
18.pdf. 
Otuoze, A., O.M.W. Mustafa, and R.M. Larik. 2018. “Smart Grids Security Challenges: 
Classification by Sources of Threats.” Journal of Electrical Systems and Information Technology 
February. 
Ozgur, U., H.T. Nair, A. Sundararajan, K. Akkaya, and A.I. Sarwat. 2017. “An Efficient mqtt 
Framework for Control and Protection of Networked Cyber-Physical Systems.” In IEEE 
Conference on Communications and Network Security. Piscataway, NJ: IEEE. 
Parks, K., B. Woerner, and K. Ardani. 2014. “Innovation in the Interconnection Application 
Process.” Presentation, April 2, 2014. https://www.nrel.gov/dgic/assets/pdfs/2014-04-
02_innovation-in-the-interconnection-application-process.pdf. 
Pathways to an Open Grid: O’ahu. 2017. “Pathways to an Open Grid: Locational Net Benefit 
Analysis Best Practices.” Presented at the Locational Net Benefit Analysis Workshop, January 
18, 2017. 
https://static1.squarespace.com/static/598e0823e3df282e209b27b0/t/5a6286668165f5f2ad306b6
e/1516406388156/POG+LNBA+Full+Deck.pdf. 
Pender-Bey, G. 2013. “The Parkerian Hexad: The CIA Triad Model Expanded.” Master’s thesis, 
Lewis University. 


---

Page 82

---

73 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
PG&E (Pacific Gas & Electric). n.d. “Discover the Electric Program Investment Charge 
Program.” Accessed September 25, 2018. https://www.pge.com/en_US/about-
pge/environment/what-we-are-doing/electric-program-investment-charge/electric-program-
investment-charge.page.  
PG&E (Pacific Gas & Electric). 2017a. EPIC Project 1.02 – Demonstrate Use of Distributed 
Energy Storage for Transmission and Distribution Cost Reduction. Electric Program Investment 
Charge (EPIC) project report, June 20. San Francisco: PG&E. 
https://www.pge.com/pge_global/common/pdfs/about-pge/environment/what-we-are-
doing/electric-program-investment-charge/PGE-EPIC-Project-1.02.pdf.  
PG&E (Pacific Gas & Electric). 2017b. Distribution Interconnection Handbook. San Francisco: 
PG&E. 
https://www.pge.com/includes/docs/pdfs/shared/customerservice/nonpgeutility/electrictransmissi
on/handbook/distribution-interconnection-handbook.pdf. 
Pillitteri, V.Y., and T.L. Brewer. 2014. Guidelines for Smart Grid Cybersecurity. NIST 
Interagency/Internal Report (NISTIR)-7628, Revision 1. Gaithersburg, MD: National Institute of 
Standards and Technology. 
Qi, J., A. Hahn, Z. Lu, J. Wang, and C.C. Liu. 2016. “Cybersecurity for Distributed Energy 
Resources and Smart Inverters.” IET Cyber-Physical Systems: Theory & Applications 1(1): 28–
39. doi: 10.1049/iet-cps.2016.0018. 
Rai, V., and S.A. Robinson. 2015. “Agent-Based Modeling of Energy Technology Adoption: 
Empirical Integration of Social, Behavioral, Economic, and Environmental Factors.” 
Environmental Modelling and Software 70: 163–177. 
http://dx.doi.org/10.1016/j.envsoft.2015.04.014. 
Reno, M. J. and R. J. Broderick. 2015. Technical Evaluation of the 15% of Peak Load PV 
Interconnection Screen. IEEE 42nd Photovoltaic Specialists Conference (PVSC). New Orleans, 
LA: IEEE. 
REV Connect. 2018. “Lessons from REV Demos in New York’s Energy System.” From REV 
Connect Webinar Series, January 17, 2018. https://nyrevconnect.com/wp-
content/uploads/2018/01/Webinar2_Demo-Principles-v6-01-17-18.pdf.  
SANS 2001. “Defense in Depth.” SANS Institute InfoSec Reading Room Report. 
 
SCE (Southern California Edison). 2016. Rule 21: Generating Facility Interconnections. U 338-
E. Rosemead, CA: SCE. 
Seguin, R., J. Woyak, D. Costyk, J. Hambrick, and B. Mather. 2016. High-Penetration PV 
Integration Handbook for Distribution Engineers. NREL/TP-5D00-63114. Golden, CO: 
National Renewable Energy Laboratory. https://www.nrel.gov/docs/fy16osti/63114.pdf.  


---

Page 83

---

74 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
Sena, S.S., J.E. Quiroz, and R.J. Broderick. 2014. Analysis of 100 SGIP Interconnection Studies. 
SAND2014-4753. Albuquerque, NM: Sandia National Laboratories. 
http://energy.sandia.gov/wp-content/gallery/uploads/dlm_uploads/Analysis-of-100-SGIP-
Interconnection-Studies.pdf. 
Shamim, A., B. Fayyaz, and V. Balakrishnan. 2014. “Layered Defense in Depth Model for IT 
Organizations.” In 2nd International Conference on Innovations in Engineering and Technology. 
Penang, Malaysia: The IRES.  
Sheehan, M.T., and T. Cleveland. 2010. Updated Recommendations for Federal Energy 
Regulatory Commission Small Generator Interconnection Procedures Screens. Solar American 
Board for Codes and Standards. http://www.solarabcs.org/about/publications/reports/ferc-
screens/pdfs/ABCS-FERC_studyreport.pdf. 
Sigrin, B., and M. Mooney. 2018. Rooftop Solar Technical Potential for Low-to-Moderate 
Income Households in the United States. NREL/TP-6A20-70901. Golden, CO: National 
Renewable Energy Laboratory. 
Sigrin, B., M. Gleason, R. Preus, I. Baring-Gould, and R. Margolis. 2016. Distributed 
Generation Market Demand Model (dGen): Documentation. NREL/TP-6A20-65231. Golden, 
CO: National Renewable Energy Laboratory. 
Small, P. E. 2011. “Defense in Depth: An Impractical Strategy for Cyber World.” SANS 
Institute InfoSec Reading Room Report. 
 
Stamber, K.L., A. Kelic, R.A. Taylor, J.M. Henry, and J.E. Stamp. 2017. Distributed Energy 
Systems: Security Implications of the Grid of the Future. SAND2017-0794. Albuquerque, NM: 
Sandia National Laboratories. https://prod.sandia.gov/techlib-noauth/access-
control.cgi/2017/170794.pdf. 
Stanfield, S., S. Safdi, Shute Mihaly & Weinberger LLP, and S. Baldwin Auck. 2017. 
Optimizing the Grid: A Regulator’s Guide to Hosting Capacity Analyses for Distributed Energy 
Resources. Latham, NY: Interstate Renewable Energy Council. 
https://irecusa.org/publications/optimizing-the-grid-regulators-guide-to-hosting-capacity-
analyses-for-distributed-energy-resources/. 
Strom, B.E., J.A. Battaglia, M.S. Kemmerer, et al. 2017. “Finding Cyber Threats with 
ATT&CK-Based Analytics.” MTR170202. Annapolis Junction, MD: MITRE.  
Sundararajan, A., A. Chavan, D. Saleem, and A. Sarwat. 2018. “A Survey of Protocol-Level 
Challenges and Solutions for Distributed Energy Resource Cyber-Physical Security.” Energies 
11 (9): 2360. https://doi.org/10.3390/en11092360. 
SunSpec. 2018. “SunSpec DER Cybersecurity Working Group.” Accessed September 2018. 
https://sunspec.org/sunspec-cybersecurity-workgroup/. 


---

Page 84

---

75 
This report is available at no cost from the National Renewable Energy Laboratory (NREL) at www.nrel.gov/publications. 
UL. 2018. Drive Innovation and Streamline Advanced Distributed Energy Resource Market 
Acceptance. Northbrook, IL: UL. https://industries.ul.com/wp-
content/uploads/sites/2/2016/08/UL-1741-SA-Advanced-Inverters.pdf.  
Wang, W., N. Yu, and R. Johnson. 2017. “A Model for Commercial Adoption of Photovoltaic 
Systems in California.” Journal of Renewable and Sustainable Energy 9: 025904. 
https://doi.org/10.1063/1.4979899. 
Wei, L., A. Sundararajan, A. I. Sarwat, S. Biswas and E. Ibrahim. 2017. “A Distributed 
Intelligent Framework for Electricity Theft Detection using Benford's Law and Stackelberg 
Game." In 2017 Resilience Week (RWS), Wilmington, DE: IEEE. 
https://doi.org/10.1109/RWEEK.2017.8088640 
 
Xcel. 2017a. Guidance No. 1 for the Interconnection of Electric Storage as Stand-Alone Sources, 
Parallel Operation for Customers without Generation, and in Parallel with Self-Generation. 
Minneapolis, MN: Xcel Energy. https://www.xcelenergy.com/staticfiles/xe-
responsive/Programs%20and%20Rebates/Residential/CO-solar-residence-Storage-Guidance-
1.pdf. 
Xcel. 2017b. Guidance No. 2 for Interconnection of Energy Storage Systems Operated in Front 
of a Production Meter and Paired with Onsite Renewable Generation Connected Under a Net 
Metering Tarif. Minneapolis, MN: Xcel Energy . https://www.xcelenergy.com/staticfiles/xe-
responsive/Programs%20and%20Rebates/Residential/CO-solar-residents-Storage-Guidance-
2.pdf. 
Xcel. 2017c. Guidance No. 3 for Interconnection of Energy Storage Systems Operated Behind a 
Production Meter and Paired with Onsite Renewable Generation Connected Under a Net 
Metering Tariff. Minneapolis, MN: Xcel Energy. https://www.xcelenergy.com/staticfiles/xe-
responsive/Programs%20and%20Rebates/Residential/CO-solar-residence-Storage-Guidance-
3.pdf. 
Xcel. 2018. “How to Interconnect.” Accessed September 2018. 
https://www.xcelenergy.com/working_with_us/how_to_interconnect. 
Xcel Energy Minnesota. 2018. “Example Drawings for Small Solar Interconnections.” Accessed 
August 29, 2018. https://www.xcelenergy.com/staticfiles/xe-
responsive/Programs%20and%20Rebates/Residential/MN-Sample-IC-Drawings.pdf.  
Zhang, H., Y. Vorobeychik, J. Letchford, and K. Lakkaraju. 2015. “Data-Driven Agent-Based 
Modeling, with Application to Rooftop Solar Adoption.” In Proceedings of the 2015 
International Conference on Autonomous Agents and Multiagent Systems, 513–521. 
