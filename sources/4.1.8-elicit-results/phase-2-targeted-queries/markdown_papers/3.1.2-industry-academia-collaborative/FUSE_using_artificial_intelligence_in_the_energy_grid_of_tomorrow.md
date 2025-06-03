# FUSE – using artificial intelligence in the energy grid of tomorrow

## Paper Metadata

- **Filename:** FUSE – using artificial intelligence in the energy grid of tomorrow.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:03.658073
- **Total Pages:** 3

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

ISSN 2515-0855
doi: 10.1049/oap-cired.2021.0091
www.ietdl.org
FUSE – using artificial intelligence
in the energy grid of tomorrow
Thomas Vögele1 ✉, Christian Backe1, Miguel Bande1, Peter Conradi2,
Petri Hovila3, Kimmo Kauhaniemi4, Haresh Kumar4, Timo Kyntäjä5,
Matti Rita-Kasari6, Muhammad Shafiq4, Stefan Werner7,
Christian Wiezorek8
1Robotics Innovation Center, German Research Center for Artificial Intelligence DFKI, Bremen,
Germany
2All4IP, Darmstadt, Germany
3ABB, Vaasa, Finland
4School of Technology and Innovations, University of Vaasa, Vaasa, Finland
5VTT, Espoo, Finland
6Jubic Oy, Vaasa, Finland
7Easy Smart Grid, Karlsruhe, Germany
8Technical University of Berlin, Berlin, Germany
✉E-mail: thomas.voegele@dfki.de
Abstract: The objective of Future Smart Energy (FUSE), a Finnish-German research and development project, is to develop
methods based on artificial intelligence (AI) that will help to increase the resilience of future energy distribution grids. The
use cases that are investigated include both condition monitoring/predictive maintenance, and distributed demand-side
management in medium-voltage and low-voltage grids. The FUSE concept foresees a hierarchical infrastructure of
sensing- and data processing nodes that use AI to transform raw data into information on asset and grid status and
performance. FUSE supports the upward flow of data and aggregation of information into high-level visualisations for
grid operators, as well as the downward flow of soft control signals that trigger the distributed self-control of assets.
This study outlines the FUSE concept and presents the first results.
1
Introduction
A well-functioning distribution grid able to deliver energy reliably
and with high quality is the backbone of modern society. For
distribution system operators (DSOs), keeping the grid operational
and efﬁcient requires considerable efforts for monitoring and
maintenance. These efforts will have to increase in the future
because the growing contribution of renewable energy sources will
lead to new, cellular local grid topologies (with the possibility of
bi-directional
energy
ﬂows),
more
long-distance
energy
transmission from producers to consumers, and more ﬂuctuations
in energy production.
† Condition monitoring (CM) and predictive maintenance (PM),
i.e. the optimisation of maintenance and repair of assets based on
predictions of their behaviour and the occurrence of faults, can
offer a tool to retain today’s high quality of service in the
distribution grid without exploding the maintenance costs.
† Distributed
demand-side
management
(d-DSM),
i.e.
the
(automated) adaptation of the energy demands of distributed loads
to variations in energy production help to improve the stability of
energy grids that include a high percentage of renewable energy
sources.
The bi-national Finnish-German research project FUSE (Future
Smart Energy) investigates the applicability of artiﬁcial intelligence
(AI) for both concepts. The goal is to develop methods that
improve the resilience of power grids, both on a medium-voltage
(MV) and on a low-voltage (LV) level. In FUSE, both grid
domains are connected through a hierarchical Information and
Communication
Technology
infrastructure,
with
use
cases,
demonstrated both in Finland and in Germany.
In CM and PM, FUSE follows the concept to improve existing
methods for asset-monitoring and fault detection with machine
learning (ML). The objective is to identify potential problems
earlier and with more conﬁdence, and to enable grid operators to
implement a ﬂexible maintenance schedule based on actual risks
and needs, thereby reducing costs.
In d-DSM, the project evaluates an innovative approach for
the dynamic, automated and decentralised control of energy
consumers based exclusively on (real-time and predicted) energy
availability [1].
2
Methodology
2.1
FUSE architecture
FUSE implements a hierarchical infrastructure of nodes equipped
with
AI-based
data
processing
and
reasoning
capabilities.
The leaves of this tree (Level 1) are smart sensors that use
lightweight algorithms for data-driven ML and data processing
on embedded hardware. Level 1 nodes pre-process massive raw
data (e.g. high-frequency measurements of grid parameters) and
convert them into labelled information (e.g. on critical events,
irregular system behaviour), which is propagated upward in the
hierarchy.
Higher up in the hierarchy (e.g. Level 2), the information is
aggregated
and
further
processed,
using
a
combination
of
data-driven and knowledge-driven AI methods. More complex
information is generated, and suggestions are formulated by
user-friendly
visualisations
to
empower
grid
operators
to
understand the current and future state of the grid and to initiate
appropriate management and maintenance measures.
CIRED 2020 Berlin Workshop (CIRED 2020)
22-23 September 2020
Theme 2: Opportunities and Challenges with Operation using Flexibility
CIRED, Open Access Proc. J., 2020, Vol. 2020, Iss. 1, pp. 466–468
466
This is an open access article published by the IET under the Creative Commons
Attribution License (http://creativecommons.org/licenses/by/3.0/)

---


### Page 2

The FUSE infrastructure supports CM and PM in both MV and
LV grids. In the LV grid, the algorithms are also used for d-DSM
to cope with energy congestion or shortage as a result of
malfunctions and shut-downs in the MV grid.
While the FUSE demonstrator implements only a three-tier
hierarchy (Fig. 1), the infrastructure is in principle fully scalable
and can be extended with as many levels as required.
2.1.1 Level 1:
On Level 1, raw data on system performance
are collected, processed and analysed by smart sensors. The
embedded sensor hardware consists of a processor for high-level
data analysis, plus a programmable FPGA for low-level data
pre-processing
and
parallel
computations,
such
as the
ones
required in artiﬁcial neural networks. Both HW components are
interconnected
in
a
compact
system-on-chip
module,
which
enables the fast exchange of data.
In the MV grid, these smart sensors are used to identify and
localise anomalies in power lines, transformers and feeder bays.
Here, deviations from the standard condition are caused, e.g. by
partial discharges (PDs). Temporal PD patterns are analysed to
predict faults in the MV grid (e.g. in power lines) [2].
In the LV grid, physical interferences, such as harmonics,
transients, voltage deviations and sags can cause poor power
quality, affecting the network and its efﬁciencies, and even
causing asset damages. The smart sensors on Level 1 can measure
and even forecast these anomalies, as long as they are caused by
speciﬁc loads in the grid. From both measurements and forecasts,
features can be extracted to identify which device type and device
condition is causing a speciﬁc change in power quality.
Other common grid-state values (e.g. main frequency or power
consumption) are measured and forecast to support optimised
demand-side management. The information is used to generate
soft-control
signals
that
are
distributed
through
the
grid
infrastructure to the appliance controllers on Level 1. Here, they
trigger a response, i.e. regulate the energy consumption of each
individual appliance and thus make optimal use of its current
ﬂexibility reserve. Such is decentralised optimisation is expected to
help stabilise the grid and reduce costs for the consumer – this
will be further investigated in FUSE with future results.
The ﬂexibility reserve of an appliance can be predeﬁned or
dynamically deﬁned according to individual usage patterns. In
FUSE, such patterns are learned on the Level 1 nodes from user
behaviour, based on data recorded in the smart sensors and using
ML algorithms on the Level 1 embedded hardware.
2.1.2 Level 2:
Each Level 2 node represents a speciﬁc grid section
or sub-system of which data are collected and pre-processed in
multiple Level 1 nodes.
† In the MV use case, the objective on Level 2 is to achieve an
overview of the state of the respective MV grid section and to
identify and localise existing or pending system malfunction
events. If possible, this includes the prediction of when and where
this malfunction may happen.
† In the LV use case, we look at multiple Level 1 nodes that
perceive the same power quality event generated by a device, but
with different magnitudes. The algorithms on Level 2 use the
Level 1 data to localise and create a map of all events.
On Level 2, both present and future events are mapped by using
direct
measurements
and
forecasts,
respectively.
With
this
information as training data, the state of the grid section or
sub-system is learned and used for both energy management
and PM.
On Level 2, we investigate the combination of ML and rule-based
reasoning. By using rule-based reasoning, implicit expert knowledge
can be leveraged without the need to deduct this knowledge from
training data. This is particularly useful for the identiﬁcation and
prediction of large-scale and serious fault events, which do not
happen very often and thus are not well documented.
The hardware of Level 2 supports data fusion and real-time big
data, ML and simulation algorithms. This allows us to make
predictions about the functioning of individual assets and of the
respective grid segment in real time.
2.1.3 Level 3:
On Level 3, data and information from multiple
Level
2
nodes
are
brought
together
and
visualised
in
a
user-friendly manner, using the Thingsboard framework [3]. Grid
operators are enabled to view and evaluate the information created
by the Level 2 nodes, to make decisions regarding maintenance
measures, and to transmit respective soft control commands (e.g.
to trigger the d-DSM controllers to reduce the power demand in
the LV sub-grid) if needed.
2.1.4 5G communications:
For the communication and data
exchange between the nodes on Level 1 and Level 2, FUSE
investigates the use of 5G technology.
Level 1 communication requires 5G user equipment (UE)
capability. This can be implemented with 5G modems attached to
the Level 1 embedded devices. Level 2 nodes correspond to both
the 5G access network and the 5G core network, which are
services provided by a telecommunications operator. In addition,
other 5G services like mobile edge/fog computing may be used.
The 5G security mechanisms are an important part of the FUSE
system functionality. These mechanisms include, e.g., device
identity management, communication encryption and security
monitoring with anomaly detection. In order to provide more
advanced 5G communication services also micro-segmentation and
slicing techniques can be used.
2.1.5 Tests and validations:
The FUSE ICT infrastructure is
tested and validated both in Vaasa, Finland, and with a pilot
implementation in the SENSE Smart Grid Laboratory of TUB in
Berlin, Germany [4]. Testing includes the integration of embedded
hardware as well as the conﬁguration of data interfaces and digital
twins for selected assets.
3
Results
FUSE is an ongoing project. First results were achieved regarding
the selection of data and algorithms that can be used for CM/PM
and d-DSM in the MV and LV use cases.
3.1
CM/PM in the MV grid
In the MV grid, we looked at event data (e.g. control events,
warnings, alarms) from protective relays, which operators had
registered for concurrent fault monitoring [5]. To prevent damages
to MV power equipment, faults need to be anticipated with
enough lead time, and their root causes need to be identiﬁed and
localised. To harness the full potential of the event data for fault
prediction and root cause analysis, extensive persistence and a
central collection of high-volume data are required. Also, the
Fig. 1
FUSE hierarchical infrastructure
CIRED, Open Access Proc. J., 2020, Vol. 2020, Iss. 1, pp. 466–468
467
This is an open access article published by the IET under the Creative Commons
Attribution License (http://creativecommons.org/licenses/by/3.0/)

---


### Page 3

sensitivity of thresholds for alarms and warnings needs to be
calibrated (further increasing the number of data points) to allow
the tracking of gradual fault evolution over long time periods.
We explored the potential of event data from protective relays for
fault prediction by analysing a dataset of 80,000 data points recorded
between May 2017 and September 2019 at a substation with 13 bays
in the Finnish Noormarkku area. During this time period, 250 fault
events (short circuits and earth faults), which can be categorised in
14 event types in 8 groups were registered.
The results are visualised in Fig. 2. For each fault event, we plotted
all signals that occur in the fault’s neighbourhood, both topologically
(signals at neighbouring bays), and temporally (signals before and
after the event). Signals are colour-coded by an event-type group
to facilitate manual pattern recognition. The time resolution ranges
over seven orders of magnitude, between 0.3 s and 3.5 days before
and after the fault. This reﬂects the fact that characteristic event
patterns, indicating the evolution of speciﬁc fault types, may occur
on multiple time scales.
This visualisation allows domain experts to explore the data in
various dimensions simultaneously to discover patterns of fault
pre-indications. Such patterns may subsequently be formalised into
rules for automated fault forecasting.
While the current data density proved to be too low to support the
extraction of such rules purely based on data mining and ML, this
may be possible – and will be explored in FUSE – with more
dense data in the future.
3.2
LV network pilot implementation
The FUSE pilot for the LV grid was implemented in the SENSE
Smart Grid Laboratory of TU Berlin. It comprises Level 1
embedded hardware and data interfaces to selected assets (LV
energy consumers), as well as their parametrised digital twins in
the lab, and interfaces to the FUSE ICT infrastructure. The pilot
covers both the CM/PM and the d-DSM use case.
3.2.1
CM/PM
application:
For
the
CM/PM
application,
high-frequency data are recorded and used to train suitable ML
algorithms. Using the Ether CAT protocol [6] according to IEC
61158, the data are recorded in hard real time to ensure a very
high quality of the input data for the ML.
As of today, the ﬁrst set of CM/PM training data has been
recorded as the basis to develop the ML conceptual design. The
data set includes current and voltage measurements with a
resolution of 20 k Hz and will be used for detecting power quality
events, occurring in the LV network.
3.2.2 d-DSM application:
For the d-DSM application, the Level
1 embedded hardware was integrated into the SENSE Lab control
system architecture. This allows evaluating the behaviour of
multiple assets controlled by the d-DSM controllers as a function
of an external soft control signal. In the demonstrator, the signal is
caused by a partial shutdown of the MV grid feeding the LV grid
(Fig. 3).
The d-DSM pilot was
implemented using three different
application schemes for the investigated LV network cell:
(i) grid-connected cell with a high degree of self-sufﬁciency
(non-congested Po CC),
(ii) grid-connected cell with frequency stabilisation and congestion
management (congested Po CC),
(iii) islanded cell (grid-de-coupled Po CC).
The Level 1 controllers were fully integrated into the laboratory’s
SCADA system and are now subjected to stress testing for
stability and reliability. Currently, they are controlling digital twins
of energy assets before successful testing results will allow for
control of physical devices in the lab. The ﬁrst results look
promising, but more detailed analysis is still needed [7].
4
Conclusion
FUSE, a bi-lateral Finnish-German R&D project, investigates the
use of AI for CM/PM and d-DSM in both the MV and LV grids.
The objective is to implement a hierarchical data processing
infrastructure,
enabling
the
distributed
processing
of
data,
generation of information and self-control of assets.
So far, the ﬁrst data sets have been gathered in an MV
demonstrator in Finland and the LV SENSE Lab in Germany, and
tests with ML algorithms and visualisation tools were performed.
The preliminary results are promising and support the FUSE
concept. However, a further collection of data and optimisation of
AI-based
data
processing,
combining
ML
with
rule-based
methods, will be needed to achieve the objectives of FUSE.
5
Acknowledgments
FUSE is a bi-national project with teams from Germany and Finland.
FUSE is funded by the German Federal Ministry of Economic
Affairs and Energy, and by Business Finland.
6
References
1
Werner, S., Wiezorek, C., Backe, C., et al.: ‘Smart decentralized energy
management’. CIRED Workshop 2020, Berlin, Germany, September 2020
2
Mithun, M., Kumbhar, G.B.: ‘Detection, measurement, and classiﬁcation of partial
discharge in a power transformer: methods, trends, and future research’, IETE Tech.
Rev., 2018, 35, (5), pp. 483–493
3
‘Thingsboard’, Available at https://thingsboard.io/docs/, accessed 10 March 2020
4
‘SENSE Smart Grid Laboratory’, Available at https://www.sense.tu-berlin.de/
menue/labor/parameter/en/, accessed 06 March 2020
5
Lundqvist, B.: ‘100 years of relay protection, the Swedish ABB relay history’ (ABB,
Sweden, 2004), Available at https://library.e.abb.com/public/, accessed 29 January
2020
6
‘Ether CAT – the ethernet ﬁeldbus’, Available at https://c2mon.web.cern.ch/c2mon/,
accessed 06 March 2020
7
Wiezorek, C., Werner, S., Backe, C., et al.: ‘Design and operation of sector-coupled
energy systems using the ﬂexibility of smart DSM’. CIRED Workshop 2020, Berlin,
Germany, September 2020
Fig. 2
Fault visualisation for pre-indication pattern discovery by domain
experts
Fig. 3
Integration scheme of the Level 1 controller into the control
framework of the SENSE Smart Grid Laboratory
CIRED, Open Access Proc. J., 2020, Vol. 2020, Iss. 1, pp. 466–468
468
This is an open access article published by the IET under the Creative Commons
Attribution License (http://creativecommons.org/licenses/by/3.0/)

---
