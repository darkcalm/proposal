

---

Page 1

---

 
Abstract—The massive penetration of Renewable Energy 
Sources, preminently wind and photovoltaic power plants, 
and Distributed Energy Resources (DERs), such as 
Combined Heat and Power plants, Battery Energy Storage 
System, Electric Vehicles impose additional challenges in 
power system planning and operation. Pushing towards a 
low-carbon electricity system can increase potential issues 
such 
as 
congestion 
management, 
voltage 
control, 
controllability, 
observability, 
and 
generation-load 
forecasting. In this context, coordinated actions between 
Transmission System Operators (TSOs) and Distribution 
Systems Operators (DSOs) could be a valuable solution. For 
instance, through the DERs installed on the distribution 
network, the DSO could help the TSO to relieve a network 
contingency on the HV/HHV grid. This paper proposes a 
feasibility study of TSO-DSO coordination that allows using 
DERs to solve transmission network criticalities, both in 
operational and short- to medium-term time horizons, that 
does not involve the exchange of sensitive information 
between the two utilities. A straightforward algorithm is 
proposed for evaluating DERs available flexibility in terms of 
active and reactive power, and for estimating the aggregated 
capability curve at the point of common coupling, i.e., the 
flexibility available downstream a HV/MV substation. The 
proposed algorithm has been applied to Milan's case study 
using real data from Unareti, the local DSO, and Terna, the 
Italian TSO. 
Index Terms--Distributed power generation, power 
distribution, 
power 
system 
management, 
power 
transmission.  
I.  INTRODUCTION 
The growing and rapid diffusion of Distributed Energy 
Resources (DERs), such as Renewable Energy Sources 
(RESs) [1], Electric Vehicles (EVs) [2], Battery Energy 
Storage Systems (BESSs) [3][4], and Demand Response 
(DR) systems [5], often located in the Distribution System 
Operator (DSO) network, poses new challenges in power 
system balancing, congestion management, voltage 
control, controllability, observability and forecasting of 
DERs, but, at the same time, makes available new 
opportunities in the management and planning of the 
electricity system as a whole. In this context, interaction 
with the Transmission System Operator (TSO) is essential, 
including the possibility for the DSO to provide support, 
among others, in terms of flexibility, balancing, voltage 
control, and congestion [6]. 
To successfully manage the aforementioned challenges, 
it is crucial that the TSO and DSO are efficiently 
coordinated to allow for the greatest possible flexibility 
and interoperability [7]. Directive (EU) 2019/944 of the 
European Legislation and Council of 5 June 2019 [8] lays 
down in Article 32 of the incentives for the use of 
flexibility in distribution networks, providing for the need 
for coordination between TSO and DSO, in particular:    
• 
DSOs shall exchange all necessary information and 
coordinate with TSOs to ensure optimal use of 
resources, the safe and efficient operation of the 
system, and facilitate market development; 
• 
The DSO shall consult all relevant system users 
and TSOs on the network development plan. 
At the same time, the push for a constant and continuous 
energy transition towards the "fit for 55" targets [9], and 
the experience gained with the recent, is becoming 
increasingly necessary to plan the network, which, given 
the ever-increasing presence of distributed resources, 
requires new models of coordinated TSO-DSO planning. 
The analysis of the technical regulations focused on the 
coordination between TSOs and DSOs is crucial to look 
for references in the network codes that regulate the 
activities in which the two entities must interface. To this 
end, the Italian network code [10] has to be analyzed to 
understand the types of information currently exchanged 
between TSOs and DSOs, the purposes of the information 
exchanged, and data on cooperation in the implementation 
of network development plans. Currently, the DSOs 
annually report data to the TSO on the installed power 
downstream of their network broken down by source type. 
Still, they do not provide details of their network, such 
types of information are, in fact, defined as sensitive and, 
therefore, not reported.  
The key issues related to the interaction of TSOs and 
DSOs proposed in the current literature cover the domains 
of markets [11], network operations and network planning 
A feasibility study of using MV and LV 
distributed energy resources flexibility in a 
TSO/DSO coordination perspective: the case 
study of Milan, Italy 
A. Bosisio*, A. Berizzi**, C. Mosca***, C. Vergine***, D. Castiglioni***, A. Morotti**** 
*Department of Electrical, Computer and Biomedical Engineering - University of Pavia, Via Adolfo Ferrata, 5 
27100 Pavia, (Italy) 
**Energy Department - Politecnico di Milano, Via La Masa, 34 20156 Milano (Italy) 
***Dispatching and Control Department – Terna Rete Italia S.p.A., Via G. Galilei, 18 20016 Pero (Italy) 
****Energy Planning Department, Unareti S.p.A., Via Ponte Nuovo, 100 20128 Milano (Italy)  


---

Page 2

---

 
[12], and data handling [13]. On the one hand, the literature 
shows an increasing number of papers dealing with the 
market framework in the last years, followed by network 
operation-related documents. Operational planning covers 
the third position in terms of papers number. On the other 
hand, data handling and expansion planning have rarely 
been investigated, and only a few papers or studies have 
been published.  
Establishing an appropriate market framework is a 
prerequisite for ensuring DERs maximize the value of their 
assets and activity in the power system [14][15][16][17]. 
While TSOs and DSOs have traditionally not been visible 
or active in energy retail markets, they will have a growing 
stake in their development as DERs increasingly engage in 
providing system services, e.g., frequency response, 
reactive power, balancing, etc., and competing on the 
wholesale energy market. Developing a market for system 
services will require well-functioning retail markets where 
DERs can easily switch suppliers, have access to clear 
information, and make informed choices. The market 
framework should also define the roles and responsibilities 
of TSOs and DSOs and the process between them 
regarding their use of resources. 
Given the DERs priority in the future energy system, 
operational actions must be optimized to support the 
necessary market framework while maximizing cost-
efficiency and supply security [18][19][20][21][22]. As an 
increasing share of generation connects to DSO grids, in 
particular, the majority of RES is connected at low and 
medium voltage levels, one of the most operational 
challenges for TSOs is maintaining overall system 
security. As decentralized, non-synchronous forms of 
power production displace conventional forms of 
generation, TSOs have been left with a shorter pool of 
units available to provide system services, e.g., thermal 
generation providing frequency response, voltage control, 
and inertia. The growing scarcity of system services will 
become more acute in the future and necessitates new 
operational arrangements between TSOs and DSOs to 
unlock the capabilities of DERs to plug the shortfall in 
these services. 
As with operational interaction, network planning 
processes between TSOs and DSOs need to be optimized 
and developed to support a DERs-centric market model 
[23][18][19]. This will require integrated planning 
approaches that recognize the growing interdependence of 
the transmission and distribution networks. Taking 
account of the increasing potential of DERs to provide 
system services, this should be incorporated into the 
planning stage. In this sense, network planning should be 
based on achieving the broadest possible net benefit that 
considers regional and European system needs. 
Finally, establishing the necessary market framework 
with 
the 
concomitant 
operational 
and 
planning 
arrangements will require a new approach to data handling 
[26][27][28]. More data will not only become available 
through the entry of new market participants, such as 
energy service companies (ESCOs) or independent 
aggregators but will be needed for the enhanced 
requirements around observability and putting in place the 
market framework that supports DERs engagement. The 
question of data handling should be considered from two 
different perspectives. From a network operator point of 
view, TSOs and DSOs should define their needs and 
anticipate their future needs in terms of information 
exchange for the system's secure operation for both 
network planning purposes and real-time operations. 
Meanwhile, developments in the distribution networks 
have led to new requirements for operational data which 
can be difficult or costly to obtain, e.g., real-time 
information on small-scale RES levels, and DERs 
observability is not a reality for all TSOs and DSOs [29]. 
Within this framework, this paper proposes a feasibility 
study of TSO-DSO coordination which allows using DERs 
to solve transmission network criticalities, both in 
operational and short- to medium-term time horizons, that 
does not involve the exchange of sensitive information 
between the two utilities. A straightforward algorithm is 
proposed for evaluating DERs available flexibility in 
terms of active and reactive power, and for estimating the 
aggregated capability curve at the Point of Common 
Coupling (PCC), i.e., the flexibility available downstream 
a HV/MV substation (Primary Substation (PS))). Each 
DERs is analyzed, and based on the CEI 0-16 [30] and CEI 
0-21 [31] standards, the capability curve is drawn. The CEI 
0-16 states the required standard to connect active and 
passive users to the HV and MV networks, while CEI 0-
21 states the required standard to connect active and 
passive users to the LV networks. The DERs power profile 
is derived from either real measured data coming from 
Unareti [32], the DSO of Milan and Brescia metropolitan 
area in Italy, or from the literature, while the load profile 
of the PS selected as the case study, as well as the output 
of transmission network analysis in the Milan area, from 
Terna, the Italian TSO. The primary outcome of applying 
the proposed methodology is to estimate the available 
flexibility, in terms of timing and intensity, to figure out 
the current and mid-long-term, i.e., 2030, potential 
contribution of the DERs to solve transmission network 
criticalities.  
The remaining paper is designed as follows: Section II 
presents the methodology for estimating the DERs 
available flexibility and the aggregate capability curve at 
the PS level: in the meantime the proposed approach is 
presented, the study case of a PS in Milan is used to explain 
the procedure steps more clearly. Section III shows the 
detailed results of the presented study case, using statistics 
and focusing on intraday and seasonal variation on DERs 
flexibility. Moreover, an assessment of the PS potential 
contribution to transmission network contingency relieve 
is presented. Finally, section IV summarizes the main 
findings and outlines potential future work. 


---

Page 3

---

 
II.  PROPOSED METHODOLOGY TO COMPUTE DERS 
AVAILABLE FLEXIBILITY AND THE RESULTING 
AGGREGATED DERS CAPABILITY CURVE 
The strategy implemented to obtain the resulting DERs 
aggregate capability curve is illustrated in Fig.1. The input 
data needed are the following: (1) yearly PS hourly values 
of active and reactive power. The values are measured and 
can refer either to a specific year or a combination of 
several years; (2) yearly DERs Per Unit (P.U.) hourly 
active power production. The curves are computed on 
historical data and customized based on the type of DER. 
The P.U. approach allows the algorithm to be highly 
flexible in studying as-is and mid-long-term scenarios as 
well as any PS whose input data are known; (3) capability 
curve of the DERs based on the Italian CEI 0-16 and CEI 
0-21 standards; (4) installed power of each type of DER 
downstream the considered PS.  
 
Fig. 1. Flow chart of the proposed methodology for DERs available 
flexibility and the resulting DERs aggregate capability curve. 
It is worth to be mentioned that, for the sake of 
explaining, all the following data and results refer to the 
PS Sud, one of the PS located in Milan and operated by 
Unareti, whose primary data are reported in Table 1. The 
PS is connected to the national 220kV system and, using 
four transformers, step-down the voltage to 23 kV. The 
MV and LV systems connect 5 MW of PV, 420 kW of 
hydro, and 27 MW of CHP.      
TABLE I 
PS SUD MAIN INPUT DATA 
PS main data 
Installed capacity on MV/LV grid 
[MW] 
Anom 
[MVA] 
V 
[kV] 
n° 
Tr 
PV 
Biomass/ 
Biogas 
Hydro 
 
CHP 
376 
220/23 
4 
5 
- 
0,420 
27 
 
It is worth noticing also that the proposed methodology 
used the capability curve given in the CEI 0-16 standard. 
In fact, for simplicity and based on the statistics reported 
in the Unareti Developing Plan [33], the authors assumed 
a predominance of DERs connected to the MV network, 
rather than the LV ones. As reported in table 5 of [33], in 
2019, the electricity produced by MV DERs connected to 
the Milan distribution network was 213 GWh with respect 
to only 7 GWh generated by DERs connected to LV 
feeders.    
A.  PS yearly capability curve  
As a first step, two vectors containing the 8760 hourly 
values of active and reactive power measured at the PS are 
loaded. Fig. 2 reports, for the sake of clarity, the yearly 
trend of active and reactive power measured at PS Sud, as 
well as in red the interpolating line. 
 
 
 
Fig. 2. Hourly PS active power (upper left picture) and reactive power 
(upper right picture) load profile. The lower plot is the PS yearly 
capability curve.   
Moreover, the code plots on a 2D graph the 8760 values 
of active power on the X-axis and reactive power on the 
Y-axis to realize the as-is capability curve of the PS. It is 
worth noticing that this curve already contains the DERs 
contribution. The PS capability curve is reported in the 
lower part of Fig. 2. In the following, only the boundary 
points will be drawn to facilitate interpreting the 
simulation results. 
B.  DERs available flexibility computation 
The second step of the procedure computes the 
available flexibility of each type of DER based on the 
yearly production trend and the capability curve laid down 
in CEI 0-16 standard. 
 
PV power plants 
The available PV flexibility is obtained from the yearly 
PV power output downloaded from PVGIS software [34]. 
By entering the PV installed power and the geographical 
location, PVGIS gives back the hourly annual power 
output, whose trend in P.U. is shown in Fig. 3. It is 
noticeable that, to take into account the yearly variability 
of PV production, the hourly average of the years from 
2005 to 2020 has been considered. 
 


---

Page 4

---

 
 
 
 
Fig. 3. Hourly PV power production in P.U. of the installed capacity 
(upper left picture); CEI 0-16 and standard capability curve considered 
for PV (upper right picture); boundaries of the as-is PS yearly capability 
curve in green, and considering the as-is PV flexibility in red (lower 
picture). 
Once the yearly trend is obtained, the PV capability 
curve reported in Fig. 3 is applied to each hourly power 
production, assuming that the PV installed capacity equals 
the apparent power Sn. The area highlighted in red 
represents the PV control area, bounded by the six 
operating points specified in Fig. 3. Point 1 represents the 
PV production, which is dependent, hour by hour, on the 
available solar radiation. On the one hand, it is impossible 
to have extra active power (Pupward=0), while the Pdownward 
can be computed by considering the distance between 
points 1 and 6. On the other hand, exploiting the inverter's 
peculiarities makes it possible to feed (Qupward) or absorb 
(Qdownward) reactive power into the grid, with a maximum 
power factor of 0.9, even if there is no active power 
production at that time.  
Finally, starting from the PS active-reactive power 
measurements, the 8760 corresponding PV capability 
curves are drawn to find the flexibility from PV. Fig. 3 
reports in green the boundary of the as-is PS yearly 
capability curve and the as-is PV flexibility in red. 
     
CHP power plants 
A similar approach has been implemented to estimate 
the available CHP flexibility. A statistical analysis has 
evaluated the hourly power production based on real data 
of several MV and LV CHP currently connected to the 
Unareti distribution network to find a standard yearly 
production trend. While real data are the blue dots in Fig. 
4, the fifth-degree polynomial curve computed by 
interpolating the CHP P.U. hourly production is reported 
in red. Equation (1) is the fitting curve: 
  1,89	
  5,46	  5,43		 
2,07  1,67  0,67         (1) 
where:  
• 
y is the power production in P.U. of the nominal 
power; 
• 
x is the considered hour. 
 
 
 
Fig. 4. Hourly CHP power production in P.U. of the installed capacity 
(upper left picture); CEI 0-16 and standard capability curve considered 
for CHP (upper right picture); boundaries of the as-is PS yearly 
capability curve in green, and considering the as-is CHP flexibility in 
red (lower picture).     
Fig. 4 shows that CHP production is the highest during 
winter due to the increased thermal demand. On the other 
hand, production falls during the spring and summer, 
releasing potentially more considerable flexibility.  
Once the yearly trend is estimated, the CHP capability 
curve reported in Fig. 4 is applied to each hourly power 
production, assuming that the CHP installed capacity 
equals the apparent power Sn. As for the PV, the red 
highlighted area represents the CHP control area, bounded 
by the six operating points specified in Fig. 4. Point b 
represents the CHP production. Contrary to PV, on the one 
hand, it is possible to exploit extra active power Pupward, 
i.e., the distance from point b to 1. Pdownward can be 
computed by considering the spread between points b and 
6. It is worth noticing that Pupward and Pdownward vary 
between 30% and 70% of the install capacity. On the other 
hand, exploiting the synchronous generators' peculiarities 
makes it possible to feed (Qupward) or absorb (Qdownward) 
reactive power into the grid, with a maximum power factor 
of 0.8 in overexcitation and 0.98 in under excitation, 
respectively.  
Finally, starting from the PS active-reactive power 
measurements, the corresponding 8760 CHP capability 
curves are drawn to find the flexibility made available 
from CHP. Fig. 4 reports in green the boundary of the as-
is PS yearly capability curve and in red the as-is PV 
flexibility.    
 
Hydro power plants 
A similar approach to CHP has been implemented to 
estimate the available hydropower plants' flexibility. As 
for CHP, a statistical analysis has evaluated the hourly 
power production based on real data of several MV and 
LV hydropower plants currently connected to the Unareti 
distribution network to find a standard yearly production 
trend. While real data are the blue dots in Fig. 5, the fifth-
degree polynomial curve computed by interpolating the 
hydropower plants' P.U. hourly production is reported in 
red. Equation (2) is the fitting curve: 
  4,37	
  1,08	  9,85		 


---

Page 5

---

 
3,96  6,35  0,632    (2) 
where: 
• 
y is the power production in P.U. of the nominal 
power; 
• 
x is the considered hour. 
 
 
 
Fig. 5. Hourly Hydro power production in P.U. of the installed capacity 
(upper left picture); CEI 0-16 standard capability curve considered for 
hydro (upper right picture); boundaries of the as-is PS yearly capability 
curve in green (lower picture). 
Fig. 5 clearly shows that hydropower plants' production 
follows the water availability, which increases at the 
winter season's end. Once the yearly trend is estimated, the 
same capability curve and almost the same approach used 
for CHP are applied to each hourly power production. The 
only additional assumption is that the hydropower plants 
are run-of-the-river hydroelectricity; therefore, the active 
power produced depends on water availability. Thus, it is 
assumed that the plants cannot exploit extra active power, 
i.e., Pupward=0. 
Finally, starting from the PS active-reactive power 
measurements, the corresponding 8760 hydropower 
plants' capability curves are drawn to find the flexibility 
made available by hydropower plants. It is worth noting 
that, Fig. 5, only shows the limit of the PS as-is annual 
capacity curve in green. In fact, the little hydroelectric 
power available downstream of the PS Sud, only 420 kW, 
cannot guarantee a potentially interesting value of 
flexibility to a load far greater than the current 
hydroelectric power. 
 
Electric Vehicles 
The contribution of EVs has been estimated using the 
information and data contained in [35]. Authors in [35] 
propose four hourly charge profiles of EVs, which differ 
depending on where recharging takes place: home, work, 
B2C (Business Activity), and public. Moreover, the 
proposed curves distinguish between a working day and a 
weekday. Since nowadays, the EVs are still few in Milan, 
their contribution is taken into account only in the 2030 
scenario. In the Developing Plan [33], Unareti foresees 
204,000 EVs in 2030, and demand is estimated to be 340 
GWh annually.  
Once the yearly trend is obtained, the EVs capability 
curve reported in Fig. 6 is applied to each hourly power. 
On the one hand, it is assumed that all public and work-
related charging points will be equipped with V2G 
technology, thus exploiting all four quadrants. On the other 
hand, it is supposed that home charging does not allow the 
reverse of the energy flow: in this case, the grid only sees 
the EVs as a load. Moreover, the apparent nominal power 
is assumed to be equal to the active power required in a 
specific hour, and point 1 to be the P-Q measured value in 
PS, supposing that the current contribution of EVs on PS 
active and reactive power is negligible.  
Fig. 6. CEI 0-16 standard BESS capability curve considered as EVs 
capability curve (left picture); boundaries of the as-is PS yearly 
capability curve in green, and considering the 2030 scenario EVs 
flexibility in blue (right picture).  
C.  Resulting PS aggregated DERs flexibility assessment  
The procedure's last step aims to compute the 
aggregated DERs flexibility at the PCC between the 
transmission and the distribution network in the as-is and 
2030 scenarios. The following Table II reports the 
expected DERs deployment downstream of the PS Sud 
within 2030.   
TABLE. II  
PS SUD INSTALLED CAPACITY IN THE AS-IS AND 2030 SCENARIOS 
Scenario 
Installed capacity on MV/LV grid [MW] 
PV 
Biomass/ 
Biogas 
Hydro 
 
CHP 
as-is 
5 
- 
0,420 
27 
2030 
16 
- 
0,420 
29 
 
Based on the National Trend (NT) Italia scenario [36], 
the PV installed capacity should increase in the service 
area of the PS Sud by 11 MW before 2030. Instead, based 
on Unareti scenario, deployment of an additional 2 MW of 
CHP is expected [33]. On the other hand, no new 
installation of hydro and biomass/biogas is envisaged.  
Fig. 7 summarizes the simulation results. Starting from 
the as-is PS Sud capability curve, in green, the resulting 
DERs flexibility is highlighted in red for the as-is scenario 
and blue for the 2030 ones.     
 
 


---

Page 6

---

 
Fig. 7. Boundaries of the as-is PS yearly capability curve (in green), 
considering the as-is flexibility (in red) and the    
2030 scenario flexibility (in blue).  
Looking at Fig. 7, it can be easily seen that there is 
already consistent potential flexibility, which is expected 
to rise in 2030. A significant additional contribution to 
upward and downward active power flexibility will be 
available thanks to the foreseen installation of new PV and 
EVs. Moreover, a proportional increase in upward and 
downward reactive power flexibility is expected.  
III.  ASSESSMENT OF PS SUD POTENTIAL CONTRIBUTION TO 
TRANSMISSION NETWORK CONTINGENCY RELIEVE  
This last section aims at assessing the potential 
contribution of DERs flexibility in relieving voltage and 
current contingency on the HV grid. Based on 
transmission network analysis and operation evidence in 
the area of Milan, it is determined that meaningful values 
of flexibility to relieve HV transmission network 
constraints are at least either 10 MW or 10 Mvar. In 
general 10 MW variation brings to an appreciable variation 
of the line's power flows departing from the PS Sud, while 
10 Mvar can be able to vary the voltage at the PS Sud of 
about 0.5 kV.  
To better determine if DERs installed in the Milan area 
could help manage transmission grid issues, Fig. 8 reports 
the normal distribution related to the computed Pupward and 
Pdownward values in the 2030 scenario. On the one hand, the 
simulation suggests an average upward active power of 
about 20 MW, varying in the range 10 MW-30 MW. On 
the other hand, a more limited downward contribution is 
expected: 17 on average, ranging from 0 to -30 MW. 
Regarding reactive power, instead, it is expected a 
pretty stable Qupward of 35 Mvar and a Qdownward of 25 Mvar. 
Thus, the outcomes of the simulations suggest that DERs 
installed on the distribution network could contribute to a 
better transmission network operation, and help in 
managing voltage and power flow issues.    
 
 
 
Fig. 8. Normal probability distribution in 2030 scenario: Pupward (upper 
picture) and Pdownward (lower picture). 
Fig. 9 shows the hourly trend of the active and reactive 
flexibility, upward in blue and downward in red, for the 
2030 scenario. Regarding active power, during summer 
months, upward flexibility has a large contribution, mainly 
related to the flexibility provided by CHPs. On the one 
hand, during winter months, CHPs operate at higher power 
to satisfy the greater thermal demand, so upward flexibility 
from the operating point to the install capacity is reduced. 
On the other hand, in the warmer months, when the heating 
demand is lower, CHPs operate less, making available a 
more significant potential upward flexibility. Vice versa 
works for downward flexibility, potentially higher in 
winter months and more down in warmer ones.  
Regarding reactive power, the potential flexibility is 
stable, predominating upward rather than downward. 
 
 


---

Page 7

---

 
 
Fig. 9. Trend of hourly Pupward and Pdownward (upper picture) and Qupward 
and Qdownward (lower picture) in the 2030 scenario. 
As an additional outcome, Fig. 10 reports the 
availability of active power flexibility during daytime and 
night hours in the form of maximum upward and 
downward for each day. It can be observed that the 
downward PV contribution is more relevant during the 
daytime and especially during the summer months when 
the contribution of CHPs is reduced. During night hours, 
there is no contribution of PV, and therefore flexibility 
remains mainly linked to CHPs and EVs.  
 
 
 
Fig. 10. Trend of daily maximum Pupward and Pdownward during daylight 
hours (upper picture) and night hours (lower picture) in the 2030 
scenario. 
Moreover, considering the daily values, the box plots 
reported in Fig. 11 can be set up. The upward flexibility 
has a narrow gap between minimum and maximum values 
and even between the first and the third quartile: we can 
conclude that upward flexibility is more predictable than 
downward ones, probably due to the downward flexibility 
related to the stochastic behavior of PV. Moreover, it is 
worth noticing that downward flexibility shows several 
outliers during the winter months, making a prediction of 
the power available for flexibility again more complicated.    
A similar analysis on reactive power flexibilities is not 
reported due to pretty constant values throughout the year. 
 
  
 
Fig. 11.  Monthly Pupward (upper picture) and Pdownward (lower picture) in 
2030 scenario. 
Finally, the graphs reported in Fig. 12 show a typical 
trend of Pupward for a sample day, i.e., September 4th 2022. 
It is possible to observe that the flexibility is greater during 
daylight hours, with a steep ramp and a peak around 10 
A.M. and a second smaller peak around 9:00 P.M.. This is 
another interesting outcome of the analysis. In fact, the 
time of higher DERs upward flexibility seems to match 
with the time of higher demand, making the flexibility a 
valuable tool to smooth the load demand curve and help in 


---

Page 8

---

 
relieving potential network contingencies.       
 
 
 
Fig. 12.  Pupward daily normal probability distribution (upper picture) 
and hourly trend (lower picture) in the 2030 scenario. 
IV.  CONCLUSION 
This paper proposes a feasibility study of TSO-DSO 
coordination which allows using DERs to solve 
transmission network criticalities, both in operational and 
short- to medium-term time horizons, without involving 
the exchange of sensitive information between the two 
utilities. A detailed analysis has been carried out on the 
available flexibility of DERs active and reactive power. 
The results obtained show that aggregated DERs under the 
PS Sud, used as a case study, can provide an interesting 
degree of flexibility to the TSO. In particular, DERs could 
be used to control the HV bus voltage through a substantial 
variation in reactive power to be fed into or absorbed by 
the transmission grid. DERs can also be helpful in terms 
of active power: they could help the TSO by limiting the 
active power production or, vice versa, by increasing the 
output to reduce the power flow from the transmission to 
the distribution network. As a future development, 
additional simulations can be easily carried out, including 
other possible DERs: storage systems, static synchronous 
compensator, and tap-changer of HV/MV transformers 
installed in PS, distribution network reconfiguration. 
Moreover, the distribution network constraints can be also 
taken into account to verify the required flexibility would 
be exploited without any network violations. Regarding 
the issue of data exchange and the TSO's visibility over the 
downstream DSO networks instead, nowadays, the TSO 
only observes power exchanges between the transmission 
grid and each PS, but this information is no longer 
sufficient for an efficient integrated transmission and 
distribution network planning process and to understand 
the dynamics of events in real-time, to adopt the most 
effective and efficient countermeasures. Enhancing the 
observability of the DSO grid would lead to improvements 
in many applications used for the planning and secure 
management of the transmission network by Terna.  
REFERENCES 
[1] 
A. Bosisio, A. Berizzi, A. Morotti, G. Iannarelli, B. 
Greco, and C. Boccaletti, “A GIS-based approach to 
assessing large-scale building-integrated photovoltaic 
generation: a case study of Milan, Italy,” in 2022 AEIT 
International Annual Conference (AEIT), 2022, pp. 1–
6. doi: 10.23919/AEIT56783.2022.9951760. 
[2] 
G. Iannarelli, A. Cirocco, B. Greco, C. Moscatiello, A. 
Bosisio, and C. Boccaletti, “Management strategy of EV 
fleets 
charging 
stations 
for 
demand 
response 
capabilities: a case study,” in 2022 AEIT International 
Annual Conference (AEIT), 2022, pp. 1–6. doi: 
10.23919/AEIT56783.2022.9951728. 
[3] 
R. Faranda, L. Gozzi, A. Bosisio, and K. Akkala, 
“SCADA system for optimization of energy exchange 
with the BESS in a residential case,” in Proceedings - 
2019 IEEE International Conference on Environment 
and Electrical Engineering and 2019 IEEE Industrial 
and Commercial Power Systems Europe, EEEIC/I and 
CPS 
Europe 
2019, 
2019. 
doi: 
10.1109/EEEIC.2019.8783941. 
[4] 
C. Mosca et al., “Mitigation of frequency stability issues 
in low inertia power systems using synchronous 
compensators and battery energy storage systems,” IET 
Generation, Transmission & Distribution, vol. 13, no. 
17, pp. 3951–3959, Sep. 2019, doi: 10.1049/IET-
GTD.2018.7008. 
[5] 
G. Iannarelli, A. Bosisio, B. Greco, C. Moscatiello, and 
C. Boccaletti, “Flexible resources dispatching to assist 
DR management in urban distribution network 
scenarios including PV generation: An Italian case 
study,” in Proceedings - 2020 IEEE International 
Conference on Environment and Electrical Engineering 
and 2020 IEEE Industrial and Commercial Power 
Systems Europe, EEEIC / I and CPS Europe 2020, 
Institute of Electrical and Electronics Engineers Inc., 
Jun. 
2020. 
doi: 
10.1109/EEEIC/ICPSEUROPE49358.2020.9160856. 
[6] 
CEDEC, EDSO, entsoe, Eurelectric, and GEODE, 
“General guidelines for reinforcing the cooperation 
between 
TSOs 
and 
DSOs.” 
https://eepublicdownloads.entsoe.eu/clean-
documents/Publications/Position%20papers%20and%2
0reports/entsoe_pp_TSO-DSO_web.pdf (accessed Feb. 
22, 2023). 
[7] 
T. Alazemi, M. Darwish, and M. Radi, “TSO/DSO 
Coordination for RES Integration: A Systematic 
Literature Review,” Energies (Basel), vol. 15, no. 19, p. 
7312, Oct. 2022, doi: 10.3390/en15197312. 
[8] 
European Parliament and Council, “Directive (EU) 
2019/944 of the European Parliament and of the Council 


---

Page 9

---

 
of 5 June 2019 on common rules for the internal market 
for electricity and amending Directive 2012/27/EU 
(recast) (Text with EEA relevance.).” https://eur-
lex.europa.eu/legal-
content/EN/TXT/?uri=celex%3A32019L0944 
(accessed Dec. 09, 2022). 
[9] 
European Parliament and Council, “Fit for 55 - The 
EU’s 
plan 
for 
a 
green 
transition.” 
https://www.consilium.europa.eu/en/policies/green-
deal/fit-for-55-the-eu-plan-for-a-green-transition/ 
(accessed Jan. 09, 2023). 
[10] 
Terna 
S.p.A., 
“Italian 
Grid 
Code.” 
https://www.terna.it/en/electric-system/grid-
codes/italian-grid-code (accessed Dec. 07, 2022). 
[11] 
Y. Liu and L. Wu, “Integrating Distributed Energy 
Resources into the Independent System Operators’ 
Energy 
Market: 
a 
Review,” 
Current 
Sustainable/Renewable Energy Reports, vol. 8, no. 4, 
pp. 233–241, 2021, doi: 10.1007/s40518-021-00190-8. 
[12] 
A. G. Givisiez, K. Petrou, and L. F. Ochoa, “A Review 
on TSO-DSO Coordination Models and Solution 
Techniques,” Electric Power Systems Research, vol. 
189, 
p. 
106659, 
2020, 
doi: 
https://doi.org/10.1016/j.epsr.2020.106659. 
[13] 
A. Bytyqi, S. Gandhi, E. Lambert, and N. Petrovič, “A 
Review on TSO-DSO Data Exchange, CIM Extensions 
and Interoperability Aspects,” Journal of Modern 
Power Systems and Clean Energy, vol. 10, no. 2, pp. 
309–315, 2022, doi: 10.35833/MPCE.2021.000770. 
[14] 
M. Khojasteh, P. Faria, F. Lezama, and Z. Vale, “A 
hierarchy model to use local resources by DSO and TSO 
in the balancing market,” Energy, vol. 267, p. 126461, 
2023, 
doi: 
https://doi.org/10.1016/j.energy.2022.126461. 
[15] 
S. I. Vagropoulos, P. N. Biskas, and A. G. Bakirtzis, 
“Market-based TSO-DSO coordination for enhanced 
flexibility services provision,” Electric Power Systems 
Research, 
vol. 
208, 
p. 
107883, 
2022, 
doi: 
https://doi.org/10.1016/j.epsr.2022.107883. 
[16] 
A. Papalexopoulos, R. Frowd, and A. Birbas, “On the 
development of organized nodal local energy markets 
and a framework for the TSO-DSO coordination,” 
Electric Power Systems Research, vol. 189, p. 106810, 
2020, doi: https://doi.org/10.1016/j.epsr.2020.106810. 
[17] 
A. Vicente-Pastor, J. Nieto-Martin, D. W. Bunn, and A. 
Laur, “Evaluation of flexibility markets for retailer-dso-
tso coordination,” IEEE Transactions on Power 
Systems, vol. 34, no. 3, pp. 2003–2012, 2019, doi: 
10.1109/TPWRS.2018.2880123. 
[18] 
M. Usman, M. I. Alizadeh, F. Capitanescu, I.-I. 
Avramidis, and A. G. Madureira, “A novel two-stage 
TSO–DSO coordination approach for managing 
congestion and voltages,” International Journal of 
Electrical Power and Energy Systems, vol. 147, 2023, 
doi: 10.1016/j.ijepes.2022.108887. 
[19] 
J. Ringelstein, M. Vogt, A. M. Khavari, R. Ciavarella, 
M. di Somma, and G. Graditi, “A methodology for 
improved TSO-DSO coordination in grid operation 
planning,” Electric Power Systems Research, vol. 211, 
p. 
108445, 
2022, 
doi: 
https://doi.org/10.1016/j.epsr.2022.108445. 
[20] 
M. Resener, B. Venkatesh, B. M. P. Ferraz, S. Haffner, 
A. Balbinot, and L. A. Pereira, “MILP Model for 
Optimal Day-Ahead PDS Scheduling Considering TSO-
DSO Interconnection Power Flow Commitment Under 
Uncertainty,” IEEE Transactions on Power Systems, pp. 
1–14, 2022, doi: 10.1109/TPWRS.2022.3228838. 
[21] 
R. Dzikowski, “DSO-TSO coordination of day-ahead 
operation planning with the use of distributed energy 
resources,” Energies (Basel), vol. 13, no. 14, 2020, doi: 
10.3390/en13143559. 
[22] 
C. Mosca et al., “Technical and Economic Impact of the 
Inertia Constraints on Power Plant Unit Commitment,” 
IEEE Open Access Journal of Power and Energy, vol. 
7, 
pp. 
441–452, 
2020, 
doi: 
10.1109/OAJPE.2020.3029118. 
[23] 
G. Celli, F. Pilo, G. Pisano, S. Ruggeri, and G. G. Soma, 
“Risk-oriented 
planning 
for 
flexibility-based 
distribution system development,” Sustainable Energy, 
Grids and Networks, vol. 30, p. 100594, 2022, doi: 
https://doi.org/10.1016/j.segan.2021.100594. 
[24] 
J. Liu, L. Zhang, K. Liu, Z. Tang, P. P. Zeng, and Y. Li, 
“To exploit the flexibility of TSO–DSO interaction: A 
coordinated 
transmission 
robust 
planning 
and 
distribution stochastic reinforcement solution,” Energy 
Reports, 
vol. 
9, 
pp. 
27–36, 
2023, 
doi: 
https://doi.org/10.1016/j.egyr.2022.10.368. 
[25] 
E. F. Alvarez, L. Olmos, A. Ramos, K. Antoniadou-
Plytaria, D. Steen, and L. A. Tuan, “Values and impacts 
of 
incorporating 
local 
flexibility 
services 
in 
transmission expansion planning,” Electric Power 
Systems Research, vol. 212, p. 108480, 2022, doi: 
https://doi.org/10.1016/j.epsr.2022.108480. 
[26] 
N. R. Perez et al., “ICT architectures for TSO-DSO 
coordination 
and 
data 
exchange: 
a 
European 
perspective,” IEEE Trans Smart Grid, p. 1, 2022, doi: 
10.1109/TSG.2022.3206092. 
[27] 
M. Radi, G. Taylor, J. Cantenot, E. Lambert, and N. 
Suljanovic, 
“Developing 
Enhanced 
TSO-DSO 
Information and Data Exchange Based on a Novel Use 
Case Methodology,” Front Energy Res, vol. 9, 2021, 
doi: 10.3389/fenrg.2021.670573. 
[28] 
S. Skok, A. Mutapčić, R. Rubesa, and M. Bazina, 
“Transmission power system modeling by using 
aggregated distributed generation model based on a 
TSO—DSO data exchange scheme,” Energies (Basel), 
vol. 13, no. 15, 2020, doi: 10.3390/en13153949. 
[29] 
C. Mosca et al., “A new real-time approach for the load 
forecasting in the operation of sub-transmission 
systems,” 
in 
2019 
AEIT 
International 
Annual 
Conference 
(AEIT), 
2019, 
pp. 
1–6. 
doi: 
10.23919/AEIT.2019.8893398. 
[30] 
Comitato Elettrotecnico Italiano (CEI), “CEI-016 
standard.” Accessed: Jan. 09, 2023. [Online]. Available: 
https://www.ceinorme.it/strumenti-online/norme-cei-0-
16-e-0-21/ 
[31] 
Comitato Elettrotecnico Italiano (CEI), “CEI  0-21 
standard.” Accessed: Jan. 09, 2023. [Online]. Available: 
https://www.ceinorme.it/strumenti-online/norme-cei-0-
16-e-0-21/ 
[32] 
A. Bosisio, D. D. Giustina, S. Fratti, A. Dede, and S. 
Gozzi, 
“A 
metamodel 
for 
multi-utilities 
asset 
management,” in 2019 IEEE Milan PowerTech, 
PowerTech 
2019, 
2019. 
doi: 
10.1109/PTC.2019.8810812. 
[33] 
UNARETI S.p.A., “Piano di Sviluppo e Incremento 
resilienza,” 
2021. 
https://www.unareti.it/unr/unareti/elettricita/cittadini/pi
ano-di-sviluppo-e-incremento-resilienza/ 
(accessed 
Feb. 16, 2021). 
[34] 
European Commission, “Photovoltaic Geographical 
Information 
System 
(PVGIS).” 
https://re.jrc.ec.europa.eu/pvg_tools/en/ (accessed Jan. 
09, 2023). 


---

Page 10

---

 
[35] 
G. Rancilio, F. Bovera, and M. Delfanti, “Tariff-based 
regulatory sandboxes for EV smart charging: Impacts on 
the tariff and the power system in a national 
framework,” Int J Energy Res, vol. 46, no. 11, pp. 
14794–14813, Sep. 2022, doi: 10.1002/ER.8183. 
[36] 
Terna spa, “Scenarios.” https://www.terna.it/it/sistema-
elettrico/rete/piano-sviluppo-rete/scenari (accessed Jan. 
09, 2023). 
  
 
