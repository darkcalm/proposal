# TSO DSO coordination in a context of distributed energy resource penetration

## Paper Metadata

- **Filename:** TSO_DSO coordination in a context of distributed energy resource penetration.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:09.141594
- **Total Pages:** 28

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

TSO/DSO Coordination in a 
Context of Distributed Energy 
Resource Penetration
Michael Birk, José Pablo Chaves-Ávila, Tomás Gómez, and 
Richard Tabors
M A S S A C H U S E T T S I N S T I T U T E O F T E C H N O L O G Y
October 2017 CEEPR WP 2017-017
Working Paper Series

---


### Page 3

a Corresponding author. MIT Energy Initiative and Institute for Data, Systems, and Society, Massachusetts Institute of 
Technology (MIT), 77 Massachusetts Ave., Cambridge, MA 02139, USA. Tel: +1 516 448 7803. Email: birkm@mit.edu. 
b Institute for Research in Technology (IIT), Comillas Pontifical University, Sta. Cruz de Marcenado 26, Madrid, Spain. Email: 
Jose.Chaves@comillas.edu 
c Institute for Research in Technology (IIT), Comillas Pontifical University, Sta. Cruz de Marcenado 26, Madrid, Spain. Email: 
Tomas.Gomez@comillas.edu 
d Massachusetts Institute of Technology (MIT), 77 Massachusetts Ave, Cambridge, MA, USA. Email: rtabors@mit.edu 
1 

TSO/DSO COORDINATION IN A CONTEXT OF DISTRIBUTED ENERGY 
RESOURCE PENETRATION 
Michael Birka, José Pablo Chaves-Ávilab, Tomás Gómezc, Richard Taborsd 
Abstract 
With respect to electrical grids and power systems there is a trend towards a greater penetration and 
subsequent utilization of distributed energy resources (“DERs”). DERs can provide services to both 
Distribution System Operators (“DSOs”)1 and Transmission System Operators (“TSOs”)2. Distributed 
energy resources are typically installed and interconnected to electricity networks that may or may not be 
completely controlled, monitored or analyzed by the power system operators themselves. If and when 
DERs are operated to provide system services and/or market actions, this may lead to system benefits and 
efficiency improvements, but can come with technical, economic, and jurisdictional challenges. 
Aggregators, DSOs, and TSOs, must be able to coordinate, monitor and dispatch resources as well as 
study and share information in a timely manner. Examples and recommendations for future coordination 
and interactions between the TSO, DSO, DER owners, and aggregators are presented and examined, in 
operation and market-based contexts, relevant to European and US electricity networks. 
Keywords: Distribution system operator, utility, transmission system operator, distributed energy 
resources, wholesale markets, distribution-level markets, transmission-distribution coordination functions, 
electricity services. 

1 Distribution System Operators and Utilities 
2 TSOs and Independent System Operators or Regional Transmission Operators

---


### Page 4

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
2 
1 INTRODUCTION 
Distributed Energy Resources typically are defined as technologies that can be installed “behind the 
meter” on consumer premises connected to on-site loads or remote premises without on-site load. DERs 
are typically interconnected on distribution and lower voltage networks, and are smaller in installed 
capacity; ranging in the order of a few kilowatts ("k W") to a few megawatts ("MW") in rated nameplate 
capacity. A multitude of governments, transmission system or regional operators, public utility 
commissions and regulators, utility companies or distribution system operators, workshops, think tanks, 
research laboratories, and research communities will define DERs slightly differently, that include a 
diversity of energy resource types, capacity, and where on the power system the resources are 
interconnected. 
Recent technological advances and cost declines in distributed energy resources and information and 
communication technologies ("ICT") as well as specific regional and state policies, mandates, and 
incentives, regulatory paradigms, and consumer trends have been major driving forces behind the 
increasing penetration of DERs. DERs can and do provide many services to the electric grid, and this 
trend will only increase as the ubiquity and ability to control these assets, for instance through 
management systems and smart inverters, continues to increase. However, current market designs and 
operational practices do not provide a level playing field for DERs to deliver services. Existing markets 
need to evolve, new markets need to be created, and new roles and coordination functions need to be 
established between distribution and transmission system operators. 
This paper is structured as an exploration into the services that DERs can provide, market structures 
observed in the European Union and United States, the interaction between distribution and transmission 
system operators, the new roles that DSOs would need to perform to unlock the most value from DERs, 
and certain market barriers for DERs at the transmission level. Coordinating and co-optimizing 
distributed, typically low-voltage assets, across jurisdictions and levels of the power system are still quite 
nascent. Future roles of Utilities and distribution system operators, new planning and interconnection 
methodologies, and new wholesale market designs for DERs have been researched in theory, but not yet 
extensively adopted in industry. This paper highlights and advocates for not only a level-playing field for 
DERs where their services can be valued in markets, but also for managing the complexities associated 
with communication, coordination, and interactions between grid operators to coordinate the services 
provided by DERs. 
1.1 
The global reach of distributed energy resources 
Distributed generation technologies, and their impacts on operations and markets, have been researched 
previously, but only now have they reached significant levels of penetration in the European Union (EU)

---


### Page 5

Birk et al, 2017 
3 
and popularity in the United States (US). The penetration of distributed energy resources into markets 
through the provision of electricity services has important consequences for different stakeholders: 
consumers, system operators, energy service providers and technology companies, market traders, power 
equipment manufacturers, and regulators. From a market perspective, new business models are emerging 
related to DERs. Certain regulatory agencies are incentivizing and requiring network operators to take a 
more active role in the operation of their systems and to utilize innovative solutions related to distributed 
energy resource adoption and integration (Eurelectric, 2013; IDE4L, 2014). For grid operations, 
transitioning from passive to active distribution network management systems require education and 
training for the workforce as well as technology upgrades in communication, hardware and software. 
With DERs, consumers are becoming more active participants on the electric grid, helping to provide 
system services, which may lead to a more efficient and flexible power system. 
Different actions and initiatives are currently under development globally to efficiently integrate DERs 
into the power system and to reform the roles of the agents involved in the transformation. The European 
Commission (EC) and the New York State Department of Public Service in Reforming the Energy Vision 
(REV) are two examples of institutions actively pursuing increased coordination between the DSOs or 
Utilities and the TSOs or Independent System Operators (ISOs), respectively. Both the European 
Commission and the REV proceedings are actively pursuing considerations for new electricity market 
designs (European Commission, 2015; New York State Department of Public Service, 2015). ENTSO-E 
(European Network of Transmission System Operators for electricity), ISGAN (International Smart Grid 
Action Networks), CIRED (International Conference on Electricity Distribution), EDSOs (European 
Distribution System Operators), CIGRÉ (International Council on Large Electric Systems), GO153 have 
task forces and working groups investigating future roles, relationships, markets, and coordination 
requirements for and between the operators of the electric grid. 
1.2 
A phased approach framework for distributed resource penetration 
The research presented in this paper focuses on the organization of the interactions between TSOs and 
DSOs within a time frame within about 10 years. In this time frame, two situations are likely to unfold. 
An initial phase where current markets and practices of DSOs and TSOs continue to exist, there is low 
penetration of distributed energy resource and low deployment of advance metering infrastructure 
(AMI4). In this initial phase, DERs can provide services that have, in the past, dominantly been provided 
 
3 GO15 Reliable and Sustainable Power Grids. http://www.go15.org/ 
4 Advanced metering infrastructure is commonly used or being assessed in industry. It is possible that future technologies or 
techniques that can provide the same or similar services will be used with greater ubiquity (i.e. monitoring and control of solar 
PV, smart inverter, battery, and/or load assets by an aggregator can help inform the utility of the assets)

---


### Page 6

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
4 
by centralized resources. In this initial phase, DERs provide services mainly to Transmission System 
Operators through the applicable market mechanisms or are operated in a limited fashion by DSOs. DERs 
may access the Wholesale or Transmission level markets through demand response programs typically 
operated by an aggregator5. In a subsequent phase, a higher integration of DERs and AMI are expected 
and DERs will be able to provide new services be compensated by the applicable market mechanism. The 
developments of both phases are contingent upon many system specific factors and, in particular, total 
amount of distributed resources connected to the networks, market designs, regulatory frameworks and 
vicissitudes. A high-level visual representation of the main interactions between DERs and system 
operators are shown in Fig. 1. 
In the initial phase, the net power flows are mainly unidirectional from transmission networks to endusers; DERs would provide services to the TSO and the TSO would send operational signals to DERs. 
Distribution System Operators have limited or nonexistent interactions with the TSO or DERs, in regards 
to utilization of DERs for system services. Typical services provided by DERs or Aggregators are load or 
demand reducing. In the subsequent phase, power flows can be bidirectional; DERs can provide services 
to TSO and DSO and both the TSO and DSO send operational signals to DERs. In addition, operational 
signals may be coordinated between both operators. In this phase, DERs would be able to provide a wider 
range of services to the different levels of the power system, so long as the appropriate market designs are 
in place and the operators have some level of visibility and/or control. 
 
Fig. 1: Simplified diagram of the main interactions between TSO, DSO and DERs 
 
5 Wholesale power markets exist in the EU and the US with many different constructs and designs. Essentially, these markets 
exist at the bulk or transmission or high-voltage level of the power system. These markets traditionally have been the platform 
where the supply from large centralized power generation facilities is matched with the electric demand, typically from load 
serving entities such as utilities. In the US, the transmission system operator is generally also the wholesale market operator 
 
TSO$
DSO$
DERs/
Aggregators$
Ini4al$Phase$
Subsequent$Phase$
DERs/
Aggregators$
DSO$
TSO$
Power$Flow$
Services$
Opera4onal$Signals$

---


### Page 7

Birk et al, 2017 
5 
In the initial phase, DERs can provide services to the TSO in established markets without violating 
constraints within the distribution networks. In this initial phase, the margin or buffer built within 
distribution networks would be enough to manage flows and DSOs may not need to buy services from 
DERs (this phase is similar to most of the current practices where DSOs use only “wire solutions” to 
solve network constraints). The initial phase mentioned in Fig. 1 is a generalization because there are 
some networks where there is DSO-level communication with DERs, but the DERs may not be 
participants in those markets. In this initial phase, there are challenges with respect to the effectiveness of 
DERs providing TSO services and the need to extend price signals further into distribution networks to 
guarantee a level playing field between centralized and distributed resources. Creating a level-playing 
field for distributed and centralized resources is a complex undertaking involving extensive and perhaps 
lengthy stakeholder processes, but there are regions such as in New York, Massachusetts, Hawaii, 
California, Spain, and the UK that are advancing well into this new paradigm by being open to the 
utilization of DERs for system services; however, the paradigm shifts are far from complete in many of 
the developed power systems (Newcomb, 2013). 
In a subsequent phase, and in some jurisdictions this is already occurring, DSOs or utilities will buy 
services from DERs, such as in non-wires alternatives (NWA). Non-wires alternatives are programs in 
which alternative or new proposed solutions are put through the same cost-benefit analysis, as would a 
traditional solution for the chance to be used to delay or defer potentially costly upgrades. Other, more 
active services provided on the distribution network could potentially be in conflict with TSO services. 
Different challenges need to be addressed prior to, and during this phase; first to establish new roles of 
DSOs and the mechanisms for purchasing distribution services, and second, to make those mechanisms 
coherent and coordinated with those managed by the TSO. The specific roles, functions and interactions 
between DSOs and TSOs will depend upon many factors. Research suggests that a few models could 
emerge where there is a different extent to the interaction and coordination between DERs, Distribution 
Operators, and Transmission System Operators (De Martini, 2015; Migliavacca, 2016). 
1.3 
Distributed energy services and market presence 
DERs can provide both energy-related services as well as network-related services (Pérez-Arriaga, 2015). 
Electricity services are detailed in Fig. 2. Energy related services include real power, frequency 
regulation, and operating reserves, black start capability, and firm capacity (defined as enough capability 
of generation and demand to respond during operations). Frequency regulation is an energy-related 
 
and is required to meet a “standard market design” as defined by FERC (i.e. NYISO, CAISO, ISONE, PJM, MISO). In the EU, 
the transmission network operator is a separate entity from the market operator.

---


### Page 8

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
6 
service that is utilized to maintain the frequency of the electrical grid within a specific bound. To 
maintain the frequency within the specified grid code limits, the grid operators typically send automatic 
communications and signals to the power generation units (i.e. automatic generation control (AGC), as it 
is in the US, communicates set points for maintaining frequency on a sub-ten second basis). In the US, the 
frequency is maintained around a nominal 60Hz and in Europe the frequency is maintained around a 
nominal 50Hz; to maintain these nominal frequencies the grid supply and demand must be in constantly 
and automatically monitored and controlled. Reserves are typically more discrete and the hierarchy of 
operating reserves corresponds to the timing with which generators6 can respond to system loading 
conditions, or fluctuations, and can vary from milliseconds to hours (i.e. tertiary reserves respond slower 
than secondary which respond slower than primary). Network-related services include voltage control 
through reactive power support, power quality, mitigation of thermal or voltage constraints, and reduction 
in losses. 
 
Fig. 2: Primary electricity services separated into two categories: energy and network, as well secondary services 
(Pérez-Arriaga et al, 2016). 
Distributed energy resources can provide services to the power system at the distribution level or 
transmission level. For instance, a PJM pilot project found that electric vehicles could effectively provide 
ancillary services to the grid, such as real-time frequency regulation and spinning reserves (Kempton, 
2008; Fitzgerald, 2015). These services are typically provided through an applicable market mechanism 
and corresponding price signal. Currently, services are most commonly priced, valued and cleared in 
wholesale markets. In some circumstances there are regulations or market structures that make it 
challenging for DERs to access wholesale markets and enable a level playing field for DERs. The 
transmission system and wholesale market operator may or may not be able to purchase different services 
from DERs, such as spinning and non-spinning reserves (or frequency reserves/response in the European 
Union), firm capacity, voltage support, and black-start. Future electricity systems might have very 
different ways to charge for different services. For instance, firm capacity could be automated with the 
right tariff structures, voltage control could be fixed or variable depending on the technology connected 
 
6 Or demand response, which is typically the curtailment of load. 
Energy Related Services 
 
Electrical Energy 
 
Firm Capacity Black-start 
 
Primary Operating Reserves 
 
Secondary and Tertiary Reserves 
Network Related Services 
 
Network Connection 
 
Voltage Control Power Quality 
 
Energy Loss Reduction 
 
Network Constraint Management 
Secondary Electricity 
Services 
 
Emissions Restrictions 
 
Renewables Incentives (Fi T, ITC, or PTC) 
 
Domestic Fuel Content Requirement

---


### Page 9

Birk et al, 2017 
7 
on the grid, even grid interconnection, given the potential future for islanded grids, microgrids and 
potential for load defection, could be fixed or variable in nature, depending upon the regulatory 
framework (Pérez-Arriaga, 2014; Rocky Mountain Institute, 2015; Fitzgerald, 2015). Resources and 
technologies that are capable of providing system services should have fair and equal access to participate 
under appropriate market designs, and compensated for their quality of provision of the services to the 
grid. 
In certain cases where DERs have limited participation in markets it is due in part to market rule 
restrictions, such as minimum resource size (capacity), shown in Table 1. In the United States, DERs are 
generally located on distribution grids at lower voltages (35 k V or below7) and they have limited access to 
wholesale markets due to utility imposed standards for interconnection or capacity restrictions in 
wholesale markets (IRC, 2014)8. Many of these requirements to participate in wholesale markets unfairly 
restrict DERs from providing system services. In European wholesale markets, these requirements are 
much higher and on the order of 5 to 10 MW (ENTSO-E, 2015). If the markets allow for aggregation, 
Aggregators may be able to leap those barriers, but in some markets they still may be restricted to 
participate in the provision of those services. 
Table 1 Requirements to participate in US regulation markets (Mac Donald et al., 2012). 
 
At first the PJM tariff for ancillary service provision required 5 MW for offers into the markets, but 
decreased over time to 100 k W; even though this decrease benefited the smaller curtailment service 
providers, it would occasionally still be a barrier because most providers had small portfolios when they 
 
7 The precise voltage specification for distribution or transmission networks depends on the location. Germany for instance has 
over 98% of their 1 million plus solar PV plants connected to the decentralized low-voltage grid, most of it being on the low and 
medium voltage grid (Wirth, 2015), but the classification for the distribution grid can vary widely in voltage from 230 V to 
110k V (Volkmar, 2012). 
8 In the US, the meshed network, typically under the jurisdiction of the regional or transmission operator, usually exists between 
34.5 k V and 100 k V. Below the 34.5 k V is typically operated radially. Radial lines are typical for low voltage systems due to the 
ubiquity of unidirectional flow to end-consumers and are typically out of the definition for the bulk electric system (FERC Order 
No. 773-A).

---


### Page 10

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
8 
wanted to provide services into the wholesale market (PJM, 2016). In order the access the market, the 
curtailment service providers would need to utilize electronic systems, and the system, at first, could not 
accommodate such decimal places for resources such as demand response, because the only resources that 
used to access these markets were larger scale central generation resources (PJM, 2016). 
Distributed energy resources access wholesale markets through demand response programs behind the 
meter ordered by state commissions to the electric distribution company (EDC) or by competitive 
curtailment service providers (CSP), i.e. energy efficiency measures or battery storage in the PJM market 
(DNV GL Energy, 2014). In the PJM jurisdiction, about 30% of the demand response participation comes 
from Electric Distribution Company (EDC) programs, whereas 70% comes from “competitive 
curtailment service providers” (PJM, 2016). Most wholesale markets in the US support demand response 
integration by having an energy, capacity, regulation or reserve market mechanisms to support demand 
response integration (IRC, 2014). Wholesale markets in the US allow DERs as a “demand response 
resource, a production resource or storage resource” (DNV GL Energy, 2014). There are some wholesale 
markets where distributed energy resources can bid into such as in the forward capacity market in PJM 
where more than 14 GW of demand response and energy efficiency have cleared over the past 5 years 
(Newcomb, 2013). 
However, allowing distributed resources to participate in wholesale markets through only demand 
response programs has its limitations. PJM, like NYISO, prohibits power exports from customers that 
participate in wholesale demand response programs, to distinguish between demand response with and 
without generation (PJM, 2016). Certain resources can provide services above and beyond a load 
curtailment service. By placing restrictions, the markets are limiting the services these resources could 
provide, and therefore reducing the value it could provide to the electricity system. 
Energy storage is a technology that could provide a much wider range of services to the power system if 
certain barriers are overcome. Storage can be modeled as a load as well as a generation resource, and a 
lack of proper classification of energy storage across multiple markets has led to a limitation of its 
potential (RMI, 2015). Although energy storage has been a part of US wholesale markets for many years 
though its role varies from market to market; for instance, Electricity Reliability Council of Texas 
(ERCOT) defines storage as a generation asset. In the PJM Regional Transmission Organization (PJM 
RTO), MISO (Midcontinent Independent System Operator), California Independent System Operator 
(CAISO), and New York Independent System Operator (NYISO) storage is mainly used as a regulation 
service and paid accordingly to the performance (DNV GL Energy, 2014). 
Additional rules limit the participation of DERs in wholesale markets. In NYISO, if an onsite generation 
resource is operated to reduce load and there is excess generation, it is not allowed to sell the excess into 
NYISO wholesale markets, but instead must sell it to the local distribution operator via a retail tariff

---


### Page 11

Birk et al, 2017 
9 
(DNV GL Energy, 2014)9. In contrast, in PJM, market rules for demand response provided with and 
without distributed generation are basically the same. For the capacity market in PJM, the distribution 
operator, not PJM, determine the installed capacity that DERs can provide, since the resource is 
connected at distribution voltage levels (DNV GL Energy, 2014). The Electricity Reliability Council of 
Texas has designated a separate category for distributed energy resources in markets; defined as a 
resource below 10 MW connected at distribution voltages. Distributed energy resources below 10 MW 
are considered a load offsetting resource; therefore, if activated in wholesale markets, the DER is paid the 
“load zone locational marginal price,” as opposed to the nodal price that a generation resource would be 
paid (DNV GL Energy, 2014). In the PJM jurisdiction, the demand response settlement can be calculated 
on the “zone, aggregate or node depending on how the site’s energy is billed” which means the resource 
has the capability on deciding how to be billed, due to the nature of these resources and how they perform 
within the markets (PJM, 2016). DERs face intricate state-jurisdictional processes for interconnection; if 
DERs are activated in wholesale markets, then they are subject to US Federal Energy Regulatory 
Commission (FERC) restrictions as well as state level standards/restrictions (De Martini, 2015). Even if 
DERs are able to meet the criteria to interconnect to the grid, go through the lengthy and complex 
registration process to be able to physically participate in the market, there is typically a fee to enter the 
market, which might restrict smaller resources/generators from providing their service. 
1.4 
Pricing of distributed energy resources 
In the United States, most organized wholesale markets (i.e. ISOs/RTOs) typically compute locational 
marginal prices (LMPs), on hourly or sub-hourly timescales, for economic dispatch that matches supply 
with demand and incorporates the valuing of energy, losses, and network congestion across zones and 
nodes. The market operators commit specific power generation units and calculate marginal prices for the 
transmission networks under reliability constraints. Distribution networks are orders of magnitude larger 
in scale due to the number of customers, length of wires, system components, complexity of networks and 
constraints. Calculating locational marginal pricing in the lower voltage distribution network is 
computationally challenging and not currently adopted in the US; however, co-optimization of services 
may provide system efficiency gains (Caramanis, 2016). 
In the EU, wholesale markets are organized differently than in the US. In the EU, generally speaking, 
there is a Power Exchange (PX), which runs the spot market (day-ahead and intraday markets), and is 
separate and apart from the Transmission System Operator, which manages the reserve and network 
 
9 Depending on the market, retail prices do not always correspond to the wholesale value of energy and a retail tariff might be 
more profitable (i.e. Net Energy Metering).

---


### Page 12

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
10 
constraints market, at the transmission level. To solve network constraints at the transmission level, 
congestion markets are in place in many countries or other market arrangements are possible, such as 
bilateral contracts. Most of the member states in the EU electricity market use supply and demand bids 
that do not consider operational or network constraints, and where reserves and network constraints are 
handled in separate markets run by the TSO. The EU electricity markets are diverse and contain many 
different market structures; however, most are abstractions from a single price market, see Table 2 and 3 
for more detail. Network constraint markets would need to be adapted to allow DERs to participate, 
considering, as in the US context, the effect of energy losses. 
Pricing services provided by DERs, or valuing their benefits and costs, is necessary to enable more 
economically efficient markets and operations. Transmission-level services are currently priced 
differently in the European Union (EU) and US markets and how new distribution-level services will be 
priced in the future may differ as well. Policy makers and regulators should carefully consider the 
potential for and tradeoffs between increased scheduling complexity, market power concerns, and other 
operational challenges when investigating spot or real-time markets at the distribution level (De Martini, 
2015). 
Currently, most transmission level services are provided by conventional and large-scale generation 
sources, priced and cleared in wholesale markets. Tables 2 and 3 detail the current methods and 
categorization of prices and services in the US and EU at the transmission/wholesale level and a first and 
second-best approach for pricing distribution services10. 
Table 2: ISO and TSO services and pricing in the US and EU, respectively 
 
Table 3: DSO services and pricing in the US and EU 
 
10 First-best pricing is a term that represents the marginal cost based approach to pricing and providing electricity and electricity 
services. The prices would reflect all the costs associated with providing electricity, including, but not limited to, generation 
costs, constraints, losses, degradation of infrastructure, and reserves into the formulation for electricity prices. Reliability options 
are described in more detail in section 3.3.

---


### Page 13

Birk et al, 2017 
11 
 
An open question still remains as to an appropriate structure for future pricing of services provided by 
DERs, be it distribution locational marginal prices (DLMPs), bilateral market clearing, cost reflective 
network tariffs or average bundled network tariffs. In a truly granular approach to pricing services, 
wholesale market prices may be extended to lower voltage distribution networks. Wholesale market 
prices (i.e. locational marginal prices) could be computed at the TSO-DSO interface and then DSOs could 
theoretically compute distribution locational marginal prices by using an optimal power flow for both 
active and reactive power; if and only if the market and communication protocols are set so that there is 
enough time to simulate and calculate these prices, dispatch the services, and optimize across the 
transmission and distribution system. With DLMPs, congestion and energy losses can be captured. 
DLMPs may need to be complemented with reserve pricing, network charges and long-term contracts of 
services (e.g. firm capacity, network deferral, black start) if DLMPs would not fully recover the total cost 
of distribution networks; therefore, network charges may need to be efficiently designed to allocate the 
remaining network costs (Pérez-Arriaga & Bharatkumar, 2014; Ntakou & Caramanis, 2015). This topic is 
being actively researched, but is not yet adopted in the field due to the underlying jurisdictional and 
operational complexities involved. 
1.5 
Possible conflicts between electricity services 
Services can conflict and compete with one-another within the same level of the grid (e.g. a resource may 
be able to provide real-time or day-ahead energy, but not capacity). Services can compete across the 
system; a service utilized at the transmission level, may not be able to provide a service because it creates 
issues on the distribution system or vice versa (e.g. local network conditions/constraints might not be 
perfectly reflective of transmission system conditions). Utilization of a distributed energy resource 
providing a service at the transmission level could, in theory, activate a voltage or some other constraint 
on the local distribution system, although this is more likely to occur years from now in markets where 
there is much greater distributed energy resource adoption, or, as previously mentioned, a potential 
subsequent phase with larger penetration and adoption of distributed energy resources. 
A major responsibility of transmission system operators is to balance generation and demand at the bulk 
power system level, at all times; however, the capacity and interconnection requirements for distributed 
generation located on the distribution network is currently the responsibility of the DSO. If DERs

---


### Page 14

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
12 
continue to play a larger role in wholesale markets and provision of services, there will need to be 
increased cooperation and data exchange between the TSO and DSO when it comes to provision of those 
services. “TSOs and DSOs should coordinate in solving congestions at the operation planning stage and 
before real time, and share upfront information about foreseen congestions” (ENTSO-E, 2015). Perhaps 
new market design rules11 and frameworks may facilitate TSO and DSO interaction at the interface of 
transmission and distribution. 
Price signals can be a main driver for coordination, and relying on markets might be the most efficient 
way to allocate resources and services. A market, in theory, and the transactions that are included, could 
be a mechanism to remove potential conflicts between services, if properly co-optimized and coordinated 
across levels of the electricity system12. 
2 NEW ROLES OF DISTRIBUTION SYSTEM OPERATORS 
In the European context, the DSO has two main roles: system operator and market facilitator (i.e. market 
operator). A new agent, “an independent platform,” can operate and clear the DSO service market. In this 
paper, it is assumed that the DSO can carry out this role. This paper does not enter into the discussion of 
independent platforms that might run local markets. 
Gaining momentum in the electric and power system industry are the additional roles that distribution 
system operators might be performing in the future, such as data or information manager, but they are 
discussed briefly in this paper (evolv DSO, 2015; Chatillon, 2015). This paper considers utilities or DSOs 
that are unbundled from retail activities, as it is the case in most European markets. In certain US 
jurisdictions, there are bundled retail and network operations as well as loosely bundled retail activities 
with electricity services. In New York State there are local utility companies that operate the network, and 
depending on customer preferences, may or may not be the default supplier. DSOs are responsible for 
maintaining local constraints within certain specifications and margins, ensuring power quality (i.e. 
managing harmonics and flicker.), managing Voltage/VAR (i.e. Volt/Volt-Ampere Reactive power) 
regulation, outage management and reducing energy losses. To fulfill those tasks, DSOs take different 
actions, such as network planning, network maintenance (preventive and corrective) as well as operation 
through actions, such as line switching or load shedding during emergency situations. 
 
11 DSOs should not be allowed to facilitate the same market that they provide services to (ENTSO-E, 2015). 
12 Transmission, distribution, retail which might include such transactions and markets such as day-ahead, intraday, real-time, 
forward bi-lateral contracts, and tariff offerings.

---


### Page 15

Birk et al, 2017 
13 
2.1 
Distribution system operator roles for initial phase of distributed energy resource penetration 
With low penetration of DERs, DSOs can maintain and operate their grids reliably via voltage regulation, 
power factors and phase balances as well as Fault Location Isolation and Service Restoration (FLISR) 
(De Martini, 2015). FLISR is a process by which DSOs switch power flows over lines, by opening and 
closing circuits, during periods of operation, for maintenance purposes or more generally to maintain grid 
reliability. Some forward-looking distribution system operators are gradually increasing the control and 
monitoring of their distribution grid, at different voltage levels including the distributed resources 
connected to their grid. In an initial phase, it would be good practice for DSOs to adapt protection 
systems to handle multi-dimensional power flows and for the system to be able to function in islanding 
operation in case of outages. In order for DSOs to perform more efficient operations in this initial phase 
of penetration, DSOs would need to be able to receive availability schedules from all connected users 
with enough time to perform reliability and security analyses to identify possible grid constraints. 
2.2 
Distribution system operators roles in subsequent phase of distributed energy resources 
penetration 
In a subsequent phase, with increasing penetration of DERs, there may be a shift in load and generation 
patterns. In order to operate the network reliably and manage constraints if they arise, DSOs would need 
schedules from all connected users over different timeframes and perform optimal power flows. DSOs 
should have at least monitoring and perhaps control over certain grid assets. With increasing penetration 
of DERs, a DSO might even become an active network manager, facilitating transparent retail markets, 
owning or operating advanced metering infrastructure, storing data regarding customer loads and resource 
patterns, as well as newer roles, such as energy efficiency facilitator, as occurred in Denmark, and even 
potentially controlling infrastructure for electric vehicle charging, whether these functions should be 
performed by the DSO is still an open question (EDSO, 2012). 
With increasing penetration of DERs, it has been suggested that DSOs might take on the role of dispatch 
coordinator by not only operating their own network, but also coordinating and optimizing with the TSO 
for scheduling interchanges, perhaps even enabling a more transactive market (Barrager, 2014; De 
Martini, 2015; Grid Wise, 2015). More local markets may be necessary to solve local constraints. The 
topic of local markets is important due to the nature of its dependence or independence from the 
transmission markets and operations. A distribution system platform provider is a role being discussed 
throughout New York State in regards to the utilities running local markets/platforms for electricity 
services (NY Department of Public Service, 2014; Tabors, 2016). Transactive energy is a concept in 
which markets are used to connect buyers and sellers of electricity services more efficiently. The goal of 
transactive energy is to enable markets to provide for the economic efficiency, environmental

---


### Page 16

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
14 
sustainability and reliability for the grid of the future. DSOs in subsequent phases may be the entities 
sending economic signals to the DERs on their networks, and transactive markets may become utilized in 
subsequent phases. 
As DERs become more prevalent, the likelihood of increased bi-directional flows increases; this could 
pave the way for new services, such as storage and additional ancillary services to maintain equilibrium 
of supply and demand (EDSO, 2012). As DERs become ubiquitous on the grid, the increased bidirectional flows and back feed of electricity can cause new complexities and issues for both TSOs and 
DSOs. For instance, a substation that used to be classified within a load zone, but due to bi-directional 
flows becomes a generator node for many hours or for set seasons/time-periods, than the ISO/RTO will 
need to devise a method/mechanism of modeling and dispatching the grid under this possibility. 
The intermittency of renewables, larger swings in load, and the mismatch of renewable generation to 
scheduled forecasts are increasing the difficulty that operators have in matching supply and demand. In 
the past, the challenge was to match supply with demand. Many operators still have the capability to 
match demand with supply. With demand response, operators can tweak and utilize mechanisms to 
change loading patterns. As more DERs become interconnected, it might become more complex or 
challenging to match demand with supply during high penetration of DERs and low loads, and local 
challenges such as voltage constraints may become more prolific. 
2.3 
Long-term planning and procurement of distributed energy resources 
Many distribution services and traditional methods for grid stability are mature enough for an initial stage 
of DER penetration, but as the grid transforms and new resources with complexities of their own are 
added to networks, alternate schemes for maintaining reliable systems may need to be implemented. 
When utilities or distribution operators upgrade their system, they typically overbuild the infrastructure to 
account for years of forecasted load growth; but this is inherently inefficient and costly. In a subsequent 
phase, or higher penetration of DERs, DSOs could establish more dynamic prices/costs associated with 
network constraints. To determine prices, market mechanisms need to be created. Currently in the US and 
EU, market mechanisms such as non-wires alternative solicitations are being considered in which an 
alternative solution such as a distributed resource could provide a more cost-effective solution as 
compared to the traditional upgrade or service need. Non-wires alternatives are mechanisms where there 
is a specific value or avoided cost with deferring infrastructure upgrades, and if an alternative or new 
solution were proposed more cost-effectively, the resource would be compensated for that service. 
Solicitations for DERs and targeted alternative solutions may become ubiquitous on the electric grid. 
At the distribution level in the EU, different designs might be feasible when pricing DSO services that 
depend on different variables: product definition, procurement method (i.e. markets, contracts, and

---


### Page 17

Birk et al, 2017 
15 
incentives), procurement time (i.e. in coordination with existing markets at TSO level and sequential 
markets), remuneration (i.e. marginal price and opportunity costs) and penalties for non-delivery. 
Compared to the US, in the EU it is common to have multiple DSOs that operate the distribution systems 
under a single transmission system; therefore, additional inter and intra-system coordination may be 
necessary. 
When planning for network expansion, operators should understand the status and trends in development 
and penetration of DERs and consider non-wire solutions as alternatives. Reliability options are one way 
in which DSOs in the EU, under incentive regulation, can auction firm capacity annually for “[Distributed 
Generation] DG in network planning” (Trebolle, 2010). A platform may exist in the future, as a basis for 
pricing products at the distribution level, and facilitating auctions for DSOs to incorporate DERs into 
functions for long term planning. Integrated and structured planning processes between TSOs and DSOs 
have also been proposed and are good practices (ENTSO-E, 2015). In certain power systems the Utility 
receives revenues based on realized costs plus some regulated return on investment, which provides a disincentive for the provision of more cost-effective non-wires or non-substation transformer upgrades that 
might erode profits (i.e. the Utility would have little incentive to pursue cost-saving actions). It is 
important to shift the traditional remuneration schemes for DSOs and Utilities to perhaps more 
performance-based metrics and revenue decoupling to better align incentives (Jenkins, 2014; NYS DPS, 
2014). 
3 INTERACTIONS 
BETWEEN 
TRANSMISSION 
AND 
DISTRIBUTION 
SYSTEM OPERATORS DURING THE OPERATIONAL PHASE 
Interactions and coordination among the system operators will need to be improved both for shorter timescale operational actions and longer-term network expansion planning. This section focuses specifically 
on interactions and coordination between system operators during the operational phase. 
Examples of long-term coordination already exist; for instance, the EU has planned a nine-year research 
program to develop smart grid initiatives and operational coordination between TSOs and DSOs termed 
the European Electricity Grid Initiative (EEGI). The EEGI seeks to reduce network operating and capital 
expenditures, increase decentralized renewables and guarantee security of supply and reliability across 
Europe (Mallet, 2014). The EEGI details a roadmap and objectives, roles for each operator and 
coordination between the operators as well as budgets for the plan and activities, such as joint research 
and investigation activities between TSOs and DSOs (Mallet et al., 2014). ENTSO-E has numerous 
position papers from market frameworks to regulatory governance to security of supply on the interaction 
between TSOs and DSOs, and describes the key role in Network Codes in defining the different aspects 
and collaborations between transmission and distribution (ENTSO-E, 2015).

---


### Page 18

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
16 
Scarcity of system services are a concern especially for TSOs as there may be a “shrinking pool” of 
conventional units that provide system services, therefore new arrangements between TSOs and DSOs are 
needed to fully optimize the use of DERs and maintain security of supply (ENTSO-E, 2015). Information 
exchange between the operators would need to be ubiquitous regarding the resources connected at the 
transmission and distribution networks. Schedules and forecasts for demand and generation would need to 
be sent in real time or prior to real time for activation of services and safe operations of the networks 
during emergency situations. The TSO and DSOs may need to exchange new information, as detailed 
below. The format, time and means of the relevant information and communications should be clearly 
specified in network codes and operational guidelines. 
3.1 
Energy flows and forecasting 
Under an initial phase of distributed resource penetration, there typically has been enough buffer built 
into electrical grid infrastructure to manage DERs; there is usually hosting capacity available for the 
distribution circuits to integrate and interconnect DERs up to a certain amount. In this initial phase, 
however, the relevant hosting capacity information has not widely been disseminated to relevant parties 
such as developers and consumers that wish to purchase or have access to DERs. 
As penetration of distributed energy resources increases, there will be a much greater need for more 
accurate forecasting of load and generation patterns. DSOs would have the responsibility to monitor more 
actively the resources and loads connected at distribution voltages and therefore would monitor and may 
even control resources in order to maintain a balanced grid and solve distribution level constraints. 
Similar to the transmission level, proper forecasting techniques, scheduling and outage maintenance 
should be utilized by DSOs to more effectively operate their networks. Distribution system operators in 
the EU are currently missing this information, and in some rare cases, the TSO actually receives the 
information from DG resource profiles, bypassing the DSO (Mallet et al., 2014). As DERs change load 
shapes, the bulk power system operator will need to better-forecast loads and generation. System 
operators in the US are already integrating forecasting of distributed resource generation on their electric 
grids (i.e. NYISO and ISONE). Smart metering is essential for market facilitation and reliable system 
operation with increased penetration of DERs (ENTSO-E, 2015). 
3.2 
Energy pricing, scheduling, and activation of services 
In an initial phase of DER penetration, DERs may act more as passive participants that can provide 
services to the electric grid incidentally or not as the primary purpose (i.e. solar PV could be used to 
reduce load onsite through self-consumption during coincident peak hours, thermal or energy storage 
could be used to load shift, and these DERs may in fact provide electric system-benefits through peak and

---


### Page 19

Birk et al, 2017 
17 
load reduction as well as providing customer benefits such as bill savings or renewable energy 
integration). 
As larger amounts of DERs become interconnected to the electric grid, and DERs provide services more 
dynamically, energy schedules, after positions are taken in different markets, need to be shared between 
the TSO and DSOs to update forecasts and perform power flow analyses closer to real time. Load swings 
across the day might become wilder, causing the need for greater communication and coordination. 
Closer to real-time coordination could be captured with a market design that expands the current dayahead planning which includes DERs and any local constraints. After the day-ahead market, the TSO 
could inform final schedules of DERs that participate in the market to the DSO. In the same way, if the 
DSO changes DERs schedules because of local constraints, DSOs would inform the TSO. Lack of 
schedule information may lead to suboptimal dispatch of the system. In some wholesale markets, such as 
PJM, some DERs are not registered at the wholesale level and their dispatch is not taken into 
consideration when running an optimization for the whole system (PJM, 2015). In a subsequent phase, it 
is important that distributed resources are monitored or visible to grid operators. 
Energy prices at the interface between TSO and DSO may be communicated and defined in a hierarchical 
way. Perhaps, the wholesale market operator could first compute energy prices for the meshed bulk 
network, then those prices would be sent to the DSOs to incorporate the system conditions and prices into 
the computation of distribution locational marginal prices or when clearing local markets in radial 
networks. A market framework should take into account economic optimization of resources, fair 
competition, transparent rules, data security and confidentiality as well as proper cost allocation (ENTSOE). As stated before, if DLMPs are not computed, other solutions could be implemented, such as local 
market mechanisms or value-reflective tariffs. 
With greater penetration of DERs, services will need to be activated and final positions determined. 
Distributed energy resource owners or third party aggregators could take on the responsibility of 
activation based on dispatch directives, price signals, and penalties for non-fulfillment of commitments. 
Transmission system operators should not bypass the DSOs regarding information gathering or activation 
of services in case of emergency issues on the distribution system. 
Currently, some DERs, and loads, connected at distribution networks provide services to the ISO, such as 
in PJM, where Curtailment Service Providers can aggregate different resources to provide economic and 
emergency demand response (PJM, 2014). Although utilities are informed when DERs register with PJM, 
utilities are not always informed when activation take place. In a subsequent phase of DER penetration, 
gaps in communication may cause constraints in distribution networks to occur or to worsen. Protocols 
for effective communication need to be properly standardized and aligned with actual operations, if not, 
for example, potential counteractive actions between the different operators and resource activation that

---


### Page 20

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
18 
has already been exhausted may occur (i.e. a distributed energy storage resource that has depleted its 
energy capacity, but gets called upon for discharging). 
3.3 
Emergency situations 
In the initial phase of DER penetration, the electric grid, both the bulk power system and distribution 
networks, are typically reliable enough to maintain supply and demand as well as manage most real-time 
changes. Electric grids are built with infrastructure that can handle the peak hours of the year when 
electricity is needed the most and can handle fluctuations in load or supply through network or generator 
operations and real-time monitoring and control. Most electric grids in the US and EU have very good 
reliability statistics year after year, with minimal disruptions for the large majority of customers. During 
emergency situations such as contingency events and outages, when a line trips or is knocked down, sadly 
those who are connected to the electric system at or near those points of failure, typically lose power for 
hours, days or even weeks at a time, depending on the length of time that it takes distribution operators to 
dispatch crews to fix and re-energize the network in a safe manner. One of the major benefits of 
distributed energy resources is there ability to provide backup power and electricity during grid outages or 
interruptions. 
As DERs become more ubiquitous on the electric grid, more and more customers would have access to 
backup power and can potentially operate off grid, when the grid has an outage. Perhaps as the 
penetration of DERs increases, there could be neighborhoods and communities, which during a grid 
outage, can effectively operate as a microgrid. It is important that grid operators are aware of the 
distributed assets on their networks, so that they can manage their grids in the most efficient manner and 
that the full benefits of DERs can be realized. 
As penetration of DERs increase, there could also be much larger fluctuations in load and supply 
depending on the time of day. These variations in load and supply can be managed by energy schedules 
that capture the relevant changes and forecasts as long as they are monitored, recorded and sent to the 
operators. The TSO may need support from the DSO to reduce or curtail loads or generation connected to 
the distribution network. In addition, the DSO may have local issues (e.g. line faults) that may be relevant 
to communicate to the TSO. Advanced network codes, under a paradigm of high penetration of DERs, 
need to incorporate new actions and procedures in emergency situations and establish the communication 
protocols between the operators, such as the Network Code of Emergency and Restoration (CEER, 2015; 
ACER, 2015).

---


### Page 21

Birk et al, 2017 
19 
4 CONLUSIONS 
The energy sector is in a period of rapid growth and transformation unlike anything seen in the past 
century. Decentralization and decarbonization are driving greater penetrations of distributed and 
renewable energy systems and the subsequent need for greater system awareness, forecasting, and 
intelligence. Distributed energy resources can provide system services, which may enable even greater 
penetration of these resources. Specific responsibilities of operators, including coordination and 
information exchange between the operators, are of utmost importance. The European and the US 
electricity sectors are taking positive steps towards a decentralized paradigm for enhancing network 
operations as well as new tariff and market designs. 
This paper highlights phases of DER penetration on electric grids in the US and Europe and the 
interactions between the transmission and distribution system operators. At present, the penetration of 
DERs is still relatively small, although in many regions the yearly installed capacities are growing 
rapidly. In initial phases of DER integration, distribution networks are expected to be able to manage the 
presence of small amounts of DERs. The challenge in this initial phase is to be able to have visibility and 
monitor the assets on the distribution network. 
In a subsequent phase, there could be significantly higher penetration levels of DERs in the system that 
provides services to the transmission and distribution system. In this subsequent phase, energy and load 
forecasting, scheduling, activation of resources and procedures to manage emergency situations will need 
to be defined and implemented. Under these conditions, the DSOs will likely need to perform new 
functions, such as determining prices for local constraints and coordinating those prices with those of the 
transmission system operator or wholesale market operator. New market rules and requirements, tariff 
designs, and price signals could mitigate many of the potential conflicts between services. New wholesale 
market rules, requirements, and mechanisms for distributed resources to provide services should be 
codified, as DERs are able to provide system services. Today, there exists a lack of proper market 
structures, rules, and access as well as compensation mechanisms for DERs to actively provide services 
across the power system. Coordination between DSOs and TSOs will become increasingly salient as more 
and more distributed resources interconnect to the grid and provide system services. 
Acknowledgements 
We are greatly appreciative of the contributions from Susan Covino, Andrew Levitt, and Scott Baker 
from PJM Interconnection, Brian Conroy from AVANGRID, partners at Électricité de France (EDF) and 
all the consortium members from the Utility of the Future Project. The authors would like to thank the 
anonymous reviewers of the journal as well as the Energy Economics Iberian Conference (EEIC|CIEE 
2016).

---


### Page 22

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
20 
REFERENCES 
Agency for the Cooperation of Energy Regulators (2015). System operation. June 23rd, 2015. Retrieved December 
29th, 2015 from http://www.acer.europa.eu/electricity/fg_and_network_codes/pages/system-operation.aspx 
Agency for the Cooperation of Energy Regulators (2015). ENTSO-E Network Code on Emergency and Restoration. 
March 25th, 2015. Retrieved December 29th, 2015 from 
http://www.acer.europa.eu/electricity/fg_and_network_codes/responses_nc_emergency_restoration/12.%20
acer%20network%20code%20emergency%20and%20restoration_rev%20enel%20final.pdf 
Barrager, S. and Cazalet, E. (2014). Transactive Energy: A Sustainable Business and Regulatory Model for 
Electricity. 
California Independent System Operator (2013). Fast Facts What the duck curve tells us about managing a green 
grid. October 2013. Retrieved December 27th, 2015 from 
https://www.caiso.com/Documents/Flexible Resources Help Renewables_Fast Facts.pdf 
California PUC proceeding on Distribution Resources Plans (R. 14-08-013) August 20th, 2014. 
http://docs.cpuc.ca.gov/Published Docs/Published/G000/M103/K223/103223470.pdf 
Caramanis, M., Ntakou, E., Hogan, W., Chakrabortty, A., and Schoene, J. (2016) Co-Optimization of Power and 
Reserves in Dynamic T&D Power Markets With Nondispatchable Renewable Generation and Distributed 
Energy Resources. March 17th, 2016. http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7429676 
Caramanis, M. (2015) Extending Locational Marginal Cost Pricing to Retail Electricity Markets and Distributed 
Energy Resources. Harvard JFK Energy Policy Seminar. September 21st, 2015. Retrieved September 21, 
2015 from http://www.hks.harvard.edu/m-rcbg/cepr/Caramanis Harvard Sept21%202015.pdf 
Case 14-M-0101, Proceeding on Motion of the Commission in Regard to Reforming the Energy Vision, Order 
Adopting Regulatory Policy Framework and Implementation Plan (issued February 26, 2015). 
Chatillon, O. (2015). Central DSO Data Hub The French Example. High-level conference Eurelectric: Data, the 
Gate to Smart Energy System. ERDF. http://www.eurelectric.org/media/176928/chatillon.pdf 
Council of European Energy Regulators (2015). The Future Role of DSOs. July 13th, 2015. Retrieved on December 
29th, 2015 from 
http://www.ceer.eu/portal/page/portal/EER_HOME/EER_PUBLICATIONS/CEER_PAPERS/CrossSectoral/Tab1/C15-DSO-16-03_DSO%20Conclusions_13%20July%202015.pdf 
Commission Staff Report AD 14-7. (2014) Payment for Reactive Power. April 22nd, 2014. Retrieved December 8th, 
2015 from https://www.ferc.gov/legal/staff-reports/2014/04-11-14-reactive-power.pdf 
De Martini, P., Kristov, L., Schwartz, L. (2015) Distribution Systems in A High Distributed Energy Resources 
Future. Planning, Market Design, Operation and Oversight. Berkeley Lab. Future Electric Utility 
Regulation. October 2015. Retrieved December 14th, 2015 from 
https://emp.lbl.gov/sites/all/files/FEUR_2%20distribution%20systems%2020151023.pdf

---


### Page 23

Birk et al, 2017 
21 
DNV GL Energy. (2014) A Review of Distributed Energy Resources: New York Independent System Operator. 
September 23rd, 2014. Retrieved December 15th, 2015 from 
http://www.nyiso.com/public/webdocs/media_room/publications_presentations/Other_Reports/Other_Repo
rts/A_Review_of_Distributed_Energy_Resources_September_2014.pdf 
EDSO for smart grids. (2012) The role of the DSO in the Electricity Market - from a Smart Grid perspective. 
November 12th, 2012. Retrieved December 14th, 2015 from http://www.edsoforsmartgrids.eu/wpcontent/uploads/public/EDSO-role-of-the-DSO-from-a-smart-grid-perspective.pdf 
ENTSO-E (2015). ENTSO-E Work Programme. https://www.entsoe.eu/Documents/Publications/ENTSOE%20general%20publications/151218_AWP2016_Final_post_ACER_opinion.pdf 
ENTSOE (2015). General Guidelines for Reinforcing the Cooperation Between TSOs and DSOs. September 11th, 
2015. https://www.entsoe.eu/publications/position-papers/position-papersarchive/Pages/Position%20Papers/general-guidelines-for-reinforcing-the-cooperation-between-tsosdsos.aspx 
 ENTSO-E (2015). Markets and Innovation Deliver the Energy Union. 
https://www.entsoe.eu/Documents/Publications/vision/entsoe_vision02_market_web.pdf 
 ENTSO-E (2015). Regulatory Governance for the Energy Union: Implement and Update. 
https://www.entsoe.eu/Documents/Publications/vision/entsoe_vision05_regulation_web.pdf 
ENTSO-E (2015). Towards smarter grids: Developing TSO and DSO roles and interactions for the benefit of 
consumers. ENTSO-E Position Paper. https://www.entsoe.eu/publications/position-papers/position-papersarchive/Pages/Position%20Papers/Position-Paper-on-TSO-DSO-interactions.aspx 
 ENTSO-E (2015). Where Markets Meet Security of Supply. 
https://www.entsoe.eu/Documents/Publications/vision/entsoe_vision03_security_web.pdf 
 ENTSO-E (2015). Where the Energy Union starts: Regions. 
https://www.entsoe.eu/Documents/Publications/vision/entsoe_vision04_regions_web.pdf 
ENTSO-E WGAS. (2015). Survey on Ancillary services procurement, Balancing market design 2014. January 27th, 
2015. Retrieved December 23rd, 2015 from 
https://www.entsoe.eu/Documents/Publications/Market%20Committee%20publications/150127_WGAS_S
urvey_2014.pdf 
European Commission. (2015). Launching the public consultation process on a new energy market design. July 15th, 
2015. Retrieved December 26th, 2015 from 
http://ec.europa.eu/energy/sites/ener/files/documents/1_EN_ACT_part1_v11.pdf 
FERC (2003), Notice of White Paper, U.S. Federal Energy Regulatory Commission, Issued April 28. 
Fitzgerald, G., Mandel, J., and Morris, J. (2015) The Economics of Battery Energy Storage. How Multi-use 
Customer-Sited Batteries Deliver the Most Services and Value to Customers and the Grid. Rocky Mountain

---


### Page 24

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
22 
Institute. October 2015. Retrieved November 10th, 2015 from http://www.rmi.org/Content/Files/RMIThe Economics Of Battery Energy Storage-Full Report-FINAL.pdf 
The Grid Wise Architecture Council. (2015). Grid Wise Transactive Energy Framework Version 1.0. PNNL-22946. 
Hallberg, P et al. (2013). Active Distribution System Management a key tool for the smooth integration of 
distributed generation http://www.eurelectric.org/media/74356/asm_full_report_discussion_paper_final2013-030-0117-01-e.pdf 
Hedman, K., Ferris, M., O'Neill, R., Bartholomew, E., and Oren, S. (2010). Co-Optimization of Generation Unit 
Commitment and Transmission Switching with N-1 Reliability. Power Systems, IEEE Transactions, 25(2) 
1052-1063. DOI 10.1109/TPWRS.2009.2037232 
Iberdrola USA (2016). Personal communication with Iberdrola USA Operations Division, March 4th, 2016. 
IDE4L Deliverable 2.1 (2014). Specification of Active Distribution Network Concept. April 25th, 2014. 
http://www.tut.fi/cs/groups/public/@l813/@web/@p/documents/liit/mdbw/mdy4/~edisp/p068770.pdf 
IRC ISO/RTO Council. (2014) 2013 North American Demand Response Characteristics Comparison. February 28th, 
2014. Retrieved December 15th, 2015 from http://www.isorto.org/Reports/default 
Jenkins, J.D. & Pérez-Arriaga, I. (2014), “The Remuneration Challenge: New Solutions for the Regulation of 
Electricity Distribution Utilities Under High Penetrations of Distributed Energy Resources and Smart Grid 
Technologies,” MIT CEEPR Working Paper No. 2014-005. 
Kempton, W., Udo, V., Huber, K., Komara, K., Letendre, S., Baker, S., ... & Pearre, N. (2008). A test of vehicle-togrid (V2G) for energy storage and frequency regulation in the PJM system. Univ of Deleware, Tech. Rep. 
<www.udel.edu/V2G/resources/test-v2g-in-pjm-jan09.pdf> 
Kristov, L., and De Martini, P (2014) 21st Century Electric Distribution System Operations. 
http://smart.caltech.edu/papers/21st CElectric System Operations050714.pdf 
Kristov, L (2015) The Future History of Tomorrow’s Energy Network. May 2015. 
http://www.fortnightly.com/fortnightly/2015/05/future-history-tomorrows-energynetwork?page=0,0&authkey=afacbc896edc40f5dd20b28daf63936dd95e38713e904992a60a99e937e19028 
Mac Donald, J., Cappers, P., Callaway, D., and Kiliccote, S. (2012). Demand Response Providing Ancillary 
Services. Presented at Grid-Interop. November 2012. Retrieved December 23, 2015 from 
http://eande.lbl.gov/sites/all/files/lbnl-5958e_0.pdf 
Mallet, P., Granström, P., Hallberg, P., Lorenz, G., and Mandatova, P. (2014) Power to the People. European 
Perspective on the Future of Electric Distribution. IEEE Power and Energy Magazine. 51-64. DOI 
10.1109/MPE.2013.2294512. 
Ntakou, E. (2014) Price Discovery in Dynamic Power Markets with Low-Voltage Distribution Network 
Participants. IEEE T&D. April 16th, 2014. Retrieved December 15th, 2015 from http://www.ieeepes.org/presentations/td2014/td2014p-000485.pdf

---


### Page 25

Birk et al, 2017 
23 
Ntakou, E. and Caramanis, M. (2015). Distribution network spatiotemporal marginal cost of reactive power. Power 
& Energy Society General Meeting, 2015 IEEE, 1-5. DOI 10.1109/PESGM.2015.7286547 
Newcomb, J., and Paulos, B (2013). Distributed Energy: The Power Sector’s Wild Card. Greentech Media. 
http://www.greentechmedia.com/articles/read/distributed-energy-the-power-sectors-wild-card 
Newcomb, J., Lacy, V., Hansen, L., and Bell M. (2013). Distributed Energy Resources: Policy Implications of 
Decentralization. Rocky Mountain Institute. September, 2013. http://americaspowerplan.com/wpcontent/uploads/2013/09/APP-DER-PAPER.pdf 
Order No. 773-A, 143 FERC ¶ 61,053 https://www.ferc.gov/whats-new/comm-meet/2014/032014/E-7.pdf 
Pérez-Arriaga, I. J., and Bharatkumar, A. (2014). A Framework for Redesigning Distribution Network Use of 
System Charges Under High Penetration of Distributed Energy Resources: New Principles for New 
Problems. CEEPR WP 2014-006. October 2014. Retrieved December 14th, 2015 from 
http://ceepr.mit.edu/?wpdmdl=625%22%20%3E%3Ci%20class= 
Pérez-Arriaga, I. J., Burger, S., & Gómez, T. (2016). Electricity Services in a More Distributed Energy System. 
CEEPR WP 2016-005. March 2016. Retrieved April 27th, 2016 
PJM Interconnection. (2015). Demand Response Fact Sheet. June 29th, 2015. https://www.pjm.com/~/media/aboutpjm/newsroom/fact-sheets/demand-response-fact-sheet.ashx 
PJM Interconnection. (2015). PJM Manual 27: Open Access Transmission Tariff Accounting. July 15th, 2015. 
Retrieved December 24th, 2015 from http://www.pjm.com/~/media/documents/manuals/m27.ashx 
PJM Interconnection. (2015). RTEP Process Scope and Input Assumptions White Paper. 
http://pjm.com/~/media/documents/reports/2015-rtep-process-scope-and-input-assumptions.ashx 
PJM Interconnection. (2014). Retail Electricity Consumer Opportunities for Demand Response in PJM’s Wholesale 
Markets. Retrieved December 24th, 2015 from http://www.pjm.com/~/media/markets-ops/dsr/end-usecustomer-fact-sheet.ashx 
PJM Interconnection (2016). Personal communication with PJM Interconnection Emerging Markets Team. February 
19th, 2016. 
PSEG LI (2014). Utility 2.0 Long Range Plan Prepared for Long Island Power Authority PSEG Long Island. July 1, 
2014. https://www.psegliny.com/files.cfm/2014-07-01_PSEG_LI_Utility_2_0_Long Range Plan.pdf 
New York State Public Service Commission. (2014). New York Reforming the Energy Vision (REV) Market 
Design and Platform Technology Groups. Case No. 14-M-0101. August 17th, 2014. Retrieved December 
24th, 2015 from https://newyorkrevworkinggroups.com/ 
Rivero, E., Six. D., and Gerard, H. (2015). Deliverable 1.4 - Assessment of future market architectures and 
regulatory frameworks for network integration of DRES – the future roles of DSOs. Evolv DSO. October 
29th, 2015. Retrieved December 9th, 2015 from http://www.evolvdso.eu/getattachment/6f0142bf-0e66470c-a724-4a8cbe9c8d5c/Deliverable-1-4.aspx

---


### Page 26

TSO/DSO Coordination in a Context of Distributed Energy Resource Penetration 
24 
Rocky Mountain Institute. (2015). “The Economics of Load Defection.” 
Sun, J., and Tesfatsion, L (2010). DC Optimal Power Flow Formulation and Solution Using Quad Prog J. ISU 
Economics Working Paper No. 06014 March 1st, 2010. http://www2.econ.iastate.edu/tesfatsi/DCOPF.JSLT.pdf 
Tabors, R., Parker, G., Centollela, P., and Caramanis, M. (April 2016). White Paper on Developing Competitive 
Electricity Markets and Pricing Structures. Boston, MA. Tabors Caramanis Rudkevich, Inc. Prepared under 
contract for the New York State Energy Research and Development Authority. 
Topaz Power Management. (2009, September 18th) 10-Minute Non-Spinning Reserve Service. Retrieved December 
7th, 2015 from http://www.ercot.com/content/meetings/qstf/keydocs/2009/20091023-QSTF/2009-0918_10MNSRS_Proposal.pdf 
Trebolle, D., Gómez, T., Cossent, R., and Frías, P. (2010). Distribution planning with reliability options for 
distributed generation. Electric Power Systems Research, 80(2), 222–229. DOI 10.1016/j.epsr.2009.09.004 
U.S. Federal Energy Regulatory Commission (1996). Promoting Wholesale Competition Through Open Access 
Non-discriminatory Transmission Services by Public Utilities; Recover of Stranded Costs by Public 
Utilities and Transmitting Utilities. Order No. 888. May 18th, 1996. Retrieved December 8th, 2015 from 
http://www.ferc.gov/legal/maj-ord-reg/land-docs/order888.asp 
Volkmar, M. (2012). High Penetration PV: Experiences in Germany and technical solutions. SMA Solar 
Technology AG. iea-pvps.org/index.php?id=153&e ID=dam_frontend_push&doc ID=1492 
Wirth, 
H. 
(2015). 
Recent 
Facts 
about 
Photovoltaics 
in 
Germany. 
Fraunhofer 
ISE. 
https://www.ise.fraunhofer.de/en/publications/veroeffentlichungen-pdf-dateien-en/studien-undkonzeptpapiere/recent-facts-about-photovoltaics-in-germany.pdf 
Wong, Lana. (2011). A Review of Transmission Losses in Planning Studies. California Energy Commission. CEC200-2011-009.

---


### Page 28

MIT CEEPR Working Paper Series is published by 
the MIT Center for Energy and Environmental 
Policy Research from submissions by affiliated 
researchers.
Copyright © 2017
Massachusetts Institute of Technology
MIT Center for Energy and 
Environmental Policy Research 
77 Massachusetts Avenue, E19-411
Cambridge, MA 02139 
USA
Website: ceepr.mit.edu
For inquiries and/or for permission to reproduce 
material in this working paper, please contact:
Email	
ceepr@mit.edu
Phone	 (617) 253-3551
Fax	
(617) 253-9845
Since 1977, the Center for Energy and Environmental Policy Research (CEEPR) has been a focal point for research on 
energy and environmental policy at MIT. CEEPR promotes rigorous, objective research for improved decision making 
in government and the private sector, and secures the relevance of its work through close cooperation with industry 
partners from around the globe. Drawing on the unparalleled resources available at MIT, affiliated faculty and research 
staff as well as international research associates contribute to the empirical study of a wide range of policy issues 
related to energy supply, energy demand, and the environment.
 
An important dissemination channel for these research efforts is the MIT CEEPR Working Paper series. CEEPR 
releases Working Papers written by researchers from MIT and other academic institutions in order to enable timely 
consideration and reaction to energy and environmental policy research, but does not conduct a selection process or 
peer review prior to posting. CEEPR’s posting of a Working Paper, therefore, does not constitute an endorsement of 
the accuracy or merit of the Working Paper. If you have questions about a particular Working Paper, please contact 
the authors or their home institutions.

---
