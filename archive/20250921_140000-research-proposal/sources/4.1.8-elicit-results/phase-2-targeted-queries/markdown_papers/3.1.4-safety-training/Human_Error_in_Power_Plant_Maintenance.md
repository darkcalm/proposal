# Human Error in Power Plant Maintenance

## Paper Metadata

- **Filename:** Human Error in Power Plant Maintenance.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:12.855605
- **Total Pages:** 193

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Springer Series in Reliability Engineering
Human Reliability, 
Error, and Human 
Factors in Power 
Generation
B. S. Dhillon

---


### Page 2

Springer Series in Reliability Engineering
Series editor
Hoang Pham, Piscataway, USA
For further volumes:
http://www.springer.com/series/6917

---


### Page 3

B. S. Dhillon
Human Reliability, Error,
and Human Factors
in Power Generation
123

---


### Page 4

B. S. Dhillon
Department of Mechanical Engineering
University of Ottawa
Ottawa
Canada
ISSN 1614-7839
ISSN 2196-999X
(electronic)
ISBN 978-3-319-04018-9
ISBN 978-3-319-04019-6
(e Book)
DOI 10.1007/978-3-319-04019-6
Springer Cham Heidelberg New York Dordrecht London
Library of Congress Control Number: 2013956804
 Springer International Publishing Switzerland 2014
This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of
the material is concerned, speciﬁcally the rights of translation, reprinting, reuse of illustrations,
recitation, broadcasting, reproduction on microﬁlms or in any other physical way, and transmission or
information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar
methodology now known or hereafter developed. Exempted from this legal reservation are brief
excerpts in connection with reviews or scholarly analysis or material supplied speciﬁcally for the
purpose of being entered and executed on a computer system, for exclusive use by the purchaser of the
work. Duplication of this publication or parts thereof is permitted only under the provisions of
the Copyright Law of the Publisher’s location, in its current version, and permission for use must
always be obtained from Springer. Permissions for use may be obtained through Rights Link at the
Copyright Clearance Center. Violations are liable to prosecution under the respective Copyright Law.
The use of general descriptive names, registered names, trademarks, service marks, etc. in this
publication does not imply, even in the absence of a speciﬁc statement, that such names are exempt
from the relevant protective laws and regulations and therefore free for general use.
While the advice and information in this book are believed to be true and accurate at the date of
publication, neither the authors nor the editors nor the publisher can accept any legal responsibility for
any errors or omissions that may be made. The publisher makes no warranty, express or implied, with
respect to the material contained herein.
Printed on acid-free paper
Springer is part of Springer Science+Business Media (www.springer.com)

---


### Page 5

This book is affectionately dedicated to
my granddaughter, Sianna

---


### Page 6

Preface
Each year billions of dollars are spent in the area of power generation to design,
construct/manufacture, operate, and maintain various types of power systems
around the globe. Many times such systems fail due to human error. For example,
during the period 1990–1994 about 27 % of commercial nuclear power plants
outages in the United States resulted from human error.
Needless to say, human reliability, error, and human factors in the area of power
generation have been receiving increasing attention over the years. Although over
the years a large number of journal and conference proceedings articles related to
human reliability, error, and human factors in power generation have appeared, but
to the best of the author’s knowledge, there is no speciﬁc book on the topic. This
causes a great deal of difﬁculty to information seekers because they have to consult
many different and diverse sources.
Thus, the main objective of this book is to combine these topics into a single
volume and eliminate the need to consult many diverse sources to obtain desired
information. The sources of most of the material presented are listed in the reference section at the end of each chapter. These will be useful to readers if they
desire to delve more deeply into a speciﬁc area or topic of interest.
The book contains a chapter on mathematical concepts and another chapter on
introductory human factors, human reliability, and human error concepts considered useful to understand contents of subsequent chapters.
The topics covered in the book are treated in such a manner that the reader will
require no previous knowledge to understand the contents. At appropriate places,
the book contains examples along with their solutions, and at the end of each
chapter there are numerous problems to test the reader’s comprehension. An
extensive list of publications dating from 1971 to 2012, directly or indirectly on
human reliability, error, and human factors in power generation, is provided at the
end of this book to give readers a view of intensity of developments in the area.
The book is composed of 11 chapters. Chapter 1 presents various introductory
aspects, directly or indirectly related to human reliability, error, and human factors
in power generation including facts, ﬁgures, and examples; terms and deﬁnitions;
and sources for obtaining useful information on human reliability, error, and
human factors in power generation.
Chapter 2 reviews mathematical concepts considered useful to understanding
subsequent chapters. Some of the topics covered in the chapter are sets, Boolean
vii

---


### Page 7

algebra laws, probability properties, useful deﬁnitions, and probability distributions. Chapter 3 presents various introductory human factors, reliability, and error
concepts. Chapter 4 presents six general methods considered useful to perform
human reliability and error analysis in power generation. These methods are errorcause removal program, man–machine systems analysis, failure modes and effect
analysis, probability tree method, Markov method, and fault tree analysis.
Chapter 5 is devoted to speciﬁc human reliability analysis methods for nuclear
power plants. The methods presented in the chapter are a technique for human
event analysis (ATHEANA), cognitive reliability and error analysis method
(CREAM), technique for human error rate prediction (THERP), success likelihood
index method-multiattribute utility decomposition (SLIM-MAUD), accident
sequence evaluation program (ASEP), human cognitive reliability model (HCR),
standardized plant analysis risk-human reliability analysis (SPAR-H), and human
error assessment and reduction technique (HEART).
Chapters 6 and 7 present various important aspects of human factors and human
error in power generation, respectively. Chapter 8 is devoted to human factors in
control systems. It covers topics such as control room deﬁciencies that can lead to
human error, common problems associated with controls and displays and their
corrective measures, human factors guidelines for digital control system displays,
and human engineering discrepancies in control room visual displays.
Chapter 9 covers various important aspects of human factors in power plant
maintenance, including power plant systems’ human factors engineering maintenance-related shortcomings, advantages of human factors engineering applications
in power plants, and human factors methods to assess and improve power plant
maintainability. Chapter 10 is devoted to human error in power plant maintenance.
Some of the topics covered in the chapter are facts and ﬁgures, maintenance tasks
most susceptible to human error in power generation, useful guidelines to reduce
and prevent human errors in power plant maintenance, and methods for performing human error analysis in power plant maintenance.
Finally, Chap. 11 presents a total of six mathematical models for performing
human reliability and error analysis in power generation.
The book will be useful to many individuals, including engineering professionals working in the area of power generation, power generation administrators,
engineering undergraduate and graduate students, power system engineering
researchers and instructors; reliability, safety, human factors, and psychology
professionals; and design engineers and associated professionals.
The author is deeply indebted to many individuals, including family members,
friends, colleagues, and students for their invisible input. The unseen contributions
of my children also are appreciated. Last but not least, I thank my wife, Rosy, my
other half and friend, for typing this entire book and timely help in proofreading.
Ottawa, Ontario
B. S. Dhillon
viii
Preface

---


### Page 8

Contents
1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.1
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1
1.2
Human Reliability, Error, and Human Factors in Power
Generation-Related Facts, Figures, and Examples. . . . . . . . . .
1
1.3
Terms and Definitions. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.4
Useful Information on Human Reliability, Error, and Human
Factors in Power Generation . . . . . . . . . . . . . . . . . . . . . . . .
4
1.4.1
Books . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.4.2
Journals. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.4.3
Technical Reports. . . . . . . . . . . . . . . . . . . . . . . . . .
6
1.4.4
Conference Proceedings . . . . . . . . . . . . . . . . . . . . .
6
1.4.5
Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
1.4.6
Organizations. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
1.5
Scope of the Book . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
1.6
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2
Basic Mathematical Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
2.2
Sets and Boolean Algebra Laws . . . . . . . . . . . . . . . . . . . . . .
13
2.3
Probability Definition and Properties . . . . . . . . . . . . . . . . . .
15
2.4
Useful Mathematical Definitions . . . . . . . . . . . . . . . . . . . . .
16
2.4.1
Definition I: Probability Density Function . . . . . . . . .
16
2.4.2
Definition II: Cumulative Distribution Function . . . . .
17
2.4.3
Definition III: Expected Value . . . . . . . . . . . . . . . . .
18
2.4.4
Definition IV: Laplace Transform. . . . . . . . . . . . . . .
19
2.4.5
Definition V: Laplace Transform:
Final-Value Theorem . . . . . . . . . . . . . . . . . . . . . . .
19
2.5
Probability Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
2.5.1
Exponential Distribution . . . . . . . . . . . . . . . . . . . . .
20
2.5.2
Rayleigh Distribution . . . . . . . . . . . . . . . . . . . . . . .
21
2.5.3
Weibull Distribution . . . . . . . . . . . . . . . . . . . . . . . .
22
2.5.4
Bathtub Hazard Rate Curve Distribution . . . . . . . . . .
23
ix

---


### Page 9

2.6
Solving First-Order Differential Equations
with Laplace Transforms . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
2.7
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3
Basic Human Factors, Reliability, and Error Concepts . . . . . . . .
27
3.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.2
Human Factors Objectives, Human and Machine
Characteristics Comparisons, and Types
of Man–Machine Systems . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.3
Typical Human Behaviours and Their Corresponding
Design Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
3.4
Human-Sensory Capacities . . . . . . . . . . . . . . . . . . . . . . . . .
30
3.4.1
Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
3.4.2
Touch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
3.4.3
Vibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
3.4.4
Sight. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
3.5
Useful Human Factors Formulas . . . . . . . . . . . . . . . . . . . . .
33
3.5.1
Formula for Estimating Character Height . . . . . . . . .
33
3.5.2
Formula for Estimating Rest Period . . . . . . . . . . . . .
34
3.5.3
Formula for Estimating Glare Constant . . . . . . . . . . .
34
3.5.4
Formula for Estimating Human Energy Cost
Associated with Lifting Weights. . . . . . . . . . . . . . . .
35
3.6
Human Factors Checklist, Guidelines, and Data
Collection Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
3.7
Operator Stress Characteristics, Occupational Stressors,
and General Stress Factors. . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.8
Human Performance Reliability Function . . . . . . . . . . . . . . .
39
3.9
Human Error Occurrence Reasons, Common Ways,
Consequences, and Human Error Classifications. . . . . . . . . . .
41
3.10
Human Reliability and Error Data Collection Sources
and Quantitative Data Values. . . . . . . . . . . . . . . . . . . . . . . .
44
3.11
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
4
General Methods for Performing Human Reliability
and Error Analysis in Power Plants . . . . . . . . . . . . . . . . . . . . . .
49
4.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
4.2
Error-Cause Removal Programme (ECRP). . . . . . . . . . . . . . .
49
4.3
Man–Machine Systems Analysis . . . . . . . . . . . . . . . . . . . . .
51
4.4
Failure Modes and Effect Analysis . . . . . . . . . . . . . . . . . . . .
51
4.5
Probability Tree Method . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
4.6
Markov Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
x
Contents

---


### Page 10

4.7
Fault Tree Analysis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
4.7.1
Fault Tree Probability Evaluation . . . . . . . . . . . . . . .
59
4.7.2
Fault Tree Analysis Advantages
and Disadvantages . . . . . . . . . . . . . . . . . . . . . . . . .
62
4.8
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
5
Speciﬁc Human Reliability Analysis Methods for Nuclear
Power Plants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
5.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
5.2
Incorporation of the Human Reliability Analysis Integrally
into a Probabilistic Risk Assessment and Requirements
for Human Reliability Analysis Method . . . . . . . . . . . . . . . .
65
5.3
Human Reliability Analysis Process Steps and Their
End Products . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
5.4
Human Reliability Analysis Methods . . . . . . . . . . . . . . . . . .
68
5.4.1
A Technique for Human Event Analysis . . . . . . . . . .
69
5.4.2
Cognitive Reliability and Error Analysis Method . . . .
70
5.4.3
Technique for Human Error Rate Prediction . . . . . . .
72
5.4.4
Success Likelihood Index Method–Multi-Attribute
Utility Decomposition . . . . . . . . . . . . . . . . . . . . . . .
73
5.4.5
Accident Sequence Evaluation Program . . . . . . . . . .
74
5.4.6
Human Cognitive Reliability Model . . . . . . . . . . . . .
74
5.4.7
Standardized Plant Analysis Risk–Human
Reliability Analysis . . . . . . . . . . . . . . . . . . . . . . . .
75
5.4.8
Human Error Assessment and Reduction
Technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
5.5
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
6
Human Factors in Power Generation . . . . . . . . . . . . . . . . . . . . .
81
6.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
6.2
Human Factors Engineering Design Goals
and Responsibilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
6.3
Human Factors Issues in Ageing Power Plants. . . . . . . . . . . .
82
6.4
Human Factors Issues that Can have Positive Impact
on Nuclear Power Plant Decommissioning . . . . . . . . . . . . . .
83
6.5
Human Factors Review Guide for Next-Generation Reactors
and Guidance Documents for Human Factors . . . . . . . . . . . .
86
6.5.1
Guidance Documents for Human Factors. . . . . . . . . .
88
6.6
Potential Human Factors Engineering Application Areas
and Expected Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . .
89
6.7
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91
Contents
xi

---


### Page 11

7
Human Error in Power Generation. . . . . . . . . . . . . . . . . . . . . . .
93
7.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
93
7.2
Facts, Figures, and Examples . . . . . . . . . . . . . . . . . . . . . . . .
93
7.3
Major Factors for Human Errors and Their
Occurrence Preventions . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
7.4
Occurrences Caused by Operator Errors During Operation
and Operator Error Causes. . . . . . . . . . . . . . . . . . . . . . . . . .
95
7.5
Questions to Measure Up Electrical Power System Operating
Practices to Reduce Human Errors . . . . . . . . . . . . . . . . . . . .
95
7.6
Performance Shaping Factors. . . . . . . . . . . . . . . . . . . . . . . .
97
7.7
Methods for Analyzing Human Errors in Power Generation . .
98
7.7.1
Pontecorvo Method. . . . . . . . . . . . . . . . . . . . . . . . .
98
7.7.2
Probability Tree Method . . . . . . . . . . . . . . . . . . . . .
100
7.7.3
Pareto Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . .
103
7.8
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
104
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
104
8
Human Factors in Control Systems. . . . . . . . . . . . . . . . . . . . . . .
107
8.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
107
8.2
Control Room Design Deficiencies that can Lead
to Human Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
107
8.3
Advantages of Considering Human Factors in Digital Control
Room Upgrades, an Approach to Incorporate Human
Factors Considerations in Digital Control Room Upgrades,
and Recommendations to Overcome Problems When Digital
Control Room Upgrades are Undertaken Without Considering
Human Factors into Design . . . . . . . . . . . . . . . . . . . . . . . . .
108
8.4
Common Problems Associated with Controls and Displays
and Their Corrective Measures. . . . . . . . . . . . . . . . . . . . . . .
110
8.5
Human Engineering Discrepancies in Control Room
Visual Displays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
111
8.6
Human Factors Guidelines for Digital Control
System Displays . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
112
8.6.1
Windows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
113
8.6.2
Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
114
8.6.3
Manual/Auto Stations, Controls on Mimics,
and Permissive and Tag Outs. . . . . . . . . . . . . . . . . .
115
8.6.4
Inter-Frame Navigation . . . . . . . . . . . . . . . . . . . . . .
115
8.6.5
Colour Usage. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
116
8.7
Human Performance-Related Advanced Control
Room Technology Issues. . . . . . . . . . . . . . . . . . . . . . . . . . .
116
xii
Contents

---


### Page 12

8.8
Control Room Annunciator’s Human Factors-Related
Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
117
8.9
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
119
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
120
9
Human Factors in Power Plant Maintenance. . . . . . . . . . . . . . . .
123
9.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
123
9.2
Power Plant Systems’ Human Factors Engineering
Maintenance-Related Shortcomings. . . . . . . . . . . . . . . . . . . .
123
9.3
Desirable Human Factors Engineering Maintenance-Related
Attributes of a Power Plant’s Well-Designed Systems
and Elements Relating to Human Performance that Can
Contribute to a Successful Maintenance Programme . . . . . . . .
124
9.4
Performance Goals of a Power Plant that Drive Decisions
About Human Factors and a Study of Human Factors
in Power Plants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
125
9.5
Advantages of Human Factors Engineering Applications
in Power Plants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
128
9.6
Human Factors’ Methods to Assess and Improve
Power Plant Maintainability. . . . . . . . . . . . . . . . . . . . . . . . .
129
9.6.1
Critical Incident Method . . . . . . . . . . . . . . . . . . . . .
129
9.6.2
Task Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . .
130
9.6.3
Structured Interviews . . . . . . . . . . . . . . . . . . . . . . .
130
9.6.4
Maintainability Checklist. . . . . . . . . . . . . . . . . . . . .
131
9.6.5
Potential Accident/Damage Analyses . . . . . . . . . . . .
132
9.7
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
132
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
132
10
Human Error in Power Plant Maintenance . . . . . . . . . . . . . . . . .
135
10.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
135
10.2
Facts, Figures, and Examples . . . . . . . . . . . . . . . . . . . . . . . .
135
10.3
Maintenance Tasks Most Susceptible to Human Error
in Power Generation and Types of Human Errors in Digital
Plant Protection Systems Maintenance Tasks . . . . . . . . . . . . .
136
10.4
Causal Factors for Critical Incidents and Reported Events
Related to Maintenance Error in Power Plants
and Classifications of Causes of Human Error
in Power Plant Maintenance. . . . . . . . . . . . . . . . . . . . . . . . .
137
10.5
Steps for Improving Maintenance-Related Procedures
in Power Plants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
140
10.6
Useful Guidelines to Reduce and Prevent Human Errors
in Power Plant Maintenance. . . . . . . . . . . . . . . . . . . . . . . . .
140
Contents
xiii

---


### Page 13

10.7
Methods for Performing Human Error Analysis
in Power Plant Maintenance. . . . . . . . . . . . . . . . . . . . . . . . .
141
10.7.1
Maintenance Personnel Performance Simulation
(MAPPS) Model. . . . . . . . . . . . . . . . . . . . . . . . . . .
142
10.7.2
Markov Method . . . . . . . . . . . . . . . . . . . . . . . . . . .
142
10.7.3
Fault Tree Analysis. . . . . . . . . . . . . . . . . . . . . . . . .
146
10.8
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
148
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
149
11
Mathematical Models for Performing Human Reliability
and Error Analysis in Power Plants . . . . . . . . . . . . . . . . . . . . . .
151
11.1
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
151
11.2
Model I: Human Correctability Probability Function. . . . . . . .
151
11.3
Model II: Critical and Non-Critical Human Errors
Probability Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
153
11.4
Model III: Human Performance Reliability
in Fluctuating Environment . . . . . . . . . . . . . . . . . . . . . . . . .
156
11.5
Model IV: Human Performance Reliability Prediction
with Critical and Non-Critical Self-Generated
Errors and Corrective Action . . . . . . . . . . . . . . . . . . . . . . . .
159
11.6
Model V: Availability Analysis of a Power Plant
System with Human Error . . . . . . . . . . . . . . . . . . . . . . . . . .
162
11.7
Model VI: Reliability Analysis of a Power Plant Redundant
System with Human Errors . . . . . . . . . . . . . . . . . . . . . . . . .
165
11.8
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
167
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
168
Author Biography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
169
Appendix Bibliography: Literature on Human Reliability, Error,
and Human Factors in Power Generation. . .
171
xiv
Contents

---


### Page 14

Chapter 1
Introduction
1.1 Background
Over the years, since the way to generate electricity discovered by M. Faraday in
the United Kingdom in the early part of the nineteenth century, the use of electricity has been continuously increasing. Each year, a vast sum of money is being
spent in the area of power generation to design, construct/manufacture, operate,
and maintain various types of power systems around the globe. Nuclear power
plants are one example of such systems. They generate around 16 % of the world’s
electricity, and there are over 440 commercial nuclear reactors operating in 30
countries, with another 65 reactors under construction [1].
Needless to say, many times, such systems fail due to human error. For
example, during the period 1990–1994, about 27 % of commercial nuclear plants
outages in the United States resulted from human error [2]. Since 1971, a large
number of publications directly or indirectly related to human reliability, error, or
human factors in power generation have appeared. A list of over 240 such publications is provided in the Appendix.
1.2 Human Reliability, Error, and Human Factors
in Power Generation-Related Facts, Figures,
and Examples
Some of the facts, ﬁgures, and examples directly or indirectly concerned with
human reliability, error, and human factors in power generation are as follows:
• During the period 1969–1986, about 54 % of the incidents due to human errors
in Japan resulted in automatic shutdown of nuclear reactors and 15 % of that
resulted in power reduction [3].
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_1,
 Springer International Publishing Switzerland 2014
1

---


### Page 15

• A study of 255 shutdowns that occurred in Korean nuclear power plants during
the period 1978–1992 reported that 77 of these shutdowns were human induced
[4, 5].
• During the period 1990–1994, around 27 % of the commercial nuclear power
plant outages in the United States were the result of human error [2].
• A study of 143 occurrences of operating US commercial nuclear power plants
during the period from February 1975 to April 1975 revealed that about 20 % of
the occurrences were due to operator errors [6, 7].
• A study of over 4,400 maintenance-related history records concerning a boiling
water reactor (BWR) nuclear power plant covering the period from 1992 to 1994
revealed that about 7.5 % of all failure records could be attributed to human
errors related to maintenance activities [8, 9].
• In 1990, in the area of nuclear power generation, a study of 126 human errorrelated signiﬁcant events revealed that about 42 % of the problems were linked
to modiﬁcation and maintenance [10].
• As per Ref. [11], during the period from 1965 to 1995, a total of 199 human
errors occurred in Japanese nuclear power plants, out of which 50 of them were
concerned with maintenance tasks.
• As per Refs. [12, 13], operation errors associated with control centres in fossilﬁred steam generating power plants in the United States could result in up to
3.85 % of plants’ unavailability.
• As per Ref. [14], a study by the United States Nuclear regulatory Commission
(NRC) of Licensee Reports reported that around 65 % of nuclear system failures
involve human error [15].
• As per Refs. [10, 16], a number of studies reported that between 55 and 65 %,
human performance-related problems surveyed in the area of power generation
were concerned with maintenance activities.
• As per Refs. [12, 17], about 70 % of nuclear power plant operation errors appear
to have a human factor origin.
• As per Ref. [18], 25 % of unexpected shutdowns in Korean nuclear power plants
were due to human errors, out which more than 80 % of human errors resulted
from usual testing and maintenance tasks.
• As per Ref. [11], maintenance errors account for around 60 % of the annual
power loss due to human errors in fossil power plants.
• As per Ref. [19], the major incident/accident reports of nuclear power plants in
Korea indicate that about 20 % of the total events occur due to human error.
• As per Ref. [20], in 1979, the Three Mile Island nuclear power plant accident in
the United States was the result of human-related problems.
• In 1986, Chernobyl nuclear power plant accident in Ukraine, widely regarded as
the worst accident in the history of nuclear power, was also the result of humanrelated problems [20].
• As per Ref. [21], in the state of Florida, on Christmas Day in 1989, two nuclear
reactors were shut down due to maintenance error and caused rolling blackouts.
• In the late 1990s, a blast at the Ford Rouge power plant in Dearborn, Michigan,
due to a maintenance error killed six workers and injured many others [22, 23].
2
1
Introduction

---


### Page 16

1.3 Terms and Deﬁnitions
This section presents some useful terms and deﬁnitions directly or indirectly
related to human reliability, error, and human factors in power generation [23–31]:
• Human factors. This is a study of the interrelationships between humans, the
tools they utilize, and the surrounding environment in which they work and live.
• Power system reliability. This is the degree to which the performance of the
elements in a bulk system results in electrical energy being delivered to customers within the speciﬁed standards and in the amount needed.
• Human error. This is the failure to perform a speciﬁed task (or the performance
of a forbidden action) that could lead to disruption of scheduled operations or
result in damage to equipment and property.
• Continuous task. This is a task that involves some kind of tracking activity (e.g.
monitoring a changing condition or situation).
• Human performance. This is a measure of failures and actions under speciﬁed
conditions.
• Human reliability. This is the probability of accomplishing a task successfully
by humans at any required stage in system operation within a speciﬁed minimum time limit (i.e. if the time requirement is stated).
• Failure. This is the inability of an equipment/system/item to carry out its
speciﬁed function.
• Mission time. This is that element of uptime required to perform a speciﬁed
mission proﬁle.
• Maintenance. This is all actions appropriate to retain an item/equipment in, or
restoring it to, a stated condition.
• Reliability. This is the probability that an item will carry out its stated function
satisfactorily for the desired period when used according to the speciﬁed
conditions.
• Man function. This is that function which is allocated to the system’s human
element.
• Unsafe behaviour. This is the manner in which a person carries out actions that
are considered unsafe to himself/herself or others.
• Human error consequence. This is an undesired consequence of human failure.
• Maintainability. This is the probability that a failed equipment/system/item
will be restored to satisfactorily working condition.
• Maintenance person. This is a person who carries out preventive maintenance
and responds to a user’s service call to a repair facility and performs appropriate
corrective maintenance on an equipment/item/system. Some of the other names
used for this individual are repair person, technician, ﬁeld engineer, and service
person.
• Redundancy. This is the existence of more than one means to perform a stated
function.
• Downtime. This is the time during which the item/equipment/system is not in a
condition to carry out its deﬁned mission.
1.3
Terms and Deﬁnitions
3

---


### Page 17

• Useful life. This is the length of time an item/equipment/system functions
within an acceptable level of failure rate.
• Safety. This is conservation of human life and its effectiveness and the prevention of damage to items as per stated mission requirements.
1.4 Useful Information on Human Reliability, Error,
and Human Factors in Power Generation
This section lists books, journals, technical reports, conference proceedings, data
sources, and organizations that are considered directly or indirectly useful for
obtaining information on human reliability, error, and human factors in the area of
power generation.
1.4.1 Books
Some of the books, directly or indirectly, concerned with human reliability, error,
and human factors in power generation are as follows:
• Whittingham, R.B., The Blame Machine: Why Human Error Causes Accidents,
Elsevier Butterworth-Heinemann, Oxford, U.K., 2004.
• Dekker, S., Ten Questions About Human Error: A New View of Human Factors
and System Safety, Lawrence Erlbaum Associates, Mahwah, New Jersey, 2005.
• Dhillon, B.S., Human Reliability: with Human Factors, Pergamon Press, New
York, 1986.
• Salvendy, G., Editor, Handbook of Human Factors and Ergonomics, John Wiley
and Sons, New York, 2006.
• Proctor, R.W.,Van Zandt, T., Human Factors in Simple and Complex Systems,
CRC Press, Boca Raton, Florida, 2008.
• Dhillon, B.S., Human Reliability, Error, and Human Factors in Engineering
Maintenance, CRC Press, Boca Raton, Florida, 2009.
• Grigsby, L.E., editor, Electric Power Generation, Transmission, and Distribution, CRC Press, Boca Raton, Florida 2007.
• Dhillon, B.S., Power System Reliability, Safety, and Management, Ann Arbor
Science Publishers, Ann Arbor, Michigan, 1983.
• Cepin, M., Assessment of Power System Reliability: Methods and Applications,
Springer, London, 2011.
• Strauch, B., Investigating Human Error: Incidents, Accidents, and Complex
Systems, Ashgate Publishing, Aldershot, UK, 2002.
• Reason, J., Hobbs, A., Managing Maintenance Error: A Practical Guide, Ashgate Publishing, Aldershot, UK, 2003.
4
1
Introduction

---


### Page 18

• Kletz, T.A., An Engineer’s View of Human Error, Taylor and Francis, New
York, 2001.
• Peters, G.A., Peters, B.J., Human Error: Causes and Control, CRC Press, Boca
Raton, Florida, 2006.
• Oborne, D.J., Ergonomics at Work: Human Factors in Design and Development,
John Wiley and Sons, New York, 1995.
• Willis, H.E., Scott, W.G., Distributed Power Generation: Planning and Evaluation, Marcel Dekker, New York, 2000.
• Corlett, E.N., Clark, T.S., The Ergonomics of Workspaces and Machines, Taylor
and Francis, London, 1995.
1.4.2 Journals
Some of the journals that time to time publish articles, directly or indirectly,
concerned with human reliability, error, and human factors in power generation are
listed below.
• Reliability Engineering and System Safety.
• IEEE Transactions on Power Apparatus and Systems.
• IEEE Transaction on Reliability.
• IEEE Power & Energy Magazine.
• Human Factors.
• International Journal of Man–Machine Studies.
• Accident Prevention and Analysis.
• Nuclear Safety.
• Human Factors in Aerospace and Safety.
• Journal of Quality in Maintenance Engineering.
• Applied Ergonomics.
• Nuclear Engineering and Design.
• IEEE Transactions on Industry Applications.
• Journal of Risk and Reliability.
• Journal of Korean Nuclear Society.
• Power Engineering.
• International Journal of Reliability, Quality, and Safety Engineering.
• Human Factors and Ergonomics in Manufacturing.
• Nuclear Europe Worldscan.
• Ergonomics.
• IEEE Transactions on Power Delivery.
• IEEE Transactions on Systems, Man, and Cybernetics.
• International Journal of Power and Energy Systems.
• Nuclear Energy and Engineering.
• Electric Power Systems Research.
1.4
Useful Information on Human Reliability
5

---


### Page 19

1.4.3 Technical Reports
Some of the technical reports, directly or indirectly, concerned with human reliability, error, and human factors in power generation are as follows:
• Kolaczkowshi, A., Forester, J., Lois, E., Cooper, S., Good Practices for
Implementing Human Reliability Analysis (HRA), Report No. NUREG-1792,
United States Nuclear Regulatory Commission, Washington, D.C., April 2005.
• Nuclear Power Plant Operating Experience, from the IAEA/NEA Incident
Reporting System, Report, Organization for Economic Co-operation and
Development (OECD), 2 rue Andre-Pascal, 7575 Paris Cedex 16, France, 2000.
• ‘‘An Analysis of 1990 signiﬁcant Events’’, Report No. INP091-018, Institute of
Nuclear Power Operations (INPO), Atlanta, Georgia, 1991.
• ‘‘Assessment of the Use of Human Factors in the Design of Fossil-Fired Steam
Generating Systems’’, Report No. EPRI CS-1760, Electric Power Research
Institute (EPRI), Palo Alto, California, 1981.
• Trager, T.A., Jr., Case Study Report on Loss of Safety System Function Events,
Report No. AEOD/C504, United States Nuclear Regulatory Commission,
Washington, D.C., 1985.
• ‘‘An Analysis of Root Causes in 1983 and 1984 Signiﬁcant Event Reports’’,
Report No. 85-027, Institute of Nuclear Power Operations, Atlanta, Georgia,
July 1985.
• Seminara, J.L., Parsons, S.O., Human Factors Review of Power Plant Maintenance, Report No. EPRI NP-1567, Electric Power Research Institute, Palo Alto,
California, 1981.
• WASH-1400, Reactor Safety Study: An Assessment of Accident Risks in U.S.
Commercial Nuclear Power Plants, U.S. Nuclear Regulatory Commission,
Washington, D.C., 1975.
• Mc Cornack, R.L., Inspector Accuracy: A Study of the Literature, Report No.
SCTM 53-61 (14), Sandia Corporation, Albuquerque, New Mexico, 1961.
• Maintenance Error Decision Aid (MEDA), Developed by Boeing Commercial
Airplane Group, Seattle, Washington, 1994.
1.4.4 Conference Proceedings
Some of the conference proceedings that contain articles, directly or indirectly,
concerned with human reliability, error, and human factors in power generation are
listed below.
• Proceedings of the American Nuclear Society International Topical Meeting on
Nuclear Power Plant Instrumentation Controls, and Human Machine Interface
Technology, 2009.
• Proceedings of the IEEE Conference on Human Factors and Power Plants, 2007.
6
1
Introduction

---


### Page 20

• Proceedings of the International Conference on Nuclear Energy for New Europe, 2006.
• Proceedings of the Human Factors and Ergonomics Society Annual Meeting,
2005.
• Proceedings of the IEEE Power Engineering Society General Meeting, 2006.
• Proceedings of the IEEE International Conference on Systems, Man, and
Cybernetics, 2007.
• Proceedings of the International Conference on Nuclear Power Plant Aging,
Availability Factor, and Reliability Analysis, 1985.
• Proceedings of the International Conference on Design and Safety of Advanced
Nuclear Power Plants, 1992.
• Proceedings of the Annual Reliability and Maintainability Symposium, 2001.
• Proceedings of the Annual Symposium on Reliability, 1969.
• Proceedings of the IEEE International Conference on Human Interfaces in
Control Rooms, 1999.
1.4.5 Data Sources
There are many sources to obtain human reliability and error data. Some of the
sources that could be useful, directly or indirectly, for obtaining human reliability
and error data in the area of power generation are as follows:
• Human Error Classiﬁcation and Data Collection, Report No. IAEA-TEC DOC538, International Atomic Energy Agency (IAEA), Vienna, Austria, 1990.
• Government Industry Data Exchange Program (GIDEP), GIDEP Operations
Center, U.S. Department of Navy, Corona, California, USA.
• Stewart, C., The Probability of Human Error in Selected Nuclear Maintenance
Tasks, Report No. EGG-SSDC-5580, Idaho National Engineering Laboratory,
Idaho Falls, Idaho, USA, 1981.
• Dhillon, B.S., Human Reliability: With Human Factors, Pergamon Press, New
York, 1986 (This book lists over 20 sources for obtaining human reliabilityrelated data).
• Gertman, D.I., Blackman, H.S., Human Reliability and Safety Analysis Data
Handbook, John Wiley and Sons, New York, 1994.
• Data on Equipment Used in Electric Power Generation, Equipment Reliability
Information Center (ERIC), Canadian Electrical Association, Montreal, Quebec,
Canada.
• Swain, A.D., Guttman, H.E., Handbook of Human Reliability Analysis with
Emphasis on Nuclear Power Plant Applications, Report No. NUREG/CR-1278,
U.S. Nuclear Regulatory Commission, Washington, D.C., 1983.
• Collection and Classiﬁcation of Human Reliability Data for Use in Probabilistic
Safety Assessments, Report No. IAEA-TECDOC-1048, International Atomic
Energy Agency, Vienna, Austria, 1998.
1.4
Useful Information on Human Reliability
7

---


### Page 21

• Dhillon, B.S., Human Error Data Banks, Microelectronics and Reliability, Vol.
30, 1990, pp. 963–971.
• Boff, K.R., Lincoln, J.E., Engineering Data Compendium: Human Perception
and Performance, Vols. 1–3, Armstrong Aerospace Medical Research Laboratory, Wright-Patterson Air Force Base, Ohio, USA, 1988.
• Schmidtke, H., Editor, Ergonomic Data for Equipment Design, Plenum Press,
New York, 1984.
• National Technical Information Service, 5285 Port Royal Road, Springﬁeld,
Virginia, USA.
1.4.6 Organizations
There are many organizations that collect human reliability, error, and human
factor-related data. Some of the organizations that could be useful, directly or
indirectly, to obtain human reliability, error, and human factors in power generation-related data are listed below.
• IEEE Power & Energy Society, 445 Hoes Lane, Piscataway, New Jersey, USA.
• Human Factors and Ergonomics Society, 1124 Montana Avenue, Suite B, Santa
Monica, California, USA.
• American Nuclear Society, 555 North Kensington Avenue, La Grange Park,
Illinois, USA.
• International Atomic Energy Agency, Wagramer Strasse 5, Vienna, Austria.
• Canadian Nuclear Society, 655 Bay Street, 17th Floor, Toronto, Ontario,
Canada.
• National Research Council, 2101 Constitution Avenue, NW, Washington, D.C.,
USA.
• American Society for Quality, 600 North Plankinton Avenue, Milwaukee,
Wisconsin, USA.
• American Society of Safety Engineers, 1800 E Oakton Street, Des Plaines,
Illinois, USA.
• International System Safety Society, Unionville, Virginia, USA.
• IEEE Reliability Society, c/o IEEE Corporate Ofﬁce, 3 Oak Avenue, 17th Floor,
New York, USA.
• Society for Maintenance and Reliability Professionals, 401 N. Michigan Avenue, Chicago, Illinois, USA.
• Society for Machinery Failure Prevention Technology, 4193 Sudley Road,
Haymarket, Virginia, USA.
8
1
Introduction

---


### Page 22

1.5 Scope of the Book
Just like any other area of engineering, electrical power generation is also subjected to human-related problems. In recent years, increasing attention is being
given to human-related problems in the area of power generation due to various
factors, including cost and serious consequences such as a blast at the Ford Rouge
power plant and the Three Mile Island Nuclear accident.
Over the years, a large number of publications, directly or indirectly, related to
human reliability, error, and human factors in power generation have appeared.
Almost all of these publications are in the form of conference proceedings or
journal articles, or technical reports. At present, to the best of author’s knowledge,
there is no speciﬁc book that covers the topic of this book within its framework.
This book attempts to provide up-to-date coverage not only of the ongoing effort in
human reliability, error, and human factors in power generation, but also of useful
developments in the general areas of human reliability, human error, and human
factors.
Finally, the main objective of this book is to provide professionals concerned
with human reliability, error, and human factors in power generation information
that could be useful to reduce or eradicate altogether the occurrence of human
errors in this area. The book will be useful to many individuals including engineering professionals working in the area of power generation, researchers and
instructors involved with power systems, reliability, and human factors, safety
professionals and administrators involved with power generation, and graduate
students in the area of power generation and reliability engineering.
1.6 Problems
1. Deﬁne the following terms:
• Human factors.
• Human error.
• Human reliability.
2. Write an essay on human reliability, error, and human factors in power
generation.
3. List at least six facts and ﬁgures concerned with human error/reliability in
power generation.
4. Compare the terms ‘‘human performance’’ and ‘‘human reliability’’.
5. List ﬁve most important organizations to obtain human error and human
reliability in power generation-related information.
6. List at least six important books for obtaining, directly or indirectly, human
reliability and error in power generation-related information.
1.5
Scope of the Book
9

---


### Page 23

7. Deﬁne the following four terms:
• Power system reliability.
• Unsafe behaviour.
• Mission time.
• Human error consequence.
8. List at least six sources for obtaining human reliability and error in power
generation-related data.
9. List six most important journals to obtain human reliability and error in power
generation-related information.
10. Deﬁne the following terms:
• Continuous task.
• Man function.
• Downtime.
References
1. Nuclear Industry Association (NIA) (2013) Facts and ﬁgures, Carlton House, London
2. Varma V (1996) Maintenance training reduces human errors. Power Eng 100:44–47
3. Mishima S (1988) Human factors research program: long term plan in cooperation with
government and private research centers. In: Proceedings of the IEEE conference on human
factors and power plants, pp 50–54
4. Heo G, Park J (2010) A framework for evaluating the effects of maintenance-related human
errors in nuclear power plants. Reliab Eng Syst Saf 95:797–805
5. Lee JW, Park GO, Park JC, Sim BS (1996) Analysis of error trip cases in Korean NPPs.
J Korean Nucl Soc 28:563–575
6. Scott RL (1975) Recent occurrences of nuclear reactors and their causes. Nucl Saf
16:496–497
7. Husseiny AA, Sabry ZA (1980) Analysis of human factor in operation of nuclear power
plants. Atomkernenergie Kerntechnik 36:115–121
8. Pyy P, Laakso K, Reiman L (1997) A study of human errors related to NPP maintenance
activities. In: Proceedings of the IEEE sixth annual human factors meeting, pp 12.23–12.28
9. Pyy P (2001) An analysis of maintenance failures at a nuclear power plant. Reliab Eng Syst
Saf 72:293–302
10. Reason J (1997) Human factors in nuclear power generation: a systems perspective. Nucl Eur
Worldscan 17(5–6):35–36
11. Daniels RW (1985) The formula for improved plant maintainability must include human
factors. In: Proceedings of the IEEE conference on human factors and nuclear safety,
pp 242–244
12. Williams JC (1988) A data-based method for assessing and reducing human error to improve
operational performance. In: Proceedings of the IEEE conference on human factors and
power plants, pp 436–450
13. Assessment of the Use of Human Factors in the Design of Fossil-Fired Steam Generating
Systems (1981) EPRI Report No. CS-1760, Electric Power Research Institute (EPRI), Palo
Alto, California
14. Ryan GT (1988) A task analysis-linked approach for integrating the human factor in
reliability assessments of nuclear power plants. Reliab Eng Syst Saf 22:219–234
10
1
Introduction

---


### Page 24

15. Trager TA Jr (1985) Case study report on loss of safety system function events. Report No.
AEOD/C 504, United States Nuclear Regulatory Commission (NRC), Washington, D.C
16. An Analysis of 1990 Signiﬁcant Events (1991) Report No. INPO 91-018, Institute of Nuclear
Power Operations (INPO), Atlanta, Georgia
17. An Analysis of Root Causes in 1983 and 1984 Signiﬁcant Event Reports (1985) Report No.
85-027, Institute of Nuclear Power Operations (INPO), Atlanta, Georgia, July 1985
18. Heo G, Park J (2009) Framework of quantifying human error effects in testing and
maintenance. In: Proceedings of the sixth American nuclear society international topical
meeting
on
nuclear
plant
instrumentation,
control,
and
human-machine
interface
technologies, pp 2083–2092
19. Kim J, Park J, Jung W, Kim JT (2009) Characteristics of test and maintenance human errors
leading to unplanned reactor trips in nuclear power plants. Nucl Eng Des 239:2530–2536
20. Kawano R (1997) Steps toward the realization of human-centered systems: an overview of
the human factors activities at TEPCO. In: Proceedings of the IEEE 6th annual human factors
meeting, pp 13.27–13.32
21. Maintenance Error a Factor in Blackouts (1989) Miami Herald, Miami, Florida, 29 Dec, p 4
22. The UAW and the Rouge Explosion: A Pat on the Head (1999) Detroit news, Detroit,
Michigan, 6 Feb, p 6
23. Kueck JD, Kirby BJ, Overholt PN, Markel LC (2004) Measurement practices for reliability
and power quality. Report No. ORNL/TM-2004/91, June 2004. Available from the Oak
Ridge National Laboratory, Oak Ridge, Tennessee, USA
24. Omdahl TP (ed) (1988) Reliability, availability, and maintainability (RAM) dictionary.
ASQC Quality Press, Milwaukee
25. Mc Kenna T, Oliverson R (1997) Glossary of reliability and maintenance terms. Gulf
Publishing Company, Houston
26. MIL-STD-721C, Deﬁnitions of terms for reliability and maintainability. Department of
Defense, Washington, D.C
27. Naresky JJ (1970) Reliability deﬁnitions. IEEE Trans Reliab 19:198–200
28. Meister D (1966) Human factors in reliability. In: Ireson WG (ed) Reliability handbook.
Mc Graw Hill Book Company, New York
29. MIL-STD-721B (1996) Deﬁnitions of effectiveness for reliability, maintainability, human
factors, and safety. Department of Defense, Washington, D.C., August 1966. Available from
the Naval Publications and Forms Center, 5801 Tabor Avenue, Philadelphia, Pennsylvania
30. MIL-STD-1908, Deﬁnitions of human factors terms. Department of Defense, Washington,
D.C
31. Dhillon BS (1986) Human reliability: with human factors. Pergamon Press, New York
References
11

---


### Page 25

Chapter 2
Basic Mathematical Concepts
2.1 Introduction
Just like in other areas of science and engineering, mathematics also plays an
important role in the area of human reliability, error, and human factors. The
history of mathematics may be traced back to more than 2,200 years to the
development of our day-to-day used number symbols. The very ﬁrst evidence of
the use of these symbols is found on stone columns erected around 250 BC by the
Scythian emperor of India named Asoka [1].
However, the development of the probability ﬁeld is relatively new, and its
history may be traced back to the writings of Girolamo Cardano (1501–1576) in
which he considered some interesting probability issues [1, 2]. Blaise Pascal
(1623–1662) and Peirre de Fermat (1601–1665) solved the problem of dividing the
winnings in a game of chance, independently and correctly [2]. The ﬁrst formal
treatise on probability based on the Pascal-Fermat correspondence was written by
Christiaan Huygens (1629–1695) in 1657 [2]. Needless to say, additional information on historical developments in the area of mathematics is available in Refs.
[1, 2].
This chapter presents basic mathematical concepts considered useful in performing human reliability and error analysis in the area of power generation.
2.2 Sets and Boolean Algebra Laws
A set may be deﬁned as any well-deﬁned collection or list of objects. Usually, the
objects comprising the set are known as its elements. Normally, capital letters such
as X, Y, and Z are used to denote sets and their elements by the lower-case letters
such as a, b, and c.
Two basic set operations are referred to as the union of sets and the intersection
of sets. Either of the following two symbols is used to denote the union of sets [3]:
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_2,
 Springer International Publishing Switzerland 2014
13

---


### Page 26

• þ
• [
For example, if X ? Y = Z, it simply means that all the elements in set X or in
set Y or in both sets (i.e. X and Y) are contained in set Z.
Similarly, either of the following two symbols is used to denote the intersection
of sets:
• \
• dot :ð Þ
For example, if A \ B = C, it simply means that set C contains all elements
which belong to both sets A and B. However, when sets A and B have no common
elements, then these two sets are referred to as mutually exclusive or disjoint sets
or events.
Boolean algebra plays an important role in probability theory and reliabilityrelated studies and is named after a mathematician named George Boole
(1813–1864). Some of its laws are as follows [3–5]:
Cummutative Law
X þ Y ¼ Y þ X
ð2:1Þ
X:Y ¼ Y:X
ð2:2Þ
where
X
is an arbitrary set or event.
Y
is an arbitrary set or event.
+
denotes the union of sets.
.
denotes the intersection of sets. It is to be noted that sometimes, Eq. (2.2) is
written without the dot, but it still conveys the same meaning.
Associative Law
XY
ð
ÞZ ¼ X YZ
ð
Þ
ð2:3Þ
X þ Y
ð
Þ þ Z ¼ X þ Y þ Z
ð
Þ
ð2:4Þ
where
Z
is an arbitrary set or event.
Idempotent Law
X þ X ¼ X
ð2:5Þ
XX ¼ X
ð2:6Þ
Absorption Law
X þ ðXYÞ ¼ X
ð2:7Þ
X X þ Y
ð
Þ ¼ X
ð2:8Þ
14
2
Basic Mathematical Concepts

---


### Page 27

Distributive Law
X Y þ Z
ð
Þ ¼ XY þ XZ
ð2:9Þ
X þ YZ ¼ X þ Y
ð
Þ X þ Z
ð
Þ
ð2:10Þ
2.3 Probability Deﬁnition and Properties
Probability may be deﬁned as follows [4, 6]:
PðXÞ ¼ lim
n!1
N
n
 
ð2:11Þ
where
P(X)
is the probability of occurrence of event X.
N
is the number of times event X occurs in the n repeated experiments.
Some of the basic properties of probability are presented below [4, 6].
• The probability of occurrence of event, say Y, is
0  PðYÞ  1:
ð2:12Þ
• The probability of occurrence and non-occurrence of an event, say Y, is always
PðYÞ þ PðYÞ ¼ 1
ð2:13Þ
where
P(Y)
is the probability of occurrence of event Y.
P Y
ð Þ
is the probability of non-occurrence of event Y.
• Probability of the sample space S is
P S
ð Þ ¼ 1:
ð2:14Þ
• Probability of negation of the sample space S is
P S
ð Þ ¼ 0:
ð2:15Þ
• The probability of the union of m independent events is
P Y1 þ Y2 þ    þ Ym
ð
Þ ¼ 1 
Y
m
i¼1
1  P Yi
ð Þ
ð
Þ
ð2:16Þ
where
PðYiÞ
is the probability of occurrence of event Yi; for i = 1, 2, 3,…, m.
2.2
Sets and Boolean Algebra Laws
15

---


### Page 28

• The probability of the union of m mutually exclusive events is given by
P Y1 þ Y2 þ    þ Ym
ð
Þ ¼
X
m
i¼1
PðYiÞ:
ð2:17Þ
• The probability of an intersection of m independent events is given by
P Y1Y2. . .Ym
ð
Þ ¼ P Y1
ð
ÞP Y2
ð
Þ. . .P Ym
ð
Þ:
ð2:18Þ
Example 2.1 Assume that a system used in a power generation plant is composed
of three subsystems Y1; Y2; and Y3 and which must be operated by three independent operators. For the successful operation of the system, all the three operators must perform their tasks correctly. The reliabilities of operators, operating
subsystems Y1; Y2; and Y3 are 0.95, 0.92, and 0.9, respectively.
Calculate the probability of successful operation of the system.
By substituting the given data values in Eq. (2.18), we get
P Y1Y2Y3
ð
Þ ¼ PðY1ÞPðY2ÞPðY3Þ
¼ 0:95
ð
Þ 0:92
ð
Þ 0:9
ð
Þ
¼ 0:7866:
Thus, the probability of successful operation of the system is 0.7866.
2.4 Useful Mathematical Deﬁnitions
This section presents ﬁve mathematical deﬁnitions considered useful to perform
human reliability-related studies in the area of power generation.
2.4.1 Deﬁnition I: Probability Density Function
For a continuous random variable, the probability density function is deﬁned by
[6, 7]
fðtÞ ¼ d FðtÞ
dt
ð2:19Þ
where
t
is time (i.e. a continuous random variable).
f(t)
is the probability density function. In the area of human reliability, it is
often referred to as error density function.
F(t)
is the cumulative distribution function.
16
2
Basic Mathematical Concepts

---


### Page 29

Example 2.2 Assume that the error probability at time t (i.e. cumulative distribution function) of a power generating system operator is expressed by
F tð Þ ¼ 1  eht
ð2:20Þ
where
h
is the constant error rate of the power generating system operator.
F(t)
is the cumulative distribution function or the operator error probability at
time t.
Obtain an expression for the probability density function (i.e. in this case, the
operator error density function) by using Eq. (2.19).
By inserting Eq. (2.20) into Eq. (2.19), we obtain
fðtÞ ¼ d 1  eht


dt
¼ heht
ð2:21Þ
Thus, Eq. (2.21) is the expression for the operator error density function.
2.4.2 Deﬁnition II: Cumulative Distribution Function
Cumulative distribution function for a continuous random variable is expressed by
[6, 7]
FðtÞ ¼
Zt
1
fðyÞdy
ð2:22Þ
where
y
is a continuous random variable.
f(y)
is the probability density function.
For t = ? in Eq. (2.22), we get
Fð1Þ ¼
Z1
1
fðyÞdy
¼ 1:
ð2:23Þ
It simply means that the total area under the probability density curve is always
equal to unity.
2.4
Useful Mathematical Deﬁnitions
17

---


### Page 30

Example 2.3 Prove Eq. (2.20) with the aid of Eq. (2.21).
Thus, for t  0; by inserting Eq. (2.21) into Eq. (2.22), we obtain
FðtÞ ¼
Zt
0
hehtdt
¼ 1  eht:
ð2:24Þ
Both Eqs. (2.20) and (2.24) are identical.
2.4.3 Deﬁnition III: Expected Value
The expected value of a continuous random variable is expressed by [6, 7]
EðtÞ ¼
Z1
1
tfðtÞdt
ð2:25Þ
where
E(t)
is the expected value or mean value of the continuous random variable t. It
is to be noted that in the area of human reliability and error, the expected
value is known as the mean time to human error.
Example 2.4 Assume that a power generating system operator’s error density
function, for time t  0; is expressed by Eq. (2.21) and the operator’s error rate is
0.0005 errors/h. Calculate mean time to human error of the power generating
system operator.
For t  0; by inserting Eq. (2.21) into Eq. (2.25), we get
EðtÞ ¼
Z1
0
t hehtdt
¼ 1
h :
ð2:26Þ
By substituting the given data value for h in Eq. (2.26), we obtain
EðtÞ ¼
1
0:0005
¼ 2,000 h:
Thus, the mean time to human error of the power generating system operator is
2,000 h.
18
2
Basic Mathematical Concepts

---


### Page 31

2.4.4 Deﬁnition IV: Laplace Transform
The Laplace transform of the function f(t) is deﬁned by [8]
fðsÞ ¼
Z1
0
fðtÞestdt
ð2:27Þ
where
s
is the Laplace transform variable.
f(s)
is the Laplace transform of f(t).
t
is the time variable.
Laplace transforms of some frequently used functions to perform human reliability-related mathematical analysis in the area of power generation are presented
in Table 2.1 [8, 9].
2.4.5 Deﬁnition V: Laplace Transform: Final-Value
Theorem
If the following limits exist, then the ﬁnal-value theorem may be expressed as
follows:
lim
t!1 fðtÞ ¼ lim
s!0 sfðsÞ
½

ð2:28Þ
Example 2.5 Prove with the aid of the equation presented below that the right side
of Eq. (2.28) is equal to its left side.
fðtÞ ¼
c
ðc þ dÞ 
c
ðc þ dÞ eðcþdÞt
ð2:29Þ
where c and d are constants.
With the aid of Table 2.1, we get the following Laplace transforms of
Eq. (2.29)
fðsÞ ¼
c
sðc þ dÞ 
c
ðc þ dÞ 
1
ðs þ c þ dÞ :
ð2:30Þ
By inserting Eq. (2.30) into the right side of Eq. (2.28), we get
lim
s!0 s
c
sðc þ dÞ 
c
ðc þ dÞðs þ c þ dÞ


¼
c
ðc þ dÞ :
ð2:31Þ
2.4
Useful Mathematical Deﬁnitions
19

---


### Page 32

By substituting Eq. (2.29) into the left side of Eq. (2.28), we obtain
lim
t!1
c
ðc þ dÞ 
c
ðc þ dÞ eðcþdÞt


¼
c
ðc þ dÞ :
ð2:32Þ
As the right sides of Eqs. (2.31) and (2.32) are exactly the same, it proves that
the right side of Eq. (2.28) is equal to its left side.
2.5 Probability Distributions
Over the years, a large number of probability distributions have been developed to
perform various types of statistical analysis [10]. This section presents some of
these probability distributions considered useful to perform human reliabilityrelated probability analysis in the area of power generation.
2.5.1 Exponential Distribution
This is probably the most widely used probability distribution to perform various
types of reliability-related studies [11]. Its probability density function is deﬁned by
fðtÞ ¼ heht
for t  0; h [ 0
ð2:33Þ
where
f(t)
is the probability density function.
t
is the time variable.
h
is the distribution parameter.
Table 2.1 Laplace
transforms of some
frequently used functions to
perform human reliabilityrelated mathematical analysis
in the area of power
generation
f(t)
f(s)
tm; for m = 0, 1, 2, 3, …
m!=smþ1
c, a constant
c/s
ebt
1
sþb
dfðtÞ
dt
s f(s) - f(0)
tfðtÞ
dt
 dfðsÞ
ds
a1f1ðtÞ þ a2f2ðtÞ
a1f1ðsÞ þ a2f2ðsÞ
tebt
1=ðs þ bÞ2
20
2
Basic Mathematical Concepts

---


### Page 33

By inserting Eq. (2.33) into Eq. (2.22), we obtain the following expression for
cumulative distribution function:
FðtÞ ¼
Zt
0
hehtdt
¼ 1  eht:
ð2:34Þ
By substituting Eq. (2.33) in Eq. (2.25), we get the following expression for the
distribution mean value:
m ¼ EðtÞ ¼
Z1
0
thehtdt
¼ 1
h
ð2:35Þ
where
m
is the distribution mean value.
Example 2.6 Assume that in a power generating station, the human error rate is
0.08 errors per week. Calculate the probability of an error occurrence during a 30week period with the aid of Eq. (2.34).
Thus, we have
t ¼ 30 weeks and
h ¼ 0:08 errors=week:
By substituting the above data values in Eq. (2.34), we get
F 30
ð
Þ ¼ 1  eð0:08Þð30Þ
¼ 0:9093:
This means that there is 90.93 % chance for the occurrence of human error
during the 30-week period.
2.5.2 Rayleigh Distribution
This distribution is named after John Rayleigh (1842–1919), its founder, and is
frequently used in reliability work and in the theory of sound [1]. The probability
density function of the distribution is deﬁned by
2.5
Probability Distributions
21

---


### Page 34

fðtÞ ¼ 2
a2 te
t
að Þ
2
for t  0; a [ 0
ð2:36Þ
where
t
is time.
a
is the distribution parameter.
By substituting Eq. (2.36) into Eq. (2.22), we obtain the following equation for
the cumulative distribution function:
FðtÞ ¼ 1  e
t
að Þ
2
:
ð2:37Þ
With the aid of Eqs. (2.25) and (2.36), we obtain the following expression for
the expected value of t:
EðtÞ ¼ a Cð3=2Þ
ð2:38Þ
where
CðyÞ ¼
Z1
0
ty1etdt;
for y [ 0:
ð2:39Þ
2.5.3 Weibull Distribution
This distribution can be used to represent many different physical phenomena, and
it is named after Weibull [12], a Swedish mechanical engineering professor, who
developed it in the early 1950s. The probability density function of the distribution
is deﬁned by
fðtÞ ¼ btb1
hb
e
t
hð Þ
b
t  0; b [ 0; h [ 0
ð2:40Þ
where
t
is time.
h and b
are the scale and shape parameters, respectively.
By substituting Eq (2.40) into Eq (2.22), we obtain the following equation for
the cumulative distribution function:
FðtÞ ¼ 1  e
t
hð Þ
b
:
ð2:41Þ
By inserting Eq. (2.40) into Eq. (2.25), we get the following equation for the
expected value of t:
22
2
Basic Mathematical Concepts

---


### Page 35

EðtÞ ¼ h C 1 þ 1
b


ð2:42Þ
where
Cð:Þ
is the gamma function and is expressed by Eq. (2.39).
For b = 2 and 1, the Rayleigh and exponential distributions are the special
cases of this distribution, respectively.
2.5.4 Bathtub Hazard Rate Curve Distribution
This probability distribution can be used to represent bathtub-shaped, decreasing
and increasing, and increasing hazard/human error rates. It was developed in 1981
[13], and in the published literature, it is generally known as the Dhillon distribution/law/model [14–33].
The probability density function for the distribution is deﬁned by [13].
fðtÞ ¼ bh ht
ð
Þb1e
e ht
ð
Þb ht
ð
Þb1

	
for h [ 0; b [ 0; t  0
ð2:43Þ
where
t
is time.
b and h
are the distribution shape and scale parameters, respectively.
By inserting Eq. (2.43) into Eq. (2.22), we get the following equation for the
cumulative distribution function:
FðtÞ ¼ 1  e
e htt
ð
Þb1

	
:
ð2:44Þ
At b ¼ 0:5; this distribution gives the bathtub hazard rate curve, and at b = 1, it
becomes the extreme value distribution. In other words, the extreme value distribution is the special case of this distribution at b = 1.
2.6 Solving First-Order Differential Equations
with Laplace Transforms
Laplace transforms are an effective tool to ﬁnd solution to linear ﬁrst-order differential equations, and in human reliability-related studies, time-to-time linear
ﬁrst-order differential equations are solved. The application of Laplace transforms
to ﬁnd solution to a set of ﬁrst-order differential equations describing the reliability
of maintenance personnel in a power plant is demonstrated through the following
example:
2.5
Probability Distributions
23

---


### Page 36

Example 2.7 Assume that the reliability of maintenance personnel in a power
plant with respect to human error is described by the following two linear ﬁrstorder differential equations:
d PnðtÞ
dt
þ hm PnðtÞ ¼ 0
ð2:45Þ
d PeðtÞ
dt
 hm PnðtÞ ¼ 0
ð2:46Þ
where
PnðtÞ
is the probability that the maintenance personnel are performing their tasks
normally at time t.
PeðtÞ
is the probability that the maintenance personnel have committed an error
at time t.
hm
is the constant error rate of the maintenance personnel.
At time t ¼ 0; Pnð0Þ ¼ 1; and Peð0Þ ¼ 0:
Find solutions to Eqs. (2.45) and (2.46) with the aid of Laplace transforms.
By taking the Laplace transforms of Eqs. (2.45) and (2.46) and then using the
given initial conditions, we get
PnðsÞ ¼
1
s þ hm
ð2:47Þ
PeðsÞ ¼
hm
sðs þ hmÞ
ð2:48Þ
where
s
is the Laplace transform variable.
Taking the inverse Laplace transforms of Eqs. (2.47) and (2.48), we obtain
PnðtÞ ¼ ehmt
ð2:49Þ
PeðtÞ ¼ 1  ehmt:
ð2:50Þ
Thus, Eqs. (2.49) and (2.50) are the solutions to Eqs. (2.45) and (2.46).
2.7 Problems
1. Write an essay on the history of mathematics.
2. Describe the following three laws:
• Idempotent law.
• Absorption law.
• Distributive law.
24
2
Basic Mathematical Concepts

---


### Page 37

3. What is the difference between mutually exclusive and independent events?
4. Discuss the basic properties of probability.
5. Deﬁne the following:
• Cumulative distribution function.
• Expected value.
6. Prove that the right-hand side of Eq. (2.10) is equal to its left-hand side.
7. Write down the probability density function for Rayleigh distribution.
8. What are the special case probability distributions of the Weibull distribution?
9. Using Eq. (2.27), obtain Laplace transform of the following function:
fðtÞ ¼ 1  elt
ð2:51Þ
where
t
is a variable.
l
is a constant.
10. Prove Eq. (2.44) using Eqs. (2.22) and (2.43).
References
1. Eves H (1976) An introduction to the history of mathematics. Holt, Rinehart, and Winston,
New York
2. Owen DB (ed) (1976) On the history of statistics and probability. Marcel Dekker, New York
3. Lipschutz S (1964) Set theory and related topics. Mc Graw Hill Book Company, New York
4. Lipschutz S (1965) Probability. Mc Graw Hill Book Company, New York
5. Fault Tree Handbook (1981) Report
No. NUREG-0492, U.S.
Nuclear Regulatory
Commission, Washington, D.C.
6. Mann NR, Schafer RE, Singpurwalla ND (1974) Methods for statistical analysis of reliability
and life data. Wiley, New York
7. Shooman ML (1968) Probabilistic reliability: an engineering approach. Mc Graw-Hill Book
Company, New York
8. Spiegel MR (1965) Laplace transforms. Mc Graw Hill Book Company, New York
9. Oberhettinger F, Baddii L (1973) Tables of Laplace transforms. Springer, New York
10. Patel JK, Kapadia CH, Owen DB (1976) Handbook of statistical distributions. Marcel
Dekker, New York
11. Davis DJ (1952) An analysis of some failure data. J Am Stat Assoc 113–150
12. Weibull W (1951) A statistical distribution function of wide applicability. J Appl Mech
18:293–297
13. Dhillon BS (1981) Life distributions. IEEE Trans Reliab 30(5):457–460
14. Baker AD (1993) A nonparametric estimation of the renewal function. Comput Oper Res
20(2):167–178
15. Cabana A, Cabana EM (2005) Goodness-of-ﬁt to the exponential distribution, focused on
Weibull alternatives. Commun Stat Simul Comput 34:711–723
16. Grane A, Fortiana J (2011) A directional test of exponentiality based on maximum
correlations. Metrika 73:255–274
17. Henze N, Meintnis SG (2005) Recent and classical tests for exponentiality: a partial review
with comparisons. Metrika 61:29–45
2.7
Problems
25

---


### Page 38

18. Hollander M, Laird G, Song KS (2003) Nonparametric interference for the proportionality
function in the random censorship model. Nonparametric Stat 15(2):151–169
19. Jammalamadaka SR, Taufer E (2003) Testing exponentiality by comparing the empirical
distribution
function
of
the
normalized
spacings
with
that
of
the
original
data.
J Nonparametric Stat 15(6):719–729
20. Jammalamadaka SR, Taufer E (2006) Use of mean residual life in testing departures from
exponentiality. J Nonparametric Stat 18(3):277–292
21. Kunitz H (1989) A new class of bathtub-shaped hazard rates and its application in
comparison of two test-statistics. IEEE Trans Reliab 38(3):351–354
22. Kunitz H, Pamme H (1993) The mixed gamma ageing model in life data analysis. Stat Pap
34:303–318
23. Meintanis SG (2009) A class of tests for exponentiality based on a continuum of moment
conditions. Kybernetika 45(6):946–959
24. Morris K, Szynal D (2008) Some U-statistics in goodness-of-ﬁt tests derived from
characterizations via record values. Int J Pure Appl Math 46(4):339–414
25. Morris K, Szynal D (2007) Goodness-of-ﬁt tests based on characterizations involving
moments of order statistics. Int J Pure Appl Math 38(1):83–121
26. Na MH (1999) Spline hazard rate estimation using censored data. J KSIAM 3(2):99–106
27. Nam KH, Chang SJ (2006) Approximation of the renewal function for Hjorth model and
Dhillon model. J Korean Soc Qual Manage 34(1):34–39
28. Nam KH, Park DH (1997) Failure rate for Dhillon model. In: Proceedings of the spring
conference of the Korean society, pp 114–118
29. Nimoto N, Zitikis R (2008) The Atkinson index, the moran statistic, and testing
exponentiality. J Jpn Stat Soc 38(2):187–205
30. Noughabi HA, Arghami NR (2011) Testing exponentiality based on characterizations of the
exponential distribution. J Stat Comput Simul i First:1–11
31. Szynal D (2010) Goodness-of-ﬁt tests derived from characterizations of continuous
distributions, stability in probability, Banach Center Publications, vol 90. Institute of
Mathematics, Polish Academy of Sciences, Warszawa, pp 203–223
32. Szynal D, Wolynski W (2012) Goodness-of-ﬁt tests for exponentiality and Rayleigh
distribution. Int J Pure Appl Math 78(5):751–772
33. Na MH, Lee HW, Kim JJ (1997) A smooth estimation of failure rate function. J Korean Soc
Qual Manage 25(3):51–61
26
2
Basic Mathematical Concepts

---


### Page 39

Chapter 3
Basic Human Factors, Reliability,
and Error Concepts
3.1 Introduction
Over the years, many new developments have taken place in the areas of human
factors, reliability, and error as humans play a key role in the overall reliability of
engineering systems. In fact, human factors, reliability, and error have become
recognizable disciplines in industry in many parts of the world. There are many
standard documents concerning human factors that also, directly or indirectly,
cover human reliability and error. Often, such standard documents are cited in the
design speciﬁcation of complex engineering systems [1, 2].
More speciﬁcally, the requirements speciﬁed in these documents must be satisﬁed by the new system design. Needless to say, during the design and development
of power generation systems, particularly in the area of nuclear power generation,
nowadays, it is common to come across human factors specialists (who cover human
reliability and error as well) working alongside design engineers. These specialists,
in order to produce effective power generation systems with respect to humans,
make use of various human factors, reliability, and error concepts [3, 4].
This chapter presents various useful basic human factors, reliability, and error
concepts for application in the area of power generation.
3.2 Human Factors Objectives, Human and Machine
Characteristics Comparisons, and Types
of Man–Machine Systems
There are many objectives of human factors. They may be grouped under the
following four categories [5]:
• Category I Objectives: Fundamental Operational Objectives. These are
concerned with increasing safety, reducing human errors, and improving system
performance.
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_3,
 Springer International Publishing Switzerland 2014
27

---


### Page 40

• Category II Objectives: Objectives Affecting Reliability and Maintainability.
These are concerned with improving maintainability, reducing the need for
manpower, increasing reliability, and reducing training requirements.
• Category III Objectives: Objectives Affecting Operators and Users. These
are concerned with improving ease of use and user acceptance, improving
aesthetic appearance, improving the work environment, and reducing fatigue,
physical stress, boredom, and monotony.
• Category IV Objectives: Miscellaneous Objectives. These are concerned with
items such as lowering losses of time and equipment and improving production
economy.
Humans and machines possess many characteristics that can be compared.
Thus, some of the important comparable human and machine characteristics are
presented in Table 3.1 [6, 7].
Although there are many different types of man–machine systems, they may be
grouped under three types as shown in Fig. 3.1 [8].
The automated systems perform operation-related functions such as processing,
decision making, action, and sensing. Most of these systems are of the closed-loop
type (a closed-loop system may be expressed as a continuous system performing
some processes that need continuous control and feedback for its successful
operational mission) and usually the basic functions associated with such systems
are programming, maintenance, and monitoring.
The manual systems are made up of hand tools and other aids along with the
operator who controls the overall operation. The operator makes use of his/her
own physical energy as a power source, and then transmits/receives from the tools
a great amount of information.
Finally, the mechanical or semi-automatic systems are made up of well integrated parts, such as various types of powered machine tools. Usually, in these
systems, the machines provide the power and the human operators typically perform the control-related functions.
3.3 Typical Human Behaviours and Their Corresponding
Design Considerations
Over the years, the researchers working in the area of human factors have observed
various human behaviours. Some of the typical human behaviours and their corresponding design considerations in the parentheses are as follows [3]:
• Humans will often use their sense of touch to test or explore the unknown (pay
special attention to this factor during the design process, particularly to the
product handling aspect).
• Humans get easily confused with unfamiliar items (avoid designing totally
unfamiliar items).
28
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 41

Table 3.1 Human and machine characteristics comparisons
No. Human
Machine
1
Humans possess inductive capabilities
Machines possess poor inductive capability, but a good deductive
ability
2
Humans’ memory could be constrained by elapsed time, but it has no capacity
limitation problem
Machines’ memory is not inﬂuenced by absolute and elapsed times
3
Humans are subject to fatigue that increases with the number of hours worked
and lowers with rest
Machines are free from fatigue, but require periodic maintenance
4
Humans require some degree of motivation
Machines require no motivation at all
5
Humans are affected by environmental factors such as temperature, noise, and
hazardous materials; and they need air to breathe
Machines are not easily affected by the environment, thus they are
useful for application in unfriendly environments
6
Humans’ consistency can be low
Machines are consistent, unless there are failures
7
Humans may be absent from work due to factors such as strikes, illness,
personal matters, and training
Machines are subject to malfunctions or failures
8
Humans possess a high degree of intelligence and are capable to apply
judgements to solve unexpected problems
Machines possess limited intelligence and judgemental capability
9
Humans’ reaction time is rather slow in comparison to that of machines
Machines have a fast reaction time to external signals
3.3
Typical Human Behaviours and Their Corresponding Design Considerations
29

---


### Page 42

• Humans frequently tend to hurry (develop design so that it clearly takes into
consideration the human hurry element).
• Humans frequently regard manufactured products as being safe (design products
so that they become impossible to be used incorrectly).
• Humans have become accustomed to certain colour meanings (during the design
process strictly observe existing colour-coding standards).
• Humans generally possess very little knowledge regarding their physical
shortcomings (develop proper design by taking into consideration the basic
characteristics and shortcomings of humans).
• Humans always expect that faucets/valve handles will rotate counter-clockwise
for increasing the ﬂow of steam, liquid, or gas (design such items according to
the expectations of humans).
• Humans generally expect to turn on the electrical power, the switches have to
move upward, or to the right, etc. (design such switches according to the
expectations of the humans).
3.4 Human-Sensory Capacities
As humans possess many useful sensors (i.e., touch, smell, hearing, sight, and
taste), a clear understanding of their sensory capacities can be very helpful to
reduce the occurrence of human errors in the area of power generation. Thus, four
human-sensory capacities are described below, separately [4, 9].
3.4.1 Noise
Noise may simply be described as sounds that lack coherence and reactions of
humans to noise extend beyond the auditory systems (i.e., to feelings such as
fatigue, boredom, well-being, or irritability). Furthermore, excessive noise can
Mechanical or semiautomatic systems
Manual systems
Automated systems
Types
Fig. 3.1 Types of man–machine systems
30
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 43

lead to various types of problems including adverse effects on tasks requiring a
high degree of muscular coordination and precision or intense concentration, loss
of hearing if exposed for long periods, and reduction in the efﬁciency of workers.
Generally, two major physical characteristics (i.e., frequency and intensity) are
used in describing noise. In the case of frequency, the human ears are most sensitive to frequencies in the range of 600–900 Hz and they have the capacity to
detect sounds of frequencies from 20 to 20,000 Hz. As per the past experiences
[9, 10], humans can suffer a major loss of hearing, if they are exposed to noise
frequencies between 4,000 and 6,000 Hz for a long period of time.
In the case of intensity, it is usually measured in decibels (d B) and a person
exposed to over 80 d B of noise can experience permanent or temporary loss of
hearing. It is to be noted that intensity levels for noise sources such as heavy
trafﬁc, normal conversation, household ventilation fan, quiet residential area, voice
whisper, and motion picture sound studio are 70, 60, 56, 40, 20, and 10 d B,
respectively [8, 10].
3.4.2 Touch
The sense of touch is related to the ability of humans in interpreting auditory and
visual stimuli. The sensory cues received by the skin and muscles can be used to
send messages to the brain, thus relieving the ears and the eyes a part of the
workload. In situations when human users are expected to rely completely on their
touch sensors, different types of knob shapes can be adopted for potential
applications.
It is to be added that the application of the touch sensor in technical tasks is not
new; in fact, it has been used by craft workers quite successfully for centuries to
detect surface roughness and irregularities in their work. Nonetheless, various
studies performed over the years clearly indicate that the detection accuracy of
surface irregularities improves dramatically when a person moves an intermediate
thin cloth or a piece of paper over the object surface instead of using bare ﬁngers
[11].
3.4.3 Vibration
Various studies conducted over the years clearly indicate that the existence of
vibration could be detrimental to the performance of both mental and physical
tasks by humans such as operation and maintenance personnel in the area of power
generation. There are many parameters of vibrations including acceleration, frequency, velocity, and amplitude. In particular, low frequency and large amplitude
vibrations contribute to various problems including motion sickness, headaches,
fatigue, eyestrain, and interference with one’s ability to read and interpret
3.4
Human-Sensory Capacities
31

---


### Page 44

instruments effectively [9]. Symptoms such as these become less pronounced as
the vibration amplitude decreases and the frequency increases. Nonetheless, it is to
be noted that low amplitude and high frequency vibration can also cause fatigue to
a certain degree.
Some of the useful guidelines to reduce vibration and motion effects are presented below [9, 12].
• Resist shocks and vibrations through proper designs or isolate them using
springs, cushioned mountings, shock absorbers, etc.
• Aim to eliminate vibrations in excess of 0.08 mil amplitude.
• Use cushioned seats or damping materials to lower vibrations transmitted to a
seated person and avoid vibrations of frequencies 3–4 Hz as this is a vertically
seated person’s resonant frequency.
3.4.4 Sight
This is stimulated by the electromagnetic radiation of certain wavelengths, generally known as the visible portion of the electromagnetic spectrum. The areas of
the spectrum, as seen by the human eyes appear to vary in brightness. For example,
during the day, the eyes of humans are most sensitive to greenish-yellow light with
a wavelength of about 5,500 Å [9].
Furthermore, the human eyes perceive all colours when they are looking
straight ahead but as the viewing angle increases, the colour perception begins to
decrease. In addition, the eyes of humans see differently from different angles.
Some of the additional factors concerned with colour are presented below [9].
• Colour differences are very minimal at night or in poorly illuminated places. In
particular, for a small point source (e.g., a small warning light) or from a distant,
it is quite impossible to make a distinction between blue, green, yellow, and
orange. In fact, all of them will appear to be white.
• Staring at a speciﬁc coloured light and then glancing away may result in the
reversal of colour in the brain. For example, to stare at a red or green light and
then glance away, the signal to the brain may completely reverse the colour.
• Colour-weak individuals do not see colours in a similar way as normal people
do.
Three sight-related useful guidelines are as follows:
• Aim to use red ﬁlters with wavelengths greater than 6,500 Å.
• Avoid relying too much on colour when critical activities may be carried out by
fatigues persons.
• Select the proper colour so that colour-weak individuals do not get confused.
32
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 45

3.5 Useful Human Factors Formulas
Over the years, researchers working in the area of human factors have developed
various types of mathematical formulas to estimate human factors-related information. Some of these formulas considered useful for application in the area of
power generation are presented below.
3.5.1 Formula for Estimating Character Height
This formula is concerned with estimating the character height by considering
factors such as viewing distance, the importance of reading accuracy, viewing
conditions, and illumination. Thus, the character height is expressed by [13]
CH ¼ a VD þ CFI þ CFVI
ð3:1Þ
where
CH
is the correction height in inches.
a
is a constant with the speciﬁed value of 0.0022.
CFVI
is the correction factor for viewing and illumination conditions. Its
recommended values are as follows: 0.26 (below a 1 foot-candle and
unfavourable reading conditions), 0.16 (below a 1 foot-candle and
favourable reading conditions), 0.16 (above a 1 foot-candle and unfavourable reading conditions), and 0.06 (above a 1 foot-candle and
favourable reading conditions).
CFI
is the correction factor for importance. Its recommended values for
similar items or emergency labels is 0.075 and for other items CFI = 0.
VD
is the viewing distance expressed in inches.
Example 3.1 In a power generating station’s control room, the estimated viewing
distance of an instrument panel is 40 inches and after a careful consideration, the
values of CFVI and CFI were decided to be 0.06 and 0.075, respectively. Calculate
the height of the label characters to be used at the instrument panel.
By substituting the given data values into Eq. (3.1), we obtain
CH ¼ 0:0022
ð
Þ 40
ð
Þ þ 0:075 þ 0:06
¼ 0:223 inch
Thus, the label characters’ height to be used is 0.223 inch.
3.5
Useful Human Factors Formulas
33

---


### Page 46

3.5.2 Formula for Estimating Rest Period
Past experience clearly indicates that the incorporation of appropriate rest periods
is essential, when humans perform lengthy or strenuous tasks. Thus, this formula is
concerned with determining the length of unscheduled or scheduled required rest
periods.
The length of the required rest period is expressed by [14]
RLRP ¼ WT AEC  SE
ð
Þ
AEC  ARL
ð
Þ
ð3:2Þ
where
RLRP
is the required length of the rest period expressed in minutes.
AEC
is the average energy cost/expenditure expressed in kilocalories per
minute of work.
SE
is the kilocalories per minute adopted as standard.
ARL
is the approximate resting level expressed in kilocalories per minute.
Usually, the value of ARL is taken as 1.5.
WT
is the working time expressed in minutes.
It is to be noted that the average energy expenditure in kilocalories per minute
(i.e., SE) and the human heart rate in beats per minute (in parentheses) for tasks
such as packing on conveyors, cleaning tables and ﬂoors, and unloading coal cars
in power generation plants are 3.7 (113), 4.5 (112), and 8 (150), respectively.
Example 3.2 Assume that a worker is performing a certain task at a power generation plant for 120 min and his/her average energy expenditure is 9 kcal/min.
Calculate the length of the required rest period if SC = 8 kcal/min and
ARL = 1.5 kcal/min.
By inserting the speciﬁed data values into Eq. (3.2), we get
RLRP ¼ 120 9  8
ð
Þ
9  1:5
ð
Þ
¼ 16 min
Thus, the length of the required rest period is 16 min.
3.5.3 Formula for Estimating Glare Constant
Past experience over the years, clearly indicates that various types of human errors
can occur in the area of power generation due to glare. Thus, this formula is
concerned with estimating the value of the glare constant. The glare constant is
expressed by [14]
34
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 47

h ¼ a0:8
ð
Þ c1:6


A2 GBL
ð
Þ
ð3:3Þ
where
h
is the glare constant.
A
is the angle between the direction of the glare source and the viewing
distance.
GBL
is the general background luminance.
a
is the solid angle subtended at the eye by the source.
c
is the source luminance.
3.5.4 Formula for Estimating Human Energy Cost
Associated with Lifting Weights
As tasks such as lifting weights cost human energy, this formula is concerned with
estimating human energy cost (EC) associated with lifting weights. The EC, is
kilocalories per hour, is expressed by [15].
EC ¼ LH
ð
Þ n
ð Þ w
ð Þ l
ð Þ
1,000
ð3:4Þ
where
LH
is the lifting height in feet.
n
is the number of lifts per hour.
w
is the weight to be lifted in pounds.
l
is the cost of energy per lift (gcal/ft.lb).
Example 3.3 Assume that we have the following data values:
• LH = 3 ft
• n = 30 lifts/h
• w = 10 lb
• l = 5 gcal/ft.lb
Calculate the hourly EC.
By substituting the given data values into Eq. (3.4), we get
EC ¼ 3
ð Þ 30
ð
Þ 10
ð
Þ 5
ð Þ
1,000
¼ 4:5 kcal=h
Thus, the hourly EC is 4.5 kcal/h.
3.5
Useful Human Factors Formulas
35

---


### Page 48

3.6 Human Factors Checklist, Guidelines, and Data
Collection Sources
Over the years, professionals working in the area of human factors have developed
a checklists of questions to be addressed for incorporating human factors into the
designs of engineering systems. These questions can easily be tailored to suit
speciﬁc engineering systems’ designs under consideration. Some examples of such
questions are presented in Table 3.2 [6].
Some of the general human factors’ guidelines considered useful for application
in power generation systems’ designs are as follows [3, 7]:
• Make use of services of human factors specialists as considered appropriate.
• Review system/product objectives in regard to human factors.
• Review all ﬁnal production drawings with respect to human factors.
• Develop an effective human factors checklist for application during system/
product design and production phases.
• Use mock-ups to ‘‘test’’ the effectiveness of user–hardware interface designs.
• Obtain
appropriate
human
factors-related
design
guide
and
reference
documents.
• Perform appropriate ﬁeld test of the system/product design prior to its approval
for delivery to customer.
There are many sources from which human factors-related data can be collected. Some of the important ones are shown in Fig. 3.2 [6, 13].
The test reports contain data obtained from testing manufactured goods. The
published standards are the documents developed by organizations such as
Table 3.2 A sample of questions to be addressed to incorporate human factors into the designs
of engineering systems
Question
no.
Question
1
• Were the human factor principles considered clearly in the workspace design?
2
• Were all controls designed by taking into consideration factors such as
accessibility, size, and shape?
3
• Were environmental factors such as noise, illumination, and temperature
considered in regard to satisfactory levels of human performance?
4
• Is it simple and straightforward to identify each control device?
5
• Are all the displays compatible with their corresponding control devices with
respect to human factors?
6
• Was proper attention given to training and complementing work-related aids?
7
• What type of sensory channels would be the most suitable for messages to be
delivered through the displays?
8
• Were visual display arrangements optimized?
9
• Were human decision making and adaptive capabilities used properly in the
design?
36
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 49

professional societies and government agencies, and they are considered a good
source for obtaining human factors-related data. The previous experience is a good
source to obtain data from similar cases that have occurred in the past.
The user experience reports contain data-reﬂecting users’ experiences with
system/equipment in the ﬁeld-use environment. The published literature is another
good source to obtain human factors-related data, and it includes items such books,
conference proceedings, and journals. Finally, various types of human factorsrelated data can also be obtained during the system/equipment development phase.
3.7 Operator Stress Characteristics, Occupational
Stressors, and General Stress Factors
In order to operate engineering systems, human operators perform various types of
tasks and in performing such tasks, they may have certain limitations or shortcomings. The probability of human error occurrence increases quite signiﬁcantly
when these limitations are violated. During the system design process, a careful
consideration to operator characteristics or limitations can reduce the probability
of human error occurrence quite signiﬁcantly. Some of these characteristics are
presented below [16]:
Sources
Test reports
Previous 
experience
Published 
standards
User
experience 
reports
Published 
literature
System/
equipment 
development 
phase
Fig. 3.2 Sources for collecting human factors-related data
3.6
Human Factors Checklist
37

---


### Page 50

• Requirements for making decisions on the basis of data obtained from diverse
sources.
• Performing task steps at quite high speed.
• Requirements for making quick comparisons of two or more displays.
• Having short decision-making time.
• Requirements for operating more than one control simultaneously at high speed.
• Poor feedback information to determine whether the actions taken were correct
or not.
• Performing tasks that need a fairly long sequence of steps.
• The requirements or prolonged monitoring.
Past experiences, over the years, clearly indicate that stress plays an important
role in the reliability of a person performing a certain task. There are basically four
types of occupational stressors as shown in Fig. 3.3 [4, 17].
The occupational frustration-related stressors are concerned with the problems
related to occupational frustration. This frustration is generated in conditions when
the job inhibits the meeting of speciﬁed goals. The factors that form elements of
occupational
frustration
include
ineffective
career
development
guidance,
bureaucracy difﬁculties, and lack of effective communication.
The occupational change-related stressors are concerned with the occupational
change that disrupts cognitive, behavioural, and physiological patterns of functioning of the person. Some examples of the occupational change are organizational
restructuring, relocation, and promotion. The workload-related stressors are concerned with the problems related to work underload or work overload. In the case of
Occupational 
frustration-related
stressors
Workload-related 
stressors
Occupational changerelated stressors
Miscellaneous stressors
Types
Fig. 3.3 Types of occupational stressors
38
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 51

work underload, the work activities being carried out by the individual fail to provide
appropriate stimulation. Some examples of the work underload are lack of opportunities to use acquired skills and expertise of an individual, lack of any intellectual
input, and repetitive performance. In contrast, in the case of work overload, job
requirements exceed the ability of the individual to satisfy them effectively.
Finally, the miscellaneous stressors are concerned with those stressors that are
not incorporated into the above three categories or types. Some examples of these
stressors are too little or too much lighting, too much noise, and poor interpersonal
relationships.
Various studies conducted, over the years in the area of human factors, have
clearly indicated that there are many general factors that signiﬁcantly increase
stress on a person, in turn resulting in a considerable deterioration in his/her
reliability. Some of these general factors are as follows [2, 18]:
• Low chances for promotion.
• Serious ﬁnance-related difﬁculties.
• Poor health.
• Lacking the necessary expertise to carry out the ongoing job.
• Having difﬁculties with children or spouse or both.
• Possibility of redundancy at work.
• Rather excessive demands at work from superiors.
• Having to work with people with unpredictable temperaments.
3.8 Human Performance Reliability Function
In the area of engineering, humans perform time-continuous tasks such as scope
monitoring, missile countdown, and aircraft manoeuvring. In such situations,
human performance reliability parameter plays a crucial role. The general human
performance reliability function for time-continuous tasks can be developed the
same way as the development of the general reliability function for hardware
engineering systems/items. Thus, using Ref. [19], we write
eh tð Þ ¼  d Rh tð Þ
dt
:
1
Rh tð Þ
ð3:5Þ
where
Rh tð Þ
is the human performance reliability at time t
eh tð Þ
is the time t dependent human error rate
By rearranging Eq. (3.5), we obtain
d Rh tð Þ
Rh tð Þ ¼ eh tð Þdt
ð3:6Þ
3.7
Operator Stress Characteristics
39

---


### Page 52

Integrating both sides of Eq. (3.6) over the time interval 0; t
½
, we obtain
Zt
0
1
Rh tð Þ : d Rh tð Þ ¼ 
Zt
0
eh tð Þdt
ð3:7Þ
Since at t = 0, Rh tð Þ ¼ 1; we rewrite Eq. (3.7) to the following form:
ZRh tð Þ
1
1
Rh tð Þ : d Rh tð Þ ¼ 
Zt
0
eh tð Þdt
ð3:8Þ
After evaluating the left side of Eq. (3.8), we obtain
ln Rh tð Þ ¼ 
Zt
0
eh tð Þdt
ð3:9Þ
Using Eq. (3.9), we obtain the following expression for human performance
reliability:
Rh tð Þ ¼ e
Rt
0
eh tð Þdt
ð3:10Þ
Equation (3.10) is the general expression for human performance reliability,
and it can be used to calculate human performance reliability for any time to
human error statistical distribution including exponential, gamma, and Weibull.
Example 3.4 Assume that the times to human error of a power generation system
operator follow Weibull distribution. Thus, his/her time-dependent error rate is
deﬁned by
eh tð Þ ¼ l
c
t
c
 l1
ð3:11Þ
where
l
is the shape parameter.
c
is the scale parameter.
t
is time.
Obtain the following:
• An expression for the performance reliability function of the power generation
system operator.
• Reliability of the power generation system operator for a 8-hour mission, if
l ¼ 1 and c ¼ 200 h.
40
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 53

By inserting Eq. (3.11) into Eq. (3.10), we obtain
Rh tð Þ ¼ e
Rt
0
l
c
t
cð Þ
l1dt
¼ exp 
t
c
 l


ð3:12Þ
By substituting the speciﬁed data values into Eq. (3.12), we get
Rh 8
ð Þ ¼ exp 
8
200




¼ 0:9607
Thus, the expression for the performance reliability function of the power
generation system operator is given by Eq. (3.12) and his/her reliability for an
8-hour mission is 0.9607.
3.9 Human Error Occurrence Reasons, Common Ways,
Consequences, and Human Error Classiﬁcations
There are many reasons for the occurrence of human errors. Some of the important
ones are shown in Fig. 3.4 [4, 20].
There are many ways for the occurrence of human error. The common ones are
as follows [21]:
• Making an incorrect decision in response to a problem.
• Poor timing and inadequate response to a contingency.
• Failure to carry out a required function.
• Failure to recognize a hazardous situation.
• Performing a task that should not have been executed.
There are various consequences for the occurrence of human errors. They may
vary from one piece of equipment to another, from one situation to another, or
from one task to another. Furthermore, a consequence can range from minor to
severe, for example, from a short delay in system performance to a major loss of
lives and property. Nonetheless, in regard to equipment, the consequences of
human errors may be grouped under the following three classiﬁcations:
• Delay in equipment operation is insigniﬁcant.
• Equipment operation is delayed signiﬁcant but not stopped.
• Equipment operation is stopped completely.
Human errors may be grouped under many classiﬁcations. The seven commonly used classiﬁcations are shown in Fig. 3.5 [20, 22].
3.8
Human Performance Reliability Function
41

---


### Page 54

The operator errors occur in the ﬁeld-use environment of equipment due to
operating personnel, when these personnel overlook to follow correct procedures,
or there is lack of proper procedures. More speciﬁcally, the factors that can lead to
operator errors include poor training, task complexity, poor environmental
conditions, and operator carelessness. The design errors occur due to poor design
and the types of design errors are failure to ensure the effectiveness of the man and
machine interactions, failure to implement human-related needs in the design,
and assigning inappropriate functions to humans. An example of a design error is
the placement of displays and controls so much apart that operating personnel ﬁnd
quite difﬁcult to use both of them in an effective manner.
The fabrication errors occur during the product assembly process due to poor
workmanship. Some examples of these errors are incorrect soldering, using a
Poor skill or 
training
Poorly written 
equipment operating and 
maintenance procedures
Poor management
Distraction in the work 
area
Complex task
Improper work tools
Crowded work space
Poor equipment design
Poor lighting in the 
work area
Poor work layout
Poor motivation
Poor verbal 
communication
High noise or 
temperature level in the 
work area
Reasons
Fig. 3.4 Reasons for the occurrence of human errors
42
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 55

wrong part, assembly incompatible with blueprints, and omitting a component.
Some of the reasons for the occurrence of fabrication errors are poor illumination,
excessive temperature, excessive noise level, and poor blueprints [22]. The
maintenance errors occur generally during the ﬁeld-use environment of equipment/
item due to incorrect installation or repair. Two examples of maintenance errors
are the use of incorrect grease at appropriate points of the equipment/item and
wrong calibration of equipment/item.
The handling errors occur due to poor storage or transport facilities that are not
in accordance with the recommendations of equipment/item manufacturer. The
inspection errors are associated with accepting out-of-tolerance items or rejecting
in-tolerance items. As per Ref. [23], according to various studies, the inspection
effectiveness average is about 85 %.
Finally, the contributory errors are the ones that are quite difﬁcult to deﬁne
either human or related to equipment.
Design errors
Fabrication 
errors
Contributory 
errors
Handling 
errors
Maintenance 
errors
Operator 
errors
Classifications
Inspection 
errors
Fig. 3.5 Classiﬁcations of human errors
3.9
Human Error Occurrence Reasons
43

---


### Page 56

3.10 Human Reliability and Error Data Collection Sources
and Quantitative Data Values
Human reliability and error data are the backbone of any human reliability-related
prediction. These data can be collected through means such as shown in Fig. 3.6
[4, 24–26].
The expert judgements approach is frequently used by human reliability
methodologists to obtain human reliability-related data, and it has the following
two attractive features:
• It is relatively easy to develop because a large amount of data can be collected
from a small number of expert respondents.
• It is comparatively cheaper to develop.
In contrast, the two main drawbacks of this approach are frequent use of less
experienced experts than required and less reliable than data collected through
other means or approaches. The data collected from experimental studies is normally generated under the laboratory conditions. These conditions may not be the
actual representative of the real life conditions. Furthermore, the approach is
expensive and time-consuming. Nonetheless, the main advantage of data collected
through the experimental studies approach is that the data are probably the least
inﬂuenced by the subjective elements that may induce some error. An example of
data based on the ﬁndings of experimental studies is the Data Store [27].
The automatic data recorder approach makes use of instrumentation that permits the automatic recording of operator actions. An example is the operational
Approaches
Expert judgements
Experimental 
studies
Published 
literature
Human data 
recorder
Self-made error 
reports
Automatic data 
recorder
Fig. 3.6 Approaches for collecting human reliability and error data
44
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 57

performance recording and evaluation data system (OPREDS) [28]. The human
data recorder approach calls for the physical presence of a person for observing
task performance and documenting events as necessary. The drawbacks of this
approach include costly and the observer may overlook to recognize committed
errors.
The published literature approach is concerned with collecting data from
publications such as books, journals, and conference proceedings. Finally, in the
case of self-made error reports’ approach, the individual who makes the error also
reports that error. The main drawback of this approach is that humans are generally
quite reluctant to admit making an error.
Some of the speciﬁc data banks for collecting human reliability-related data are
as follows:
• Nuclear Plant Reliability Data System [29].
• Safety-Related Operator Action (SROA) Program [30].
• Technique for Establishing Personnel Performance Standards (TEPPS) [30].
• Aerojet General Method [31].
• Operational Performance Recording and Evaluation Data System (OPREDS)
[28].
• Data Store [27].
• Aviation Safety Reporting System [32].
Human reliability and error data for selective tasks taken from published
sources, directly or indirectly related to power generation systems, are presented in
Table 3.3 [4].
Table 3.3 Human reliability and error data for selective tasks
No. Error/task description
Errors per plant
month
(boiling water
reactors)
Errors per
million
operations
Performance
reliability
1
Wrong servicing
0.03
–
–
2
Requirement misunderstanding/
misinterpretation
0.0074
–
–
3
Adjusting incorrectly
0.026
–
–
4
Closing valve incorrectly
–
1,800
–
5
Reading gauge incorrectly
–
5,000
–
6
Turning rotary selector switch
to certain position
–
–
0.9996
7
Finding maintenance (scheduled)
approaches in maintenance manual
–
–
0.997
3.10
Human Reliability and Error Data Collection
45

---


### Page 58

3.11 Problems
1. Compare human and machine characteristics.
2. List at least eight typical human behaviours.
3. Discuss the following two human-sensory capacities:
• Noise.
• Touch.
4. Write down the formula that can be used to estimate rest period.
5. Discuss typical sources for collecting human factors-related data.
6. Discuss the following three types of occupational-related stressors:
• Workload-related stressors.
• Occupational frustration-related stressors.
• Occupational change-related stressors.
7. Prove Eq. (3.10) using Eq. (3.5).
8. Assume that the error rate of a person performing a task in a power generation
station is 0.005 errors per hour. Calculate his/her reliability during an 8-hour
mission.
9. List at least thirteen reasons for the occurrence of human errors.
10. What are the main approaches for collecting human reliability and error data?
Discuss each of these approaches in detail.
References
1. MIL-H-46855 (1972) Human engineering requirements for military systems, equipment, and
facilities. Department of Defense, Washington, D.C., May 1972
2. Dhillon BS (2009) Human reliability, error, and human factors in engineering maintenance:
with reference to aviation and power generation. CRC Press, Boca Raton
3. Woodson WE (1981) Human factors design handbook. Mc Graw-Hill Book Company, New
York
4. Dhillon BS (1986) Human reliability: with human factors. Pergamon Press, New York
5. Chapanis A (1996) Human factors in systems engineering. Wiley, New York
6. Dhillon BS (1996) Engineering design: a modern approach. Richard D. Irwin Inc, Chicago
7. Dhillon BS (1998) Advanced design concepts for engineers. Technomic Publishing
Company, Lancaster
8. Mc Cormick EJ, Sanders MS (1982) Human factors in engineering and design. Mc Graw-Hill
Book Company, New York
9. AMCP 706-134 (1972) Engineering design handbook: maintainability guide for design.
Prepared by the United States Army Material Command, 5001 Eisenhower Avenue,
Alexandria, Virginia
10. AMCP 706-133 (1976) Engineering design handbook: maintainability engineering theory and
practice. Prepared by the United States Army Material Command, 5001 Eisenhower Avenue,
Alexandria, Virginia
46
3
Basic Human Factors, Reliability, and Error Concepts

---


### Page 59

11. Lederman S (1978) Heightening tactile impression of surface texture. In: Gordon G (ed)
Active touch. Pregamon Press, New York, pp 40–44
12. Altman JW et al (1961) Guide to design mechanical equipment for maintainability. Report
no. ASD-TR-61-381, Air Force Systems Command, Wright-Patterson Air Force Base, Ohio
13. Peters GA, Adams BB (1959) Three criteria for readable panel markings. Prod Eng
30(21):55–57
14. Oborne DJ (1982) Ergonomics at work. Wiley, New York
15. Murrell KFH (1965) Human performance in industry. Reinhold, New York
16. Meister D (1966) Human factors in reliability. In: Ireson WG (ed) Reliability handbook.
Mc Graw-Hill Book Company, New York, pp 400–415
17. Beech HR, Burns LE, Shefﬁeld BF (1982) A behavioural approach to the management of
stress. Wiley, New York
18. Dhillon BS (1980) On human reliability: bibliography. Microelectron Reliab 20:371–373
19. Shooman ML (1968) Probabilistic reliability: an engineering approach. Mc Graw-Hill Book
Company, New York
20. Meister D (1962) The problem of human-initiated failures. In: Proceedings of the 8th national
symposium on reliability and quality control, pp 234–239
21. Hammer W (1980) Product safety management and engineering. Prentice Hall Inc.,
Englewood Cliffs
22. Meister D (1971) Human factors: theory and practice. Wiley, New York
23. Mc Cormack RL (1961) Inspection accuracy: a study of the literature. Report no. SCTM 5361 (14), Sandia Corporation, Albuquerque, New Mexico
24. Meister D (1984) Human reliability. In: Muckler FA (ed) Human factors review. Human
Factors Society, Santa Monica, California, pp 13–53
25. Dhillon BS (1990) Human error data banks. Microelectron Reliab 30:963–971
26. Dhillon BS, Singh C (1981) Engineering reliability: new techniques and applications. Wiley,
New York
27. Munger SJ, Smith RW, Payne D (1962) An index of electronic equipment operability: data
store. Report no. AIR-C43-1/62 RP(1), American Institute for Research, Pittsburgh,
Pennsylvania
28. Urmston R (1971) Operational performance recording and evaluation data system
(OPREDS). Descriptive Brochures, Code 3400, Navy Electronics Laboratory Center, San
Diego, California, Nov 1971
29. Reporting Procedures Manual for the Nuclear Plant Reliability Data System (NPRDS) (1980)
South-West Research Institute, San Antonio, Texas, Dec 1980
30. Topmiller DA, Eckel JS, Kozinsky EJ (1982) Human reliability data bank for nuclear power
plant operations: a review of existing human reliability data banks. Report no. NUREG/
CR2744/1, U.S. Nuclear Regulatory Commission, Washington, D.C
31. Irwin IA, Levitz JJ, Freed AM (1964) Human reliability in the performance of maintenance.
Report no. LRP 317/TDR-63-218, Aerojet-General Corporation, Sacramento, California
32. Aviation Safety Reporting Program (1979) FAA advisory circular no. 00-46B. Federal
Aviation Administration (FAA), Washington, D.C., 15 Jun 1979
References
47

---


### Page 60

Chapter 4
General Methods for Performing Human
Reliability and Error Analysis in Power
Plants
4.1 Introduction
Over the years, a vast amount of the literature in the areas of reliability, human
factors, and safety has appeared in the form of books, journal articles, technical
reports, and conference proceedings articles [1–3]. Many new methods have been
developed in these very three areas. Some of these methods are being used quite
successfully across many diverse areas including engineering design, engineering
maintenance, health care, and management. Some examples of these methods are
fault tree analysis (FTA), failure modes and effect analysis (FMEA), and the
Markov method.
The FTA method was developed in the early 1960s to analyse rocket launch
control systems from the safety aspect [1]. Nowadays, it is being used in many
diverse areas such as aerospace, management, nuclear power generation, and
health care. FMEA was developed in the early 1950s to perform reliability analysis
of engineering systems. Nowadays, it is also being used across many diverse areas
such as aerospace, health care, and power generation. The Markov method was
developed by Andrei Andreyevich Markov (1856–1922), a Russian mathematician, and is a highly mathematical approach frequently used to perform reliability
and safety analyses of engineering systems. Nowadays, it is also being used in
areas such as health care, maintenance, and power generation.
This chapter presents a number of methods and approaches, extracted from the
published literature on reliability, human factors, and safety, considered useful to
perform human reliability and error analysis in power plants.
4.2 Error-Cause Removal Programme (ECRP)
This method was developed to reduce human errors to some tolerable level in the
area of production operations, and it may simply be described as the production
worker-participation programme for reducing human errors [4]. The method
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_4,
 Springer International Publishing Switzerland 2014
49

---


### Page 61

emphasizes preventive measures rather than the remedial ones. Some examples of
the production workers are inspection and maintenance personnel, assembly personnel, and machinists.
All involved production workers are divided into groups/teams, and in turn,
each group/team has a coordinator with necessary technical and group skills. The
maximum number of team members is restricted to twelve persons. Each team
holds its meeting regularly, in which team members present error-likely and error
reports. The reports are reviewed, and then, appropriate recommendations are
made to take necessary remedial measures. The team coordinators present all the
recommendations to appropriate management personnel for their actions.
It is to be noted with care that human factors and other specialists also assist
both team and management personnel with respect to various factors including
evaluation and implementation of the proposed design-related solutions. More
speciﬁcally, the ECRP is composed of the following seven basic elements [2, 4, 5]:
• Element I: All personnel involved with ECRP are properly educated about the
ECRP usefulness.
• Element II: Management clearly values the efforts of production personnel with
respect to ECRP.
• Element III: Management ensures the implementation of the most promising
proposed design-related solutions.
• Element IV: All involved coordinators and workers are trained properly in data
collection and analysis techniques.
• Element V: The effects of changes in the production process by considering the
ECRP inputs are determined by the human factors and other specialists.
• Element VI: Production personnel report and evaluate errors and error-likely
situations and propose possible design solutions to eradicate causes of errors.
• Element VII: Human factors and other specialists review all the proposed
design solutions in regard to cost.
Finally, three guidelines considered most useful concerning ECRP are as follows [4, 5]:
• Review with care each work redesign recommended by the team with respect to
factors such as increment in job satisfaction, cost-effectiveness, and the degree
of error reduction.
• Focus data collection to items such as errors, error-likely conditions, and
accident-prone conditions.
• Restrict to highlighting those work conditions that need redesign for reducing
the error occurrence potential.
50
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 62

4.3 Man–Machine Systems Analysis
This method was developed in the early 1950s and is concerned with reducing
human error-caused unwanted effects to some acceptable level in a system. The
method is composed of ten steps shown in Fig. 4.1 [5, 6].
4.4 Failure Modes and Effect Analysis
This is probably the most widely used method to perform reliability analysis of
engineering systems in industry. FMEA may simply be described as an effective
approach to perform analysis of each potential failure mode in a given system for
determining the effects of such failure modes on the entire system [7]. When the
effect of each failure mode is classiﬁed according to its severity, the method is
known as failure mode effects and critical analysis (FMECA).
The history of FMEA goes back to the early 1950s, and it was developed by the
United States Navy’s Bureau of Aeronautics and was called ‘‘Failure Analysis’’
[8]. Subsequently, ‘‘Failure Analysis’’ was renamed to ‘‘Failure Effect Analysis’’
and the successor to the Bureau of Aeronautics (i.e. Bureau of Naval Weapons)
introduced ‘‘Failure Effect Analysis’’ into its new speciﬁcation on ﬂight controls
[9]. Needless to say, National Aeronautics and Astronautics Administration
(NASA) extended the FMEA functions and then renamed FMEA to FMECA [10].
The following seven main steps are followed to perform FMEA [1, 5, 11]:
• Step 1: Deﬁne system boundaries and all its associated requirements in detail.
• Step 2: List system subsystems and parts.
• Step 3: Identify and describe each part and list its failure modes.
• Step 4: Assign probabilities or failure rates to each part’s failure modes.
• Step 5: List effect or effects of each and every failure mode on subsystem,
system, and plant.
• Step 6: Enter remarks for all failure modes.
• Step 7: Review critical failure modes and take appropriate actions.
There are many advantages of performing FMEA, including a systematic
approach for classifying hardware failures, useful for identifying safety concerned
to be focused on, useful to reduce engineering changes, useful to improve customer satisfaction, a visibility tool for management, useful to improve communication among design interface personnel, a useful approach that starts from the
detailed level and works upward, useful for providing safeguard against repeating
the same mistakes in the future, easy to understand, and useful for reducing
development cost and time [5, 11, 12].
All in all, additional information on FMEA is available in Refs. [11–13].
4.3
Man–Machine Systems Analysis
51

---


### Page 63

4.5 Probability Tree Method
This method is often used for performing task analysis in the technique for the
human error rate prediction (THERP) [14]. In performing task analysis, the
method diagrammatically represents critical human actions and other associated
Step 1:
Define system goals and functions
Define concerned situational characteristics (i.e., the 
Step 2: 
performance shaping factors such as illumination and air 
quality under which tasks have to be performed)
Define characteristics (e.g., experience, skills, training, and
Step 3:
motivation) of involved individuals
Step 4:
Define jobs performed by involved individuals
Analyze jobs with respect to identifying potential error-likely
Step 5:
situations and other associated difficulties
Estimate chances or other information with respect to potential
Step 6:
human error occurrence
Step 7:
Determine the likelihood of failure to detect and rectify a 
potential human error
Step 8:
Determine the possible consequences of failure to detect 
potential human errors
Step9:
Recommend appropriate changes
Step 10:
Re evaluate each and every change by repeating most of the 
above steps
Fig. 4.1 Man–machine systems analysis steps
52
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 64

events. More speciﬁcally, diagrammatic task analysis is denoted by the probability
tree branches. The branching limbs denote outcomes (i.e. success or failure) of
each and every event related to a problem under consideration, and each branch is
assigned probability of occurrence.
There are many advantages of the probability tree method. The three important
ones are as follows [11, 14]:
• Simpliﬁed mathematical computations.
• An effective visibility tool.
• An effective tool for predicting the quantitative effects of errors.
Also, it is to be noted that this method can incorporate, with some modiﬁcations, factors such as interaction effects, emotional stress, and interaction stress [2].
More detailed information on the method is available in Refs. [2, 14].
The application of this method to a human reliability-related power generation
system problem is demonstrated through the following example:
Example 4.1 A power generation system operator performs two independent
tasks: a and b. Task a is performed before task b, and each of these tasks can be
performed either correctly or incorrectly. In other words, the incorrectly performed
tasks are the only errors that can occur in this situation.
Develop a probability tree for this example and obtain an expression for the
probability of failure to accomplish the overall mission by the power generation
system operator.
This example states that the power generation system operator ﬁrst performs
task a correctly or incorrectly and then proceeds to perform task b. Task b can also
be performed correctly or incorrectly by the operator. This complete scenario is
depicted by the probability tree shown in Fig. 4.2.
The four symbols used in Fig. 4.2 are deﬁned below.
a
denotes the event that task a is performed correctly.
a
denotes the event that task a is performed incorrectly.
b
denotes the event that task b is performed correctly.
b
denotes the event that task b is performed incorrectly.
By examining Fig. 4.2, it can be concluded that there are three distinct possibilities (i.e. ab; ab, and ab) for having an overall mission failure. Thus, the probability of failure to accomplish the overall mission by the power generation system
operator is given by
Ppgso ¼ P ab þ ab þ ab


ð4:1Þ
where
Ppgso
is the probability of failure to accomplish the overall mission by the power
generation system operator.
4.5
Probability Tree Method
53

---


### Page 65

For mutually exclusive and independent events using Eq. (4.1), we get
Ppgso ¼ Pa Pb þ Pa Pb þ Pa Pb
ð4:2Þ
where
Pa
is the probability of performing task a correctly.
Pa
is the probability of performing task a incorrectly.
Pb
is the probability of performing task b correctly.
Pb
is the probability of performing task b incorrectly.
Since Pa ¼ 1  Pa and Pb ¼ 1  Pb, Eq. (4.2) reduces to
Ppgso ¼ Pa 1  Pb
ð
Þ þ 1  Pa
ð
ÞPb þ 1  Pa
ð
Þ 1  Pb
ð
Þ
¼ 1  Pa Pb
ð4:3Þ
Example 4.2 Assume that in Example 4.1, the probabilities of failure to accomplish tasks a and b by the power generation system operator are 0.15 and 0.05,
respectively. Calculate the probability of failure to accomplish the overall mission
by the operator.
Thus, we have
Pa ¼ 1  Pa ¼ 1  0:15 ¼ 0:85
Pb ¼ 1  Pb ¼ 1  0:05 ¼ 0:95
By inserting the above-calculated values into Eq. (4.3), we obtain
Ppgso ¼ 1  0:85
ð
Þ 0:95
ð
Þ
¼ 0:1925
Thus, the probability of failure to accomplish the overall mission by the power
generation system operator is 0.1925.
a
b
b
b
b
a
ab
ab
ab
a b
Fig. 4.2 Probability tree for
the power generation system
operator performing tasks a
and b
54
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 66

4.6 Markov Method
This method was developed by Andrei Andreyevich Markov (1856–1922), a
Russian mathematician, and is frequently used to perform various types of reliability-related studies in industry. The method has also been used to perform
human reliability analysis [2]. Thus, it could be a very useful tool to perform
various types of human reliability analysis in the area of power generation.
The Markov method is based on the following three assumptions [11, 15]:
• The probability of the occurrence of a transition from one system state to
another in the ﬁnite time interval Dt is given by h Dt, where h is the constant
transition rate from one system state to another.
• The probability of more than one occurrences in the ﬁnite time interval Dt from
one system state to another is negligible (e.g. ðh DtÞðh DtÞ ! 0).
• All occurrences are independent.
The application of the Markov method to perform human reliability analysis in
the area of power generation is demonstrated through the following example:
Example 4.3 Assume that a power generation system operator makes errors at a
constant rate, h. The state space diagram shown in Fig. 4.3 describes this scenario
in more detail. The numerals shown in the state space diagram denote system
states. By using the Markov method develop expressions for the operator’s reliability at time t and mean time to human error.
With the aid of the Markov method, we write down the following equations for
the state space diagram shown in Fig. 4.3 [11, 15]:
P0 t þ Dt
ð
Þ ¼ P0ðtÞ 1  h Dt
ð
Þ
ð4:4Þ
P1 t þ Dt
ð
Þ ¼ P0ðtÞðh DtÞ þ P1ðtÞ
ð4:5Þ
where
h
is the constant error rate of the power generation system operator.
P0 t þ Dt
ð
Þ
is the probability that the operator is performing his/her task
normally or correctly at time t þ Dt
ð
Þ.
P1 t þ Dt
ð
Þ
is the probability that the operator has committed an error at time
ðt þ DtÞ.
h Dt
is the probability of human error by the power generation system
operator in ﬁnite time interval Dt.
ð1  h DtÞ
is the probability of no human error by the power generation system
operator in ﬁnite time interval Dt.
P0ðtÞ
is the probability that the operator is performing his/her task
normally at time t.
P1ðtÞ
is the probability that the operator has committed an error at time t.
4.6
Markov Method
55

---


### Page 67

By rearranging Eqs. (4.4)–(4.5) and taking the limit as Dt ! 0; we obtain
lim
Dt!0
P0 t þ Dt
ð
Þ  P0ðtÞ
Dt
¼ d P0ðtÞ
dt
¼ h P0ðtÞ
ð4:6Þ
lim
Dt!0
P1ðt þ DtÞ  P1ðtÞ
Dt
¼ d P1ðtÞ
dt
¼ h P0ðtÞ
ð4:7Þ
At time t ¼ 0; P0ð0Þ ¼ 1 and P1ð0Þ ¼ 0:
By solving Eqs. (4.6)–(4.7) with the aid of Laplace transforms, we obtain
P0ðsÞ ¼
1
s þ h
ð4:8Þ
P1ðsÞ ¼
h
s s þ h
ð
Þ
ð4:9Þ
where
s
is the Laplace transform variable.
Taking the inverse Laplace transforms of Eqs. (4.8)–(4.9), we get
P0ðtÞ ¼ eht
ð4:10Þ
P1ðtÞ ¼ 1  eht
ð4:11Þ
Thus, reliability of the power generation system operator is given by
RpgsoðtÞ ¼ P0ðtÞ ¼ eht
ð4:12Þ
where
RpgsoðtÞ
is the reliability of the power generation system operator at time t.
The power generation system operator’s mean time to human error is given by
[11]
Operator 
performing 
his/her t ask 
normally
0
Operator 
committed an 
error
1
θ
Fig. 4.3 State space diagram representing the power generation system operator
56
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 68

MTTHEpgso ¼
Z1
0
RpgsoðtÞdt
¼
Z1
0
ehtdt
¼ 1
h
ð4:13Þ
where
MTTHEpgso
is the mean time to human error of the power generation system
operator.
Example 4.4 A power generation system operator’s constant error rate is
0.0008 errors/h. Calculate the operator’s mean time to human error and reliability
for a 8-h mission.
By inserting the given data values into Eqs. (4.13) and (4.12), we obtain
MTTHEpgso ¼
1
0:0008
¼ 1;250 h
and
Rpgsoð8Þ ¼ eð0:0008Þð8Þ
¼ 0:9936
Thus, the power generation system operator’s mean time to human error and
reliability are 1,250 h and 0.9936, respectively.
4.7 Fault Tree Analysis
This is a widely used method to perform reliability analysis of engineering systems
in industry, particularly in the area of nuclear power generation. The method was
developed in the early 1960s to perform safety analysis of the Minuteman Launch
Control System at the Bell Telephone Laboratories [1].
A fault tree may simply be described as a logical representation of the relationship of primary fault events that may cause the occurrence of a speciﬁed
undesirable event, called the ‘‘top event’’. It is depicted using a tree structure with
logic gates such as AND and OR.
4.6
Markov Method
57

---


### Page 69

It is to be noted that there is probably nothing basically new regarding the
principle used for the generation of fault trees. It consists of successively asking
the following question:
‘‘What are the possible ways for this fault event to occur?’’
Nonetheless, the newness lies in the utilization of logic operators (i.e. gates) in
the organization and graphical representation of the logic structure relating the
primary or basic fault events to the top event.
In the construction of fault trees, there are many symbols used. The four basic
ones are shown in Fig. 4.4 [1, 16]. Information on other symbols is available in
Refs. [1, 11, 16, 17].
All the four symbols in Fig. 4.4 are described below.
• Circle. It denotes a primary or basic fault event or the failure of an elementary
component or part.
• Rectangle. It represents a fault event which results from the logical combination
of fault events through the input of a logic gate.
• AND gate. It denotes that an output fault event will occur only if all of the fault
events occur.
• OR gate. It denotes that an output event will occur if one or more of the input
fault events occur.
Usually, the following steps are followed in performing FTA [11, 18]:
• Step 1: Deﬁne the system and analysis associated assumptions.
• Step 2: Identify the system undesirable or top fault event (i.e. the system
undesirable or top fault event to be investigated).
• Step 3: Identify all the causes that can make the top fault event to occur, by
using fault tree symbols and the logic tree format.
• Step 4: Develop the fault tree to the lowest level of detail as per the
requirements.
• Step 5: Perform analysis of the completed fault tree with respect to factors such
as gaining proper insight into the unique modes of product faults and understanding the proper logic and the interrelationships among various fault paths.
• Step 6: Determine most appropriate corrective actions.
• Step 7: Document the analysis and follow up on the identiﬁed corrective
actions.
Example 4.5 Assume that a power generation system operator is required to
perform task Z. The task is composed of three subtasks: i, j, and k. If one or more
of these subtasks is/are performed incorrectly, the task Z will be performed
incorrectly. Subtask i composed of two steps: m and n. Both these steps must be
performed incorrectly for subtask i to be performed incorrectly. Subtask j is also
composed of two steps: a and b. If one or both of these two steps is/are performed
incorrectly, the subtask j will be performed incorrectly.
58
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 70

If subtasks and steps are independent, develop a fault tree for the undesired
event (i.e. top event): power generation system operator will not perform the task,
Z, correctly.
By using the symbols in Fig. 4.4, the fault tree shown in Fig. 4.5 for this
example is developed. Each fault event in Fig. 4.5 is labelled as E1; E2; E3;
E4; E5; E6; E7; and E8.
4.7.1 Fault Tree Probability Evaluation
The probability of occurrence of the top fault event of a fault tree can be calculated
when the occurrence probabilities of primary or basic fault events are know. This
can only be calculated by ﬁrst calculating the probability of occurrence of the
output (i.e. resultant) fault events of lower and intermediate logic gates such as OR
and AND. Thus, the occurrence probability of the OR gate output fault event is
expressed by [11].
P x0
ð
Þ ¼ 1 
Y
m
j1
1  P xj
 


ð4:14Þ
---
---
(a)
(b)
Output fault event
Output fault event
Input fault events
Input fault 
events
(c)
(d)
Fig. 4.4 Basic fault tree symbols: a Circle, b Rectangle, c AND gate, d OR gate
4.7
Fault Tree Analysis
59

---


### Page 71

where
P x0
ð
Þ
is the occurrence probability of the output fault event, x0, of the OR gate.
m
is the total number of input fault events of the OR gate.
P xj
 
is the probability of occurrence of the OR gate input fault event, xj; for
j = 1, 2, 3, …, m.
Similarly, the occurrence probability of the AND gate output fault event is
given by [11]
P y0
ð
Þ ¼
Y
k
j¼1
P yj
 
ð4:15Þ
where
P y0
ð
Þ
is the occurrence probability of the output fault event, y0, of the AND
gate.
Power generation system 
operator will not perform 
the task, Z correctly
The subtask, i, will 
not be performed 
correctly
The subtask, 
k, will not be 
performed 
correctly
The subtask, j, will 
not be performed 
correctly
The step, 
m, will not 
be
performed 
correctly
The step, 
n, will not 
be
performed 
correctly
The step, 
a, will not 
be
performed 
correctly
The step, 
b, will not 
be
performed 
correctly
Top event
8
E
6
E
5
E
1
E
2
E
3
E
4
E
7
E
Fig. 4.5 A fault tree for the unsuccessful performance of task, Z, by the power generation
system operator
60
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 72

k
is the total number of input fault events of the AND gate.
P yj
 
is the probability of occurrence of the AND gate input fault event yj; for
j = 1, 2, 3, …, k.
Example
4.6 Assume
that
the
occurrence
probabilities
of
fault
events
E1; E2; E3; E4; and E5 in Fig. 4.5 fault tree are 0.01, 0.03, 0.04, 0.05, and 0.02,
respectively.
Calculate the occurrence probability of the top fault event (i.e. power generation system operator will not perform the task, Z, correctly) and then redraw the
fault tree in Fig. 4.5 with the given and calculated fault event occurrence probability values.
By substituting the given data values into Eq. (4.15), we obtain the following
probability value, for the occurrence of event E6: the subtask, i, will not be
performed correctly:
P E6
ð
Þ ¼ P E1
ð
ÞP E2
ð
Þ
¼ 0:01
ð
Þ 0:03
ð
Þ
¼ 0:0003
Similarly, by inserting the speciﬁed data values into Eq. (4.14), we obtain the
following probability value, for the occurrence of event E7: the subtask, j, will not
be performed correctly:
P E7
ð
Þ ¼ 1  1  P E3
ð
Þ
f
g 1  P E4
ð
Þ
f
g
¼ 1  1  0:04
f
g 1  0:05
f
g
¼ 1  0:96
ð
Þ 0:95
ð
Þ
¼ 0:088
By inserting the above two calculated values and the speciﬁed data value for
fault event E5 into Eq. (4.14), we obtain the following probability value for the
occurrence of the top event, E8: power generation system operator will not perform
the task, Z, correctly:
P E8
ð
Þ ¼ 1  1  P E6
ð
Þ
f
g 1  P E5
ð
Þ
f
g 1  P E7
ð
Þ
f
g
¼ 1  1  0:0003
f
g 1  0:02
f
g 1  0:088
f
g
¼ 0:1065
Thus, the occurrence probability of the top fault event (i.e. power generation
system operator will not perform the task, Z, correctly) is 0.1065. The fault tree
with the calculated and given fault event occurrence probability values is shown in
Fig. 4.6.
4.7
Fault Tree Analysis
61

---


### Page 73

4.7.2 Fault Tree Analysis Advantages and Disadvantages
Just like any other reliability analysis approach, the FTA method too has its
advantages and disadvantages. Thus, some of the advantages of the FTA method
are as follows [11]:
• It provides insight into the system behaviour and can handle complex systems
more easily than any other method.
• It serves as a graphic aid for system management and provides options for
management and others to perform either quantitative or qualitative reliability
analysis.
• It highlights failures deductively.
• It allows concentration on one speciﬁc failure at a time and requires the involved
analyst to comprehend thoroughly the system under consideration before
starting the FTA process.
In contrast, some of the disadvantages of the FTA method are as follows [11]:
• It is a time consuming and a costly method.
• Its end results are difﬁcult to check.
• It considers parts/components in either working or failed state. More clearly, the
partial failure states of parts/components are quite difﬁcult to handle.
0.1065
0.0003
0.088
0.02
0.04
0.01
0.03
0.05
8
E
6
E
5
E
1
E
2
E
3
E
4
E
7
E
Fig. 4.6 Redrawn Fig. 4.5 fault tree with the calculated and given fault occurrence probability
values
62
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 74

4.8 Problems
1. Describe error-cause removal programme.
2. What are the guidelines considered most useful concerning ECRP?
3. Describe man–machine systems analysis.
4. Describe failure modes and effect analysis.
5. List at least six advantages of failure modes and effect analysis.
6. Assume that a power generation system operator performs three independent
tasks: x, y, and z. Task x is performed before task y, and task y before task z.
Each of these three tasks can be performed either correctly or incorrectly. In
other words, the incorrectly performed tasks are the only errors that can occur
in this situation.
Develop a probability tree for this example and obtain an expression for the
probability of failure to accomplish the overall mission by the power generation system operator.
7. Assume that in the proceeding question (i.e. question no. 6), the probabilities
of failure to accomplish tasks x, y, and z by the power generation system
operator are 0.2, 0.1, and 0.05, respectively. Calculate the probability of
failure to accomplish the overall mission by the operator.
8. Prove Eqs. (4.10) and (4.11) by using Eqs. (4.6) and (4.7).
9. Describe the following terms used in the fault tree construction with the aid of
diagrams:
• OR gate
• Resultant event
• Basic event
• AND gate.
10. What are the advantages and disadvantages of the FTA method?
References
1. Dhillon BS, Singh C (1981) Engineering reliability: new techniques and applications. Wiley,
New York
2. Dhillon BS (1986) Human reliability with human factors. Pergamon Press, New York
3. Dhillon BS (2003) Engineering safety: fundamentals, techniques, and applications. World
Scientiﬁc Publishing, New Jersey
4. Swain AD (1973) An error-cause removal program for industry. Hum Factors 12:207–221
5. Dhillon BS (2007) Human reliability and error in transportation systems. Springer Inc,
London
6. Miller RB (1953) A method for man-machine task analysis, Report No. 53-137, Wright Air
Development Center, Wright-Patterson Air Force Base, U.S. Air Force (USAF), Ohio
7. Omdahl TP (ed) (1988) Reliability, availability, and maintainability (RAM) dictionary.
American Society of Quality Control (ASQC) Press, Milwaukee
4.8
Problems
63

---


### Page 75

8. MIL-F-18372 (Aer.) General speciﬁcation for design, installation, and test of aircraft ﬂight
control systems. Bureau of Naval Weapons, Department of the Navy, Washington, D.C.,
Paragraph 3.5.2.3
9. Continho JS (1963–1964) Failure effect analysis, Transactions of the New York Academy of
Sciences, vol 26, Series II, pp 564–584
10. Jordan WE (1972) Failure modes, effects and criticality analyses. In: Proceedings of the
annual reliability and maintainability symposium, pp 30–37
11. Dhillon BS (1999) Design reliability: fundamentals and applications. CRC Press, Boca Raton
12. Palady P (1995) Failure modes and effects analysis. PT Publications, West Palm Beach
13. Dhillon BS (1992) Failure modes and effect analysis. Microelectron Reliab 32:719–731
14. Swain AD (1963) A method for performing a human-factors reliability analysis. Report No.
SCR-685, Sandia Corporation, Albuquerque, New Mexico, August 1963
15. Shooman ML (1968) Probabilistic reliability: an engineering approach. Mc Graw Hill Book
Company, New York
16. Schroder RJ (1970) Fault tree for reliability analysis. In: Proceedings of the annual
symposium on reliability, pp 170–174
17. Risk analysis using the fault tree technique. Flow research report, Flow Research, Inc.,
Washington, D.C., 1973
18. Grant Ireson W, Coombs CF, Moss RY (ed) (1996) Handbook of reliability engineering and
management, Mc Graw-Hill Book Company, New York
64
4
General Methods for Performing Human Reliability and Error Analysis

---


### Page 76

Chapter 5
Speciﬁc Human Reliability Analysis
Methods for Nuclear Power Plants
5.1 Introduction
Nuclear power plants generate about 16 % of the world’s electricity, and there are
over 440 commercial nuclear reactors operating in 30 countries, with another
65 reactors under construction [1]. Furthermore, in 2007, 104 nuclear power
plants generated around 19 % of the electricity consumed in the United States [2].
Needless to say, nuclear power plants have become an important element in power
generation throughout the world.
Humans play an important role in nuclear power generation and their reliability
has become an important issue as human error can result in nuclear power plant
accidents such as Chernobyl and Three Mile Island. Furthermore, as per Refs. [3, 4],
a study of Licensee Event Reports (LERs) conducted by the United States Nuclear
Regulatory Commission (USNRC) indicates that upward of 65 % of nuclear system
failures involve human error to a certain degree.
Over the years to perform human reliability analysis (HRA) is nuclear power
plants, a number of methods have been developed. These methods include technique
for human error rate prediction (THERP), task analysis-linked evaluation technique
(TALENT), cognitive reliability and error analysis method (CREAM), and a technique for human event analysis (ATHEANA). This chapter presents important
aspects of HRA methods and a number of methods used in nuclear power plants.
5.2 Incorporation of the Human Reliability Analysis
Integrally into a Probabilistic Risk Assessment
and Requirements for Human Reliability
Analysis Method
As the risk associated with a nuclear power plant is very much dependent on the
reliability of all involved humans and their interactions with the equipment and
controls in the plant, an HRA is an integral part of probabilistic risk assessment (PRA).
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_5,
 Springer International Publishing Switzerland 2014
65

---


### Page 77

Thus, the incorporation of the HRA integrally into a PRA includes the four issued
shown in Fig. 5.1 [5].
The issue ‘‘The relationship of approach to results’’ is basically concerned with
the relationship between the way in which an HRA is carried out, its philosophy,
and the end results or the insights that may be obtained. The issue ‘‘PRA compatibility’’ is concerned with the compatibility of an HRA with the PRA of which
it is an element/part. It is to be noted that the risk applications of PRA require the
HRA process to specify clearly human interaction-related events in qualitative
detail, adequate for guiding the risk management efforts from the perspective of
human factors.
The issue ‘‘Limits’’ is concerned with the HRA limits or the limits of HRA
results. Thus, HRA results should be documented in such a way that is clearly
understandable to general PRA users. Furthermore, the results should be easily
traceable to their data sources, basic assumptions, and models. Finally, the issue
‘‘Flexibility’’ is concerned with the ﬂexibility needed in using behavioural science
technologies associated with HRA. It is to be noted that HRA is a relatively
immature method; however, the method is based on the scientiﬁc disciplines
developed in the area of behavioural sciences with their inherent uncertainties to a
certain degree. All in all, HRA should be ﬂexible enough for accommodating new
ﬁndings and model developments effectively while structured enough to be tractable and repeatable properly.
As HRA forms an important element of nuclear power plants’ probabilistic safety
assessment (PSA) studies, the objective of the PSA ought to be reﬂected in the
choice of the HRA method [6]. This way, if the PSA were to be used by a regulatory
body personnel for assessing the general risk of the industry, one would make use of
generic technique/method representative of a nominal nuclear power plant. Needless
to say, HRA quality is one of the requirements to setting PSA usage. Quality is
reﬂected in both what technique/method is selected and how it is used.
Issues 
Flexibility 
Limits 
PRA compatibility 
The relationship of 
approach to results 
Fig. 5.1 Issues concerning the incorporation of the HRA integrally into a PSA
66
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 78

In order to achieve a ‘‘good’’ quality rating, one has to tie the technique/method
to the use of a non-generic technique/method supported by the use of power plant
personnel (i.e. experts in their specializations) as well as feedback received from
plant experience and the application of the simulator. Additional information on
requirements for an HRA method is available in Ref. [6].
5.3 Human Reliability Analysis Process Steps
and Their End Products
HRA process for use in nuclear power plants is made up of eight steps as shown in
Fig. 5.2 [5]. These steps result in various types of end results or products. The
corresponding result or product of each of these steps is presented below in
parentheses [5].
Step 1: 
Choose and train team members 
Step 2:
 
Familiarize team members with power plant 
Step 3:
 
Build initial power plant model 
Step 4:
 
Screen human interactions 
Step 5:
 
Characterize human interactions 
Step 6:
 
Quantify human interactions 
Sep 7: 
Update power plant model 
Step 8:
 
Review end results 
Fig. 5.2 Human reliability
analysis (HRA) process steps
5.2
Incorporation of the Human Reliability Analysis Integrally
67

---


### Page 79

• Step 1: (Set of various types of skills embodied in an integrated team.)
• Step 2: (Initial identiﬁcation of human functions and activities. Furthermore,
problems can be spotted although without much risk context yet.)
• Step 3: (Most important human interactions identiﬁed, system interactions
identiﬁed, all major systems modelled, and a measure of the defence barriers
against major classes of off-normal events.)
• Step 4: (Important human interactions highlighted, initial quantiﬁcation performed, and screening values chosen.)
• Step 5: (Failure modes, causes, effects, mechanisms, and inﬂuences of the
important human interactions are determined.)
• Step 6: (Importance ranking, likelihood and uncertainties of important human
interactions.)
• Step 7: (Interactions and recovery models added to model.)
• Step 8: (Conﬁdence that end results make sense and can be utilized by plant
personnel in risk applications.)
Additional information on HRA process steps and their end products/results is
available in Ref. [5].
5.4 Human Reliability Analysis Methods
Over the years, many methods have been developed, directly or indirectly, for
generating human error probabilities for application in the nuclear power industrial
sector. Some of these methods are as follows [7–12]:
• Technique for human error rate prediction (THERP).
• Accident sequence evaluation program (ASEP).
• Success likelihood index method–multi-attribute utility decomposition (SLIMMAUD).
• Human cognitive reliability model (HCR).
• A technique for human event analysis (ATHEANA).
• Standardized plant analysis risk–human reliability analysis (SPAR-H).
• Human error assessment and reduction technique (HEART).
• Cognitive reliability and error analysis method (CREAM).
• Justiﬁed human error data information (JHEDI).
The information requirements of THERP, SLIM, HCR, and ASEP are as follows
[7, 13]:
• Appropriate description of the task and the action.
• The available procedures.
• The teams or individuals that have to carry out the task.
• The time required to carry out the task properly.
• The dependence of these different times.
• The technical systems and their associated dynamics.
68
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 80

• The dependence of the different tasks.
• Inﬂuence factors (e.g. skill, stress, and fatigue).
• Recovery factors for all the different tasks.
• The error type.
• The available total time for diagnosis and execution of a task correctly (i.e. total
time window for action).
• The working media or the man–machine interface.
• Demands of cognition and action, the level of experience, and perception.
Additional information on the above information requirements is available in
Ref. [13].
Eight of the above nine HRA methods are described below, separately, and the
information on the remaining method (i.e. JHEDI) is available in Ref. [14].
5.4.1 A Technique for Human Event Analysis
This is a post-incident HRA method, and it was developed by the USNRC [15, 16].
Following were the main reasons to develop ATHEANA [14]:
• In understanding human error, the accident record and advances in behavioural
sciences both clearly supported a stronger focus on the contextual factors,
particularly plant conditions.
• Advances made in the area of psychology were integrated with the disciplines of
human factors, engineering, and PRA when modelling human failure-related
events.
• Human events modelled in earlier human reliability assessment/PRA models
were considered to be inconsistent with the degree of roles that human operators
have played in operational events.
Seven basic steps to the ATHEANA methodology are as follows [16, 17]:
• Step 1: Deﬁne and interpret with care the issue under consideration.
• Step 2: Deﬁne and detail the required scope of the analysis.
• Step 3: Describe with care the base-case scenario including the norm of operations within the environments, considering procedures and actions.
• Step 4: Deﬁne human failure events and/or unsafe actions which may effect the
task under consideration.
• Step 5: Categorize the identiﬁed human failure events under two basic groups:
safe and unsafe actions. An unsafe action may simply be described as an action
in which the human operator in question may fail to perform a speciﬁed task or
performs it incorrectly that in turn results in the unsafe operation of the system.
• Step 6: Search with care for any deviations from the base-case scenario with
respect to any divergence in the general environmental operating behaviour in
the context of the situational scenario.
• Step 7: Preparation for applying ATHEANA.
5.4
Human Reliability Analysis Methods
69

---


### Page 81

In ATHEANA, the probability of human failure event occurring is expressed by
the following equation [9]:
Phfe ¼ Pefe Pusa Pnp
ð5:1Þ
where
Phfe
is the probability of human failure event occurrence
Pefe
is the probability of error-forcing context
Pusa
is the probability of unsafe action in the error-forcing context
Pnp
is the probability of non-recovery in the error-forcing context and given the
occurrence of the unsafe action as well as the existence of additional
evidence following the unsafe action.
There are many beneﬁts and drawbacks of ATHEANA. Some of these are
presented below, separately.
Beneﬁts
• It increases the chances that the key risks concerning the human failure events in
question have been identiﬁed.
• In comparison with many other HRA methods, it provides a much better and
more holistic understanding of the context concerning the human factors known
to be the cause of the incident.
• In comparison with many other HRA quantiﬁcation methods, it allows for the
consideration of a much wider range of performance shaping factors, as well as
it does not require that these factors to be treated as independent.
• The methodology of this method makes it possible to estimate human error
probabilities considering a variety of differing factors and combinations.
Drawbacks
• It fails to prioritize or establish details of the causal relationships between the
types of human factors contributing to an incident.
• Another drawback of this method is that, from a probability risk assessment
stance, there is no human error probability generated.
5.4.2 Cognitive Reliability and Error Analysis Method
This is a bidirectional analysis method that can be used for both accident analysis
and performance prediction. It puts emphasis on the analysis of human actions’
causes, i.e. human cognitive activities [9]. The basis for the method is the classiﬁcation schemes of error modes and of various components of the organization,
technology, and human triad, which incorporates organization-associated factors,
technology-associated factors, and human-associated factors.
70
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 82

The main objective of using this methodology is to assist analysts in the following four areas [18]:
• Area I: Highlight tasks, work, or actions within the system boundaries which
necessitate or essentially depend on a range of human thinking and which are
therefore quite vulnerable to variations in their reliability level.
• Area II: Highlight the surrounding environments in which the cognition of these
conditions may be lowered and therefore determine what type of actions may
lead to a probable risk.
• Area III: Compile an evaluation from the assessment of the various types of
human performance-related outcomes as well as their effect on system safety. In
turn, this can be used as part of the probability risk assessment.
• Area IV: Make appropriate suggestions/recommendations as to how highlighted
error generating conditions may be improved to a certain degree and how the
reliability of system can be improved while also lowering risk.
The generic cognitive function failure types used in CREAM are shown in
Fig. 5.3 [9].
‘‘Interpretation errors’’ include items such as faulty diagnosis (i.e. either an
incorrect diagnosis or an incomplete diagnosis), delayed interpretation (i.e. not
made in time), and decision error (i.e. either not making a decision or making an
incorrect or incomplete decision). ‘‘Observation errors’’ include items such as
observation of incorrect object (i.e. a response is given to the incorrect event or
stimulus) and observation not made (i.e. overlooking a signal or a measurement).
Cognitive function 
failures types 
Planning 
errors 
Interpretation 
errors 
Observation 
errors 
Execution 
errors 
Fig. 5.3 Generic cognitive function failure types used in CREAM
5.4
Human Reliability Analysis Methods
71

---


### Page 83

‘‘Execution errors’’ include items such as action performed at wrong time (i.e.
either too late or too early), action of wrong type performed with respect to
distance, speed, force, or direction; action performed out of sequence, and action
missed. Finally, ‘‘Planning errors’’ include items such as priority error (i.e.
selecting the wrong goal) and inadequate plan formulated (i.e. plan is either
incomplete or directly wrong).
Some of the main beneﬁts and drawbacks of CREAM are as follows [19]:
Beneﬁts
• It is well structured, concise, and follows a well laid out system of procedure.
• It permits for the direct quantiﬁcation of human error probability.
• It uses the same principles for predictive and retrospective analyses.
Drawbacks
• It needs a quite high level of resource use, including fairly lengthy time periods
for completion.
• It fails to put forth potential means by which the highlighted errors can be cut
down.
5.4.3 Technique for Human Error Rate Prediction
This method is used in the area of human reliability assessment/analysis to evaluate the probability of a human error occurring throughout the completion of a
certain task. The method was developed at the Sandia Laboratories for the US
Nuclear Regulatory Commission [20] and was the ﬁrst method in human reliability
assessment to come into broad use. It is based upon both plant data and expert
judgements; thus, it relies on a large human reliability database that contains
human error probabilities.
THERP is a total methodology to assess human reliability that clearly deals
with task analyses (e.g. walk/talk through and documentation reviews), error
representation and identiﬁcation, and quantiﬁcation of human error probabilities
[21]. The key elements for completing the quantiﬁcation process are decomposition of tasks into elements, assignment of nominal human error probabilities to
each element, determination of effects of performance shaping factor on each
element, calculation of effects of dependence between tasks, modelling an human
reliability assessment event tree, and quantiﬁcation of total task human error
probability [14, 22].
In order to obtain the overall failure probability, the exact equation involves
summing probabilities of all failure paths in the event tree under consideration.
Some of the beneﬁts and drawbacks of THERP are as follows [7, 21]:
72
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 84

Beneﬁts
• It can be used at all stages of design.
• It has a quite powerful methodology that can easily be audited.
• It is fairly well used in practice.
Drawbacks
• It can be quite time consuming and resource intensive.
• For many assessments, the level of detail included in this method may be quite
excessive.
• It fails to offer proper guidance on modelling scenarios and the performance
shaping factors’ impact on performance.
5.4.4 Success Likelihood Index Method–Multi-Attribute
Utility Decomposition
This method was developed by British researchers as a means of automating some
of the mechanics of the existing success likelihood index method, for the US
Nuclear Regulatory Commission [12, 23]. The method uses paired-comparison
methods under the assumptions that similar tasks are grouped for analysis and
lower and upper bound anchor point human error probabilities are determined for
that group of tasks. Performance shaping factors are rated with respect to their
quality and importance, and analysts’ expert opinions are utilized to choose the
bounding human error probabilities to determine the tasks to be similar enough to
be compared as well as to assess the performance shaping factors.
Nonetheless, the SLIM-MAUD methodology breaks down into the following
seven steps [24]:
• Step 1: Deﬁnition of situations and subsets.
• Step 2: Elicitation of performance shaping factors.
• Step 3: Rating all the tasks on the performance shaping factors.
• Step 4: Ideal point elicitation and scaling calculations.
• Step 5: Independent investigations/checks.
• Step 6: Weighting approach/procedure.
• Step 7: Success likelihood index (SLI) calculation.
It is to be noted that the strength of SLIM-MAUD lies in the paired-comparison
approach that increases the analysis reliability. Furthermore, this method comes
with a set of suggested performance shaping factors, although involved analysts
are quite free to produce their own. Nonetheless, the method is considered
atomistic because of its reliance on performance shaping factors [12].
5.4
Human Reliability Analysis Methods
73

---


### Page 85

5.4.5 Accident Sequence Evaluation Program
This method was designed as a simpliﬁed version to the THERP and its unique
features include the following items [12, 25]:
• A detailed screening procedure for pre- and post-accident tasks.
• Inclusion of recovery factors.
• A simpliﬁed three-level account of dependency.
• Separate human error probabilities for pre- and post-accident tasks.
• Use of tables and software to provide uncertainty bounds.
• Tables to account for the inﬂuence of available time on the error probability.
• Consideration of the role of diagnosis in error and recovery.
The handling of the human error probability characterizes the distinction
between this method (i.e. ASEP) and THERP. More speciﬁcally, ASEP provides
predeﬁned human error probability values, whereas THERP requires the analyst to
calculate the human error probability. This in turn lowers the analysis accuracy to
the advantage of the simplicity and ease of performing the analysis. It is to be
noted that beyond open-ended performance shaping factors, the ASEP method
explicitly accounts for stress, time, immediate response, and procedures. Additional points to be noted with respect to this method are as follows [12]:
• It can be counted as an atomistic method because of the level of proceduralized
detail provided in it.
• Its format is not a worksheet or rubic but rather a checklist procedure.
• The application of lookup tables to perform calculations eliminates any ambiguity in probability assignments to events or in the overall error probability
calculation.
All in all, ASEP is a nuclear speciﬁc tool, and it has been successfully applied
in the nuclear power industrial sector.
5.4.6 Human Cognitive Reliability Model
HCR model/correlation is a method used in human reliability assessment to
evaluate the human error occurrence probability during the completion of a speciﬁc task. The method was developed in the early 1980s, and this method is based
on the premise that the likelihood of success or failure of an operator in a timecritical task is dependent on the cognitive process, used for making the critical
decisions that determine the outcome [26, 27]. Three performance shaping factors
(i.e. stress level, quality of operator/plant interface, and operator experience) also
inﬂuence the average (median) time taken to carry out the task. By combining
these three performance shaping factors enables ‘‘response time’’ curves to be
calibrated and compared to the time available for performing the task.
74
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 86

With the aid of these curves, the involved analyst can then estimate the likelihood that an operator will take the proper measure, as indicated by a given
stimulus (e.g. pressure warning signal), within the framework of available time
window. The basis for the relationship between these normalized times and human
error probabilities is the simulator experimental data.
Some of the main beneﬁts and drawbacks of this method are as follows [24]:
Beneﬁts
• It is quite quick method to perform and is easy to use.
• It explicitly models the time-dependent nature of human reliability assessment.
Drawbacks
• It is highly sensitive to changes in the estimate of the median time.
• It considers only three performance shaping factors.
• The human error probability generated by the method is not complete.
5.4.7 Standardized Plant Analysis Risk–Human Reliability
Analysis
This method was developed at the Idaho National Laboratory to estimate the
probability that an operator will fail when tasked with carrying out a basis event
[12, 28]. The method does the following [14, 28]:
(1) Decomposes probability into contributions from action-related failures and
diagnosis-related failures.
(2) Accounts for the context associated with human failure events with the aid of
performance shaping factors and dependency assignment for adjusting a basecase human error probability
(3) Makes use of pre-deﬁned and base-case human error probabilities and performance shaping factors along with guidance on how to assign the correct
value of the performance shaping factor.
(4) Makes use of a beta distribution for uncertainty analysis.
(5) Makes use of designated worksheets for ensuring analyst consistency.
Furthermore, the method assigns human activity to one of two general task
classiﬁcations: diagnosis or action. Diagnosis tasks consist of reliance on experience and knowledge to comprehend existing situations, determining proper
courses of action, and planning prioritizing activities or actions. Some examples of
action tasks are operating equipment, carrying out testing or calibration, and
starting pumps/machines.
The eight performance shaping factors shown in Fig. 5.4 are accounted for in
the quantiﬁcation process of this method [6, 14, 28].
5.4
Human Reliability Analysis Methods
75

---


### Page 87

A main element of this method is the SPAR-H worksheet, which signiﬁcantly
simpliﬁes the estimation procedure. The worksheet using process varies slightly,
depending on whether the analyst is using the method to conduct a more detailed
HRA, perform event analysis, or build SPAR models.
Some of the beneﬁts and drawbacks of this method are as follows [14, 29]:
Beneﬁts
• The eight performance shaping factors included in the method cover many
situations where more detailed analysis is necessary.
• A simple underlying model makes this method relatively straightforward to use,
and ﬁnal results are easily traceable.
Drawbacks
• The method may not be suitable in situations, where more detailed and realistic
analysis of diagnosis errors is required.
Performance 
shaping 
factors 
Complexity 
Experience 
and training 
Ergonomics 
(including 
the humanmachine 
interface) 
Work 
processes 
Fitness for 
duty 
Available 
time 
Stress and 
stressors 
Procedures 
Fig. 5.4 Performance shaping factors considered in the quantiﬁcation process of SPAR-H
76
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 88

• For detailed analysis, the degree of resolution of the performance shaping
factors may be insufﬁcient.
Additional information on this method is available in Ref. [28].
5.4.8 Human Error Assessment and Reduction Technique
This method is used in the area of human reliability assessment to evaluate the
human error occurrence probability throughout the completion of a certain task. The
method ﬁrst appeared in 1986 and is widely used in the United Kingdom nuclear
industry [14, 22, 30, 31]. The method is based on the following premises [14]:
• Basic human reliability depends on the generic nature of the task to be carried out.
• Under ‘‘perfect’’ situations, this level of reliability will tend to be achieved quite
consistently with a speciﬁed nominal likelihood within probabilistic limits.
• Given that the perfect situations under all circumstances do not exist, the predicted human reliability may degrade as a function of the extent to which
highlighted error producing situations might be applicable.
In this method, 9 generic task types are described, each with an associated
nominal human error occurrence potential, and a total of 38 error generating
conditions that may affect reliability of task, each with a maximum amount by
which the nominal human error occurrence potential can be multiplied. The following three are the key elements of this method [14]:
(1) Categorize the task for analysis into any one of the generic task types as well
as assign the nominal human error occurrence potential to that task.
(2) Make decision which error producing situations may affect reliability of task
and then evaluate/consider the assessed proportion of affect for each and every
error producing situation.
(3) Calculate human error occurrence potential of task.
Some of the beneﬁts and drawbacks of this method are as follows [14, 22, 30, 31]:
Beneﬁts
• It requires relatively limited resources for completing an assessment.
• It is a simple, quick, and versatile human reliability calculation approach, which
also provides the user suggestions to reduce error.
Drawbacks
• It does not include error dependency modelling.
• It lacks information concerning the extent to which tasks should be decomposed
to perform analysis.
• It needs greater clarity of description for assisting users when discriminating
between generic tasks and their related error producing situations.
5.4
Human Reliability Analysis Methods
77

---


### Page 89

5.5 Problems
1. Discuss the issues concerning the incorporation of the HRA integrally into a
PRA.
2. What are the HRA process steps in regard to nuclear power plants?
3. What are the information requirements of THERP, SLIM, HCR, and ASEP
methods?
4. What were the main reasons for developing the ATHEANA method?
5. Compare CREAM and ATHEANA methods.
6. Describe the following two methods:
• ASEP.
• THERP.
7. What are the advantages and disadvantages of the following two methods?
• HCR.
• SPAR-H.
8. What is HEART? Describe it in detail?
9. Compare HEART and ATHEANA methods.
10. What are the beneﬁts and drawbacks of the following two methods?
• THERP.
• CREAM.
References
1. Facts and Figures (2013) Nuclear industry association (NIA). Carlton House, London
2. U.S. Statistics, Institute for Energy Research (IER), Washington, DC, 2013
3. Ryan TG (1988) A task analysis-linked approach for integrating the human factor in
reliability assessments of nuclear power plants. Reliab Eng Syst Saf 22:219–234
4. Trager TA (1985) Case study report on loss of safety system function events, Report No.
AEOD/C504, U.S. Nuclear Regulatory Commission, Washington, DC, 1985
5. IEEE Guide for Incorporating Human Action Reliability Analysis for Nuclear Power
Generating Stations, IEEE Std 1082–1997, Institute of Electrical and Electronics Engineers
(IEEE), New York, 1997
6. Spurgin AJ, Lydell BOY (2002) Critique of current human reliability analysis methods. In:
Proceedings of the IEEE seventh conference on human factors and power plants,
pp 3.12–3.18
7. Strater O, Bubb H (1999) Assessment of human reliability based on evaluation of plant
experience: requirements and implementation. Reliab Eng Syst Saf 63:199–219
8. Laux L, Plott C (2007) Using operator workload data to inform human reliability analyses.
In: Proceedings of the joint 8th IEEE HFPP/13th HPRCT conference, pp 309–312
9. Kim IS (2001) Human reliability analysis in the man–machine interface design review. Ann
Nucl Energy 28:1069–1081
10. Ryan TG (1988) A task analysis-linked approach for integrating the human factor in
reliability assessments of nuclear power plants. Reliab Eng Syst Saf 22:219–234
78
5
Speciﬁc Human Reliability Analysis Methods for Nuclear Power Plants

---


### Page 90

11. Boring RL (2006) Modeling human reliability analysis using MIDAS. In: Proceedings of the
5th international topical meeting on nuclear plant instrumentation, controls, and human
machine interface technology, pp 1270–1274
12. Boring RL, Gertman DI, Joe JC, Marble JL (2005) Human reliability analysis in the U.S.
nuclear power industry: a comparison of atomistic and holistic methods. In: Proceedings of
the human factors and ergonomics society 49th annual meeting, pp 1815–1819
13. Human Error Classiﬁcation and Data Collection, Report No. IAEA.TECDOC 538,
International Atomic Energy Agency (IAEA), Vienna, Austria, 1990
14. Bell J, Holroyd J (2009) Review of human reliability assessment methods, Report No.
RR679, Health and Safety Laboratory, Buxton, UK, 2009
15. Cooper SE et al. (1996) A technique for human event analysis (ATHEANA)-technical basis
and methodological description, Report No. NUREG/CR- 6350, U.S. Nuclear Regulatory
Commission, Brookhaven National Laboratory, Upton, New York, April 1996
16. Technical Basis and Implementation Guide-lines for a Technique for Human Event Analysis
(ATHEANA),
Report
No.
NUREG-1624,
U.S.
Nuclear
Regulatory
Commission,
Washington, DC, May 2000
17. Forester J et al (2004) Expert elicitation approach for performing ATHEANA quantiﬁcation.
Reliab Eng Syst Saf 83:207–220
18. Hollnagel E (1998) Cognitive reliability and error analysis method-CREAM. Elsevier
Science, Oxford
19. Stanton NA, Salmon PM et al (2005) Human factors methods: a practical guide for
engineering and design. Ashgate Publishing, Aldershot
20. Swain AD, Guttmann HE (1983) Handbook of Human Reliability Analysis with Emphasis on
Nuclear Power Plant Applications, Report No. NUREG/CR- 1278, US Nuclear Regulatory
Commission, Washington, DC, 1983
21. Kirwin B (1994) A guide to practical human reliability assessment. CRC Press, Boca Raton
22. Kirwan B et al (1997) The validation of three human reliability quantiﬁcation techniques,
THERP, HEART, and JHEDI: Part II-results of validation exercise. Appl Ergon 28(1):17–25
23. Embrey DE et al. (1984) SLIM-MAUD: an approach to assessing human error probabilities
using unstructured expert judgement, volume I: overview of SLIM-MAUD, Report No.
NUREG/CR-3518, US Nuclear Regulatory Commission, Washington, DC, 1984
24. Humphreys P (ed) (1995) Human reliability assessor’s guide. AEA Technology, London
25. Swain AD (1987) Accident sequence evaluation program human reliability analysis
procedure,
Report
No.
NUREG/CR-4772,
US
Nuclear
Regulatory
Commission,
Washington, DC, 1987
26. Hannaman GW, Spurgin AJ, Lukic YD (1984) Human cognitive reliability model for PRA
analysis, Draft Report No. NUS-4531, EPRI Project No. RP2170-3, Electric Power and
Research Institute, Palo Alto, California, 1984
27. Rasmussen J (1983) Skills, rules, knowledge, signals, signs, and symbols and other
distinctions in human performance models. IEEE Trans Syst Man Cybern 13(3):257–266
28. Gertman D et al. (2004) The SPAR-H human reliability method, Report No. NUREG/CR6883, US Nuclear Regulatory Commission, Washington, DC
29. Forester J et al. (2006) Evaluation of analysis methods against good practices, Report No.
NUREG-1842, US Nuclear Regulatory Commission, Washington, DC, 2006
30. Kirwan B (1996) The validation of three human reliability quantiﬁcation techniques, THERP,
HEART, and JHEDI: part I-techniques descriptions and validation issues. Appl Ergon
27(6):359–373
31. Kirwan B et al (1997) The validation of three human reliability quantiﬁcation techniques,
THERP, HEART, and JHEDI: part III-practical aspects of the usage of the techniques. Appl
Ergon 28(1):27–39
References
79

---


### Page 91

Chapter 6
Human Factors in Power Generation
6.1 Introduction
A modern large electrical power plant, powered by fossil fuels, hydro, nuclear
energy, etc., may simply be called a complex human–machine system that controls
a thermodynamic process employed for generating electricity. The machine aspect
of the system is a rather sophisticated arrangement of software and hardware
elements that are generally highly reliable and redundant. The human aspect of the
system is a fairly large sociotechnological organization with engineering, management, training, operations, and maintenance manpower.
Needless to say, human factors play an important role in power generation.
Although human factors became an important element in defence equipment
design and development in the late 1950s and 1960s, in the area of power generation, it was not until the mid-1970s when the nuclear plants were designed
using human factors analytical techniques or design standards [1]. More speciﬁcally, the nuclear power industrial sector used exactly the same engineering
techniques that had been developed over the past ﬁve decades in designing fossil
fuel and hydro power plants [1–3].
This chapter presents various important aspects of human factors, directly or
indirectly, concerned with power generation.
6.2 Human Factors Engineering Design Goals
and Responsibilities
There are many human factors engineering design goals with respect to power
generation systems. Some of the main ones are as follows [4]:
• The plant design and allocation of all types of functions will clearly support
operation vigilance and provide acceptable levels of workload (i.e. to minimize
periods of operator overload and underload).
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_6,
 Springer International Publishing Switzerland 2014
81

---


### Page 92

• All personnel tasks can be performed within speciﬁed time and performance
criteria.
• The operator interfaces will minimize operator-related errors and will clearly
provide for error detection and recovery capability.
• The human–system interfaces, procedures, stafﬁng/qualiﬁcations, training, and
management and organizational support will clearly support a rather high degree
of situation awareness.
The personnel responsible for human factors engineering within a power generation organization have many responsibilities. The important ones are as follows [4]:
• Developing human factors engineering-related procedures and plans.
• Verifying the implementation of team recommendations.
• Assuring that human factors engineering-related activities comply with the
human factors engineering-related procedures and plans.
• Oversight and review of human factors engineering-related design, development, test, and evaluation-associated activities.
• Scheduling human factors engineering-related activities and milestones with
respect to other modiﬁcation activities.
• Initiation, recommendation, and provision of appropriate solutions through all
designated channels for problems or difﬁculties highlighted during the implementation process of the human factors engineering-related activities.
6.3 Human Factors Issues in Ageing Power Plants
Humans play an important role in the effects of ageing on nuclear plants’ safe and
reliable operation. Thus, human factors issues may be more important than the
issues concerned with component and materials degradation with age as human
actions can decelerate or accelerate physical ageing of a power plant. These human
factors issues can be categorized under six classiﬁcations as shown in Fig. 6.1 [5].
These classiﬁcations are management, maintenance, stafﬁng, training, man–
machine interface, and procedures.
As per past experiences [6], management impacts basically all facets of power
plant performance including technical support, design, construction and modiﬁcation, maintenance, and operations. There are many management-related issues
that may arise in ageing power plants. Some of these, directly or indirectly, are
difﬁculties in attracting and retaining good managers, lack of interest by top
management, and tendency to delay decisions as long as possible [7].
Maintenance is another area which will impact and be impacted by ageing
power plants. Some of the human factors-related issues belonging to this area are
new maintenance staff may not be adequately trained in the technology that exists
in ageing plants, loss in ﬂexibility to transfer maintenance staff to other plants
because of signiﬁcant technological differences between old and new plants, and
82
6
Human Factors in Power Generation

---


### Page 93

increment in dose rates will make maintenance more difﬁcult in certain areas of
older plants [5]. Stafﬁng-related issues in plant ageing are concerned with the
ability to attract and retain good people for older power plants, particularly in areas
such as operation and technical support.
The remaining three classiﬁcation issues (i.e. training, man–machine interface,
and procedures) are considered self-explanatory, but the information on these
issued is available in Ref. [5].
6.4 Human Factors Issues that Can have Positive Impact
on Nuclear Power Plant Decommissioning
Currently, there are around 435 nuclear reactors operating worldwide and about 57
of these reactors are in the process of decommissioning [8, 9]. It is estimated that
the decommissioning of these reactors will cost billions of dollars to the world
economy. For example, the estimated cost of decommissioning 19 reactors currently operating in the United Kingdom alone is over 70 billion pounds (i.e. over
$100 billion dollars) [8].
Needless to say, much less is known or clearly understood regarding human
factors that are crucial to, and can quite signiﬁcantly affect, the success of the
nuclear power plant decommissioning process [8, 10]. Nonetheless, some past
experiences of decommissioning clearly indicate that, aside from technical challenges, there are many organizational and human factors that also need to be
addressed with care [11, 12]. Four human factors issues that can have the most
positive impact upon safe and successful decommissioning of power plants are
shown in Fig. 6.2 [8].
Uncertainty about the future can affect decommissioning because of subsequent
impact it can have on staff morale and motivation. Uncertainty to a certain degree
is to be expected when decision is made to shut down and decommission a power
Classifications 
Staffing 
Man-machine 
interface 
Maintenance 
Management 
Training 
Procedures 
Fig. 6.1 Classiﬁcations of
human factors issues in
ageing nuclear power plants
6.3
Human Factors Issues
83

---


### Page 94

plant because to most plant staff members, decommissioning will be an entirely
new phenomenon [8]. Furthermore, uncertainty can manifest itself in many different ways including reducing the involved staff morale, motivation, and commitment to the plant.
The most effective approach to manage uncertainty is reducing it to minimum
[13]. This can be accomplished by developing an appropriate communication
strategy whereby accurate and regular information is provided to all concerned
staff members regarding future plans for decommissioning and the plant. It is to be
noted that the communication process should be interactive to allow all concerned
staff members to raise enquiries and have them properly resolved in a timely
fashion. Furthermore, inviting key staff members to get involved in planning and
preparing process for decommissioning can also be helpful to increase staff
members’ morale and ‘‘buy-in’’ to the overall process [14].
Maintaining adequate competence for decommissioning is another key human
factors issue that can have the most signiﬁcant impact upon safe and successful
decommissioning and is composed of following three stages [8]:
• Stage I: This stage is concerned with initial decommissioning and includes
defueling and removal of all non-ﬁxed contaminated parts and readily removable equipment.
• Stage II: This stage is concerned with decontamination and dismantling of
contaminated and other internal equipment.
• Stage III: This stage is concerned with demolition of those structures and
buildings that are no longer needed.
Each of the above three stages will need different skills and knowledge of the
power plant as well as of the technologies and tools to be employed and thus a
different workforce proﬁle. It simply means that during the entire decommissioning process, a signiﬁcant training program will need to be developed to satisfy
Issues 
Maintaining safety 
culture 
Retaining 
organizational 
memory 
Maintaining adequate 
competence for 
decommissioning 
Uncertainty about the 
future 
Fig. 6.2 Human factors issues that can have most positive impact upon safe and successful
decommissioning of nuclear power plants
84
6
Human Factors in Power Generation

---


### Page 95

the training needs of managers, staff members, and involved contractors. Therefore, it is essential that appropriate training strategies are developed right at the
planning stage so that required number of trainers are retained to develop and
deliver training plans during the decommissioning process.
Safety culture is fundamental to the nuclear industrial sector, and the importance of its positive maintenance is an established element of daily regime of each
and every nuclear power plant. Uncertainty and the loss of key staff members can
have a profound impact on the safety culture of staff members left behind. As
existing safety defences, processes, and procedures may no longer be effective, the
following actions could be quite useful to maintain a positive safety culture during
the decommissioning process [8, 11, 14, 15]:
• Re-evaluate safety culture indicators throughout the decommissioning process
to reﬂect new and changing activities, environments, and risks as well as to
ensure accurate measurement of safety culture.
• Provide feedback on performance to all involved workers on a regular basis to
encourage morale and motivation and to highlight and raise awareness of possible risks.
• Emphasize the importance of workers’ contribution with respect to safe and
efﬁcient decommissioning.
• Present decommissioning to all involved workers as a good opportunity for their
future career development rather than a threat to their future employment.
Finally, in regard to ‘‘retaining organizational memory’’, human factors issue
decommissioning requires accurate and clear knowledge of the plant history and
operations including any modiﬁcations to the plant design. Most of this type of
information can be retrieved from the plant documentation such as drawings,
procedures, and event reports. Thus, it is very important to perform a documentation audit as soon as possible to ﬁnd out what documentation is available and the
accuracy of the information contained in the documentation. This type of information should be catalogued and stored in such a way so that it is easily accessible
to all concerned personnel.
The knowledge held by experienced staff personnel may not have been documented through any formal processes or procedures. Because of uncertainty about
the future, there is a considerable risk of losing these key personnel in the initial
stages of planning for decommissioning. Therefore, it is very important, as soon as
possible prior to the closure of the plant, to identify key roles for decommissioning
and to develop relevant strategies to retain the key staff personnel for these roles.
An example of these strategies is raising the proﬁle of the role for making it more
attractive, providing job security for a time period or even employing these key
personnel on a part-time basis.
Additional information on the above four human factors issues is available in
Ref. [8].
6.4
Human Factors Issues that Can have Positive Impact
85

---


### Page 96

6.5 Human Factors Review Guide for Next-Generation
Reactors and Guidance Documents for Human Factors
In 1994, the United States Nuclear Regulatory Commission (NRC) developed a
document (NUREG-0711) entitled ‘‘Human Factors Engineering Program Review
Model’’ [16] to basically serve as a human factors guide for next generation of
reactors [17]. The document described background, objective, applicant submittals, and review criteria for the ten human factors engineering elements shown in
Fig. 6.3 [17].
The following inputs are considered useful with respect to each of the human
factors engineering elements shown in Fig. 6.3 [17]:
Human Factors Engineering Program Management
• All applicants should submit the appropriate human factors engineering program
plan for review by the concerned regulatory institutes.
• Human factors engineering-related tasks, organization, and relationships among
these tasks should be reviewed with care.
• As human factors engineering issue tracking is a very important task in the
human factors engineering program, issue selection criteria, issue management
and handling procedures, and issue analysis approaches must be described in
appropriate detail.
Operating Experience Review
• Important issues in the operation of earlier power plants must be analysed with
care, and the results must be reﬂected in the design under consideration.
• As near-miss cases can provide information as important as that of plant events,
it is considered essential to include the analysis of near-miss cases into the
operating experience review.
Functional Requirement Analysis and Function Allocation
• Ensure that functional requirement analysis is performed to the level with which
function allocation can be performed effectively.
• In addition to identifying functions important to safety, other general functions
should also be included in the analysis to reﬂect the results of functional
requirement analysis to the design.
Task Analysis
• Ensure that documentation clearly shows all types of relationships between task
analysis and functional requirement analysis and function allocation results.
• Consider seriously, during the task analysis process, the tasks expected to face
changes.
86
6
Human Factors in Power Generation

---


### Page 97

Procedure Development
• Ensure that interface with other information displays and controls is quite
efﬁcient to enhance operator performance and not to induce human errors.
• Ensure that guidelines for modiﬁcation, management, and validation of procedures are developed when using computerized procedures.
Human–System Interface Design
• Perform human–system interface evaluation independent of the human factors
veriﬁcation and validation.
• Ensure that the task analysis results are clearly reﬂected in human–system
interface designs.
Human Factors Veriﬁcation and Validation
• Make use of the United States NRC document entitled ‘‘Integrated System
Validation: Methodology and Review Criteria’’ [18] for this element.
Human Reliability Analysis
• Ensure that a clear deﬁnition of data input–output between the human factors
engineering design team and probabilistic risk analysis team is properly
described.
Elements 
Human factors 
engineering program 
management 
Human factors 
verification and 
validation 
Functional 
requirements analysis 
and function allocation 
Operating experience 
review 
Training program 
development 
Human-system 
interface design 
Procedure 
development 
Human reliability 
analysis 
Staffing 
Task analysis 
Fig. 6.3 Ten human factors engineering elements
6.5
Human Factors Review Guide for Next-Generation Reactors
87

---


### Page 98

• Ensure that the design-related data from probabilistic risk analysis required by
the human factors engineering design team are properly identiﬁed and interactions between probabilistic risk analysis team and the human factors engineering
design team are clearly described.
Training Program Development
• Ensure that all types of training requirements are clearly identiﬁed during the
design phase.
Stafﬁng
• Because of the changes in human–system interface design and resulting personnel tasks, ensure that stafﬁng analysis is performed with care.
6.5.1 Guidance Documents for Human Factors
There are many guidance documents for human factors that can, directly or
indirectly, be used in the area of power generation. Three of these documents
produced by the United States NRC to ensure that personnel performance and
reliability are appropriately supported in nuclear power plants are NUREG-0800,
NUREG-0711, and NUREG-0700 [19]. NUREG-0800 provides a high-level
review framework for performing human factors engineering reviews [20]. The
updated versions (i.e. Rev. 1 and Rev. 2) of NUREG-0711 and NUREG-0700,
respectively, are described below, separately [19].
NUREG-0711 (Rev. 1)
The original version of this document was described earlier. This version addresses
both new control room designs and control room modernization issues. In addition,
the version includes two more human factors engineering review elements. More
speciﬁcally, two more elements in addition to the ten elements are shown in
Fig. 6.3. The new elements are human performance monitoring and design
implementation.
Human performance monitoring is concerned with providing guidance to assure
that a human performance monitoring strategy is in place so that no major safetyrelated degradation occurs when changes are made in the plant as well as providing proper assurance that all conclusions drawn from the evaluation remain
valid over time period. Design implementation is concerned with addressing the
manner in which changes are carried out to control rooms and human–system
interfaces. Furthermore, the guidance particularly focuses on review of the
implementation of all plant changes so that their resulting effects on personnel
performance are considered properly.
Some of the human factors engineering elements in Fig. 6.3 that have changed
quite signiﬁcantly in this version are as follows [19]:
88
6
Human Factors in Power Generation

---


### Page 99

• Human–system interface design.
• Human factors veriﬁcation and validation.
• Functional requirements analysis and allocation.
• Human reliability analysis.
NUREG-0700 (Rev. 2)
The ﬁrst version of this document (i.e. NUREG-0700) provides the guidelines for
reviewing the human factors engineering aspects of human–system interface
technology such as control room design, information systems, controls, and alarms
[19]. The ﬁrst revision of this document (i.e. NUREG-0700, Rev. 1) [20] addressed
the ‘‘gaps’’ in the criteria. The second revision of the document (i.e. NUREG0700, Rev. 2) has changed quite considerably from the ﬁrst revision (i.e. NUREG0700, Rev. 1) because human–system interface characterizations have been added
to each major section. A characterization may simply be described as a description
of the functions and characteristics of the human–system interface topic area that
is crucial to human performance.
Nonetheless, the new guidance addresses the eight different aspects of human–
system interface design shown in Fig. 6.4 [19]. The human factors engineering
guidelines in the guidance are divided into four basic parts as follows [19]:
• Part I This part contains guidelines for three basic human–system interface
elements: controls, information displays, and user–interface interaction and
management. In turn, the elements are utilized as building blocks for developing
human–system interface systems to serve certain functions.
• Part II This part contains the guidelines to review soft control system, alarm
system, communication system, safety function and parameter monitoring system, computerized operator support system, group-view display system, and
computer-based procedure system.
• Part III This part contains guidelines for reviewing workstations and workplaces. Workstations, including panels and consoles, are locations where
human–system interfaces are integrated together for providing an area where
plant staff/personnel can carry out their assigned tasks. Furthermore, workstations are situated at workplaces such as remote shutdown facilities and the main
control room.
• Part IV This part contains guidelines for reviewing the human–system interface
support, i.e. maintaining digital systems.
Additional information on NUREG-0700, Rev. 2, is available in Ref. [19].
6.6 Potential Human Factors Engineering Application
Areas and Expected Problems
Some of the potential human factors engineering application areas with respect to
power generation are as follows [21]:
6.5
Human Factors Review Guide for Next-Generation Reactors
89

---


### Page 100

• Greater application of human factors engineering principles to operations and
maintenance of non-nuclear power plants.
• Assessing and understanding organizational factors’ inﬂuence on safety.
• Extension of all successful human–system interface programs and technologies
to human–system interfaces out in the power plant (i.e. outside the power plant’s
control room).
• Assessing and understanding deregulation’s inﬂuence on safety.
• Focus on crew and individual performance assessment as well as on unplanned
and unexpected events’ management.
• Improving data collection and analysis approaches, including event reporting
and human reliability analysis.
• Assessing and understanding decommissioning’s human factors engineering
aspects.
• Improvement of operations and maintenance design.
Some of the human factors engineering application-related problems in the area
of power generation to be faced and overcome are as follows [21]:
• Lack of proper standardization in the methodology and application of human
factors analytical procedures such as task analysis, function allocations, human
Aspects
Soft controls 
Alarm 
Systems 
Control room 
and work 
place 
environment 
Information 
design and 
organization 
Group view 
displays 
Interface 
management 
and 
navigation 
Digital 
system 
maintenance 
Computerbased 
procedures 
Fig. 6.4 The aspects of human–system interface design addressed by the document: NUREG0700, Rev. 2
90
6
Human Factors in Power Generation

---


### Page 101

reliability analysis, and functional requirements used during the design and
development process/phase.
• Tendency to focus intensively on human factors after the occurrence of near
disaster or catastrophe.
• Tendency of some power industry management personnel to regard the necessity for human factors in terms of a temporary ‘‘magic bullet’’ to be used,
primarily after the occurrence of a serious problem, rather than establishing
proper systematic mechanisms to address such concerns in terms of constant
proper preventive measures.
• Difﬁculty in recruiting and training resources and top talent in the area of human
factors because some people consider nuclear power, particularly in North
America, to be a dying industry.
6.7 Problems
1. Write an essay on human factors in power generation with emphasis on historical developments.
2. List at least ﬁve important responsibilities of personnel responsible for human
factors engineering within a power generation organization.
3. Discuss human factors issues in ageing power plants.
4. Discuss human factors issues that can have most positive impact upon safe and
successful decommissioning of nuclear power plants.
5. What are the actions that could be useful to maintain a positive safety culture
during the power plant decommissioning process?
6. What are the ten human factors engineering elements in the United States
NRC document: NUREG-0711?
7. Describe the United States NRC document: NUREG-0700 (Rev. 2).
8. What are the potential human factors engineering application areas with
respect to power generation?
9. What are the human factors engineering application-related problems in the
area of power generation to be faced and overcome?
10. Describe the United States NRC document: NUREG-0711 (Rev. 1).
References
1. Parsons SD, Seminara JL (2000) Power systems human factors/ergonomics activities in the
United States. In: Proceedings of the IEA/HFEA Congress, pp 3.807–3.810
2. Parsons SO, Eckert SK, Seminara JL (1978) Human factors design practices for nuclear
power plant control rooms. In: Proceedings of the human factors society annual meeting,
pp 133–139
6.6
Potential Human Factors Engineering Application Areas and Expected Problems
91

---


### Page 102

3. Seminara JL, Parsons SO (1980) Survey of control-room design practices with respect to
human factors engineering. Nucl Saf 21(5):603–617
4. Hill D, Alvarado R, Heinz M, Fink B, Naser J (2004) Integration of human factors
engineering into the design change process. In: Proceedings of the American nuclear society
international topical meeting on nuclear plant instrumentation, controls, and human–machine
interface technologies, pp 1–10
5. Widrig RD (1985) Human factors: a major issue in plant aging. In: Proceedings of the
international conference on nuclear power plant aging, availability factor, and reliability,
pp 65–68
6. Osborn R et al (1983) Organizational analysis and safety for utilities with nuclear power
plants. Report No. NUREG/CR-3215, United States Nuclear Regulatory Commission,
Washington, D.C
7. Child J, Kieser A (1981) Development of organizations overtime. In: Nystrom P, Starbuck W
(eds) Handbook of organizational design. Oxford University Press, New York, pp 28–64
8. Blackett C (2008) The role of human factors in planning for nuclear power plant
decommissioning. In: Proceedings of the 3rd IET international conference on system safety,
pp 1–6
9. ‘‘Nuclear power reactors in the world’’. IAEA 2007 Edition, International Atomic Energy
Agency (IAEA), Vienna, Austria, June 2007
10. ‘‘Organization and management for decommissioning of large nuclear facilities’’. IAEA
Technical Reports Series No. 399, International Atomic Energy Agency (IAEA), Vienna,
Austria, December 2000
11. ‘‘Planning, managing, and organizing the decommissioning of nuclear facilities: lessons
learned’’. Report No. IAEA-TECDOC-1394, International Atomic Energy Agency, Vienna,
Austria, May 2004
12. Durbin NE, Melber B, Lekberg A (2001) Decommissioning: regulatory activities and
identiﬁcation of key organizational and human factors safety issues. SKI Report No. 01:43,
Swedish Nuclear Power Inspectorate, Stockholm, Sweden, Dec 2001
13. Durbin NE, Lekberg A, Melber BD (2001) Potential effects of organizational uncertainty on
safety. SKI Report No. 01:42, Swedish Nuclear Power Inspectorate, Stockholm, Sweden, Dec
2001
14. ‘‘Managing change in nuclear facilities’’. Report No. IAEA-TECDOC-1226, International
Atomic Energy Agency (IAEA), Vienna, Austria, July 2001
15. ‘‘Managing the socio economic impact of the decommissioning of nuclear facilities’’. IAEA
Technical Reports Series No. 464, International Atomic Energy Agency, Vienna, Austria,
April 2008
16. ‘‘Human factors engineering program review model’’. Report No. NUREG-0711. U.S.
Nuclear Regulatory Commission, Washington, D.C (1994)
17. Lee JW et al (1999) Human factors review guide for Korean next generation reactor,
Transactions of the 15th conference on structural mechanics in reactor technology, pp XI353–XI-360
18. O’Hara J, Stubler J, Higgins J, Brown W (1997) Integrated system validation: methodology
and review criteria. Report No. NUREG/CR-6393, U.S. Nuclear Regulatory Commission,
Washington, D.C
19. O’Hara JM et al (2002) Updating the NRC’s guidance for human factors engineering reviews.
In: Proceedings of the IEEE 7th human factors meeting, pp 4.22–4.27
20. ‘‘Standard review plan’’. Report No. NUREG-0800, U.S. Nuclear Regulatory Commission,
Washington, D.C., 1996
21. Parsons SO, Seminara JL, O’Hara JM (2000) Power systems human factors/ergonomics
activities in the United States. In: Proceedings of the IEA/HFES Congress, pp 3-807–3-810
92
6
Human Factors in Power Generation

---


### Page 103

Chapter 7
Human Error in Power Generation
7.1 Introduction
Generally, good design, through sound quality assurance, installation, and operation and maintenance programs provide the basic foundation for power plants’
safe and reliable operations. Nonetheless, humans play an important role during
design, production, operation, and maintenance phases of systems used in power
plants. Although the degree of role of humans may vary quite considerably from
one phase to another, their interactions are subject to deterioration because of the
occurrence of human error.
A study performed by one utility indicates that failures occurring due to human
error were roughly two and a half times higher than those attributed to hardware
failures [1]. The occurrence of human error in power generation can be quite
catastrophic. Two examples are the Three Mile Island and Chernobyl nuclear
power station accidents in the United States and Ukraine, respectively. Both these
accidents that occurred on March 28, 1979, and on April 26, 1986, respectively,
were, directly or indirectly, the result of human error [2].
This chapter presents various important aspects of human error in power
generation.
7.2 Facts, Figures, and Examples
Some of the facts, ﬁgures, and examples directly or indirectly concerned with the
occurrence of human error in power generation are as follows:
• During the period 1990–1994, around 27 % of the commercial nuclear power
plant outages in the United States were the result of human error [1].
• As per Ref. [3], a study by the United States Nuclear Regulatory Commission
(NRC) of Licensee Event Reports reported that around 65 % of nuclear system
failures involve human error [4].
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_7,
 Springer International Publishing Switzerland 2014
93

---


### Page 104

• As per Ref. [5], during the period 1969–1986, 54 % of the incidents due to
human errors in Japan resulted in automatic shutdown of nuclear reactors and
15 % of that resulted in power reduction.
• As per Refs. [6, 7], about 70 % of nuclear power plant operation errors appear to
have a human factors origin.
• A study of 255 shutdowns that occurred in Korean nuclear power plants during the
period 1978–1992 reported that 77 of these shutdowns were human-induced [8, 9].
• As per Ref. [2], in 1979, Three Mile Island nuclear power plant accident in the
United States was the result of human-related problems.
• In 1986, Chernobyl nuclear power plant accident in Ukraine, widely regarded as
the worst accident in the history of nuclear power, was also the result of humanrelated problems [2].
• A study of 143 occurrences of operating US commercial nuclear power plants
during the period from February 1975 to April 1975, revealed that about 20 %
of the occurrences were due to operator errors [10, 11].
• As per Ref. [12], the major incident/accident reports of nuclear power plants in
Korea indicate that about 20 % of the total events occur due to human error.
• As per Refs. [6, 13], operation error associated with control centres in fossilﬁred steam generating power plants in the United States could result in upto
3.85 % of plants’ unavailability.
7.3 Major Factors for Human Errors and Their
Occurrence Preventions
There are many major factors for the occurrence of human errors/accidents in the
industrial sector including power generation. Eleven of these major factors along
with their corresponding preventive measures with respect to an individual (in
parentheses) are as follows [14–16]:
• Performing tasks too fast (Avoid operating equipment when you are tense,
tired, or do not feel well).
• Taking chances and high risks (Avoid ‘‘showing off’’ or thinking that an
accident cannot occur).
• Faulty equipment (Check equipment on regular basis).
• Sleeplessness and fatigue (Take breaks as considered appropriate to prevent
fatigue).
• Extreme cold or heat (Perform inside tasks/jobs or minimize exposure to
extreme temperatures as much as possible).
• Poor skill (Read instruction manuals with care and get some skilled individual
in the area to help you).
• Medication, drugs, and alcohol (Avoid operating equipment/machines or
performing dangerous tasks if you are on some form of drugs, taking medication, or have been drinking).
94
7
Human Error in Power Generation

---


### Page 105

• Panic in an emergency situation (Learn ﬁrst aid so you know exactly what
action to take).
• Let-down from low blood sugar and hunger (Take fructose tablets or eat
appropriate snacks to ﬁght let-down).
• Emotional upsets and anger (Take time to calm down to normal level).
• Daydreaming and not concentrating (Vary routine to ﬁght monotony as
appropriate).
7.4 Occurrences Caused by Operator Errors During
Operation and Operator Error Causes
Over the years, there have been many occurrences in commercial nuclear power
plants caused by operator errors during operation. Some of these occurrences are
as follows [10, 11, 17–19]:
• Reactor mode switch in incorrect mode.
• Suppression chamber water volume goes over the limit.
• Control rod inserted well beyond limit.
• Control rod not declared non-functional or inoperable when misaligned.
• Serious judgement error in monitoring.
• Reactor coolant system leakage evaluation not performed.
• A power board inadvertent trip.
• Process vent gaseous radiation monitor left in calibrate mode.
• Two adjacent control blades withdrawn during the rod driver overhaul process.
• Steam generator blow-down function not monitored at all.
• Sudden release of low-level radioactive water.
• Concentrated boric acid storage tank well below limits.
Some causes of operator errors that resulted in occurrences such as above are
shown in Fig. 7.1 [11].
Additional information on the above occurrences and the causes of operator
errors is available in Ref. [11].
7.5 Questions to Measure Up Electrical Power System
Operating Practices to Reduce Human Errors
Over the years, in the area of electric power systems, various types of failures have
occurred due to human errors. Two examples of such failures are as follows [20]:
• An electrician assigned to carry out modiﬁcation to the boiler control circuit
when one of the power plant’s two steam boilers was down for annual inspection
7.3
Major Factors for Human Errors and Their Occurrence Preventions
95

---


### Page 106

and maintenance erroneously started to work on the control circuit of the
operating boiler and shut down the operating boiler.
• After a severe thunderstorm, the shift supervisor of a power plant carried out a
walk-through inspection of primary distribution switch gear of the power plant.
After seeing a red light for each circuit breaker and erroneously thinking that the
red light means ‘‘open’’ tripped each and every circuit breaker for obtaining a
green-light indication. His action resulted in the shut down of the entire power
plant.
The following six questions are considered most useful to measure up electrical
power system operating practices to reduce human errors [20]:
• Question No. 1. Are all switching-related operations planned and reviewed with
care well in advance and do they provide a clear logical step-by-step sequence
that gives particular attention to all types of vulnerable situations?
• Question No. 2. Do you have an effective program to assure that items such as
system drawings, plant procedures, and vendor manuals are effectively ﬁled and
kept up to date?
• Question No. 3. Is the split in responsibilities between the utilization system and
distribution system clearly understood and deﬁned effectively?
• Question No. 4. Are the long-range and day-to-day functions coordinated under
a highly knowledgeable power system ‘‘expert’’ and do shift and pack up personnel clearly understand their assigned responsibilities and are they properly
trained?
Misidentification 
of an alarm 
Inadequate 
procedures and lack 
of clarity
Typographical 
error 
Lack of guidelines 
Procedural 
deficiency 
Check list not 
completed 
Use of wrong 
procedures 
Misunderstanding 
of procedures 
Operator oversight 
Misunderstanding of 
technical 
specifications 
Disregard of 
procedures 
Causes 
Fig. 7.1 Some causes of operator errors that resulted in occurrences in commercial nuclear
power plants
96
7
Human Error in Power Generation

---


### Page 107

• Question No. 5. Do you have a proper procedure for assuring that all involved
equipment is clearly identiﬁed with unique and clearly located identiﬁcation and
that ﬁeld identiﬁcation clearly agrees with drawings and all other concerned
documentation?
• Question No. 6. Are proper steps taken for assuring that all types of redundant
or adjacent systems are not accidentally turned on/operated?
7.6 Performance Shaping Factors
Performance shaping factors may simply be described as the factors that encompass those inﬂuences that degrade or enhance human performance. In human
reliability analysis methods, performance shaping factors are used to highlight
human error contributors as well as to provide a basis to quantify those contributors systematically.
Nonetheless, performance shaping factors may be classiﬁed under two categories: direct and indirect [21]. The direct performance shaping factors are those
factors that can be measured directly, whereby there is a one-to-one relationship
between the magnitude of the performance shaping factor and that which is
measured. The indirect performance shaping factors are those performance shaping factors that cannot be measured directly, whereby the magnitude of the performance shaping factor can only be measured subjectively or multi-variately. The
common direct/indirect performance shaping factors are as follows [21, 22]:
• Procedures
• Complexity
• Accessibility and equipment operability
• Experience and training
• Need for special tools
• Time available
• Ergonomic quality of human–system interface
• Availability of instrumentation
• Available stafﬁng and resources
• Special ﬁtness needs
• Workload, time pressure, and stress
• Communications
• Environment
• Consideration of realistic accident sequence diversions and deviations
• Team/crew dynamics.
Important direct/indirect performance shaping factors in nuclear power plant
operations are shown in Fig. 7.2 [23].
Additional information on all of the above performance shaping factors is
available in Refs. [21, 23].
7.5
Questions to Measure Up Electrical Power System
97

---


### Page 108

7.7 Methods for Analyzing Human Errors in Power
Generation
Over the years, many methods have been developed in the areas of safety, reliability, and quality to perform various types of analysis. Some of these methods
can also be used to perform human error analysis in power generation. Three of
these methods are presented below.
7.7.1 Pontecorvo Method
This method can be used to obtain reliability estimates of task performance by a
person in the area of power generation. The method initially obtains reliability
estimates for discrete and separate subtasks with no accurate reliability ﬁgures, and
then, it combines these very estimates for obtaining the overall task reliability.
Generally, this method is used during initial design phases to quantitatively assess
the interaction of humans and machines. The method can also be used to determine
the performance of a single person acting alone.
Pontecorvo method is composed of six steps shown in Fig. 7.3 [24, 25]. Step 1
is concerned with identifying the tasks to be performed. These tasks should be
identiﬁed at a gross level (i.e. one complete operation is to be represented by each
task). Step 2 is concerned with the identiﬁcation of those subtasks of each task that
are essential for its completion. Step 3 is concerned with collecting empirical
performance-related data from sources such as experimental literature and inhouse operations. These data should be subject to those types of environments
under which subtasks are to be performed.
Type of 
display 
feedback 
Performance 
shaping factors 
Independence of 
human actions 
Human redundancy 
Quality of training 
and practice 
Quality of human 
engineering of 
controls and displays 
Presence and quality 
of written 
instructions and 
method of use 
Level of presumed 
psychological stress 
Fig. 7.2 Important direct/indirect performance shaping factors in nuclear power plant operations
98
7
Human Error in Power Generation

---


### Page 109

Step 4 is concerned with rating each subtask according to its level of perceived
difﬁculty or potential for the occurrence of error. Usually, a 10-point scale is used
for judging the appropriate subtask rate. The scale varies from least error to most
error. Step 5 is concerned with predicting subtask reliability and is accomplished
by expressing the data’s judged ratings and the empirical data in the form of
straight line. For goodness of ﬁt, the regression line is tested.
Finally, Step 6 is concerned with determining the task reliability, which is
obtained by multiplying subtasks’ reliabilities.
It is to be noted that the above-described approach is used for estimating the
performance of a single person acting alone. However, in a situation when a back
person is available, the probability of the task being performed correctly (i.e. the
task reliability) would be higher. Nonetheless, the backup person may not be
available all of the time. In such a situation, the overall reliability of two persons
working together to perform a given task can be estimated by using the following
equation [24, 25]:
Rov ¼
1  1  R
ð
Þ2
n
o
Ta þ RTu
h
i
= Ta þ Tu
ð
Þ
ð7:1Þ
Step 1 Identify tasks 
Step 2 Identify each task’s subtasks 
Step 3 Obtain empirical performancerelated data 
Step 4 Establish subtask rate 
Step 5 Predict subtask reliability 
Step 6 Determine task 
reliability 
Fig. 7.3 Steps of Pontecorvo
method
7.7
Methods for Analyzing Human Errors in Power Generation
99

---


### Page 110

where
Rov
is the overall reliability of two persons working together to perform a task
R
is the reliability of the single person
Tu
is the percentage of time the backup individual is unavailable
Ta
is the percentage of time the backup individual is available.
Example 7.1 Two workers are working together independently in the area of
power generation to perform an operation-related task. The reliability of each
worker is 0.95, and the backup worker is available around 60 % of the time. In
other words, 40 % of the time, the backup worker is not available.
Calculate the reliability of performing the operation-related task correctly. By
substituting the given data values into Eq. (7.1), we get
Rov ¼
1  1  0:95
ð
Þ2
n
o
0:60
ð
Þ þ 0:95
ð
Þ 0:40
ð
Þ
h
i
= 0:6 þ 0:4
ð
Þ
¼ 0:9785
Thus, the reliability of performing the operation-related task correctly is 0.9785.
7.7.2 Probability Tree Method
This is another method that can also be used to perform human error analysis in
power generation [26]. The method is concerned with representing human actions
and other events associated with the system diagrammatically. Thus, diagrammatic
task analysis is denoted by the branches of the probability tree. More speciﬁcally,
the branching limbs of the tree represent outcomes (i.e. success or failure) of each
action or event associated with a given problem. Furthermore, each branch of the
tree is assigned an occurrence probability.
Some of the advantages of the probability tree method are as follows [24]:
• It serves as a visibility tool.
• It is helpful to decrease the error occurrence probability due to computation
because of computational simpliﬁcation.
• It can incorporate, with some modiﬁcations, factors such as emotional stress,
interaction effects, and interaction stress.
• It is quite useful in applying predictions of individual error rates as well as
predicts the quantitative effects of errors.
The application of this method in the area of human error in power generation is
demonstrated through the following example.
Example 7.2 Assume that a task of nuclear power station control room operator is
composed of two independent subtasks, say, x and y. Each of these two subtasks
100
7
Human Error in Power Generation

---


### Page 111

can be performed either correctly or incorrectly, and subtask x is performed before
subtask y.
Develop a probability tree for the example and obtain probability expressions
for the following:
1. Successfully accomplishing the task by the control room operator.
2. Not successfully accomplishing the task by the control room operator.
In this case, the control room operator ﬁrst carries out subtask x correctly or
incorrectly and then proceeds to carrying out subtask y. This complete scenario is
denoted by the Fig. 7.4 probability tree diagram.
The four letter symbols used in Fig. 7.4 are deﬁned below.
x
denotes the event that subtask x is performed correctly by the control room
operator.
x
denotes the event that subtask x is performed incorrectly by the control room
operator.
y
denotes the event that subtask y is performed correctly by the control room
operator.
y
denotes the event that subtask y is performed incorrectly by the control room
operator.
By examining the Fig. 7.4, it can be noted that there are three distinct possibilities (i.e. xy;xy, and xy) for not successfully accomplishing the task by the
nuclear power station control room operator. Thus, the probability of not successfully accomplishing the task by the control room operator is given by
Ptf ¼ Pðxy þ xy þ xyÞ
¼ Px Py þ Px Py þ Px Py
ð7:2Þ
x
−
x
y 
y
−
y
−
y
xy 
x
−
y
−
x
−y
−
x y 
Fig. 7.4 Probability tree for
the nuclear power station
control room operator
performing tasks x and y
7.7
Methods for Analyzing Human Errors in Power Generation
101

---


### Page 112

where
Px
is the probability of performing subtask x correctly by the control room
operator
Py
is the probability of performing subtask y incorrectly by the control room
operator
Px
is the probability of performing subtask x incorrectly by the control room
operator
Py
is the probability of performing subtask y correctly by the control room
operator
Ptf
is the probability of not successfully accomplishing the task by the control
room operator.
Since Px ¼ 1  Px and Py ¼ 1  Py, Eq. (7.2) reduces to
Ptf ¼ Px 1  Py


þ 1  Px
ð
ÞPy þ 1  Px
ð
Þ 1  Py


¼ 1  Px Py
ð7:3Þ
Similarly, by examining Fig. 7.4, it can be concluded that there is only one
possibility (i.e. xy) for successfully accomplishing the task by the control room
operator. Thus, the probability of successfully accomplishing the task by the
control room operator is expressed by
Pts ¼ PðxyÞ
¼ Px Py
ð7:4Þ
where
Pts
is the probability of successfully accomplishing the task by the nuclear
power station control room operator.
Example 7.3 Assume that in Example 7.2, the probabilities of the nuclear power
station control room operator carrying out subtasks x and y correctly are 0.97 and
0.85, respectively. Calculate the probability of failure of the control room operator
to accomplish the task successfully.
By inserting the speciﬁed data values into Eq. (7.3), we obtain
Ptf ¼ 1  0:97
ð
Þ 0:85
ð
Þ
¼ 0:1755
Thus, the probability of failure of the control room operator to accomplish the
task successfully is 0.1755.
102
7
Human Error in Power Generation

---


### Page 113

7.7.3 Pareto Analysis
This is a quite useful method that can be used to separate the important causes of
human error-related problems in the area of power generation from the trivial ones.
The method is named after its founder Vilfredo Pareto (1848–1923), an Italian
economist.
In the area of power generation, Pareto analysis is considered a powerful tool to
identify areas for concerted effort to eliminate or minimize errors.
The method is composed of six steps shown in Fig. 7.5 [27, 28]. Additional
information on this method is available in Refs. [26–29].
Step 1
List causes/activities in tabular form and count their
occurrences
Step 2
Arrange the causes in descending order
Step 3
Compute the total for the complete list 
Step 4
Determine the percentage of the total for each cause/activity
Step 5
Develop a Pareto diagram that shows percentages vertically 
and their corresponding causes horizontally
Step 6
Conclude from the end results
Fig. 7.5 Pareto analysis steps
7.7
Methods for Analyzing Human Errors in Power Generation
103

---


### Page 114

7.8 Problems
1. List at least eight facts, ﬁgures, and examples concerned with human error in
power generation.
2. List at least ten occurrences in commercial nuclear power plants caused by
operator errors during operation.
3. What were the causes of operator errors that resulted in occurrences in
commercial nuclear power plants?
4. What are the six questions considered most useful to measure up electrical
power system operating practices?
5. List at least 15 common direct/indirect performance shaping factors.
6. What are the important direct/indirect performance shaping factors in nuclear
power plant operations?
7. Describe Pontecorvo method.
8. What are the advantages of the probability tree method?
9. Assume that a task of a nuclear power station control room operator is
composed of three independent subtasks, say, x, y, and z. Each of these subtasks can be either performed correctly or incorrectly, and subtask x is performed before subtask y, and subtask y is accomplished before subtask z.
Develop a probability tree and obtain a probability expression for performing
the overall task incorrectly by the control room operator.
10. What is Pareto analysis? Describe it in detail.
References
1. Varma V (1996) Maintenance training reduces human errors. Power Eng 98:44–47
2. Kawano R (1997) Steps toward the realization of human-centered systems: an overview of
the human factors activities at TEPCO. In: Proceedings of the IEEE sixth annual human
factors meeting, pp 13.27–13.32
3. Ryan GT (1988) A task analysis-linked approach for integrating the human factor in
reliability assessments of nuclear power plants. Reliab Eng Syst Saf 22:219–234
4. Trager TA Jr (1985) Case study report on loss of safety system function events. Report No.
AEOD/C504, United States Nuclear Regulatory Commission, Washington, D.C
5. Mishima S (1988) Human factors research program: long term plan in cooperation with
government and private research centers. In: Proceedings of the IEEE conference on human
factors and power plants, pp 50–54
6. Williams JC (1988) A data-based method for assessing and reducing human error to improve
operational performance. In: Proceedings of the IEEE conference on human factors and
power plants, pp 436–450
7. An Analysis of Root Causes in 1983 and 1984 Signiﬁcant Event Reports (1985) Report No.
85-027, Institute of Nuclear Power Operations, Atlanta, Georgia, July 1985
8. Heo G, Park J (2010) A framework for evaluating the effects of maintenance-related human
errors in nuclear power plants. Reliab Eng Syst Saf 95:797–805
9. Lee JW, Park GO, Park JC, Sim BS (1996) Analysis of human error trip cases in Korean
NPPs. J Korean Nucl Soc 28:563–575
104
7
Human Error in Power Generation

---


### Page 115

10. Scott RL (1975) Recent occurrences of nuclear reactors and their causes. Nucl Saf
16:496–497
11. Husseiny AA, Sabry ZA (1980) Analysis of human factor in operation of nuclear power
plants. Atomkernenergie Kerntechnik 36:115–121
12. Kim J, Park J, Jung W, Kim JT (2009) Characteristics of test and maintenance human errors
leading to unplanned reactor trips in nuclear power plants. Nucl Eng Des 239:2530–2536
13. Oliver JA, Baker JE, Roth JW (1981) Assessment of the use of human factors in the design of
fossil-ﬁred steam generating system. EPRI Report No. CS-1760, Electric Power Research
Institute, Palo Alto, California
14. Koval DO, Floyd HL II (1998) Human element factors affecting reliability and safety. IEEE
Trans Ind Appl 34(2):406–414
15. Mc Cornack RL (1961) Inspector accuracy: a study of the literature. Report No. SCTM 53-61
(14), Sandia Corporation, Albuquerque, New Mexico
16. Etemadi AH, Fotuhi-Firuzabad M (2008) Quantitative assessment of protection system
reliability incorporating human errors. J Risk Reliab 9:255–263
17. Scott RL (1975) Recent occurrences of nuclear reactors and their causes. Nucl Saf
16:619–621
18. Thompson D (1974) Summary of recent abnormal occurrences at power-reactor facilities.
Nucl Saf 15:198–320
19. Casto WR (1974) Recent occurrences of nuclear reactors and their causes. Nucl Saf 15:79,
466, 742
20. Floyd HL II (1986) Reducing human errors in industrial electric power system operation, part
I: improving system reliability. IEEE Trans Ind Appl IA-22(3):420–424
21. Boring RL, Grifﬁth CD, Joe JC (2007) The measure of human error: direct and indirect
performance shaping factors. In: Proceedings of the IEEE conference on human factors and
power plants, pp 170–176
22. Kolaczkowshi A, Forester J, Lois E, Cooper S (2005) Good practices for implementing
human reliability analysis (HRA). Report No. NUREG-1792, United States Nuclear
Regulatory Commission, Washington, D.C., Apr 2005
23. Swain AD, Guttman HE (1975) Human reliability analysis applied to nuclear power. In:
Proceedings of the annual reliability and maintainability symposium, pp 116–119
24. Pontecorvo AB (1965) A method of predicting human reliability. In: Proceedings of the 4th
annual reliability and maintainability conference, pp 337–342
25. Dhillon BS (1986) Human reliability: with human factors. Pergamon Press, New York
26. Dhillon BS (2009) Human reliability, error, and human factors in engineering maintenance:
with reference to aviation and power generation. CRC Press, Boca Raton
27. Dhillon BS (1999) Design reliability: fundamentals and applications. CRC Press, Boca Raton
28. Kanji GK, Asher M (1996) 100 methods for total quality management. Safe Publications,
London
29. Dhillon BS (2005) Reliability, quality, and safety for engineers. CRC Press, Boca Raton
References
105

---


### Page 116

Chapter 8
Human Factors in Control Systems
8.1 Introduction
Control systems play a pivotal role in power generation, and over the years, control
systems and the role of their control room human operators have changed quite
dramatically. The activity of human operator has evolved from manually carrying
out the process, to control system supervision. In turn, the human operator requires
an in-depth knowledge of the process being monitored, the ability to make
effective decisions within demanding constraints, effective man–machine interfaces, etc.
Needless to say, after the Three Mile Island (TMI) nuclear power plant accident
in 1979, the human factors in control systems in the area of power generation have
become a very important issue. Because a Nuclear Regulatory Commission (NRC)
study reported the ﬁndings such as virtually non-existent of human engineering at
TMI, violation of number of human engineering principles in control panel
designs, and information required by operators was often non-existent, poorly
located, ambiguous, or difﬁcult to read [1, 2].
This chapter presents various important aspects of human factors in control
systems.
8.2 Control Room Design Deﬁciencies that can Lead
to Human Error
There are many control room design-related deﬁciencies that can lead to human
error. Some of these deﬁciencies are as follows [3]:
• Controls
of
subsystems
widely
separated
from
their
associated
alarm
annunciators.
• Controls and displays placed well beyond anthropometric reach and vision
envelopes.
• Poor use of shape coding and mirror-imaged control boards.
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_8,
 Springer International Publishing Switzerland 2014
107

---


### Page 117

• Lack of proper barriers for switches or control knobs considered critical.
• Poor location of some controls that can result in inadvertent activation.
• Chart recorders containing too many parameters.
• Inconsistency in colour coding within a control room.
• Reﬂection and glare from lighting on involved instruments.
• Poor labelling practice, including inconsistency in abbreviations.
• Wrong use of major, intermediate, and minor scale markings on involved
meters.
• Adjacent meters with non-identical scales that must be compared by operators.
• Illegible recorder printouts and use of qualitative instead of quantitative
indicators.
• Too complex annunciator systems along with complex procedures/equipment to
knowledge, silence, test, and reset alarms.
• Meters that malfunction with the pointer reading in the normal band of the scale.
8.3 Advantages of Considering Human Factors in Digital
Control Room Upgrades, an Approach to Incorporate
Human Factors Considerations in Digital Control
Room Upgrades, and Recommendations to Overcome
Problems When Digital Control Room Upgrades are
Undertaken Without Considering Human Factors
into Design
There are many advantages of considering human factors in digital control room
upgrades. These advantages may be grouped under the following four general
categories [4]:
• Category I: Improved equipment speciﬁcation and procurement. In this
case, all essential human factors considerations can be speciﬁed right from the
very beginning of the project.
• Category II: Increased operator acceptance. In this case, potential operators
can provide critical input to human factors design and evaluation.
• Category III: Decreased need for back ﬁts or redesigns. In this case, essential
changes can be carried out at earlier, less costly, stages of the design process.
• Category IV: Increased plant availability. In this case, operator controllable
trips and inefﬁciencies can be avoided, and downtime for system installation and
testing is shorter.
The steps of an approach considered quite useful to incorporate human factors
considerations in digital control room upgrades are shown in Fig. 8.1 [4]. Step 1 is
concerned with surveying the existing control room and its environment to
determine requirements for the new computer-based workstations. Step 2 is
108
8
Human Factors in Control Systems

---


### Page 118

concerned with analysing the tasks to be carried out; for developing information
and control requirements.
Step 3 is concerned with interviewing operators for obtaining input and feedback to gather data from the end-users early in the design process. Step 4 is
concerned with reviewing preliminary drawings and mock-ups against human
factors criteria at early stage of design to avoid costly back ﬁts.
Finally, Step 5 is concerned with developing display organization and control
grouping strategies for applying to scenarios generated during the analysis to
optimize design trade-offs.
The following recommendations classiﬁed under six areas are considered useful
to overcome problems when digital control room upgrades are undertaken without
considering human factors [4]:
• Control devices:
1. Simplify confusing control operations.
2. Position controls effectively/properly.
• Displays:
1. Simplify all confusing displays.
2. Ensure display conﬁguration consistency.
Step 1
Survey the existing control room and its 
environment
Step 2
Analyze the tasks to be carried out 
Step 3
Interview operators for obtaining input and 
feedback 
Step 4
Review preliminary drawings and mockups against human factors criteria 
Step 5
Develop display organization and control 
grouping strategies 
Fig. 8.1 Steps of an
approach for incorporating
human factors considerations
in digital control room
upgrades
8.3
Advantages of Considering Human Factors in Digital Control Room Upgrades
109

---


### Page 119

3. Improve summary displays for providing better overall plant picture.
4. Include all types of required data on relevant displays.
5. Include graphics.
6. Add displays considered relevant.
7. Use colour effectively/properly.
• Guidelines/Training:
1. Provide
appropriate
guidelines
for
control
and
display
design
and
development.
2. Provide appropriate guidelines for system implementation.
3. Provide appropriate hands-on training.
4. Ensure appropriate level of operator conﬁdence through training.
• System software:
1. Ensure that system performs all required operations properly.
2. Ensure that system software collects all types of relevant data.
3. Optimize update rates and response time/capacity.
4. Minimize confusing and multiple steps necessary for obtaining data.
• System hardware:
1. Ensure that system hardware is appropriately designed for withstanding
operational rigours.
2. Ensure that system contains all types of required hardware controls.
3. Ensure that equipment operation is not distracting or intrusive.
• Facility:
1. Ensure that system is conﬁgured so that the operator can easily and effectively carry out all required operations.
2. Ensure that surrounding environment clearly supports system operation and
does not degrade it.
3. Ensure that all system parts are appropriately placed in the environment.
8.4 Common Problems Associated with Controls
and Displays and Their Corrective Measures
There are many problems associated with controls and displays. The common ones
and their corresponding corrective measures (in parentheses) are as follows [2]:
• Poor instrument grouping (make use of demarcation lines where necessary and
rearrange during major retroﬁt).
• Displays/control too low or high (relocate as necessary within suitable anthropometric range).
110
8
Human Factors in Control Systems

---


### Page 120

• Poor labelling (use black letters on white black ground; consistent letter character size; and a hierarchical scheme).
• Glare and parallax on indicators (install appropriate diffusers in ceiling ﬁxtures
for distributing light more evenly and whenever possible choose instruments and
less glass ‘‘distortion’’).
• Poor differentiation between various controls (make use of shape coding, colour
code handles for all related systems, and shade background of all related
controls).
• Inconsistent use of wording abbreviations (use same abbreviations consistently
and use standard nomenclature and symbols for words).
• Controls near bottom edge of board inadvertently activated (install appropriate
guard rail along edge of board in question).
• Poor engineering units or scaling on recorders/indicators (avoid suppressed
scales, use units appropriate to parameter being measured, etc.)
• Nuisance alarms: annunciators (eliminate unnecessary alarms, revise set points
on others (if possible), and perform alarm review).
• Controls: violation of stereotypes (keep directions of control handles in accordance with expectations of humans).
8.5 Human Engineering Discrepancies in Control Room
Visual Displays
A study of a control room survey of several nuclear power plants reported a
number of human engineering discrepancies in control room visual displays [5].
Six main areas of these discrepancies are shown in Fig. 8.2 [5].
Two discrepancies of the area ‘‘information displayed’’ were: (1) failed displays
not apparent and (2) wrong display type. Three discrepancies of the area ‘‘scale
markings’’ were: (1) poor numerical progression, (2) wrong scale graduation
marks, and (3) log, multiple-scales. The following three discrepancies were
associated with the area ‘‘display readability’’:
1. Informal meter scales
2. Characteristics and marking too small
3. Poor contrast (glare).
Two discrepancies of the area ‘‘usability of displays’’ were: (1) inappropriate
scale or scale range limits and (2) conversion required. Three discrepancies of the
area ‘‘scale zone markings’’ were: (1) no alarm points, (2) informal banding, and
(3) no scale banding. Finally, the following two discrepancies were associated with
the area ‘‘colour coding’’:
1. Poor colour usage
2. Inconsistent colour coding practices.
8.4
Common Problems Associated with Controls and Displays
111

---


### Page 121

8.6 Human Factors Guidelines for Digital Control System
Displays
Over the years, a large number of human factors guidelines for digital control
system displays have been developed [6–9]. These guidelines cover areas such as
follows [9]:
• Screen organization and layout. The speciﬁc topics addressed in this area
include screen size, display density, grouping of information, display partitioning, sequence of information, multiple-page displays, and inter-frame
navigation.
• Colour and other coding. The speciﬁc topics addressed in this area include
colour usage, colour assignments, icons and symbols, font, brightness, line sizes,
geometric shapes, contrast reversal, blinking, combination of codes, and
magnitude.
• Windows. The speciﬁc topics addressed in this area include alert boxes, general
guidelines, dialogue boxes, and windows on real-time systems.
• Screen structures and content. The speciﬁc topics addressed in this area
include labels, error messages, character size, cursor, user aids, abbreviations
and acronyms, continuous text, data entry, and alphanumeric codes.
• Alarms. The speciﬁc topics addressed in this area include auditory alert, alarm
system controls, alarm lists, general guidelines, reduction and prioritization,
integration with other aids, and alarm message content.
Information 
displayed 
Main areas 
Usability of 
displays 
Display 
readability 
Color 
coding 
Scale zone 
markings 
Scale 
markings 
Fig. 8.2 Main areas of human engineering discrepancies in nuclear power plants’ control room
visual displays
112
8
Human Factors in Control Systems

---


### Page 122

• Control-Display integration. The speciﬁc topics addressed in this area include
manual/auto stations, controls on mimics, permissive and tag outs, user dialogue, and system feedback.
• Information formats. The speciﬁc topics addressed in this area include general
guidelines, band charts, graphs and labels, analogue representation, binary
indication, linear proﬁle, trend plot, data maps, range bar, single value line chart,
and circular proﬁle.
• Input/control devices. The speciﬁc topics addressed in this area include keyboard, touch screen, membrane keyboard, X–Y controller/mouse, track ball, and
light pen.
• Overall system requirements. The speciﬁc topics addressed in this area include
display of dynamic data and response time.
• Large screen displays. The speciﬁc topics addressed in this area include use
and types and readability and visibility.
• Menu design. The speciﬁc topics addressed in this area include menu format,
item selection, general guidelines, supplements to menus, and hierarchical
menus.
• Hardware. The speciﬁc topics addressed in this area include glare, luminance,
ﬂicker and image polarity, and hard copy devices.
Human factors guidelines for certain above areas and speciﬁc topics are presented below [9].
8.6.1 Windows
Although windows provide ﬂexibility and organization for the potential users, but
require proper window management on the part of involved users or designers, the
following two are the general styles of windows:
• Tiled. This type of windows may be placed to edge or within a speciﬁed area on
a formatted display, but at all times, the contents of all windows are visible.
• Overlapped. With this type of windows, it is possible to arrange multiple
windows like pieces of paper on a desk top, so that one may appear to a certain
degree to overlap another. Overlapping windows provide a mechanism for a
temporary display to be viewed as well as provide the place keeping or reference
advantage of keeping a certain portion of an earlier display in an easy access and
view.
Nonetheless, some of the useful guidelines in the area of windows are as
follows [6, 9–12]:
• Provide an effective means to control the size of the window. More speciﬁcally,
resizing should affect the viewing area only, not the window contents’ format.
• Provide an effective means to close the window.
8.6
Human Factors Guidelines for Digital Control System Displays
113

---


### Page 123

• Standardize effectively the format for windows.
• Provide a reserved screen area (i.e. a window tile) for display of pop-up control
stations where soft control stations are not displayed on a continuous basis, as on
schematic overview displays.
• Provide dedicated window areas (tiles) for the display of user-selected information when windows are desired on formatted real-time displays.
• Provide a clear path to choose information for each and every window (e.g.
provide a menu of window options).
• Design the display in such a way that it is impossible to change out and then
recall the parent display with the same windowed information as it had on it
when deselected, in situation where windows for user-selected information are
provided on formatted real-time displays.
• Ensure that for tiled windows, pre-format information that may be assigned to
the window, so it properly ﬁts within the tile.
• Ensure that pre-format information is available for display in tiled windows to
ﬁt the window so that there is no need for the user to devote time or attention to
manipulating the window, other than simply choosing what is to be presented.
• Provide a proper means to restore the original display rapidly, in situations
where windows will overwrite information on real-time displays (e.g. dialogue
boxes, pull-down menus, or alert boxes).
8.6.2 Alarms
In the design of displays for digital control systems, alarm management is a major
consideration. Over the years, many human factors-related guidelines in the area of
alarms have been developed [6, 13–15]. Some of the guidelines to aid in determining the necessity of alarms are as follows [9]:
• Avoid activating alarms for equipment that is out of service for some type of
maintenance. Furthermore, when equipment is taken out of service, its all
associated alarms should be disabled until it (i.e. equipment) is put back into
service.
• Ensure that the amount and content of alarm-related information to be displayed
in real time is based on what the operator requires to respond to the alarm
effectively.
• Ensure that the number of levels of alarms is kept to a minimum.
• Avoid activating alarms as part of a normal operating sequence, i.e. during
plant/system start-up or any other planned evolution.
• Provide appropriate alarms for warning of conditions that could affect personnel
safety or could result in equipment damage.
114
8
Human Factors in Control Systems

---


### Page 124

8.6.3 Manual/Auto Stations, Controls on Mimics,
and Permissive and Tag Outs
Generally, in the published literature, the human factors considerations in design
of ‘‘soft’’ (i.e. software rather than mechanical) control capabilities have not been
given much attention. Nonetheless, some of the guidelines that could be useful in
this area are as follows [9]:
• Label control stations unambiguously to highlight the controlled process or
component.
• Ensure that different types of soft control stations are distinctively different in
appearance.
• Ensure that the indicators shown on the control station are labelled according to
their function or the quantities displayed.
• Ensure that the order of control stations within the framework of an array is
based on logical relationships among the controls such as system relationships,
criticality, or sequence of use.
• In the event, when an array of soft stations are presented, highlight the one
selected for operation.
• Display the actual status of the controlled component/unit.
• Provide a proper means to indicate non-availability of control stations due to
unsatisﬁed permissive or tag outs.
Additional information on guidelines concerned with the topic of this section is
available in Ref. [9].
8.6.4 Inter-Frame Navigation
Some of the inter-frame-related guidelines are as follows [9, 16]:
• Ensure that a map of the display network is provided on request.
• Aim to provide all the necessary information required to respond to time-critical
situations, on a single display page.
• Consider providing for random access to displays by means of command entry
for sequential access systems or menu.
• Avoid requiring the user to wait for an intermediate step to be completely
displayed prior to the user can proceed to the next step in the involved selection
process.
• Ensure that the organization of the network of displays is according to some
easily understood principle, such as frequency of use, sequence of use in startup, or interconnections among plant systems.
• Make use of dedicated function keys for providing one-button access to timecritical controls and information.
8.6
Human Factors Guidelines for Digital Control System Displays
115

---


### Page 125

• Ensure that information and controls to displays are assigned according to some
acceptable meaningful logic.
• Provide an effective return-to-previous-page capability.
• Ensure that display pages are organized in such a way that the displays that are
likely to be used in sequence can be easily accessed by a single action.
• Provide a type-ahead capability that allows the system to process and act on
inputs while the intermediate displays are being drawn, in situations where
menu or sequential access cannot be avoided.
• Provide an appropriate paging capability in conditions where displays can only
be accessed indirectly (i.e. by means of a menu).
8.6.5 Colour Usage
Over the years, past experiences clearly indicate that colour aid performance in
both search and identiﬁcation-related tasks when the code is unique and known in
advance [17, 18]. Two most useful guidelines in the area of colour usage are as
follows [9]:
• Ensure that all colour codes are simple, consistent, and unambiguous.
• Ensure that the meaning assigned to particular colours are clearly consistent
across all applications within the control room.
Additional guidelines on colour usage are available in Refs. [10, 11].
8.7 Human Performance-Related Advanced Control Room
Technology Issues
Although advanced control room technology has the potential to improve system
performance, there is also potential to negatively impact human performance and
create precursors for the occurrence of human errors. Some of the human performance-related advanced control room technology issues are as follows [19, 20]:
• Shift from physical to highly cognitive inclined workload impairing the ability
of operator to process and monitor all types of relevant data.
• Loss of vigilance of operator due to automated systems resulting in decrease in
ability to detect off-normal conditions.
• Ill-deﬁned and poorly organized tasks resulting from poor allocation of functionrelated strategies.
• Very high shifts in operator workload (i.e. workload transition) whenever a
computer failure occurs.
116
8
Human Factors in Control Systems

---


### Page 126

• Difﬁculty in understanding how advanced systems work which can result in
either a lack of complete acceptance of operator aids or too much reliance on
them.
• Increment in the operator’s cognitive workload related to the management of the
interface (e.g. scaling, positioning, and opening windows).
• Considerable loss of skill proﬁciency for the occasional performance of functions that are generally automated.
• Problems in navigating through and ﬁnding pertinent information presented in a
computer-based workspace.
• Loss of ‘‘situation awareness’’ of the operator which makes it rather difﬁcult to
assume direct control when necessary.
• Loss of ability for using well-learned, rapid eye-scanning patterns and pattern
recognition from spatially ﬁxed parameter displays, particularly in the case of
highly ﬂexible CRT-type interfaces.
Additional information on the above issues is available in Ref. [19].
8.8 Control Room Annunciator’s Human Factors-Related
Evaluation
In order to alert control room operators to plant conditions, a typical commercial
nuclear power plant control room can have from 1,000 to 2,000 annunciators [21].
Since these annunciators are activated whenever plant parameter limits exceed,
they are very important to system safety design. Thus, a study was conducted to
highlight speciﬁc problem areas conducive to operator difﬁculty as well as to
provide speciﬁc and generic solutions to those problems [21]. The study evaluated
the annunciator systems in four nuclear reactor facilities and formally interviewed
39 reactor operators. Each operator interviewed 39 reactor operators. Each operator interviewed was asked a series of structured questions such as presented in
Table 8.1 [21].
The classiﬁcations of the end results of the information collected and analysed
are shown in Fig. 8.3 [21].
The items belonging to classiﬁcation: lack of organization and consistency are
as follows:
• Annunciators are rarely designed and placed in a logical, consistent, or rational
manner.
• Annunciators are generally poorly organized and structured with respect to
function, system impact, response immediacy, or importance.
• A lack of standardization in colour coding, labelling, design, script, acoustic
alarm frequency, contrast, timbre, operating logic, and abbreviations.
8.7
Human Performance-Related Advanced Control Room Technology Issues
117

---


### Page 127

The items belonging to classiﬁcation: operator problems are as follows:
• Annunciators are frequently used for displaying various types of unimportant or
relatively minor conditions.
• In the event when a major system failure occurs, many alarms that are only
indirectly concerned with the primary failure are triggered. In turn, this signiﬁcantly increases the information load that concerned operators must cognitively process to correctly highlight the primary failure source.
• For optimum viewing, letter sizes and labelling are unsatisfactory.
Table 8.1 Questions asked to nuclear power plant control room operators
Question
no.
Question
1
Are any of the annunciator displays difﬁcult to comprehend or read?
2
How easy to use are the procedures associated with annunciators?
3
Are you happy with the existing locations of all the annunciators?
4
Have you ever had any past difﬁculties or speciﬁc areas of concern with any
annunciator displays?
5
Is here a situation for which no annunciator available?
6
How helpful are the annunciators to diagnose plant conditions?
7
What type of annunciator-related hardware do you consider the best?
8
How cumbersome or easy is it to maintain the existing annunciators?
9
Do you have any suggestions for improving annunciator systems, training, and the
approaches used by operators?
10
Which annunciators in your opinion are most useful?
Classifications 
Maintenance 
problems 
Lack of organization 
and consistency 
Training problems 
Equipment 
shortcomings 
Operator problems 
Fig. 8.3 Classiﬁcations of the end results of the control room annunciators’ human factorsrelated information collected and analysed
118
8
Human Factors in Control Systems

---


### Page 128

The items belonging to classiﬁcation: equipment shortcomings are as follows:
• Some control room annunciators have quite low credibility with operators
because of a rather high number of misleading or false alarms.
• Some annunciators are not possessed with a press-to-test device to test bulb and
circuit.
• Some annunciators are not equipped with an alarm override switch such as setpoint adjustment that can be utilized during maintenance for preventing constant
and recurring acoustic alarms.
• Generally, very little descriptive information is provided on window faces for
orienting potential operators towards proper corrective measures.
• Annunciators do not totally utilize existing computer display and logic capability for ﬁltering or reducing the number of meaningless alarms, providing
automatic default action if the operator overlooks to carry out necessary action,
helping the operator to focus on the basic cause of a given alarm, and providing
written or coded procedures for operators so that appropriate corrective actions
can be undertaken.
• Generally, there is no systematic correspondence between annunciator display
elements and the controls utilized for rectifying the alarms.
The items belonging to classiﬁcation: training problems are as follows:
• Some guides-related documentation is inaccurate or incomplete.
• There is quite little agreement among operating personnel on what annunciators
are essential or most important for plant operations.
Finally, the items belonging to classiﬁcation: maintenance problems are as
follows:
• Generally bulb and logic card-related repair is relatively quite frequent.
• In some alarm systems, operators are required to make their own tools to change
bulbs.
• Tag-out procedures for annunciator maintenance are very poor in some plants.
The above control room annunciators’ human factors-related evaluation results
are considered very useful to improve human factors associated with control room
annunciators.
8.9 Problems
1. List at least 12 control room design deﬁciencies that can lead to human error.
2. Discuss the advantages of considering human factors in digital control room
upgrades.
8.8
Control Room Annunciator’s Human Factors-Related Evaluation
119

---


### Page 129

3. Describe an approach to incorporate human factors considerations in digital
control room upgrades.
4. Discuss the common problems associated with controls and displays and their
corrective measures.
5. What are the main areas of human engineering discrepancies in nuclear power
plants’ control room visual displays?
6. Discuss human factors guidelines for digital control system displays.
7. List at least ten human performance-related advanced control room technology
issues.
8. Write an essay on human factors in control systems.
9. Discuss recommendations to overcome problems when digital control room
upgrades are undertaken without considering human factors into design.
10. Discuss human engineering discrepancies in the following three areas concerning nuclear power plants’ control room visual displays:
• Display readability.
• Scale zone markings.
• Colour coding.
References
1. Malone TB et al (1980) Human factors evaluation of control room design and operator
performance at Three Mile Island-2, Final Report. Report No. NUREG/CR-1270, vol 1.
Nuclear Regulatory Commission (NRC), Washington, DC
2. Tennant DV (1986) Human factors considerations in power plant control room design. In:
Proceedings of the 29th power instrumentation symposium, pp 29–36
3. Brooks DM, Wilmington CR, Wilmington TG (2008) Role of human factors in system safety.
In: Proceedings of the international congress on advances in nuclear power plants, pp 62–75
4. Gaddy CD, Fray RR, Divakaruni SM (1991) Human factors considerations in digital control
room upgrades. In: Proceedings of the American power conference, pp 256–258
5. Lisboa J (1992) Human factors assessment of digital monitoring systems for nuclear power
plants control room. IEEE Trans Nucl Sci 39(4):9224–9932
6. Guidelines for Control Room Design Reviews. Report No. NUREG-0700, U.S. Nuclear
Regulatory Commission (NUREG), Washington, DC
7. Beare AN, Gaddy CD, Taylor JC et al (1991) Human factors guidelines for fossil power plant
control rooms and remote control stations. Report No. RP 2710-20, Electric Power Research
Institute (EPRI), Palo Alto, California
8. Daniels RW, Oliver JA (1984) Enhancing fossil power plant design and operation: human
factors guidelines. Report No. CS-3745, vol 1–3. Electric Power Research Institute, Palo
Alto, California
9. Beare AN, Gaddy CD, Gilmore WE, Taylor JC, Fray RR, Divakaruni SM (1992) Human
factors guidelines for fossil power plant digital control system displays. In: Proceedings of
the IEEE conference on human factors and power plants, pp 248–253
10. Gilmore WE, Gertman DI, Blackman HS (1989) User-computer interface in process control.
Academic Press, Boston
11. MIL-HDBK-761A (1989) Human engineering guidelines for management information
systems, Department of Defense, Washington, DC
120
8
Human Factors in Control Systems

---


### Page 130

12. Billingsley PA (1988) Taking panes: issues in the design of windowing systems. In: Helander
M (ed) Handbook of human-computer interaction. North-Holland Publishing, Amsterdam,
pp 200–209
13. Banks WE, Boone MP (1981) Nuclear control room annunciators: problems and
recommendations.
Report
No.
NUREG/CR-2147,
Nuclear
Regulatory
Commission,
Washington, DC
14. Rankin WL, Duvernoy KR, Ames KR, Morgenstern MH, Eckenrode RJ (1983) Near-term
improvements for nuclear power plant control room annunciators. Report No. NUREG/CR3217, Nuclear Regulatory Commission, Washington, DC
15. Seminara JL (1988) Control room deﬁciencies, remedial options, and human factors research
needs. Report No. EPRI NP-5795, Electric Power Research Institute, Palo Alto, California
16. Paap KR, Roske-Hofstrand RJ (1988) Design of menus. In: Helander M (ed) Handbook of
human-computer interaction. North-Holland Publishing, Amsterdam, pp 80–87
17. Blackman HS, Gilmore (1988) The analysis of visual coding variables on CRT-generated
displays. Proc Soc Inf Display 29(2):10–14
18. Christ RE (1990) Review and analysis of color coding research for visual displays. In:
Venturino M (ed) Selected readings in human factors. Human Factors Society, Santa Monica,
pp 108–115
19. O’Hara JM, Hall RE (1992) Advanced control rooms and crew performance issues:
implications for human reliability. IEEE Trans Nucl Sci 39(4):919–923
20. Rasmussen J, Duncan K, Leplat J (eds) (1987) New technology and human error. Wiley, New
York
21. Banks WW, Blackman HS, Curtis JN (1984) A human factors evaluation of nuclear power
plant control room annunciators. In: Proceedings of the annual control engineering
conference, pp 323–326
References
121

---


### Page 131

Chapter 9
Human Factors in Power Plant
Maintenance
9.1 Introduction
In power plant maintenance, human factors play an important role because by
improving the maintainability design of power plant systems, equipment, and
facilities in regard to human factors helps to increase plant safety, availability, and
productivity. In comparison to the aerospace industrial sector, interest in human
factors-related issues in the power industrial sector is relatively new. Its history
may be traced back to the 1970s, when the WASH-1400 Reactor Safety Study
criticized the deviation of the design of displays and controls and their arrangement in the United States commercial nuclear power plants from the human factors
engineering set standards [1].
Consequently, a study concerning the review of human factors in nuclear power
plant control rooms in the United States was sponsored by the Electric Power
Research Institute [2]. This study identiﬁed various major and minor human factors’ shortcomings that can lead to poor effectiveness of the man–machine interface [2–4]. Needless to say, over the years, the occurrence of many human factors’
shortcomings-related events in the area of power generation has lead to an
increased attention to human factors in power plant maintenance.
This chapter presents various important aspects of human factors in the area of
power plant maintenance.
9.2 Power Plant Systems’ Human Factors Engineering
Maintenance-Related Shortcomings
There are many human factors engineering maintenance-related shortcomings or
deﬁciencies in power plant systems. A survey-based study has classiﬁed, in
descending order, such shortcomings under the following six categories [5]:
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_9,
 Springer International Publishing Switzerland 2014
123

---


### Page 132

• Category I: Inadequate clearance or limited access to carry out maintenance activities. It means that there is inadequate clearance to carry out
inspection activities, no room for the correct tool, etc.
• Category II: Equipment poorly designed to facilitate all involved maintenance activities in an effective manner. It means that the required tasks are too
detailed to carry out with gloves and mask on, it is not possible to open all
involved cabinet doors all the way, design is too complex (i.e., too difﬁcult to
repair), etc.
• Category III: Systems/equipment inherently unreliable. It means that ﬂatbed
ﬁtter is under-designed and needs maintenance constantly, the system drifts and
is unstable, overly sensitive controllers, etc.
• Category IV: Personnel-related safety hazard. It means poorly designed
equipment in high radiation areas, no safety rail where is, say a 35-foot drop, oil
on the ﬂoor from the main feed pumps, hydrogen unloading facility is dangerous, etc.
• Category V: Impaired mobility for both equipment and involved personnel.
It means one way access to hatch into containment, lack of work platforms with
proper ladders, no cargo elevators where required, no elevator access to the
turbine deck, etc.
• Category VI: Miscellaneous. It includes items such as poor air conditioning,
lack of effective standardization, and high-temperature environment.
9.3 Desirable Human Factors Engineering MaintenanceRelated Attributes of a Power Plant’s Well-Designed
Systems and Elements Relating to Human
Performance that Can Contribute to a Successful
Maintenance Programme
There are many desirable human factors engineering maintenance-related attributes of a power plant’s well-designed systems. A survey-based study reported the
following 11 attributes [5]:
• Attribute I: Ease of servicing and inspection. It means ease of oil changes,
easy to spot problems, good access for preventive maintenance-related activities, etc.
• Attribute II: Ease of removal, disassembly, and repair. It means easy
removal of circuit breakers, modular design of rod controls, modules on roll-out
rails, etc.
• Attribute III: Effective movement and lifting capability. It means built-in
hoist always in place, access for vehicles, easy removal through roof, etc.
124
9
Human Factors in Power Plant Maintenance

---


### Page 133

• Attribute IV: Effective accessibility. It means good access to rod controls for
repair activities, easy access to repair compressors, good accessibility around the
diesels, etc.
• Attribute V: Avoidance of contaminated areas. It basically means, for
example, equipment placed in easily accessible locations well-outside areas
considered ‘‘hot’’.
• Attribute VI: Ease of system troubleshooting testing and monitoring. It
means control cabinet for boiler control easy to troubleshoot, engineered guards
easy to test, built-in calibration system, good test jacks, and easy to input
signals, etc.
• Attribute VII: Availability of all required tools. It means availability of all
types of tools required, for example, all types of special tools provided for a
complex assembly.
• Attribute VIII: Highly reliable equipment. It means reliable relays, highly
reliable engineered safeguards actuation system, air compressor easy to operate,
and rarely breaks down, etc.
• Attribute IX: Good lay down area. It basically means, for example, very good
lay down area for turbine generator.
• Attribute X: Good quality manuals and prints. It means detailed operating
instructions, readable prints, understandable procedures, etc.
• Attribute XI: Miscellaneous. It includes items such as frequent use of mockups for training and fail-safe design.
Additional information on the above attributes is available in Ref. [5].
There are many elements relating to human performance that can contribute to
a successful maintenance programme in a power plant. Six of these elements are
shown in Fig. 9.1 [6].
Additional information related to elements shown in Fig. 9.1 is available in
Ref. [6].
9.4 Performance Goals of a Power Plant that Drive
Decisions About Human Factors and a Study
of Human Factors in Power Plants
Past experiences clearly indicate that there are many performance goals of a power
plant that drive, directly or indirectly, maintenance-related decisions about human
factors. These goals may be categorized under the following three classiﬁcations
[7]:
• Classiﬁcation I: Plant productivity
• Classiﬁcation II: Plant availability
• Classiﬁcation III: Plant safety.
9.3
Desirable Human Factors Engineering Maintenance-Related Attributes
125

---


### Page 134

Classiﬁcation I goals include items such as improving efﬁciency, reliability, and
motivation of all involved personnel. Classiﬁcation II goals include increasing the
time period, the power plant can operate at its full power generation capacity by
reducing human errors that, directly or indirectly, contribute to equipment failures
or increase equipment corrective maintenance time. Finally, Classiﬁcation III
goals include minimizing injury to all involved personnel, damage to equipment/
system, and in the case of nuclear power plants, reducing the radiation exposure to
humans and eliminating altogether the potential for release of radioactivity to the
environment.
A study of maintenance in nine power generation plants (i.e., ﬁve nuclear and
four fossil fuel) in regard to human factors reported various types of, directly or
indirectly, human factors-related problems. This study was quite wide ranging in
scope, extending to an examination of items that included designs, environmental
factors, tools, procedures, facilities, spares, and organizational factors.
The ﬁndings of this study were grouped under 16 classiﬁcations shown in
Fig. 9.2 [3, 5]. Some of the classiﬁcations shown in the ﬁgure are described below.
Classiﬁcation I: environmental factors is concerned with human factors’
problems pertaining to environment and two examples of such problems are a high
variability of illumination and heat stress. An example of the problems belonging
to Classiﬁcation II: communications is an inadequate capacity of the existing
Elements 
Human performance 
program, including error 
prevention tools, and 
performance measures 
Good planning 
Design for maintainability 
Provision of appropriately 
trained and experienced 
maintenance personnel 
Strategies to learn from 
past experience 
Provision of usable, 
accurate and up to date 
maintenance procedures 
Fig. 9.1 Elements relating to human performance that can contribute to a successful
maintenance programme in a power plant
126
9
Human Factors in Power Plant Maintenance

---


### Page 135

communications system to meet the volume of communications’ trafﬁc needed
throughout the plant, particularly during outages.
Classiﬁcation III: facility design factors is concerned with, directly or indirectly, human factors’ problems pertaining to facility design and three examples of
such problems are poor temperature–ventilation control, high noise level, and
inadequate facility to store contaminated equipment. An example of the problems
belonging to Classiﬁcation IV: selection and training is the informality of the
training process, with no properly deﬁned selection criteria, and lacking validated
screening methods or tools.
Classifications 
Classification I: 
Environmental 
factors 
Classification 
VIII: Labeling 
and coding
Classification 
IX: Equipment 
maintainability
Classification II: 
Communications 
Classification III: 
Facility design 
factors 
Classification IV: 
Selection and 
training
Classification V: 
Personnel safety 
Classification VI: 
Anthropometrics and 
human strength 
Classification VII: 
Maintenance 
information, 
procedures, and 
manuals 
Classification X: 
Movement of 
humans and 
machines 
Classification XI: 
Maintenance stores, 
supplies, and tools 
Classification XII: 
Equipment 
protection 
Classification XIII: 
Productivity and 
organizational 
interfaces 
Classification XIV: 
Preventive 
maintenance and 
malfunction 
diagnosis 
Classification XV: 
Job practices 
Classification XVI: 
Maintenance errors 
and accidents 
Fig. 9.2 Classiﬁcations of the ﬁndings of a study of human factors in power plants
9.4
Performance Goals of a Power Plant
127

---


### Page 136

Classiﬁcation V: personnel safety is concerned with problems such as radiation
exposure, heat prostration, steam burns, and chemical burns. An example of the
problems belonging to Classiﬁcation VI: anthropometrics and human strength is the
lack of proper access to system/equipment requiring maintenance. Classiﬁcation
VII: maintenance information, procedures, and manuals are concerned with human
factors-related problems such as inadequate manuals and poorly written procedures.
Three examples of the problems belonging to Classiﬁcation VIII: labelling and
coding are unsystematic replacement of labels lost or obscured over time, high
likelihood of the occurrence of maintenance errors in multi-unit plants in which
units are identical or very similar in appearance, and poorly descriptive label tags.
An example of a problem belonging to Classiﬁcation IX: equipment maintainability is the placement of units/parts/components of equipment in locations that
are difﬁcult to access from a normal work position.
Information on the remaining classiﬁcations is available in Refs. [3, 5].
9.5 Advantages of Human Factors Engineering
Applications in Power Plants
Various studies conducted over the years have clearly indicated that there are
many advantages of human factors engineering applications in the area of power
plant maintenance [3, 4]. Nonetheless, the advantages of the application of human
factors engineering in the area of power generation in general that directly or
indirectly concern maintenance may be grouped under two main categories as
shown in Fig. 9.3 [7–10].
Category I: reductions includes the following reduction-related advantages:
• Reduction in needless costs.
• Reduction in the occurrence of human error.
• Reduction in number and qualiﬁcations of personnel required.
• Reduction in consequences of human error (i.e., number and severity of injuries
and damage to equipment).
• Reduction in job dissatisfaction of personnel (i.e., absenteeism and turnover).
• Reduction in training requirements and attrition.
• Reduction in wasted time and motion.
Category II: increments includes the following increment-related advantages:
• Increases in safety, productivity, and availability.
• Increases in reliability and efﬁciency of personnel performance.
• Increases in adequacy of communications.
• Increases in job satisfaction of personnel (i.e., motivation, conﬁdence, and
commitment to achieving plant goals).
• Increases in cost-effectiveness of training.
128
9
Human Factors in Power Plant Maintenance

---


### Page 137

9.6 Human Factors’ Methods to Assess and Improve
Power Plant Maintainability
There are many human factors methods that can be used for assessing and improving
power plant maintainability. Five of these methods are as follows [3, 4, 11]:
• Critical incident method
• Task analysis
• Structured interviews
• Maintainability checklist
• Potential accident/damage analyses.
All of the above methods are described below, separately.
9.6.1 Critical Incident Method
Various studies conducted, over the years, clearly indicate that the history of
maintenance errors, near-mishaps, or accidents can provide very useful information concerning needed maintainability-related improvements. The critical incident method is a very useful tool for examining such case histories with respect to
human factors. The application of this method calls for making appropriate
arrangements to meet individually with appropriate personnel of maintenance
organization under consideration. During the meeting, each of these individuals is
asked the following three questions:
• Question No. 1: Give one example of a plant system or unit of equipment that
‘‘in your opinion’’ is well ‘‘human-engineered’’ or simple and straightforward to
maintain, and describe the system/unit by emphasizing the appropriate features
that clearly makes it good from the perspective of maintainers.
• Question No. 2: Give one example of a maintenance accident, near mishap, or
error with serious or potentially serious consequences, based on your personal
experience over the time period. Furthermore, describe all the speciﬁcs of the case
involved and indicate all the possible ways the situation could have been averted.
Main categories 
Category I: 
Reductions 
Category II: 
Increments 
Fig. 9.3 Main categories of advantages of the application of human factors engineering in power
generation
9.5
Advantages of Human Factors Engineering Applications in Power Plants
129

---


### Page 138

• Question No. 3: Give one example of a plant system or unit of equipment that
‘‘in your opinion is not properly human-engineered’’ or is poorly designed from
the perspective of maintenance personnel and that has caused or could cause a
safety hazard, a human error, or damage to equipment.
After analysing the collected data, necessary changes required for improvements are recommended.
9.6.2 Task Analysis
This method is used to assess the needs of equipment maintainers for effectively
working with hardware to perform a speciﬁed task. The analyst, in addition to
making careful observations concerning impediments to effective maintainability,
records and oversees each task element and completion and start times. The
observations are grouped under the following 16 classiﬁcation [3, 4]:
• Maintenance crew interactions
• Training needs
• Equipment maintainability design features
• Facility design features
• Decision-making factors
• Availability of necessary maintenance-related information (e.g., manuals, procedures, and schematics)
• Lifting or movement aids
• Workshop adequacy
• Environmental factors
• Access factors
• Tools and job aids
• Supervisor–subordinate relationships
• Communication
• Equipment damage potential
• Spare-parts retrieval
• Personnel hazards.
Additional information on this approach is available in Ref. [11].
9.6.3 Structured Interviews
This is one of the most efﬁcient methods used for collecting maintainability data in
the shortest possible time period. The method is based on the assumption that
repair persons and their supervisors and others close to equipment/system
130
9
Human Factors in Power Plant Maintenance

---


### Page 139

maintainability problems, normally provide most useful information regarding
difﬁculties involved in performing their tasks the best possible way.
A ﬁxed set of questions such as presented below are asked during a structured
interview [3, 11].
• Is our workshop facility sized properly for accommodating effectively all the
personnel in your organization?
• Is your workshop facility arranged appropriately so that it allows safe and
efﬁcient performance of all types of maintenance tasks?
• Are appropriate workbenches and lay down areas provided?
• How well is your workshop facility integrated into the overall plant design?
• How would you describe the surrounding environment in your workshop facility
in regard to factors such as illumination, noise, and ventilation?
After analysing the data collected by asking questions such as above, necessary
recommendations for improvements are made. Additional information on structured interviews is available in Ref. [11].
9.6.4 Maintainability Checklist
This is a quite useful method and is based basically on the survey study reported in
Ref. [5]. The checklist is divided into the following 14 distinct topical areas [4, 5]:
• Equipment/system maintainability
• Equipment/system protection
• Personnel safety
• Maintenance information
• Anthropometrics and human strength
• Facilities
• Preventive maintenance
• Tools, spares, and stores
• Environmental factors
• Coding and labelling
• Communications
• Selection and training
• Job and organizational factors
• Radiation protection.
After analysing the information collected in the above 14 areas, appropriate
decisions are made. Additional information on maintainability checklist is available in Ref. [11].
9.6
Human Factors Methods to Assess and Improve Power Plant Maintainability
131

---


### Page 140

9.6.5 Potential Accident/Damage Analyses
This is a structured method often used for assessing the accident, damage, or
potential error inherent in a given task. The starting point for determining the
potential for the occurrence of mishaps in the performance of a given maintenance
task is to establish a procedure that describes effectively the task under consideration. Subsequently, the interviewer of the interviewee (e.g., repair person) asks
the following question for each task element [3, 11]:
Is there high, medium, or low chances for the occurrences of an error/an
accident/damage to system/equipment/unit in carrying out, say, Step X?
After analysing all the collected data, recommendations for changes to items
such as system/equipment/unit, procedures, and facility are made. Additional
information on potential accident/damage analyses is available in Ref. [11].
9.7 Problems
1. Discuss power plant systems’ human factors engineering maintenance-related
shortcomings.
2. What are the desirable human factors engineering maintenance-related attributes of a power plant’s well-designed systems?
3. Discuss at least six elements relating to human performance that can contribute to a successful maintenance programme.
4. Discuss the three classiﬁcations of performance goals of a power plant that drive
directly or indirectly, maintenance-related decisions about human factors.
5. What are the advantages of human factors engineering applications in power
plants?
6. Describe at least three human factors methods that can be used to assess and
improve power plant maintainability.
7. Compare critical incident method with task analysis.
8. Write an essay on human factors in power plant maintenance.
9. Discuss the classiﬁcations of the ﬁndings of the study of human factors in
power plants.
10. Write down at least ﬁve questions that can be asked during a structured
interview.
References
1. US Nuclear Regulatory Commission (1975) Reactor safety study: an assessment of accident
risks in US commercial nuclear power plants. Report No. WASH-1400, US Nuclear
Regulatory Commission, Washington
132
9
Human Factors in Power Plant Maintenance

---


### Page 141

2. Seminara JL, Gonzalez WR, Parsons SO (1976) Human factors review of nuclear power plant
control room design. Report No. EPRI NP-309, Electric Power Research Institute (EPRI),
Palo Alto
3. Seminara JL, Parsons SO (1985) Human factors engineering and power plant maintenance.
Maintenance Manage Int 6:33–71
4. Dhillon BS (2009) Human reliability, error, and human factors in engineering maintenance:
with reference to aviation and power generation. CRC Press, Boca Raton
5. Seminara JL, Parsons SO (1981) Human factors review of power plant maintainability.
Report No. EPRI NP-1567, Electric Power Research Institute, Palo Alto
6. Penington J, Shakeri S (2006) A human factors approach to effective maintenance. In:
Proceedings of 27th annual Canadian Nuclear Society (CNS) conference, pp 1–11
7. Kinkade RG (1988) Human factors primer for nuclear utility managers. Report No. EPRI NP5714, Electric Power Research Institute, Palo Alto
8. Shriver EL, Zach SE, Foley JP (1982) Test of job performance aids for power plants. Report
No. EPRI NP. 2676, Electric Power Research Institute, Palo Alto
9. Pariftt B (1986) First use: frozen water garment use at TMI-2. Report No. EPRI 4102B (RP
1705), Electric Power Research Institute, Palo Alto
10. Annual Report (1982) Electric Power Research Institute, Palo Alto
11. Seminara JL (1982) Human factors methods for assessing and enhancing power plant
maintainability. Report No. EPRI NP-2360, Electric Power Research Institute, Palo Alto
References
133

---


### Page 142

Chapter 10
Human Error in Power Plant
Maintenance
10.1 Introduction
In power plants, maintenance is an important activity and it consumes a signiﬁcant
proportion of the total amount of money spent on power generation. A number of
studies conducted over the years indicate that human error in maintenance is an
important factor in the occurrence of power generation safety-related incidents [1,
2]. For example, a study of nuclear power plant operating experiences reported that
due to errors in the maintenance of some motors in the rod drives, many motors ran in
a backward direction and withdrew rods altogether, rather than inserting them [3].
Maintenance error cost in power plant maintenance, including opportunity costs
and restoration costs, is potentially very high, the damage impact on the involved
equipment/system may decrease its life signiﬁcantly, and very serious potential
hazards to humans may occur. Therefore, because of potentially very serious
consequences such as these to human safety and equipment/system function, the
prevention of the occurrence of human errors in maintenance-related tasks is
receiving increasing attention in power generation.
This chapter presents various important aspects of human errors in the area of
power plant maintenance.
10.2 Facts, Figures, and Examples
Some of the facts, ﬁgures, and examples directly or indirectly concerned with
human error in power plant maintenance are presented below.
• As per Refs. [4, 5], a number of studies reported that between 55 and 65 %,
human-performance-related problems surveyed in the area of power generation
were concerned with maintenance activities.
• As per Ref. [6], 25 % of unexpected shutdowns in Korean nuclear power plants
were due to human errors, out of which more than 80 % of human errors were
resulted from usual testing and maintenance tasks.
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_10,
 Springer International Publishing Switzerland 2014
135

---


### Page 143

• As per Ref. [9], during the period from 1965 to 1995, a total of 199 human errors
occurred in Japanese nuclear power plants, out of which 50 of them were
concerned with maintenance tasks.
• As per Ref. [8], in the state of Florida, on Christmas Day in 1989, two nuclear
reactors were shut down due to maintenance error and caused rolling blackouts.
• As per Ref. [9], maintenance errors account for around 60 % of the annual
power loss due to human errors in fossil power plants.
• In 1990, in the area of nuclear power generation, a study of 126 human-errorrelated signiﬁcant events revealed that about 42 % of the problems were linked
to modiﬁcation and maintenance [4].
• In the late 1990s, a blast at the Ford Rouge power plant in Dearborn, Michigan,
due to a maintenance error killed six workers and injured many others [10, 11].
• A study of over 4,400 maintenance-related history records concerning a boiling
water reactor (BWR) nuclear power plant covering the period from 1992 to 1994
revealed that about 7.5 % of all failure records could be attributed to human
errors related to maintenance activities [12, 13].
10.3 Maintenance Tasks Most Susceptible to Human Error
in Power Generation and Types of Human Errors
in Digital Plant Protection Systems Maintenance
Tasks
Over the years, various studies have been performed to identify maintenance tasks
most susceptible to human error in power generation. As the result of these studies,
the following ﬁve maintenance tasks in the area of nuclear power generation are
found most susceptible to human error [14]:
• Replace reactor coolant pump (RCP) seals.
• Overhaul motor-operated valve (MOV) actuator.
• Test reactor protection system (RPS).
• Overhaul main feed water pump (MFWP).
• Overhaul mainstream isolation valves (MSIV).
In order to take advantage of digital technology, nowadays analogue RPSs are
being replaced by the DPPS. The scope of the occurrence of human error incidence
in DPPS during the performance of a maintenance task is very high, ranging from
missing an important step of work procedure to intentional deviation of work
procedure from the proper work procedure, in order to accomplish the task easily
in uncomfortable environment or save time.
As the result of DPPS maintenance task analysis and published literature survey, the types of human errors in DPPS maintenance tasks are shown in Fig. 10.1
[15, 16].
136
10
Human Error in Power Plant Maintenance

---


### Page 144

These errors are calibration error, quality error, installation/repair error, resetting
error, restoration error, and bypass error. ‘‘Calibration error’’ is associated with an
incorrect setting of trip limits or references. ‘‘Quality error’’ occurs basically due to
carelessness and limited space for work or transport. Two examples of this type of
error are too little or too much tightening of screws and deﬁcient soldering/welding
joints or insulation. ‘‘Installation/repair error’’ occurs when faulty parts are repaired
or replaced during the refuelling maintenance process as a corrective or preventive
measure.
‘‘Resetting error’’ and ‘‘restoration error’’ occur from a failure to reset bistable
process parameters after completion of a test and from an oversight to restore the
system after completion of maintenance or a test, respectively. Finally, ‘‘bypass
error’’ results whenever a channel is bypassed to carry out tests in that very channel.
10.4 Causal Factors for Critical Incidents and Reported
Events Related to Maintenance Error in Power Plants
and Classiﬁcations of Causes of Human Error
in Power Plant Maintenance
There are many causal factors for critical incidents and reported events related to
maintenance error in power plants. A study has identiﬁed ten causal factors presented in Table 10.1, in order of lowest to highest frequency of occurrence, for
critical incidents and reported events concerned with maintenance error in power
plants [17, 18].
‘‘Oversights by maintenance personnel’’ and ‘‘adverse environment factors’’ are
the seventh (or the least) most frequently occurring causal factors. ‘‘Oversights by
maintenance personnel’’ are a small fraction of those errors that would be quite
difﬁcult to anticipate and ‘‘design out’’ of power plants. The ‘‘adverse environmental factors’’ include items such as the requirement for wearing protective
Installation/repair 
error
Resetting error
Quality error
Calibration error
Bypass error
Restoration error
Types of 
human
errors
Fig. 10.1 Types of human errors in digital plant protection systems (DPPS) maintenance tasks
10.3
Maintenance Tasks Most Susceptible to Human Error in Power Generation
137

---


### Page 145

devices and garments in threatening environments that, in turn, restrict movement
capabilities and visual ﬁeld of a person, and the encouragement of haste by the
need for minimizing stay time in, say, radioactive environments.
‘‘Poor work practices’’ are the sixth most frequently occurring causal factor.
Two examples of poor work practices are not taking the time required to erect a
scaffold properly so that an item in mid-air can be accessed safely and not waiting
for operators to accomplish the tagging and switching tasks necessary for disabling
the systems requiring attention. ‘‘Problems in facility design’’, ‘‘poor unit and
equipment identiﬁcation’’, and ‘‘poor training’’ are the ﬁfth most frequently
occurring causal factors. ‘‘Problems in facility design’’ can contribute to accidents,
and some examples of these problems are as follows:
• Insufﬁcient clearances for repair workers.
• Inadequate equipment or transportation aids in the performance of maintenance
tasks.
• Inadequately sized facilities causing an overly dense packaging of equipment
systems and preventing proper performance of inspection or repair tasks.
‘‘Poor unit and equipment identiﬁcation’’ is the cause of an unexpectedly rather
high number of accidents, and frequently, the problem is between identical items
and time-to-time incorrect identiﬁcation of potential hazards. ‘‘Poor training’’ is
basically concerned with repair workers’ unfamiliarity with the task or their lack
of full awareness of the system characteristics and inherent dangers associated with
the task under consideration.
‘‘Problems in moving equipment or people’’ are the fourth most frequently
occurring causal factor. These problems usually stem from the inability to use
proper vehicular aids in shifting heavy units of equipment or from poor lifting
capability. ‘‘Deﬁciencies in equipment design’’ are the third most frequently
Table 10.1 Causal factors, in order of lowest to highest frequency of occurrence, for critical
incidents and reported events concerned with maintenance error in power plants
Causal factor
no.
Causal factor frequency of
occurrence
Causal factor
1
Lowest
• Oversights by maintenance personnel
2
• Adverse environmental factors
3
• Poor work practices
4
• Problems in facility design
5
• Poor unit and equipment identiﬁcation
6
• Poor training
7
• Problems in moving equipment or people
8
• Deﬁciencies in equipment design
9
• Problems in tagging and clearing equipment for
maintenance
10
Highest
• Faulty procedures
138
10
Human Error in Power Plant Maintenance

---


### Page 146

occurring causal factor for near-accidents/accidents revolved about equipmentdesign-associated problems. The factor includes items such as follows:
• The equipment not designed with proper mechanical safeguards to prevent the
substitution of incorrect part for the correct replacement part.
• Poorly designed and inherently unreliable parts.
• Parts placed in inaccessible locations.
• Equipment installed incorrectly from the outset.
‘‘Problems in tagging and clearing equipment for maintenance’’ are the second
most frequently occurring causal factor in reported cases where potentially serious
accidents/serious accidents could be attributed to an error/failure, directly or
indirectly, concerned with the equipment clearance activities. ‘‘Faulty procedures’’
are the most frequently (highest/greatest) occurring causal factor in the mishaps
reported. It incorporates items such as lack of adherence to a give procedure,
wrong procedures, lack of speciﬁcity, and incompleteness. The following is a good
example of faulty procedures:
Due to poor judgement and not properly following prescribed guidelines, a ground was left
on a circuit breaker. When the equipment/system was put back into service, the circuit
breaker blew up and resulted in extensive property damage.
In this situation, the correct procedure would have called for clearing the
ground before turning on the circuit breaker to its speciﬁed service.
Past experiences over the years indicate that there are many causes of human
error in power plant maintenance. On the basis of characteristics obtained from
modelling the maintenance task, causes for the occurrence of human errors in
power plant maintenance may be categorized under the following four classiﬁcations [2]:
• Classiﬁcation I: design shortcomings in hardware and software. These
shortcomings include items such as deﬁciencies in the design of controls and
displays, incorrect or confusing procedures, and insufﬁcient communication
equipment.
• Classiﬁcation II: disturbances of the external environment. Some examples
of these disturbances are the physical conditions such as temperature, ventilation, humidity, and ambient illumination.
• Classiﬁcation III: induced circumstances. Some examples of these circumstances are momentary distractions, emergency conditions, and improper communications, which may result in failures.
• Classiﬁcation IV: human ability limitations. A good example of these limitations is the limited capacity of short-term memory in the internal control
mechanism.
10.4
Causal Factors for Critical Incidents and Reported Events
139

---


### Page 147

10.5 Steps for Improving Maintenance-Related Procedures
in Power Plants
Past experiences over the years clearly indicate that improving maintenancerelated procedures in the area of power generation can be very useful, to reduce the
occurrence of performance errors along with a corresponding increase in unit
reliability. The upgrade of a maintenance procedure, generally, can be accomplished by following the eight steps shown in Fig. 10.2 [19].
It is to be noted that an improved or upgraded maintenance procedure can
substantially contribute, directly or indirectly, to many diverse areas including
fewer human-performance-related errors, higher level of employee morale, identiﬁcation of necessary plant modiﬁcations, better unit reliability, and identiﬁcation
of required training. Additional information on this topic is available in Ref. [19].
10.6 Useful Guidelines to Reduce and Prevent Human
Errors in Power Plant Maintenance
Over the years, professionals working in the area of power generation have proposed various guidelines to reduce and prevent human errors in power plant
maintenance. Four of these guidelines considered most useful are shown in
Fig. 10.3 [2].
The guideline ‘‘perform administrative policies more thoroughly’’ basically
means motivating personnel involved in maintenance properly to comply with
prescribed quality control procedures. The guideline ‘‘revise training programs for
all involved maintenance personnel’’ basically means that training programs for
personnel involved in maintenance should be revised as per the characteristic and
frequency of occurrence of each extrinsic cause. The guideline ‘‘develop proper
work safety checklists for maintenance personnel’’ basically means that maintenance personnel should be provided with appropriate work safety checklists, which
can be effectively used to determine the possibility of occurrence of human error
as well as the factors that may affect their actions before or subsequent to the
performance of maintenance tasks.
Finally, the guideline ‘‘ameliorate design shortcomings’’ calls for overcoming
shortcomings in areas such as plant layout, work environment, labelling, and
coding, as shortcomings in design can reduce attention to the tasks and may even
induce human errors. Additional information on the guidelines shown in Fig. 10.3
is available in Ref. [2].
140
10
Human Error in Power Plant Maintenance

---


### Page 148

10.7 Methods for Performing Human Error Analysis
in Power Plant Maintenance
There are many methods or models that can be used to perform human error
analysis in power plant maintenance. Three of these methods/models are described
below.
Select a procedure to be upgraded by considering factors such as
Step 1
user inputs and relative importance of the procedure
Step 3
Review the procedure for agreement with the procedure 
development guidelines
Step 4
Conduct the preliminary validation of the procedure to determine 
its usability
Step 2
Review the procedure with respect to items such as device
nomenclature, require test equipment, limits, step sequence, 
prerequisites, and precautions
Step 5
Rewrite the procedure by taking into consideration the results of
Steps 2, 3, and 4
Step 6
Review the revised procedure with respect to technical accuracy
and agreement with the “Procedure Development Guide”
Step 7
Evaluate the revised procedure with respect to its usability by 
those responsible for performing it
Step 8
Approve the upgraded procedure by involving appropriate 
supervisory and management personnel
Fig. 10.2 Steps for upgrading a maintenance procedure
10.6
Useful Guidelines to Reduce and Prevent Human Errors in Power
141

---


### Page 149

10.7.1 Maintenance Personnel Performance Simulation
(MAPPS) Model
This model was developed by the Oak Ridge National Laboratory to provide
estimates of performance measures of nuclear power plant maintenance manpower, and its development was sponsored by the United States Nuclear Regulatory Commission (NRC) [20]. The main objective for its development was the
pressing need for and lack of a human reliability data bank pertaining to nuclear
power plant maintenance-related tasks, for application in conducting probabilistic
risk-assessment-related studies.
Some of the performance measures estimated by the MAPPS model are as
follows:
• Probability of successfully accomplishing the task of interest.
• Probability of an undetected error.
• Identiﬁcation of the most and least likely error-prone sub elements.
• Maintenance team stress proﬁles during task execution.
Finally, it is added that MAPPS model is an excellent tool to estimate important
maintenance-related parameters and its ﬂexibility allows it to be used in a wide
variety of studies dealing with nuclear power plant maintenance activity.
Additional information concerning this model (i.e. MAPPS model) is available
in Ref. [20].
10.7.2 Markov Method
This method is often used to perform probability analysis of repairable engineering
systems, and it can also be used to perform human error analysis in the area of
Guidelines
Revise training programs 
for all involved 
maintenance personnel
Develop proper work 
safety checklists for 
maintenance personnel
Perform administrative 
policies more thoroughly
Ameliorate design 
shortcomings
Fig. 10.3 Useful guidelines to reduce and prevent human errors in power plant maintenance
142
10
Human Error in Power Plant Maintenance

---


### Page 150

power plant maintenance. The method is described in detail in Chap. 4. Its
application to perform human error analysis in the area of power plant maintenance is demonstrated through the following mathematical model:
Model
This mathematical model represents a power plant system that can only fail due to
non-maintenance-related failures, but the occurrence of maintenance error
degrades its performance. The power plant system state space diagram is shown in
Fig. 10.4. Numerals in boxes and circle denote power plant system states.
The following assumptions are associated with the model:
• Maintenance error causes power plant system degradation, but not failure.
• The completely or partially failed power plant system is repaired.
• The power plant system can fail from its degraded state due to failures other
than maintenance errors.
• The power plant system maintenance error and non-maintenance error failure
rates are constant.
• All power plant system repair rates are constant, and the repaired system is as
good as new.
The following symbols are associated with the model:
j
is the power plant system state j; for j = 0 (power plant system operating
normally), j = 1 (power plant system degraded due to maintenance error),
and i = 2 (power plant system failed)
Pj(t)
is the probability that the power plant system is in state j at time t; for
j = 0, 1, 2
k1
is the power plant system constant failure rate
k2
is the power plant system constant maintenance error rate
k3
is the power plant system constant failure rate when in degraded state
l1
is the power plant system constant repair rate from fully failed state (i.e.
state 2)
Power plant 
system 
degraded due to 
maintenance 
error
1
Power plant 
system operating 
normally
0
Power plant 
system failed
2
1
λ
2
λ
3
λ
2
μ
1
μ
3
μ
Fig. 10.4 Power plant system state space diagram
10.7
Methods for Performing Human Error Analysis in Power Plant Maintenance
143

---


### Page 151

l2
is the power plant system constant repair rate from degraded state (i.e. state 1)
l3
is the power plant system constant repair rate from fully failed state (i.e.
state 2) to degraded state (i.e. state 1).
By using the Markov method described in Chap. 4, we write down the following equations for Fig. 10.4 state space diagram:
d P0ðtÞ
dt
þ k1 þ k2
ð
ÞP0ðtÞ ¼ l2P1ðtÞ þ l1P2ðtÞ
ð10:1Þ
d P1ðtÞ
dt
þ l2 þ k3
ð
ÞP1ðtÞ ¼ l3P2ðtÞ þ k2P0ðtÞ
ð10:2Þ
d P2ðtÞ
dt
þ l1 þ l3
ð
ÞP2ðtÞ ¼ k1P0ðtÞ þ k3P1ðtÞ
ð10:3Þ
At time t = 0, P0ð0Þ ¼ 1; P1ð0Þ ¼ 0; and P2ð0Þ ¼ 0:
By solving Eqs. (10.1–10.3), we get
P0ðtÞ ¼ l2l1 þ k3l1 þ l2l3
X1X2
þ l2X1 þ l1X1 þ l3X1 þ X1k3 þ X2 þ l2l1 þ k3l1 þ l2l3
X1 X1  X2
ð
Þ


e X1t
þ
1  l2l1 þ k3l1 þ l2l3
ð
Þ
X1X2

 l2X1 þ l1X1 þ l3X1 þ X1k3 þ X2
1 þ l2l1 þ k3l1 þ l2l3
X1 X1  X2
ð
Þ


e X2t
ð10:4Þ
where
X1; X2 ¼ A 
A2  4 l2l1 þ k3l1 þ l2l3 þ l1k2 þ k2l3 þ k2k3 þ l2k1 þ k1l3 þ k1k3



	1=2
h
i
=2
A ¼ k2 þ k1 þ k3 þ l2 þ l1 þ l3
X1X2 ¼ l2l1 þ k3l1 þ l2l3 þ l1k2 þ k2l3 þ k2k3 þ l2k1 þ k1l3 þ k1k3
P1ðtÞ ¼ k2l1 þ k2l3 þ k1l3
X1X2
þ X1k2 þ k2l1 þ k2l3 þ k1l3
X1 X1  X2
ð
Þ


e X1t
 k2l1 þ k2l3 þ k1l3
X1X2
þ X1k2 þ k2l1 þ k2l3 þ k1l3
X1 X1  X2
ð
Þ


e X2t
ð10:5Þ
P2ðtÞ ¼ k2k3 þ l2k1 þ k1k3
X1X2
þ X2k1 þ k2k3 þ k1l2 þ k1k3
X1 X1  X2
ð
Þ


e X1t
 k2k3 þ l2k1 þ k1k3
X1X2
þ X1k1 þ k2k3 þ k1l2 þ k1k3
X1 X1  X2
ð
Þ


e X2t
ð10:6Þ
144
10
Human Error in Power Plant Maintenance

---


### Page 152

The probability of power plant system degradation due to maintenance error is
expressed by Eq. (10.5). As time t becomes very large, Eq. (10.5) reduces to
P1 ¼ k2l1 þ k2l3 þ k1l3
X1X2
ð10:7Þ
where
P1
is the steady-state probability of power plant system degradation due to
maintenance error.
The power plant system time-dependent operational availability is expressed by
PSOAVðtÞ ¼ P0ðtÞ þ P1ðtÞ
ð10:8Þ
where
PSOAV(t)
is the power plant system operational availability at time t.
As time t becomes very large, Eq. (10.8) reduces to
PSOAV ¼ l2l1 þ k3l1 þ l2l3 þ k2l1 þ k2l3 þ k1l3
X1X2
ð10:9Þ
where
PSOAV
is the power plant system steady-state operational availability.
Example 10.1 Assume that for a power system, the following data values are
given:
• k1 ¼ 0:005 failures per hour
• l1 ¼ 0:04 repairs per hour
• k2 ¼ 0:0003 failures per hour
• l2 ¼ 0:007 repairs per hour
• k3 ¼ 0:002 failures per hour
• l3 ¼ 0:08 repairs per hour
Calculate the power plant system degradation steady-state probability due to
maintenance error with the aid of Eq. (10.7).
By inserting the speciﬁed data values into Eq. (10.7), we obtain
P1 ¼
0:0003
ð
Þ 0:04
ð
Þ þ 0:0003
ð
Þ 0:08
ð
Þ þ 0:005
ð
Þ 0:08
ð
Þ
½
= 0:007
ð
Þ 0:04
ð
Þ þ 0:002
ð
Þ 0:04
ð
Þ
½
þ 0:007
ð
Þ 0:08
ð
Þ þ 0:04
ð
Þ 0:0003
ð
Þ þ 0:0003
ð
Þ 0:08
ð
Þ þ 0:0003
ð
Þ 0:002
ð
Þ
þ 0:007
ð
Þ 0:005
ð
Þ þ 0:005
ð
Þ 0:08
ð
Þ þ 0:005
ð
Þ 0:002
ð
Þ
¼ 0:3110
Thus, the power plant system degradation steady-state probability due to
maintenance error is 0.3110.
10.7
Methods for Performing Human Error Analysis in Power Plant Maintenance
145

---


### Page 153

10.7.3 Fault Tree Analysis
This method is often used to perform various types of reliability-related analysis in
the area of power generation [21, 22]. The method is described in Chap. 4. The
application of the method to perform human error analysis in power plant maintenance is demonstrated through the example presented below.
Example 10.2 A system used in a power plant can fail due to a maintenance error
caused by any of the following four factors:
• Carelessness.
• Poor work environment.
• Poor system design.
• Use of poorly written maintenance manuals.
Two major factors for carelessness are time constraints and poor training.
Similarly, two factors for poor work environment are distractions and poor
lighting.
Develop a fault tree for the top event ‘‘power plant system failure due to a
maintenance error’’ by using fault tree symbols given in Chap. 4.
A fault tree for this example is shown in Fig. 10.5.
Example 10.3 Assume that the occurrence probability of each basic event X1, X2,
X3, X4, X5, and X6 shown in Fig. 10.5 is 0.02. For independent events, calculate the
occurrence probabilities of the top event T (i.e. power plant system failure due to a
maintenance error) and intermediate events I1 (i.e. poor work environment) and I2
(i.e. carelessness). Also, redraw Fig. 10.5 fault tree with given and calculated fault
event occurrence probability values.
With the aid of Chap. 4 and the speciﬁed data values, we obtain the values of I1,
I2, and T as follows:
PðI1Þ ¼ PðX1Þ þ PðX2Þ  PðX1ÞPðX2Þ
¼ 0:02 þ 0:02  0:02
ð
Þ 0:02
ð
Þ
¼ 0:0396
ð10:10Þ
where
P(X1), P(X2), and P(I1)
are the occurrence probabilities of events X1, X2, and I1,
respectively.
The occurrence probability of event I2 is given by
PðI2Þ ¼ PðX3Þ þ PðX4Þ  PðX3ÞPðX4Þ
¼ 0:02 þ 0:02  0:02
ð
Þ 0:02
ð
Þ
¼ 0:0396
ð10:11Þ
146
10
Human Error in Power Plant Maintenance

---


### Page 154

where
P(X3), P(X4), and P(I2)
are the occurrence probabilities of events X3, X4, and I2,
respectively.
With the aid of the above calculated and speciﬁed data values and Chap. 4, we
obtain
PðTÞ ¼ 1  1  P I1
ð Þ
f
g 1  P I2
ð Þ
f
g 1  P X5
ð
Þ
f
g 1  P X6
ð
Þ
f
g
¼ 1  1  0:0396
ð
Þ 1  0:0396
ð
Þ 1  0:02
ð
Þ 1  0:02
ð
Þ
¼ 0:1141
ð10:12Þ
where
P(T), P(X5), and P(X6)
are the occurrence probabilities of events T, X5, and X6,
respectively.
Thus, the occurrence probabilities of events T, I1, and I2 are 0.1141, 0.0396, and
0.0396, respectively. Figure 10.5 fault tree with given and calculated fault event
occurrence probability values is shown in Fig. 10.6.
Power plant system 
failure due to a 
maintenance error
Carelessness
Poor 
system 
design
Use of 
poorly 
written 
maintenance 
manuals
Distractions
Poor 
lighting
Time
consstraints
Poor 
training
5
X
6
X
1
X
2
X
3
X
T
Poor work 
environment
2I
1I
4
X
Fig. 10.5 Fault tree for Example 10.2
10.7
Methods for Performing Human Error Analysis in Power Plant Maintenance
147

---


### Page 155

10.8 Problems
1. Write an essay on human error in power plant maintenance.
2. List at least six facts and ﬁgures concerned with human error in power plant
maintenance.
3. What are the maintenance tasks in the area of nuclear power generation most
susceptible to human error?
4. Discuss the types of human errors in DPPS maintenance tasks.
5. Discuss causal factors for critical incidents and reported events related to
maintenance error in power plants.
6. What are the classiﬁcations of causes of human errors in power plant maintenance? Discuss each of these classiﬁcations.
7. Discuss steps for improving maintenance-related procedures in power plants.
8. Discuss useful guidelines to reduce and prevent human errors in power plant
maintenance.
9. What is MAPPS model? Describe it in detail.
10. Prove Eq. (10.7) using Eq. (10.5).
0.1141
0.0396
0.0396
0.02
0.02
0.02
0.02
0.02
T
1I
5
X
6
X
1
X
0.02
2I
2
X
3
X
4
X
Fig. 10.6 A fault tree with given and calculated fault event occurrence probability values
148
10
Human Error in Power Plant Maintenance

---


### Page 156

References
1. Dhillon BS (2009) Human reliability, error, and human factors in engineering maintenance.
CRC Press, Boca Raton
2. Wu TM, Hwang SL (1989) Maintenance error reduction strategies in nuclear power plants,
using root cause analysis. Appl Ergon 20(2):115–121
3. Nuclear power plant operating experiences, from the IAEA/NEA incident reporting system.
Organization for Economic Co-operation and Development (OECD), Paris (2000)
4. Reason J (1997) Human Factors in nuclear power generation: a systems perspective. Nucl
Europe Worldscan 17(5–6):35–36
5. ‘‘An Analysis of 1990 Signiﬁcant Events’’, Report No. INPO 91-018, Institute of Nuclear
Power Operations (INPO), Atlanta (1991)
6. Heo G, Park J (2009) Framework of quantifying human error effects in testing and
maintenance. In: Proceedings of the sixth American nuclear society international topical
meeting
on
nuclear
plant
instrumentation,
control,
and
human-machine
interface
technologies, pp 2083–2092
7. Hasegawa T, Kameda A (1998) Analysis and evaluation of human error events in nuclear
power plants. Presented at the Meeting of the IAEA’s CRP on ‘‘collection and classiﬁcation
of human reliability data for use in probabilistic safety assessments’’, May 1998. Available
from the Institute of Human Factors, Nuclear Power Engineering Corporation, 3-17-1,
Toranomon, Minato-Ku, Tokyo, Japan
8. Maintenance Error a Factor in Blackouts, Miami Herald, 29 Dec 1989, p 4
9. Daniels RW (1985) The formula for improved plant maintainability must include human
factors. In: Proceedings of the IEEE conference on human factors and nuclear safety,
pp 242–244
10. The UAW and the rouge explosion: a pat on the head, Detroit News, Detroit, 6 Feb 1999, p 6
11. White J (2000) New revelations expose company-union complicity in Fatal Blast at US Ford
Plant. http://www.wsws.org/articles/2000/feb2000/ford-fo4.shtml
12. Pyy P, Laakso K, Reiman L (1997) A study of human errors related to NPP maintenance
activities. In: Proceedings of the IEEE 6th annual human factors meeting, pp 1223–1228
13. Pyy P (2001) An analysis of maintenance failures at a nuclear power plant. Reliab Eng Syst
Saf 72:293–302
14. Isoda H, Yasutake JY (1992) Human factors interventions to reduce human errors and
improve productivity in maintenance tasks. In: Proceedings of the international conference on
design and safety of advanced nuclear power plants, pp 3441–3446
15. Khalaquzzaman M, Kang HG, Kim MC, Seong PH (2010) A Model for estimation of reactor
spurious shutdown rate considering maintenance human errors in reactor protection system of
nuclear power plants. Nucl Eng Des 240:2963–2971
16. DPPS Maintenance Manual, Ulchin Nuclear Power Plant Unit No. 586, Document No. 9-650Z-431-100, Westinghouse Corporation, Butler County, Pennsylvania (2002)
17. Seminara JL, Persons SO (1981) Human factors review of power plant maintainability.
Report No. NP-1567 (Research Project 1136), Electric Power Research Institute, Palo Alto
18. Seminara JL, Persons SO (1985) Human factors engineering and power plant maintenance.
Maintenance Manage Int 6:33–71
19. Herrin JL, Heuertz SW (1988) Improving maintenance procedures: one utility’s perspectives.
In: Proceedings of the IEEE conference on human factors and power plants, pp 373–377
20. Knee HE (1988) The maintenance personnel performance simulation (MAPPS) model: a
human reliability analysis tool. In: Proceedings of the international conference on nuclear
power plant aging, availability factors, and power plants, pp 373–377
21. Dhillon BS (1983) Power system reliability, safety, and management. Ann Arbor Science
Publishers, Ann Arbor
22. Dhillon BS, Singh C (1981) Engineering reliability: new techniques and applications. Wiley,
New York
References
149

---


### Page 157

Chapter 11
Mathematical Models for Performing
Human Reliability and Error Analysis
in Power Plants
11.1 Introduction
Mathematical modelling is a widely used approach in the area of engineering to
perform various types of analysis. In this case, a system’s components are represented by idealized elements assumed to have representative characteristics of
real-life components, and whose behaviour is possible to be described by equations. However, the degree of realism of a mathematical model very much depends
on the assumptions imposed upon it.
Over the years, in the area of reliability engineering, a large number of
mathematical models have been developed to study various aspects of human
reliability and error in engineering systems. Most of these models were developed
using the Markov method [1–3]. Although, the effectiveness of such models can
vary from one situation to another, some of these models are being used quite
successfully to study various types of real-life environments in industry [4–6].
Thus, some of these models can also be used to study human reliability and errorrelated problems in the area of power generation.
This chapter presents the mathematical models considered most useful for
performing human reliability and error analysis in power plants.
11.2 Model I: Human Correctability Probability Function
This mathematical model is concerned with the human capacity to correct selfgenerated errors. More speciﬁcally, the model is concerned with predicting the
probability that a self-generated error will be corrected in time t. Nonetheless, Ref.
[2] deﬁnes correctability function as the probability that a task will be corrected in
time t subjected to stress constraint related to the task and its environments.
Mathematically, the correctability probability function is expressed as follows
[2, 5, 7, 8]:
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6_11,
 Springer International Publishing Switzerland 2014
151

---


### Page 158

CP tð Þ ¼ P correction of error in time t=stress
ð
Þ
ð11:1Þ
where
CP(t)
is the probability that a human error will be corrected/rectiﬁed in time t.
P
is the probability.
The time derivative of non-correctability probability function, CPðtÞ; is
expressed by [2]
CP
0ðtÞ ¼  1
n NC0ðtÞ
ð11:2Þ
where the prime denotes differentiation with respect to time t, and
NC(t)
is the number of times the task is not accomplished after time t.
n
is the number of times task correction is accomplished after time t.
By dividing the both sides of Eq. (11.2) by NC(t), and rearranging, we obtain
CP
0ðtÞ  n
NCðtÞ
¼  NC0ðtÞ
NCðtÞ
ð11:3Þ
The right-hand side of Eq. (11.3) represents the instantaneous task correction
rate, acðtÞ: Hence, with the aid of Eq. (11.1), we rewrite Eq. (11.3) as follows [8]:
CP
0ðtÞ
CPðtÞ þ acðtÞ ¼ 0
ð11:4Þ
By solving Eq. (11.4) for speciﬁed initial conditions, we obtain
CPðtÞ ¼ eR t
0 acðtÞdt
ð11:5Þ
Since CPðtÞ þ CPðtÞ ¼ 1; we get
CPðtÞ ¼ 1  eR t
0 acðtÞdt
ð11:6Þ
It is to be noted that Eq. (11.6) is a general expression for correctability
probability function (i.e. it holds for both constant or non-constant task correction
rates). More speciﬁcally, it holds whether the task correction times are described
by the exponential distribution or any other probability distribution such as
Weibull.
Example 11.1 A power plant operator’s self-generated error correction times are
Weibull distributed. Thus, his/her task/error correction rate is deﬁned by
acðtÞ ¼ ctc1
bc
ð11:7Þ
152
11
Mathematical Models for Performing Human Reliability

---


### Page 159

where
c
is the distribution shape parameter.
b
is the distribution scale parameter.
t
is time.
Obtain an expression for the correctability probability function of the operator.
By inserting Eq. (11.7) into Eq. (11.6), we obtain
CPðtÞ ¼ 1  eR t
0 ððctc1Þ=bcÞdt
¼ 1  eðt=bÞc
ð11:8Þ
Thus, Eq. (11.8) is the expression for the correctability probability function of the
power plant operator.
11.3 Model II: Critical and Non-Critical Human Errors
Probability Prediction
This mathematical model represents an operator or any other personnel in power
plants performing a time-continuous task subjected to non-critical and critical
errors. More speciﬁcally, the errors committed by these personnel are grouped
under two categories (i.e. non-critical and critical). The model can be used to
obtain information such as the following:
• The power plant operator mean time to error.
• The power plant operator performance reliability at time t.
• The probability of the power plant operator committing a non-critical error at
time t.
• The probability of the power plant operator committing a critical error.
The state space diagram of the model is shown in Fig. 11.1, and the numerals in
the diagram circle and boxes denote the states of the power plant operator.
The model is subjected to the following assumptions:
• Non-critical human error rate is constant.
• Critical human error rate is constant.
• Human errors occur independently.
The following symbols are associated with the model/diagram:
i
is the ith state of the power plant operator; i = 0 means that the power
plant operator is performing his/her task correctly; i = 1 means that the
power plant operator has committed a critical human error; and i = 2
means that the power plant operator has committed a non-critical human
error.
11.2
Model I: Human Correctability Probability Function
153

---


### Page 160

PiðtÞ
is the probability of the power plant operator being in state i at time t, for
i = 0, 1, 2.
kch
is the constant critical human error rate of the power plant operator.
knh
is the constant non-critical human error rate of the power plant operator.
Using the Markov method, we write down the following equations for the
Fig. 11.1 diagram [1, 9, 10]:
d P0ðtÞ
dt
þ knh þ kch
ð
ÞP0ðtÞ ¼ 0
ð11:9Þ
d P1ðtÞ
dt
 kch P0ðtÞ ¼ 0
ð11:10Þ
d P2ðtÞ
dt
 knh P0ðtÞ ¼ 0
ð11:11Þ
At time t = 0, P0ð0Þ ¼ 1; P1ð0Þ ¼ 0; and P2ð0Þ ¼ 0:
Solving Eqs. (11.9–11.11), we get the following equations.
P0ðtÞ ¼ e knhþkch
ð
Þt
ð11:12Þ
P1ðtÞ ¼
kch
knh þ kch
1  e knhþkch
ð
Þt
h
i
ð11:13Þ
P2ðtÞ ¼
knh
knh þ kch
1  e knhþkch
ð
Þt
h
i
ð11:14Þ
Power plant 
operator 
performing 
his/her task 
correctly
0
Power plant operator 
committed a critical 
human error
1
Power plant operator 
committed a noncritical human error
2
ch
λ
nh
λ
Fig. 11.1 State space diagram for the power plant operator subjected to non-critical and critical
human errors
154
11
Mathematical Models for Performing Human Reliability

---


### Page 161

The reliability of the power plant operator’s performance is given by
RpoðtÞ ¼ P0ðtÞ
¼ e knhþkch
ð
Þt
ð11:15Þ
where
RpoðtÞ
is the reliability of the power plant operator’s performance at time t.
Mean time to human error of the power plant operator is given by Dhillon [1,
10]
MTTHEpo ¼
Z1
0
RpoðtÞ dt
¼
Z1
0
e knhþkch
ð
Þt dt
¼
1
knh þ kch
ð11:16Þ
where
MTTHEpo
is the mean time to human error of the power plant operator.
Example 11.2 Assume that a power plant operator’s constant non-critical and
critical human error rates are 0.0008 and 0.0003 errors/h, respectively. Calculate
the power plant operator’s mean time to human error and probability of making a
critical human error during a 10-h mission.
Substituting the given data values into Eqs. (11.16) and (11.13) yields
MTTHEpo ¼
1
0:0008 þ 0:0003
¼ 909:09 h
and
P1ð10Þ ¼
0:0003
0:0008 þ 0:0003 1  eð0:0008þ0:0003Þð10Þ
h
i
¼ 0:0029
Thus, the power plant operator’s mean time to human error and probability of
making a critical human error during a 10-h mission are 909.09 h and 0.0029,
respectively.
11.3
Model II: Critical and Non-Critical Human Errors Probability Prediction
155

---


### Page 162

11.4 Model III: Human Performance Reliability
in Fluctuating Environment
This mathematical model represents a power plant operator or any other power
plant personnel performing time-continuous task in ﬂuctuating environment (i.e.
normal and stressful). As the rate of human errors can vary signiﬁcantly from
normal work environment to stressful work environment, this mathematical model
can be used to calculate the power plant operator’s performance reliability,
probabilities of making an error in normal and stressful environments, and mean
time to human error in the ﬂuctuating environment.
The state space diagram of this mathematical model is shown in Fig. 11.2, and
the numerals in the diagram boxes denote the states of the power plant operator.
The following assumptions are associated with the model:
• Rates of the environment changing from normal to stressful and vice versa are
constant.
• All power plant operator errors occur independently.
• Power plant operator error rates in normal and stressful environments are
constant.
The following symbols are associated with the diagram/model:
i
is the ith state of the power plant operator; i = 0 means that the power
plant operator is performing his/her task correctly in normal environment;
i = 1 means that the power plant operator is performing his/her task
correctly in stressful environment; i = 2 means that the power plant
operator has committed an error in normal environment; and i = 3 means
that the power plant operator has committed an error in stressful
environment.
PiðtÞ
is the probability of the power plant operator being in state i at time t, for
i = 0, 1, 2, 3.
as
is the constant transition rate from normal work environment to stressful
work environment.
an
is the constant transition rate from stressful work environment to normal
work environment.
khs
is the constant human error rate of the power plant operator performing
his/her task in stressful environment.
khn
is the constant human error rate of the power plant operator performing
his/her task in normal environment.
With the aid of Markov method, we write down the following set of equations
for the Fig. 11.2 diagram [3, 10]:
d P0ðtÞ
dt
þ khn þ as
ð
ÞP0ðtÞ ¼ an P1ðtÞ
ð11:17Þ
156
11
Mathematical Models for Performing Human Reliability

---


### Page 163

d P1ðtÞ
dt
þ khs þ an
ð
ÞP1ðtÞ ¼ as P0ðtÞ
ð11:18Þ
d P2ðtÞ
dt
¼ khn P0ðtÞ
ð11:19Þ
d P3ðtÞ
dt
¼ khs P1ðtÞ
ð11:20Þ
At time t = 0, P0ð0Þ ¼ 1; and; P1ð0Þ ¼ P2ð0Þ ¼ P3ð0Þ ¼ 0:
By solving Eqs. (11.17–11.20) with the aid of Laplace transforms, we obtain the
following state probability equations:
P0ðtÞ ¼
1
y1  y2
ð
Þ
y2 þ khs þ an
ð
Þey2t  y1 þ khs þ an
ð
Þey1t
½

ð11:21Þ
where
y1 ¼ a1 þ ða2
1  4a2Þ1=2
h
i
=2
ð11:22Þ
y2 ¼ a1  ða2
1  4a2Þ1=2
h
i
=2
ð11:23Þ
a1 ¼ khn þ khs þ an þ as
ð11:24Þ
Power plant operator 
performing his/her 
task correctly in 
stressful environment
1
Power plant operator 
performing his/her 
task correctly in 
normal environment
0
Power plant operator 
committed an error 
in normal 
environment
2
Power plant operator 
committed an error in 
stressful environment
3
n
α
s
α
hs
λ
hn
λ
Fig. 11.2 State space diagram for the power plant operator performing his/her task in ﬂuctuating
normal and stressful environments
11.4
Model III: Human Performance Reliability in Fluctuating Environment
157

---


### Page 164

a2 ¼ khnðkhs þ anÞ þ askhs
ð11:25Þ
P2ðtÞ ¼ a4 þ a5ey2t  a6ey1t
ð11:26Þ
where
a3 ¼
1
y2  y1
ð11:27Þ
a4 ¼ khn khs þ an
ð
Þ=y1y2
ð11:28Þ
a5 ¼ a3 khn þ a4y1
ð
Þ
ð11:29Þ
a6 ¼ a3 khn þ a4y2
ð
Þ
ð11:30Þ
P1ðtÞ ¼ asa3 ey2t  ey1t
ð
Þ
ð11:31Þ
P3ðtÞ ¼ a7 1 þ a3
ð
Þ y1ey2t  y2ey1t
ð
Þ
½

ð11:32Þ
where
a7 ¼ khsas=y1y2
ð11:33Þ
The performance reliability of the power plant operator is given by
RppoðtÞ ¼ P0ðtÞ þ P1ðtÞ
ð11:34Þ
where
RppoðtÞ
is the power plant operator reliability at time t.
The mean time to human error of the power plant operator is given by
MTTHEppo ¼
Z1
0
RppoðtÞdt
¼ khs þ as þ an
ð
Þ=a2
ð11:35Þ
where
MTTHEppo
is the mean time to human error of the power plant operator.
Example 11.3 Assume that an operator is performing a certain task at a power
plant in ﬂuctuating environments and his/her constant error rates in normal and
stressful environments are 0.0002 and 0.0004 errors/h, respectively. The constant
transition rates from normal to stressful environment and vice versa are 0.05 and
0.01 times/h, respectively.
Calculate the mean time to human error of the power plant operator.
By inserting the given data values into Eq. (11.35), we obtain
158
11
Mathematical Models for Performing Human Reliability

---


### Page 165

MTTHEppo ¼
0:0004 þ 0:05 þ 0:01
ð
Þ
0:0002
ð
Þ 0:0004 þ 0:01
ð
Þ þ 0:05
ð
Þ 0:0004
ð
Þ
¼ 2,735:51 h
Thus, the mean time to human error of the power plant operator is 2,735.51 h.
11.5 Model IV: Human Performance Reliability Prediction
with Critical and Non-Critical Self-Generated Errors
and Corrective Action
This mathematical model is the same as Model II but with one exception, i.e. the
corrective action is taken by the power plant operator from states 1 and 2 as shown
in Fig. 11.3 state space diagram. The additional symbols shown in the state space
diagram are lch and lnh, representing the power plant operator’s constant critical
human error correction rate and constant non-critical human error correction rate,
respectively. All other symbols and assumptions used in this model are same as the
ones in Model II.
With the aid of Markov method, we write down the following equations for
Fig. 11.3 state space diagram [9, 10]:
d P0ðtÞ
dt
þ kch þ knh
ð
ÞP0ðtÞ ¼ lch P1ðtÞ þ lnh P2ðtÞ
ð11:36Þ
d P1ðtÞ
dt
þ lch P1ðtÞ ¼ kch P0ðtÞ
ð11:37Þ
d P2ðtÞ
dt
þ lnh P2ðtÞ ¼ knh P0ðtÞ
ð11:38Þ
At time t = 0, P0ð0Þ ¼ 1; and P1ð0Þ ¼ P2ð0Þ ¼ 0:
Solving Eqs. (11.36–11.38), we obtain the following equations:
P0ðtÞ ¼ lchlnh
x1x2
þ
x1 þ lnh
ð
Þ x1 þ lch
ð
Þ
x1 x1  x2
ð
Þ


ex1t 
x2 þ lnh
ð
Þ x2 þ lch
ð
Þ
x2 x1  x2
ð
Þ


ex2t
ð11:39Þ
where
x1; x2 ¼ b  b2  4 lchlnh þ kchlnh þ knhlch
ð
Þ
ð
Þ1=2
2
ð11:40Þ
b ¼ kch þ knh þ lch þ lnh
ð11:41Þ
x1x2 ¼ lchlnh þ knhlch þ kchlnh
ð11:42Þ
11.4
Model III: Human Performance Reliability in Fluctuating Environment
159

---


### Page 166

x1 þ x2 ¼  lch þ lnh þ kch þ knh
ð
Þ
ð11:43Þ
P1ðtÞ ¼ kchlnh
x1x2
þ kchx1 þ kchlnh
x1 x1  x2
ð
Þ


ex1t 
ðlnh þ x2Þkch
ð
Þ
x2 x1  x2
ð
Þ


ex2t
ð11:44Þ
P2ðtÞ ¼ knhlch
x1x2
þ knhx1 þ knhlch
x1 x1  x2
ð
Þ


ex1t 
lch þ x2
ð
Þknh
x2 x1  x2
ð
Þ


ex2t
ð11:45Þ
Thus, the power plant operator’s performance reliability with correction is
expressed by Eq. (11.39), i.e.
RpcðtÞ ¼ P0ðtÞ
ð11:46Þ
where
RpcðtÞ
is the power plant operator’s performance reliability with correction at
time t.
As time t becomes very large, we obtain the following steady-state probability
equations from Eqs. (11.39), (11.44), and (11.45), respectively:
P0 ¼ lim
t!1 P0ðtÞ ¼ lchlnh
x1x2
ð11:47Þ
P1 ¼ lim
t!1 P1ðtÞ ¼ kchlnh
x1x2
ð11:48Þ
Power plant 
operator 
performing 
his/her task 
correctly
0
Power plant operator 
committed a critical 
human error
1
Power plant operator 
committed a noncritical human error
2
ch
μ
ch
λ
nh
λ
nh
μ
Fig. 11.3 State space diagram for the power plant operator subjected to non-critical and critical
human errors and corrections
160
11
Mathematical Models for Performing Human Reliability

---


### Page 167

P2 ¼ lim
t!1 P2ðtÞ ¼ knhlch
x1x2
ð11:49Þ
where
Pj
is the power plant operator’s steady-state probability being in state j; for
j = 0, 1, 2.
Example 11.4 A power plant operator is performing a time-continuous task, and
during an accumulated period of 12,000 h, he/she made a total of 12 non-critical
errors and self-corrected ﬁve of them. During the same time period, he/she also
made four critical human errors and self-corrected one of them. More speciﬁcally,
the operator took 3 h to correct ﬁve non-critical errors and 2 h to correct one
critical error.
Calculate the power plant operator’s steady-state probabilities of being in states
0, 1, and 2, if the times to error correction and the times to error are exponentially
distributed.
For the given data values, we get
knh ¼
12
12,000 ¼ 0:001 errors=h
kch ¼
4
12,000 ¼ 0:0003 errors=h
lnh ¼ 5
3 ¼ 1:67 corrections=h
lch ¼ 1
2 ¼ 0:5 corrections=h
By inserting the above-calculated values into Eqs. (11.47–11.49), we obtain:
P0 ¼
ð0:5Þð1:67Þ
ð0:5Þð1:67Þ þ ð0:001Þð0:5Þ þ ð0:0003Þð1:67Þ
¼ 0:9988
P1 ¼
ð0:0003Þð1:67Þ
ð0:5Þð1:67Þ þ ð0:001Þð0:5Þ þ ð0:0003Þð1:67Þ
¼ 0:0006
P2 ¼
ð0:001Þð0:5Þ
ð0:5Þð1:67Þ þ ð0:001Þð0:5Þ þ ð0:0003Þð1:67Þ
¼ 0:0006
Thus, the steady-state probabilities of the power plant operator being in states 0,
1, and 2 are 0.9988, 0.0006, and 0.0006, respectively.
11.5
Model IV: Human Performance Reliability Prediction
161

---


### Page 168

11.6 Model V: Availability Analysis of a Power Plant
System with Human Error
This mathematical model represents a power plant system that can only fail due to
the occurrence of hardware failures, but human errors made by power plant personnel can degrade its performance. The system is repaired from degraded and
failed states.
The state space diagram of this mathematical model is shown in Fig. 11.4, and
the numerals in the diagram circles and box denote the states of the power plant
system. The model is subjected to the following assumptions:
• Power plant system hardware failure and human error rates are constant.
• The degraded power plant system can only fail due to hardware failures.
• Human errors made by power plant personnel can only lead to power plant
system degradation, but not failure.
• All power plant system repair rates are constant.
• The repaired power plant system is as good as new.
• The completely or partially failed power plant system is repaired.
• The completely failed power plant system is repaired either to its degraded state
or to its normal working state.
The following symbols are associated with the model/diagram:
i
is the ith state of the power plant system; i = 0 means that the power plant
system is working normally; i = 1 means that the power plant system
degraded due to human error made by power plant personnel; and i = 3
means that the power plant system failed.
PiðtÞ
is the probability that the power plant system is in state i at time t, for
i = 0, 1, 2.
ks
is the power plant system constant failure rate.
ls
is the power plant system constant repair rate.
kh
is the constant human error rate due to power plant personnel.
ld
is the constant repair rate from the power plant system degraded state to
normal working state.
k
is the power plant system constant failure rate from its degraded state.
l
is the constant repair rate from the power plant system failed state to
degraded or partially working state.
With the aid of Markov method, we write down the following set of equations
for the Fig. 11.4 state space diagram [1, 10, 11]:
d P0ðtÞ
dt
þ kh þ ks
ð
ÞP0ðtÞ ¼ ld P1ðtÞ þ ls P2ðtÞ
ð11:50Þ
d P1ðtÞ
dt
þ k þ ld
ð
ÞP1ðtÞ ¼ kh P0ðtÞ þ l P2ðtÞ
ð11:51Þ
162
11
Mathematical Models for Performing Human Reliability

---


### Page 169

d P2ðtÞ
dt
þ l þ ls
ð
ÞP2ðtÞ ¼ ks P0ðtÞ þ k P1ðtÞ
ð11:52Þ
At time t = 0, P0ð0Þ ¼ 1; P1ð0Þ ¼ 0; and P2ð0Þ ¼ 0:
Solving Eqs. (11.50–11.52), we obtain the following equations:
P0ðtÞ ¼ ldls þ kls þ ldl
B1B2
þ ld B1 þ ls B1 þ l B1 þ k B1 þ B2
1 þ ldls þ kls þ ldl


e B1t
þ
1 
ldls þ kls þ ldl
B1B2


 ld B1 þ ls B1 þ l B1 þ B1k þ B2
1 þ ldls þ kls þ ldl
B1 B1  B2
ð
Þ



	
e B2t
ð11:53Þ
where
B1; B2 ¼
C  C2  4 ldls þ kls þ ldl þ lskh þ khl þ khk þ ldks þ ksl þ ksk
ð
Þ
f
g1=2
h
i
2
ð11:54Þ
C ¼ kh þ ks þ k þ l þ ls þ ld
ð11:55Þ
B1B2 ¼ ldls þ kls þ ldl þ lskh þ khl þ khk þ ldks þ ksl þ ksk
ð11:56Þ
P1ðtÞ ¼ khls þ khl þ ksl
B1B2
þ B1kh þ khls þ khl þ ksl
B1 B1  B2
ð
Þ


e B1t
 khls þ khl þ ksl
B1B2
þ B1kh þ khls þ khl þ ksl
B1 B1  B2
ð
Þ


e B2t
ð11:57Þ
Power plant 
system failed
2
Power plant system 
working normally
0
Power plant system 
degraded due to 
human error made 
by power plant 
personnel
1
s
λ
s
μ
λ
μ
h
λ
d
μ
Fig. 11.4 State space diagram for the power plant system
11.6
Model V: Availability Analysis of a Power Plant System with Human Error
163

---


### Page 170

P2ðtÞ ¼ khk þ ldks þ ksk
B1B2
þ B1ks þ khk þ ksld þ ksk
B1 B1  B2
ð
Þ


e B1t
 khk þ ldks þ ksk
B1B2
þ B1ks þ khk þ ksld þ ksk
B1 B1  B2
ð
Þ


e B2t
ð11:58Þ
The probability of the power plant system degradation due to human error by
the power plant personnel is expressed by Eq. (11.57). As time t becomes very
large, Eq. (11.57) reduces to
P1 ¼ khls þ khl þ ksl
B1B2
ð11:59Þ
where
P1
is the steady-state probability of the power plant system degradation due to
human error by the power plant personnel.
The power plant system operational availability at time t is expressed by
AVpsðtÞ ¼ P0ðtÞ þ P1ðtÞ
ð11:60Þ
where
AVpsðtÞ
is the power plant system operational availability at time t.
As time t becomes very large, with the aid of Eqs. (11.53) and (11.57), Eq.
(11.60) becomes
AVps ¼ ldls þ kls þ ldl þ khls þ khl þ ksl
B1B2
ð11:61Þ
where
AVps
is the power plant system steady-state operational availability.
Example 11.5 Assume that for a certain power plant system, the following data
values are known:
kh ¼ 0:0005 errors=h
ks ¼ 0:004 failures=h
k ¼ 0:001 failures=h
l ¼ 0:07 repairs=h
ls ¼ 0:06 repairs=h
ld ¼ 0:008 repairs=h
Calculate the steady-state probability of the power plant system degradation
due to human error by the power plant personnel.
By inserting the given data values into Eq. (11.59), we get
164
11
Mathematical Models for Performing Human Reliability

---


### Page 171

P1 ¼
0:0005
ð
Þ 0:06
ð
Þ þ 0:0005
ð
Þ 0:07
ð
Þ þ 0:004
ð
Þ 0:07
ð
Þ
½
= 0:008
ð
Þ 0:006
ð
Þ
½
þ 0:001
ð
Þ 0:06
ð
Þ þ 0:008
ð
Þ 0:07
ð
Þ þ 0:06
ð
Þ 0:0005
ð
Þ þ 0:0005
ð
Þ 0:07
ð
Þ
þ 0:0005
ð
Þ 0:001
ð
Þ þ 0:008
ð
Þ 0:004
ð
Þ þ 0:004
ð
Þ 0:07
ð
Þ þ 0:004
ð
Þ 0:001
ð
Þ
¼ 0:000345
0:001481 ¼ 0:2328
Thus, the steady-state probability of the power plant system degradation due to
human error by the power plant personnel is 0.2328.
11.7 Model VI: Reliability Analysis of a Power Plant
Redundant System with Human Errors
This mathematical model represents a two-identical redundant active unit power
plant system subjected to the occurrence of human errors. Each of these units can
fail either due to a human error or due to a hardware failure. For the successful
operation of the power plant system, at least one unit must operate normally.
The state space diagram of the power plant system is shown in Fig. 11.5, and
the numerals in the circle and boxes denote system states.
The following assumptions are associated with the model:
• Both the system units are identical and operate simultaneously.
• Each unit can fail either due to a human error or hardware failure.
• Failures of each unit can be categorized under two classiﬁcations: failures due to
human errors and failures due to hardware problems.
• Human errors and hardware failures occur independently.
• Human error and hardware failure rates are constant.
The following symbols are associated with the model/diagram:
j
is the jth state of the power plant system; j = 0 (both units of the power
plant system operating normally); j = 1 (one unit failed due to a hardware
failure, the other working normally); j = 2 (one unit failed due to a human
error, the other working normally); j = 3 (both units failed due to
hardware failures); and j = 4 (both units failed due to human errors).
PjðtÞ
is the probability that the power plant system is in state j at time t, for
j = 0, 1, 2, 3, 4.
au
is the constant human error rate of a unit.
ku
is the constant hardware failure rate of a unit.
With the aid of Markov method, we write down the following set of equations
for the Fig. 11.5 diagram [1]:
d P0ðtÞ
dt
þ 2ku þ 2au
ð
ÞP0ðtÞ ¼ 0
ð11:62Þ
11.6
Model V: Availability Analysis of a Power Plant System with Human Error
165

---


### Page 172

d P1ðtÞ
dt
þ ku þ au
ð
ÞP1ðtÞ ¼ 2ku P0ðtÞ
ð11:63Þ
d P2ðtÞ
dt
þ ku þ au
ð
ÞP2ðtÞ ¼ 2au P0ðtÞ
ð11:64Þ
d P3ðtÞ
dt
¼ ku P1ðtÞ þ ku P2ðtÞ
ð11:65Þ
d P4ðtÞ
dt
¼ au P1ðtÞ þ au P2ðtÞ
ð11:66Þ
At time t = 0, P0ð0Þ ¼ 1; and P1ð0Þ ¼ P2ð0Þ ¼ P3ð0Þ ¼ P4ð0Þ ¼ 0:
Solving Eqs. (11.62–11.66), we obtain the following equations for the power
plant system state probabilities:
P0ðtÞ ¼ e2 kuþau
ð
Þt
ð11:67Þ
P1ðtÞ ¼
2ku
ku þ au
ð
Þ e kuþau
ð
Þt  e
2 kuþau
ð
Þt
h
i
ð11:68Þ
P2ðtÞ ¼
2au
ku þ au
ð
Þ e kuþau
ð
Þt  e2 kuþau
ð
Þt
h
i
ð11:69Þ
P3ðtÞ ¼
ku
ku þ au
ð
Þ 1  e kuþhu
ð
Þt
h
i2
ð11:70Þ
Both units of the 
power plant 
system operating 
normally
0
One unit failed due 
to a hardware 
failure, the other 
working normally
1
One unit failed due 
to a human error, 
the other working 
normally
2
Both units failed 
due to hardware 
failures
3
Both units failed 
due to human 
errors
4
u
λ
2
u
λ
u
α
2
u
α
u
λ
u
α
Fig. 11.5 State space diagram of a two-redundant unit power plant system
166
11
Mathematical Models for Performing Human Reliability

---


### Page 173

P4ðtÞ ¼
au
ku þ au
1  e kuþau
ð
Þt
h
i2
ð11:71Þ
The power plant system reliability is expressed by
RpsðtÞ ¼ P0ðtÞ þ P1ðtÞ þ P2ðtÞ
¼ 1  1  e kuþau
ð
Þt
h
i2
ð11:72Þ
where
RpsðtÞ
is the reliability of the power plant system at time t.
By integrating Eq. (11.72) over the time interval 0; 1
½
, we obtain [10]:
MTTFps ¼
Z1
0
RpsðtÞdt
¼
3
2 ku þ au
ð
Þ
ð11:73Þ
where
MTTFps
is the mean time to failure of a two-redundant active unit power plant
system with human error.
Example 11.6 Assume that a power plant system is made up of two identical,
independent, and active units. At least one unit must work normally for its (i.e.
system) success. Each unit can fail either due to a human error or due to a
hardware failure. Constant human error and hardware failure rates of a unit are
0.0001 errors/h and 0.008 failures/h, respectively.
Calculate the power plant system mean time to failure.
By substituting the speciﬁed data values into Eq. (11.73), we obtain
MTTFps ¼
3
2 0:008 þ 0:0001
ð
Þ
¼ 185:18 h
Thus, the power plant system mean time to failure is 185.18 h.
11.8 Problems
1. Assume that a power plant operator’s self-generated error correction times are
Rayleigh distributed. Obtain an expression for the correctability probability
function of the operator.
11.7
Model VI: Reliability Analysis of a Power Plant Redundant System
167

---


### Page 174

2. Prove Eqs. (11.12–11.14) using Eqs. (11.9–11.11) and the given initial
conditions.
3. Assume that a power plant operator’s constant non-critical and critical human
error rates are 0.0006 and 0.0002 errors/h, respectively. Calculate the power
plant operator’s probability of making a non-critical human error during a
20-h mission.
4. Prove Eq. (11.35) using Eq. (11.34).
5. Prove that the sum of Eqs. (11.21), (11.26), (11.31), and (11.32) is equal to
unity.
6. Prove Eqs. (11.47–11.49) using Eqs. (11.39), (11.44), and (11.45).
7. Prove Eq. (11.59) using Eq. (11.57).
8. Prove Eqs. (11.67–11.71) with the aid of Eqs. (11.62–11.66) and the given
initial conditions.
9. Prove that the sum of Eqs. (11.67–11.71) is equal to unity.
10. A power plant system is composed of two identical, independent, and active
units. At least one unit must operate normally for the system success. Each
unit can fail either due to a hardware failure or due to a human error. Constant
human error and hardware failure rates of a unit are 0.0003 errors/h and
0.009 failures/h, respectively.
Calculate the power plant system mean time to failure and reliability for a
150-h mission.
References
1. Dhillon BS (1986) Human reliability: with human factors. Pergamon Press Inc, New York
2. Regulinski TL, Askren WB (1972) Stochastic modelling of human performance effectiveness
functions. In: Proceedings of the annual reliability and maintainability symposium,
pp. 407–416
3. Dhillon BS (1985) Stochastic models for predicting human reliability. Microelectron Reliab
25:729–752
4. Dhillon BS (2003) Human reliability and error in medical system. World Scientiﬁc
Publishing, River Edge
5. Dhillon BS (2007) Human reliability and error in transportation systems. Springer, London
6. Dhillon BS (2009) Human reliability, error, and human factors in engineering maintenance.
CRC Press, Boca Raton
7. Askren WB, Regulinski TL (1969) Quantifying human performance for reliability analysis of
systems. Hum Factors 11:393–396
8. Regulinski TL, Askren WB (1969) Mathematical modeling of human performance reliability.
In: Proceedings of the annual symposium on reliability, pp. 5–11
9. Dhillon BS (1975) The analysis of the reliability of multi-state device networks. Ph.D.
Dissertation, Available from the National Library of Canada, Ottawa, Canada
10. Dhillon BS (1999) Design reliability: fundamentals and applications. CRC Press, Boca Raton
11. Dhillon BS (2002) Engineering maintenance: a modern approach. CRC Press, Boca Raton
168
11
Mathematical Models for Performing Human Reliability

---


### Page 175

Author Biography
Dr. B.S. Dhillon is a professor of Engineering Management in the Department of
Mechanical Engineering at the University of Ottawa. He has served as a Chairman/
Director
of
Mechanical
Engineering
Department/Engineering
Management
Program for over 10 years at the same institution. He is the founder of the
probability distribution named Dhillon Distribution/Law/Model by statistical
researchers in their publications around the world. He has published over 369 (i.e.,
222(70 single authored + 152 co-authored) journal and 147 conference
proceedings)
articles
on
reliability
engineering,
maintainability,
safety,
engineering management, etc. He is or has been on the editorial boards of 11
international scientiﬁc journals. In addition, Dr. Dhillon has written 41 books on
various aspects of health care, engineering management, design, reliability, safety,
and quality published by Wiley (1981), Van Nostrand (1982), Butterworth (1983),
Marcel Dekker (1984), Pergamon (1986), etc. His books are being used in over
100 countries and many of them are translated into languages such as German,
Russian, Chinese, and Persian (Iranian).
He has served as General Chairman of two international conferences on
reliability and quality control held in Los Angeles and Paris in 1987. Prof. Dhillon
has also served as a consultant to various organizations and bodies and has many
years of experience in the industrial sector. At the University of Ottawa, he has
been teaching reliability, quality, engineering management, design, and related
areas for over 33 years and he has also lectured in over 50 countries, including
keynote addresses at various international scientiﬁc conferences held in North
America, Europe, Asia, and Africa. In March 2004, Dr. Dhillon was a
distinguished speaker at the Conf./Workshop on Surgical Errors (sponsored by
White House Health and Safety Committee and Pentagon), held at the Capitol Hill
(One Constitution Avenue, Washington, D.C.).
Professor Dhillon attended the University of Wales where he received a BS in
electrical and electronic engineering and an MS in mechanical engineering. He
received a Ph.D. in industrial engineering from the University of Windsor.
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6,
 Springer International Publishing Switzerland 2014
169

---


### Page 176

Appendix
Bibliography: Literature on Human
Reliability, Error, and Human Factors
in Power Generation
A.1
Introduction
Over the years, a large number of publications on human reliability, error, and
human factors in power generation have appeared in the form of journal articles,
conference proceedings articles, technical reports, and so on. This appendix
presents an extensive list of selective publications related, directly or indirectly, to
human reliability, error, and human factors in power generation. The period
covered by the listing is from 1971 to 2012. The main objective of this listing is to
provide readers with sources for obtaining additional information on human
reliability, error, and human factors in power generation.
A.2
Publications
1. Albert, T.P., et. al, A Computer-vision Based Power Flat Monitoring System,
Proceedings of the IEE International Conference on Advances in Power
System Control, Operation and Management, 1991, pp. 20–24.
2. Amendola, A., et. al, PSA Models for System and Human Reliability: Results
on Benchmark Exercises and Needs, Maintenance Management International,
Vol. 6, 1980, pp. 105–119.
3. Annick, C., An EDF Perspective on Human Factors, Proceedings of the IEEE
Conference on Human Factors and Power Plants, 1988, pp. 65–67.
4. Aslam, M.F., Lidgate, D., Shami, T.A., A Coupled Knowledge Based System
for Online Economic Dispatch of Multiple Fuel Units in a Thermal Plant,
Proceedings of the International Universities Power Engineering Conference,
2004, pp. 358–362.
5. Austin, R.C., 500 MW Unit Control Center—Operations and Maintenance
Oriented, Instrumentation in Power Industry, Vol. 11, 1988, pp. 56–66.
B. S. Dhillon, Human Reliability, Error, and Human Factors in Power Generation,
Springer Series in Reliability Engineering, DOI: 10.1007/978-3-319-04019-6,
 Springer International Publishing Switzerland 2014
171

---


### Page 177

6. Ayres, T.J., Gross, M.M., Exploring Power Plant Data Resources for
Organizational Epidemiology, New Century, New Trends, Proceedings of
the IEEE Conference on Human Factors and Power Plants, 2002, pp. 10–16.
7. Azadeh, A., Jamshidnezhad, B, Improvement of Information Flow in a
Thermal Power Plant within the Macro Ergonomics Framework, Proceedings
of the SICE Annual Conference, 2005, pp. 59–64.
8. Azadeh, A., Fam, I.M., Garakani, M.M., A Total Ergonomic Design Approach
to Enhance the Productivity in a Complicated Control System, Information
Technology Journal, Vol. 6, No. 7, 2007, pp. 1036–1042.
9. Azadeh, A., Hasani, F.A., Jiryaei, S.Z, Performance Assessment and
Optimization
of
HSE
Management
Systems
with
Human
Error
and
Ambiguity by an Integrated Fuzzy Multivariate Approach in a Large
Conventional Power Plant Manufacture, Journal of Loss Prevention in the
Process Industries, Vol. 25, No. 3, 2012, pp. 594–603.
10. Azadeh, M.A., Keramati, A., Mohammadfam, I., Jamshidnedjad, B., Enhancing
the Availability and Reliability of Power Plants through Macro Ergonomics
Approach, Journal of Scientiﬁc and Industrial Research, Vol. 65, No. 11, 2006,
pp. 873–878.
11. Bagchi, C.N., Gottilla, S.C., Application of Human Engineering Criteria to
Annunciator Display Systems in a Large Fossil Power Station, IEEE
Transactions on Power Apparatus and Systems, Vol. 100, No. 6, 1981,
pp. 2759–2765.
12. Banks, W.W., Blackman, H. S., Curtis, J. N., A Human Factors Evaluation of
Nuclear Power Plant Control Room Annunciators, Proceedings of Annual
Control Engineering Conference, 1984, pp. 323–326.
13. Baur, P., Strategies For Eliminating Human Error in the Control Room,
Power, Vol. 27, No. 5, 1983, pp. 21–29.
14. Beare, A.N., Gaddy, C.D, Gilmore, W.E, Taylor, J.C, Fray, R.R., Divakaruni,
S.M., Human Factors Guidelines for Fossil Power Plant Digital Control
System Displays, Proceedings of the IEEE Conference on Human Factors and
Power Plants, 1992, pp. 248–253.
15. Beattie, J.D., Bell, R.L., Ho, D.L.C., Howard, B., A Computer-Based CRT
Display System for the Thunder Bay Generating Station Control Center,
Proceedings of the Power Industry Computer Applications Conference, 1977,
pp. 42–50.
16. Bedreage, L., Guzun, B.D., Constantinescu, C., Modelling of the Human
Factors Using Petri Nets, Proceedings of the IREP Symposium on Bulb Power
System Dynamics and Control, 2007, pp. 100–104.
17. Beltracchi, L., Iconic Displays, Ranking Cycles and Human Factors for
Control Rooms of Nuclear Power Plants, IEEE Transactions on Nuclear
Science, Vol. 30, 1983, pp. 1856–1861.
18. Ben-Yaacov, G., Human Factors Considerations in the Design of the Man–
Machine Interface for Power Plant Process Computers, Proceedings of the
Conference on Instrumentation in the Power Industry, 1980, pp. 19–33.
172
Appendix

---


### Page 178

19. Bersini, U., Cacciabue, P.C., Mancini, G., Cognitive Modelling: A Basic
Complement of Human Reliability Analysis, Reliability Engineering &
System Safety, Vol. 22, 1988, pp.107–128.
20. Besco, R, Human Performance Breakdowns are Rarely Accidents: They are
Unusually very Poor Choices with Disastrous Results, Journal of Hazardous
Materials, Vol. 115, No. 1–3, 2004, pp. 155–161.
21. Beveridge, R.L., Applied Human Reliability: One Utility’s Experience,
Proceedings of the IEEE Conference on Human Factors and Nuclear Safety,
1985, pp. 316–320.
22. Bongarra, J.P., Certifying Advanced Plants: A US NRC Human Factors
Perspective, Proceedings of the IEEE Conference on Human Factors and
Power Plants, 1997, pp. 6.18–6.24.
23. Boring, R.L., Blackman, Harold. S., The Origins of the SPAR-H Method’s
Performance Shaping Factor Multipliers, Proceedings of the IEEE Conference
on Human Factors and Power Plants, 2007, pp.177–184.
24. Boring, R.L., et. al, A Taxonomy and Database for Capturing Human
Reliability and Human Performance Data, Proceedings of the Human Factors
and Ergonomics Society Annual Meeting, 2006, pp. 2217–2221.
25. Boring, R.L., et. al, Human Reliability Analysis in the U.S. Nuclear Power
Industry: A Comparison of Atomistic and Holistic Methods, Proceedings of
the Human Factors and Ergonomics Society Annual Meeting, 2005,
pp. 1814–1819.
26. Boring, R.L., et. al., Human Factors and the Nuclear Renaissance, Proceedings
of the Human Factors and Ergonomics Society Conference, 2008, pp. 763–767.
27. Boring, R.L., Grifﬁth, C.D., Joe, J.C., The Measure of Human Error : Direct
and Indirect Performance Shaping Factors, Proceedings of the IEEE
Conference on Human Factors and Power Plants, 2007, pp. 170–176.
28. Boring, R.L., Human Reliability Analysis for Control Room Upgrades,
Proceedings of the Human Factors and Ergonomics Society Conference, 2009,
pp. 1584–1588.
29. Boring,
R.L.,
Modeling
Human
Reliability
Analysis
Using
MIDAS,
Proceedings of the International Workshop on Future Control Station
Designs and Human Performance Issues in Nuclear Power Plants, 2009,
pp. 89–92.
30. Boring,
R.L.,
Modeling
Human
Reliability
Analysis
Using
MIDAS,
Proceedings
of
the
International
Topical
Meeting
on
Nuclear
Plant
Instrumentation Control, and Human Machine Interface Technology, 2006,
pp. 1270–1274.
31. Boring, R.L., Using Nuclear Power Plant Training Simulators for Operator
Performance and Human Reliability Research, Proceedings of the American
Nuclear Society International Topical Meeting on Nuclear Power Plant
Instrumentation Controls, and Human Machine Interface Technology, 2009,
pp. 1–12.
Appendix
173

---


### Page 179

32. Bransby, M., Human Contribution to Safety: Designing Alarm Systems for
Reliable Operator Performance, Measurement and Control, Vol. 32, No.7,
1999, pp. 209–213.
33. Brown, R., Sanchez, J., Mudry, R., Fleming, M., Evaluation of Extractive
Measurement Methods at the EPRI Coal Flow Loop, Proceedings of the
Annual Joint ISA/EPRI Controls and Instrumentation Conference, 2006,
pp. 346–349.
34. Byung-Soo, C., Chae-Joo, M., Design of Fuzzy Seawater Lift Pump System in
Fossil Fired Power Plant, Proceedings of the Third International Symposium
on Uncertainty Modeling and Analysis and Annual Conference of North
American Fuzzy Information Processing Society, 1995, pp. 204–208.
35. Cacciabue, P.C., Evaluation of Human Factors and Man–Machine Problems in
the Safety of Nuclear Power Plants, Nuclear Engineering and Design, Vol.
109, No. 3, 1988, pp. 417–431.
36. Carnino, A., Human Reliability, Nuclear Engineering and Design, Vol. 90,
No. 3, 1985, pp. 365–369.
37. Carpignano, A., Piccini, M., Cognitive Theories and Engineering Approaches
for Safety Assessment and Design of Automated Systems: A Case Study of
Power Plant, Cognition Technology & Work, Vol. 11, No. 1, 1999, pp. 47–61.
38. Carvalho, P.V.R., et. al, Human Factors Approach for Evaluation and
Redesign of Human-System Interfaces of a Nuclear Power Plant, Simulator,
Displays, Vol. 29, 2008, pp. 273–284.
39. Cepin, M., Prosek, A., Update of the Human Reliability Analysis for a Nuclear
Power Plant, Proceedings of the International Conference on Nuclear Energy
for New Europe, 2006, pp. 706.1–706.8.
40. Choi, S.S., et. al, Development Strategies of an Intelligent Human–Machine
Interface for Next Generation Nuclear Power Plants, IEEE Transactions on
Nuclear Science, Vol. 43, No. 3, 1996, pp. 2096–2114.
41. Clarke, L.R ., Allamby, S.P., People in Power System Control in the Next
Century, Proceedings of the International Conference on Human Interfaces in
Control Room, Cockpits, and Command Centres, 1999, pp. 434–439.
42. Collins, E.P., Mcfadden, R.H., A Human Reliability Analysis Methodology
for Industrial and Process Facilities, Proceedings of the IEEE Industrial and
Commercial Power Systems Technical Conference, 1988, pp. 81–84.
43. Comer, K., Human Reliability Data Bank: Feasibility Study, Proceedings of
the Human Factors Society Conference, 1984, pp. 235–238.
44. Comer, K., Miller, D.P., Donovan, M., Human Reliability Data Bank:
Feasibility Study, Proceedings of the Human Factors Society Annual Meeting,
1984, pp. 235–238.
45. Comer, K., Miller, D.P., Human Reliability Data Bank: Pilot Implementation,
Proceedings of the Human Factors and Ergonomics Society Conference, 1983,
pp. 175–179.
46. Coury, B.G., Terranova, M., Collaborative Decision Making in Dynamic
Systems, Proceedings of the Human Factors Society Annual Meeting, 1991,
pp. 944–948.
174
Appendix

---


### Page 180

47. Danchak, M.M., CRT Displays for Power Plants, Instrumentation Technology,
Vol. 23, No. 10,1976, pp. 29–36.
48. Dang, V.N., et. al, An Empirical Study of HRA Methods—Overall Design and
Issues, Proceedings the IEEE Conference on Human Factors and Power
Plants, 2007, pp. 243–247.
49. Dang,V., Huang, Y., Siu, N., Carroll, J ., Analyzing Cognitive Errors using a
Dynamic Crew-Simulation Model, Proceedings of the IEEE Conference on
Human Factors and Power Plants, 1992, pp. 520–526.
50. Daniel, T., Jean-Paul, L., The Impact on Safety of Computerized Control
Room in Nuclear Power Plants: The French Experience on Human Factors
with N4 Series, Proceedings of the IEA/HFES Congress, 2000, pp. 815–818.
51. Daniels, R.W., Formula for Improved Plant Maintainability Must Include
Human Factors, Proceedings of the IEEE Conference on Human Factors and
Nuclear Safety, 1985, pp. 242–244.
52. De, A., Thakur, S.S., Failure Analysis of Boiler in Thermal Power Station—A
Study, Journal of the Institution of Engineers: Mechanical Engineering
Division, Vol. 73, 1992, pp. 179–181.
53. Dicken, C.R., Soft Control Desks and Alarm Display, Computer & Control
Engineering Journal, Vol. 10, No. 1, 1999, pp. 11–16.
54. Dicken, C.R., Soft Control Desks—the Operator Interface, Proceedings of the
UKACC International Conference on Control, 1998, pp. 567–571.
55. Dineen,G.J., Development and Implementation of an Enhanced Maintenance
System for a 30 year old Power Station, Proceedings of First IEE International
Conference on Power Station Maintenance, 1988, pp. 6–10.
56. Dougherty,
E.M.,
Fragola,
J.R.,
Foundations
for
a
Time
Reliability
Correlation System to Quantify Human Reliability, IEEE Conference on
Human Factors and Power Plants, 1998, pp. 268–278.
57. Downes, B., Sandar, D., Human Reliability Program—Components and
Effects, Nuclear Materials Management, Vol. 15, 1986, pp. 661–665.
58. Doytchev, D., Szwillus, G., Combining Task Analysis and Fault Tree Analysis
for Accident and Incident Analysis: A Case Study from Bulgaria, Proceedings
of the European Safety and Reliability Conference, 2006, pp. 3–10.
59. Doytchev, D.E., Combining Task Analysis and Fault Tree Analysis for
Accident and Incident Analysis: A Case Study from Bulgaria, Accident
Analysis and Prevention, Vol. 41, No. 6, 2009, pp. 1172–1179.
60. Duffey, R.B., Saull, J.W., The Probability and Management of Human Error,
Proceedings of the International Conference on Nuclear Energy, 2004,
pp. 133–137.
61. Esther, D.S., Heising, C.D., Impact of the Organization on Human Reliability
at Ft. Calhoun Nuclear Plant, Transactions of the American Nuclear Society,
Vol. 88, 2003, pp. 888–889.
62. Etemadi, A.H., Fotuhi-Firuzabad, M., Quantitative Assessment of Protection
System Reliability Incorporating Human Errors, Journal of Risk and
Reliability, Vol. 9, 2008, pp. 255–263.
Appendix
175

---


### Page 181

63. Farinha, T., Fonseca, I ., Simoes, A., Barbosa, M., Viejas, J., New Approaches
on Predictive Maintenance Based on an Environmental Perspective, the Cases
of Wind Generators and Diesel Engines, Proceedings of the 12th WSEAS
International Conference on Circuits, 2008, pp. 420–428.
64. Fenton, E.F., et. al, Development of a Unit Control System Concept for
Lakeview Generating Station, Proceedings of Instrumentation,Control,and
Automation in the Power Industry, Vol. 33,1990, pp. 245–250.
65. Fiedlander, M.A., Evans, S.A., Inﬂuence of Organizational Culture on Human
Error, Global Perspective of Human factors in Power Generation, Proceedings
of the IEEE Conference on Human Factors and Power Plants,1997, pp. 19–22.
66. Fink, B., Hill, D., Nasser, J., Planning for Control Room Modernization,
Proceedings of the American Nuclear Society International Topical Meeting
on Nuclear Plant Instrumentation, Control, and Human Machine Interface
Technology, 2004, pp. 1475–1483.
67. Fledger, S. A., Mc Williams, M. R., Control Room Human Factors Assessment
at Bulgarian Power Plants, Proceedings of the Human Factors and Ergonomics
Society Meeting, 1995, pp. 1043–1047.
68. Floyd II, H.L, Industrial Electric Power System Operation, Part I—Improving
System Reliability, Proceedings of the IEEE Industrial and Commercial
Power Systems Technical Conference, 1984, pp. 153–158.
69. Floyd II, H.L., Reducing Human Errors in Industrial Electric Power System
Operation, Part I—Improving System Reliability, IEEE Transactions on
Industry Applications, Vol. 22, No. 3, 1986, pp. 420–424.
70. Forzano, P., Castagna, P., Procedures, Quality, Standards, and the Role of
Human Factors and Computerized Tools in Power Plant Control, Proceedings
of the IEEE Conference on Human Factors and Power Plants, 1997, pp.7–12.
71. Fredricks, P., Humanizing the Power Plant Control Room, Instrumentation in
the Power Industry, Vol. 23, 1980, pp. 149–153.
72. Fuchs, S., Hale, K.S., Axelsson, P, Augmented Cognition Can Increase
Human Performance in the Control Room, Proceedings of the IEEE
Conference on Human Factors and Power Plants, 2007, pp. 128–132.
73. Gaddy, C.D., Taylor, J.C., Fray, R. R., Divakaruni, S. M., Human Factors
Considerations in Digital Control Room Upgrades, Proceedings of the
American Power Conference, 1991, pp. 256–258.
74. Gong-Xia, Y., Gen-Xing, C., Jue-Zhong, J., A Case Study for the Design of
Visual Environment of a Control Room in a Power Plant, Lighting Research
and Technology, Vol. 17, No. 2, 1985, pp. 84–88.
75. Groth, K., Mosleh, A., Data-Driven Modelling of Dependencies Among
Inﬂuencing Factors in Human–Machine Interactions, Proceedings of the ANS/
PSA Topical Meeting on Challenges to PSA During the Nuclear Renaissance,
2008, pp. 916–926.
76. Guttmann,
H.E.,
Human
Reliability
Data:
The
Problem
and
Some
Approaches, Transactions of the American Nuclear Society, Vol. 41, No. 1,
1982, pp. 1–25.
176
Appendix

---


### Page 182

77. Ha, J.S., Seong, P.H., Lee, M.S., Hong, J. H., Development of Human
Performance Measures for Human Factors Validation in the Advanced MCR
of APR-1400, IEEE Transactions on Nuclear Science,Vol. 54, No. 6, 2007,
pp. 2687–2699.
78. Hagen, E.W., Technical Note: Quantiﬁcation of Human Error Associated with
Instrumentation and Control System Components, Nuclear Safety, Vol. 23,
No. 6, 1982, pp. 665–668.
79. Hallbert, B.P., The Evaluation of Human Reliability in Process Systems
Analysis, Proceedings of the IEEE Conference on Human Factors and Power
Plants, 1992, pp. 442–447.
80. Hannaman, G.W., The Role of Framework, Models, Data, and Judgement in
Human Reliability, Nuclear Engineering and Design, Vol. 93, 1986,
pp. 295–301.
81. Harper, A.B, Nicholas, G.R, Retroﬁt of Instrumentation and Controls for
Large Industrial and Utility Power Plants, Proceedings of the Conference on
Trends in the Generation, Transmission, Distribution and Utilisation of
Electrical Energy, 1985, pp. 273–276.
82. Harrison, M., Barnard, P., On Deﬁning Requirements for Interaction,
Proceedings
of
the
IEEE
International
Symposium
on
Requirements
Engineering, 1992, pp. 50–54.
83. Heo, G., Framework of Quantifying Human Error Effects in Testing and
Maintenance, Proceedings of the American Nuclear Society International
Topical Meeting on Nuclear Plant Instrumentation, Control, and Human–
Machine Interface Technology, 2009, pp. 2083–2092.
84. Heo, G., Park, J., A Framework for Evaluating the Effects of Maintenance
Related Human Errors in Nuclear Power Plants, Reliability Engineering and
System Safety, Vol. 95, No. 7, 2010, pp. 797–805.
85. Heuertz,
S.W.,
Herrin,
J.L.,
Validation
of
Existing
Nuclear
Station
Instrumentation and Electric Procedures to Reduce Human Errors: One
Utility’s Perspective, IEEE Transactions on Energy Conversions, Vol. 1, No.
4, 1986, pp. 33–34.
86. Higginbotham, J.W., Implementation of Human Factors Consideration in a
Coal Generating Station Control Room, IEEE Transactions on Power
Apparatus and Systems, Vol. 104, No. 4, 1985, pp. 817–820.
87. Hill, D., et. al, Integration of Human Factors Engineering into the Design
Change Process, Proceedings of the American Nuclear Society International
Topical Meeting on Nuclear Plant Instrumentation, Control, and Human–
Machine Interface Technology, 2004, pp. 1485–1494.
88. Hoag, L.L., An Overview of Research Needs in the Display Systems Design
Area, Proceedings of the Human Factors Society Annual Meeting, 1977,
pp.316–318.
89. Holmberg, K, New Techniques for Competitive Reliability, International
Journal of Comadem, Vol. 4, No. 4, 2001, pp. 41–46.
Appendix
177

---


### Page 183

90. Hopkins, C.O., Synder, H.L., Critical Human Factors Issue in Nuclear Power
Generation
and
a
Recommended
Comprehensive
Long
Range
Plan,
Proceedings
of
the
Human
Factors
Society
Annual
Meeting,
1982,
pp. 692–697.
91. Howey, G.R., Human Factors in Ontario Hydro’s Nuclear Power Stations,
IEEE Transactions on Nuclear Science, Vol. 28, No. 1, 1981, pp. 968–971.
92. Hunt, R.M., Rouse, W.B., Problem-Solving Skills of Maintenance Trainees in
Diagnosing Faults in Stimulating Power Plants, Human factors, Vol. 23, No. 3,
1981, pp. 317–328.
93. Hvelplund, R., Control Room for High-Efﬁciency Power Plant, People in
Control, Proceedings of the International Conference on Human Interfaces
in Control Room, Cockpits and Command Centres, 1999, pp. 101–117.
94. Jankala, K.E., Vaurio, J.K., Vuorio, U.M., Plant-speciﬁc Reliability and
Human Data Analysis for Safety Assessment, Proceedings of the IAEA
Conference on Nuclear Power Performance and Safety, 1988, pp. 135–151.
95. Johnson, W.B., Rouse, W.B., Analysis and Classiﬁcation of Human Errors in
Troubleshooting Live Aircraft Power Plants, IEEE Transactions on Systems,
Man and Cybernetics, Vol. 12, No. 3, 1982, pp. 389–393.
96. Jones,
J.,
Human
Factors
in
the
Acquisition
of
Data,
Control
&
Instrumentation, Vol. 22, No. 12, 1990, pp. 31–32.
97. Joseph, L., Human Factors Assessment of Digital Monitoring Systems for
Nuclear Power Plants Control Room, IEEE Transactions on Nuclear
Science, Vol. 39, No. 4, 1992, pp. 924–932.
98. Jou, Y.T., et. al, The Implementation of a Human Factors Engineering
Checklist for Human-System Interfaces Upgrade in Nuclear Power Plants,
Safety Science, Vol. 47, No. 7, 2009, pp. 1016–1025.
99. Jufang, S., Human Errors in Nuclear Power Plants, Nuclear Power
Engineering, Vol. 14, No. 4, 1993, pp. 306–309.
100. Jung, W., et. al, Analysis of an Operator’s Performance Time and Its
Application to a Human Reliability Analysis in Nuclear Power Plants, IEEE
Transactions on Nuclear Science, Vol. 54, No. 4, 2007, pp. 1801–1811.
101. Jung, W., Park, J., Jaewhan, K., Performance Time Evaluation for Human
Reliability Analysis Using a Full-Scope Simulator of Nuclear Power Plants,
Proceedings of the IEEE Conference on Human Factors and Power Plants,
2002, pp. 306–311.
102. Kang, D., Jung, W.D., Yang, J.E., Improving the PSA Quality in the Human
Reliability Analysis of Pre-Accident Human Errors, Proceedings of the
Annual Conference of the Canadian Nuclear Society, 2004, pp. 189–200.
103. Kawai, K., Takishima, S., Tsuchiya, M., Uchida, M., Operator Friendly
Man–Machine System for Computerized Power Plant Automation, Bridge
Between Control Science and Technology, Proceedings of the Ninth
Triennial World Congress of IFAC (International Federation of Automatic
Control), Vol. 5, 1985, pp. 2641–2646.
178
Appendix

---


### Page 184

104. Kengskool, K., Martinez, S.E., Cobaugh, P, Robot vs. Human Operator for
Speed, Precision and Other Aspects, Proceedings of the ﬁrst International
Conference on Ergonomics of Advanced Manufacturing and Hybrid
Automated Systems, 1988, pp. 373–380.
105. Kenny, S.D., Stamps, K., Crowther, P., Development of NDT Techniques
and Inspection for Detection and Sizing of Thermal Fatigue Cracking in
Steam-Pipework Bores of Flexibly Operated Coal-Fired Power Stations,
Insight-Non-Destructive Testing and Condition Monitoring, Vol. 45, No. 2,
2003, pp. 125–129.
106. Khalaquzzaman, M., et. al, A Model for Estimation of Reactor Spurious
Shutdown
Rate
Considering
Maintenance
Human
Errors
in
Reactor
Protection System of Nuclear Power Plants, Nuclear Engineering and
Design, Vol. 240, No. 10, 2010, pp. 2963–2971.
107. Khalaquzzaman, M., et. al, Quantiﬁcation of Unavailability Caused by
Random Failures and Maintenance Human Errors in Nuclear Power Plants,
Nuclear Engineering and Design, Vol. 240, No. 6, 2010, pp. 1606–1613.
108. Kim, B.J., Bishu, R.R., Uncertainty of Human Error and Fuzzy Approach to
Human Reliability Analysis, International Journal of Uncertainty, Fuzziness
and Knowledge-Based Systems, Vol. 14, No. 1, 2006, pp. 111–129.
109. Kim, I.S., Human Reliability Analysis in the Man–Machine Interface Design
Review, Annals of Nuclear Energy, Vol. 29, No. 11, 2001, pp. 1069–1081.
110. Kim, J., et. al, Characteristics of Test and Maintenance Human Errors
Leading to Unplanned Reactor Trips in Nuclear Power Plants, Nuclear
Engineering and Design, Vol. 239, 2009, pp. 2530–2536.
111. Kim, J., Jung, W., Park, J., AGAPE-ET: Advanced Guidelines for Human
Reliability Analysis of Emergency Tasks, Proceedings of the IEEE
conference on Human Factors and Power Plants, 2007, pp. 314–321.
112. Kim, J.W., Jung, W., A Taxonomy of Performance Inﬂuencing Factors for
Human Reliability Analysis of Emergency Tasks, Journal of Loss Prevention
in the Process Industries, Vol. 16, No. 6, 2003, pp. 479–495.
113. Kirwan, B., Scannali, S., Robinson, L., A Case Study of a Human Reliability
Assessment for an Existing Nuclear Power Plant, Applied Ergonomics, Vol.
27, No. 5, 1996, pp. 289–302.
114. Kirwan, D.O., Basra, G., Taylor-Adams, S.E., CORE-DATA: A Computerized Human Error Database for Human Reliability Support, Proceedings of
the IEEE Conference on Human Factors and Power Plants, 1997, pp. 7–9.
115. Knee, H.E., Human Factors Engineering: A Key Element of Instrumentation
and Control System Design, Proceedings of the International Symposium on
Instrumentation in the Aerospace Industry, 1993, pp. 1113–1122.
116. Knee, H.E., The Maintenance Personnel Performance Simulation (MAPPS)
Model: A Human Reliability Analysis Tool, Proceedings of the International
Conference on Nuclear Power Plant Aging, Availability Factor and
Reliability Analysis, 1985, pp. 77–80.
Appendix
179

---


### Page 185

117. Koehler, T.A., Schmachtenberger, C.L., Soft Approach to Innovative Control
Room Design, Instrumentation in the Power Industry, Vol. 28, 1985,
pp. 145–158.
118. Konig, N., Wetzl, R., Intelligent Instrumentation and Control Systems for
Optimum Power Plant Operation, Engineering & Automation, Vol. 14,
No. 6,1992, pp. 18–19.
119. Koval, D.O., Floyd, II, H.L., Human Element Factors Affecting Reliability
and Safety, IEEE Transactions on Industry Applications, Vol. 34, No. 2,
1998, pp. 45–54.
120. Koval., D.O., Floyd II, H.L., Human Element Factors Affecting Reliability
and Safety, Proceedings of the IEEE Industry and Commercial Power
Systems Technical Conference, 1997, pp. 14–21.
121. Kozinsky, E.J., Computerized Measurement of Operator Performance on
Simulators, Proceedings of the Winter Simulation Conference, 1981,
pp. 10–14.
122. Lahiri, R.N., Sinha, A., A Web-Based Fuel Management Software System
for a Typical Indian Coal Based Power Plant, Proceedings of the IEEE Power
Engineering Society General Meeting, 2007, pp. 8–9.
123. Lang, A.W., Roth, E.M ., Bladh, K., Hine, R, Using a Benchmark—
Referenced Approach for Validating a Power Plant Control Room: Results of
the Baseline Study, Proceedings of the Human Factors and Ergonomics
Society Annual Meeting, 2002, pp. 1878–1882.
124. Laux, l., Plott, C., Using Operator Workload Data to Inform Human
Reliability Analyses, Proceedings the IEEE Conference on Human Factors
and Power Plants, 2007, pp. 309–313.
125. Le Bot, P., Human Reliability Data, Human Error and Accident Models:
Illustration Through the Three Mile Island Analysis, Reliability Engineering
and System Safety, Vol. 83, No. 2, 2004, pp. 153–167.
126. Lee, B., The Nuclear Power Industry’s Approach to Human Factors,
Proceedings of the IEEE Conference on Human Factors and Power Plants,
1992, pp. 7–9.
127. Lee, J.W., et. al, Human Factors Research in KAERI for Nuclear Power
Plants, Proceedings of the IEEE Annual Human Factors Meeting, 1997,
pp. 13.11–13.16.
128. Lee, J.W., et. al., Human Factors Review Guide for Korean Next Generation
Reactors, Proceedings of the 15th International Conference on Structural
Mechanics in Reactor Technology, 1999, pp. 353–360.
129. Li, D., Li, L., Preliminary Study of Human Factor Reliability in Hydropower
Station, Advanced Materials Research, Vol. 422, 2012, pp. 803–806.
130. Li, X., Human Reliability Analysis for Guangdong Nuclear Power Station,
Atomic Energy Science and Technology, Vol. 27, No. 4, 1993, pp. 324–328.
131. Li, Z., Chao, H., Human Factors Analysis and Preventive Countermeasures in
Maintenance in Nuclear Power Plants, Nuclear Power Engineering, Vol. 19,
No. 1, 1998, pp. 64–67.
180
Appendix

---


### Page 186

132. Lisboa, J.J., Nuclear Power Plant Availability and the Role of Human Factors
Performance, IEEE Transactions on Nuclear Science, Vol. 37, No. 1, 1990,
pp. 980–986.
133. Lisboa, J.J., Quantiﬁcation of Human Error and Common-Mode Failures in
Man–Machine Systems, IEEE Transactions on Energy Conversion, Vol. 3,
No. 2, 1986, pp. 291–299.
134. Lois, E., Chang, Y., Hsien, J., Capturing Control Room Simulator Data with
the HERA System, Proceedings of the IEEE Conference on Human Factors
and Power Plants, 2007, pp. 210–217.
135. Lois, E., Cooper, S.E., How Do You Deﬁne a Human Reliability Analysis
Expert?, Invited, Transactions of the American Nuclear Society, Vol. 101,
2009, pp. 980–981.
136. Lubini, E.., Light from the Heart of Darkness, IET Power Engineer, Vol. 20,
No. 4, 2006, pp. 42–45.
137. Ma, C., Lian, J., Long-Term Risk Dispatching of Cascaded Hydropower
Stations in Electricity Market, Proceedings of the Asia–Paciﬁc Power and
Energy Engineering Conference, 2009, pp. 100–104.
138. Makansi, J., AES Extracts Top Performance from Diverse Asset Base, Power
Engineering, Vol. 108, No. 11, 2004, pp.216–222 .
139. Manicut, M., Manicut, I., Human Reliability Analysis-Component of
Probabilistic Safety Assessment of Nuclear Power Plant, Proceedings of
the International Symposium on Nuclear Energy, 1993, pp. 207–211.
140. Manrique, A., Valdivia, J.C., Human Factors Engineering Applied to Nuclear
Power Plant Design, Proceedings of the International Congress on Advances
in Nuclear Power Plants, 2008, pp. 339–346.
141. Marshall, E.J., Dykes, J.E., Reduction in Plant Operating Costs Through
Computer Evaluation of Operator Performance, Proceedings of the American
Power Conference, 1984, pp. 380–384.
142. Mashio, K., Human Factors Engineering and HSI Design in the US-APWR,
Proceedings
of
the
Annual
Joint
ISA
POWID/EPRI
Controls
and
Instrumentation Conference, 2008, pp. 206–227.
143. Maskansi, J, Power Plant Training Ensure Your Team’s Survival in the
Trenches, Power, Vol. 139, No. 1, 1995, pp. 5–6.
144. Mc Keithan, B.G., Kfoury, N.S., Increasing Electric Power Plant Productivity
through Maintenance Management, Proceedings of the Human Factors
Society Annual Meeting, Vol. 1, 1983, pp. 576–580.
145. Mc Williams, T.P., Martz, H.F., Human Error Considerations in Determining
the Optimum Test Interval for Periodically Inspected Standby Systems, IEEE
Transactions on Reliability, Vol. 29, No. 4, 1980, pp. 305–310.
146. Meshakti. N., The Safety and Reliability of Complex Energy Processing
Systems, Energy Sources, Vol. 2, No. 2, 2007, pp. 141–154.
147. Meshkati, N, Control Rooms’ Design in Industrial Facilities, Human Factors
and Ergonomics in Manufacturing, Vol. 13, No .4, 1993, pp. 269–277.
148. Minner, D.E., The Inel Human Reliability Program: The First Two Years of
Experience, Nuclear Materials Management, Vol. 15, 1986, pp. 666–669.
Appendix
181

---


### Page 187

149. Mirabdolbaqi, S., The Role of the Operator in Power Plant Incidents: People
in Control, Proceeding of the International Conference on Human Interfaces
in Control Room, Cockpits and Command Centres, 1999, pp. 276–279.
150. Mishima, S., Human Factors Research Program-Long Term Plan in
Cooperation with Government and Private Research Centers, Proceedings of
the IEEE Conference on Human Factors and Power Plants, 1988, pp. 50–54.
151. Miyazaki, T., Development of a New Cause Classiﬁcation Method
Considering Plant Aging and Human Errors for Adverse Events Occurred
in Nuclear Power Plants and Some Results of Its Application, Transactions
of the Atomic Energy Society of Japan, Vol. 6, No. 4, 2007, pp. 434–443.
152. Moieni, P., Spurgin, A.J., Singh, A., Advances in Human Reliability
Analysis Methodology, Reliability Engineering and System Safety, Vol. 44,
No. 1, 1994, pp. 27–55.
153. Mookerjee, G., Mandal, J, Modern Control Center Design—The Inﬂuence of
Operator Interface on Control Room Instrumentation and Control Devices,
Considering the Philosophy of Human-Factor Engineering Principles,
Proceedings of the American Power Conference, 1998, pp. 1009–1014.
154. Mookerjee, G., Modern Control Center Design—the Inﬂuence of Operator
Interface
on
Control
Room
Instrumentation
and
Control
Devices,
Considering the Philosophy of Human-Factors Engineering Principles,
Proceedings of the American Power Conference on Reliability and
Economy, 1998, pp. 1009–1014.
155. Morgenstern, M.H., Maintenance Management Systems: A Human Factors
Issue, Proceedings of the IEEE Conference on Human Factors and Power
Plants, 1988, pp. 390–393.
156. Moshely, A., Chang, Y.H., Model-Based Human Reliability Analysis:
Prospects and Requirements, Reliability Engineering and System Safety,
Vol. 83, No. 2, 2004, pp. 241–253.
157. Mosneron-Dupin, F., Saliou, G., Lars, R., Probabilistic Human Reliability
Analysis: The Lessons Derived for Plant Operation at Electric de France,
Reliability Engineering and System Safety, Vol. 58, No. 3, 1997, pp. 249–274.
158. Mulle, G.R., Dick, R., The Role of Human Factors in Planning for Nuclear
Power Plant Decommissioning, Proceedings of the IEEE Conference on
Human Factors and Nuclear Safety, 1985, pp. 257–262.
159. Muschara, T., A Dual Human Performance Strategy: Error Management and
Defense-in-Depth, Proceedings of the IEEE Human Factors Meeting, 2002,
pp.830–839.
160. Naser, J., Addressing Digital Control Room Human Factors Technical and
Regulatory
Issues,
Proceedings
of
the
American
Nuclear
Society
International Meeting on Nuclear Plant Instrumentation, control and
Human–Machine Interface Technology, 2009, pp. 6–10.
161. Naser, J., et. al, Nuclear Power Plant Control Room Modernization Planning,
Process, Human Factors Engineering, and Licensing Guidance, Proceedings
of the Annual Joint ISA Power Industry Division and EPRI Controls and
Instrumentation Conference, 2004, pp. 219–227.
182
Appendix

---


### Page 188

162. Naumov, V.I., Human Factors and Supporting Measures for Nuclear Power
Plant Operators, Atomnaya Energiya, Vol. 74, No. 4, 1993, pp. 344–348.
163. Nelson, R., Dynamic Accident Sequence Analysis in PRA: A Comment on
‘‘Human Reliability Analysis-Where Shouldst Thou Turn?’’, Reliability
Engineering and System Safety, Vol. 29, 1990, pp. 359–364.
164. Nelson, W.R., Integrated Design Environment for Human Performance and
Human Reliability Analysis, Proceedings of the IEEE conference on Human
Factors and Power Plants, 1997, pp. 8.7–8.11.
165. Nimmo, I., Moscatelli, J., Designing Control Rooms for Humans, Control,
Vol. 17, No. 7, 2000, pp. 47–53.
166. Nimmo, L., Putting a Human Face on the Design of Control Rooms,
Engineering Technology, Vol. 7, No. 4, 2004, pp. 42–44.
167. Nitu. V.l, Lonescu, D.C., Binig.V., Barrakat, M.T., Human Reliability:
Revue Roumaine des Sciences Techniques, Serie Electrotechnique et
Energetique, Vol. 35, No. 2, 1990, pp. 179–185.
168. O’ Brien, J.N., Lukas, W.J., A Strategy for Examining Human Reliability
Aspects of Plant Security, Proceedings of the IEEE Conference on Human
Factors and Power Plants, 1998, pp. 465–470.
169. O’Hara, J.M., A Quasi-Experimental Model of Complex Human–Machine
System Validation, Cognition, Technology & Work, Vol. 1, No. 1, 1999,
pp. 37–46 .
170. O’Hara, J.M., Brown, W.S., Higgins, J.C., Updating the NRC’s Guidance for
Human Factors Engineering Reviews, Proceedings of the IEEE Conference
on Human Factors and Power Plants, 2002, pp. 422–427.
171. O’Hara, J.M., Hall, R.E., Advanced Control Rooms and Crew Performance
Issues: Implications for Human Reliability, IEEE Transactions on Nuclear
Science, Vol. 39, No. 4, 1992, pp. 919–923.
172. Obrzut, J.J., Good Plant Design Cuts Human Errors, Iron Age, Vol. 27,
No. 16, 1971, pp. 78–79.
173. Orendi, R.G., et. al, Human Factors Consideration in Emergency Procedure
Implementation, Proceedings of the IEEE Conference on Human Factors and
Power Plants, 1988, pp. 214–221.
174. Oxstarnd, J., Boring, R.L., Human Reliability for Design Applications at a
Swedish Nuclear Power Plant, Proceedings of the International Symposium
on Resilient Control Systems, 2009, pp. 5–10.
175. Pack, R.W., Parris, H.L., Human Factors Engineering Design Guidelines for
Maintainability, Proceedings of the Inter-RAM Conference for the Electric
Power Industry, 1985, pp. 11–14.
176. Paradies, M., Positive vs. Negative Enforcement: Which Promotes High
Reliability Human Performance, Proceedings of the IEEE Conference on
Human Factors and Power Plants, 2007, pp. 185–188.
177. Paradies, M., Skompski, E., Why People Don’t Develop Effective Corrective
Actions, Proceedings of the IEEE Conference on Human Factors and Power
Plants, 2002, pp. 18–22.
Appendix
183

---


### Page 189

178. Parsons, S.O., Saminara, J.L., O’Hara, J.M., Power System Human Factors/
Ergonomics Activities in United States, Proceedings of the XIV Triennial
Congress of the International Ergonomics Association and 44th Annual
Meeting of Human Factors and Ergonomic Association, 2000, pp. 807–810.
179. Penington, J., Shakeri, S., A Human Factors Approach to Effective
Maintenance, Proceedings of the Canadian Nuclear Society Conference,
2006, pp. 1–11.
180. Pesme, H., Le Bot, P., Meyer, P., Little Stories to Explain Human Reliability
Assessment: A Practical Approach of MERMOS method, Proceedings of the
IEEE Conference on Human Factors and Power Plants, 2007, pp. 284–287.
181. Piccini, M, Human Factors in the Design of Supervisory Control Systems
and Human–Machine Interfaces for Highly Automated Complex Systems,
Cognition, Technology & Work, Vol. 4, No. 4, 2002, pp. 256–71.
182. Pine, S.M., Schulz, K.A., Applying Human Engineering Processes to Control
Room Design, Power Engineering Vol. 87, No.1,1983, pp. 38–46.
183. Poucet, A., Survey of Methods Used to Assess Human Reliability in the
Human Factors Reliability Benchmark Exercise, Reliability Engineering and
System Safety, Vol. 22, 1988, pp. 257–268.
184. Presensky, J.J., Human Factors and Power Plants: Foreword, Proceedings of
the IEEE Conference on Human Factors and Power Plants, 2002, pp. 3–4.
185. Prevost, M., et. al., Preventing Human Errors in Power Grid Management
Systems
Through
User
Interface
Design,
Proceedings
of
the
IEEE
International
Conference
on
Systems,
Man
and
Cybernetics,
2007,
pp. 626–631.
186. Pyy, P., Laakso, K., Reiman, L., Study of Human Error Related to NPP
Maintenance Activities, Proceedings of the IEEE Conference on Human
Factors and Power Plants, 1997, pp. 12.23–12.28.
187. Pyy. P., An Approach for Assessing Human Decision Reliability, Reliability
Engineering and System Safety, Vol. 68, No. 1, 2000, pp. 17–28.
188. Reiman, T., Oedewald, P., Organizational Factors and Safe Human
Performance
Work
Physiological
Model,
Proceedings
of
the
IEEE
Conference on Human Factors and Power Plants, 2007, pp. 140–144.
189. Rinkus, E.K., Power-Unit Control: Will Automation Replace the Operator,
Thermal Engineering, Vol. 42, No. 3, 1995, pp. 256–258.
190. Rja, P., Miller, C.A., Trust and Etiquette in High-Criticality Automated
Systems, Communications of the ACM, Vol. 47, No. 4, 2004, pp. 51–55.
191. Ryan, T.G., A Task Analysis-Linked Approach for Integrating the Human
Factor in Reliability Assessments of Nuclear Power Plants, Reliability
Engineering and System Safety, Vol. 22, No. 14, 1987, pp. 219–234.
192. Salge, M, Milling, P.M., Who is to Blame, the Operator or the Designer?
Two Stages of Human Failure in the Chernobyl Accident, System Dynamics
Review, Vol. 22, No. 2, 2006, pp. 89–112.
193. Schroeder, L.R., Gaddy, C.D., Beare, A. N., New Control Technologies
Require Good Human Factors Engineering, Power Engineering, Vol. 93,
No. 11, 1989, pp. 29–32.
184
Appendix

---


### Page 190

194. Seminara, J.L., Parsons, S.O., Human Factors Engineering and Power Plant
Maintenance, Maintenance Management International, Vol. 6, No. 1, 1980,
pp. 33–71.
195. Seminara, J.L., Parsons, S.O., Survey of Control-Room Design Practices
with Respect to Human Factors Engineering, Nuclear Safety, Vol. 21, No. 5,
1980, pp. 603–617.
196. Skof, M., Molan, G., Impacts of Human Fitness for Duty on System’s
Performance—Human Reliability and System’s Performance, Proceedings of
the International Conference on PSA/PRA and Severe Accidents, 1994,
pp. 428–435.
197. Smith, D.J., Integrated Control Systems: The Next Step, Power Engineering,
Vol. 95, No. 9, 1991, pp. 17–21.
198. Smith,
L.,
Human
Factors:
Operator
Task
Analysis,
ASME
Safety
Engineering and Risk Analysis, Vol. 1, 1994, pp. 57–61.
199. So, A.T.P., Chan,W.L., A Computer-Version Based Power Plant Monitoring
System, Proceedings of the International Conference on Advances in Power
System Control, Operation, and Management, 1991, pp. 335–340.
200. Sola, R., Nunez, J., Torralba, B., An Overview of Human Factors Activities
in CIEMAT, Proceedings of the IEEE Annual Human Factors Meeting,
1997, pp. 131–134.
201. Spurgin, A., Another View to the State of Human Reliability Analysis,
Reliability Engineering and System Safety, Vol. 29, No. 3, 1990, pp. 365–370.
202. Spurgin, A.J., Human/System Reliability in a Changing Environment,
Proceedings of the IEEE International Conference on Systems, Man and
Cybernetics, 2004, pp. 2746–2751.
203. Spurgin, A.J., Lydell, B.O.Y., Critique of Current Human Reliability
Analysis Methods, Proceedings of the IEEE Conference on Human Factors
and Power Plants, 2002, pp. 312–318.
204. Staples, L., Mc Robbie, H., Design Changes and Human Factors, Nuclear
Plant Journal, Vol. 2, No. 1, 2004, pp. 41–45.
205. Sternheim, E., Moser, T.D., System Design Considerations for High Powered
Testing with Real Time Computers, Proceedings of the Power Industry
Computer Applications Conference, 1977, pp. 407–410.
206. Stojka, T., Use of Expert Judgements for Assessment of Performance
Shaping Factors in Human Reliability Analysis, Proceedings of the American
Nuclear Society International Topical Meeting on Probabilistic Safety
Analysis, 2005, pp. 619–623.
207. Strater, O., Bubb, H., Assessment of Human Reliability Based on Evaluation
of
Plant
Experience:
Requirements
and
Implementation,
Reliability
Engineering and System Safety, Vol. 63, No. 2, 1999, pp. 199–219.
208. Strater, O., Consideration on the Elements of Quantifying Human Reliability,
Reliability Engineering and System Safety, Vol. 83, No. 2, 2004, pp. 255–264.
Appendix
185

---


### Page 191

209. Strod, A.A., The Importance of Human Factors in Performing Maintenance
Tasks Inside the Containment of a Nuclear Power Plant, Proceedings of the
Annual Engineering Conference on Reliability for the Electric Power
Industry, 1980, pp. 82–87.
210. Stultz, S.W., Schroeder, L.R., Incorporating Human Engineering Principles
in Distributed Controls Upgrades, Instrumentation, Control, and Automation
in the Power Industry, Vol. 31, 1988, pp. 135–141.
211. Sundstorm, G.A., User Modelling: A New Technique to Support Designers of
Graphical Support Systems in Conventional Power Plants, Proceedings of the
International Federation of Automatic Control Conference, 1989, pp. 53–57.
212. Swain, A.D., Gutmann, H.E., Human Reliability Analysis Applied to
Nuclear Power, Proceedings of the Annual Reliability and Maintainability
Symposium, 1975, pp. 116–119.
213. Swaton, E., Neboyan, V., Lederman, L., Human Factors in the Operation of
Nuclear Power Plants, International Atomic Energy Bulletin, Vol. 29, No. 4,
1987, pp. 27–30.
214. Sword, J, How Do You Know What You Don’t know? Detecting ‘‘Hidden
Trends’’ in Performance, Proceedings of the IEEE Conference on Human
Factors and Power Plants, 2007, pp. 38–41.
215. Takehisa, O., An Approach to Human Reliability in Man Machine Systems
Using Errors Possibility, Fuzzy Sets and Systems, Vol. 27, 1988, pp. 87–103.
216. Tennant, D.V., Human Factors Consideration in Power Plant Design,
Instrumentation in Power Industry, Vol. 29, 1986, pp. 29–36.
217. Thunberg,
A.,
What
Constitutes
a
Well-Designed
Alarm
System?,
Proceedings of the IEEE Conference on Human Factors and Power Plants,
2007, pp. 85–91.
218. Tonkinson, Tyrone S., SAI’s Behaviour-Based Root Cause Analysis,
Proceedings of the IEEE Conference on Human Factors and Power Plants,
2007, pp. 288–290.
219. Trager, E.A., Human Errors in Events Involving Wrong Unit or Wrong
Train, Nuclear Safety, Vol. 25, No. 5, 1983, pp. 697–703.
220. Tran, T.Q., Boring, R.L., Joe, J.C., Grifﬁth, C.D., Extracting and Converting
Quantitative Data into Human Error Probabilities, Proceedings of the IEEE
Conference on Human Factors and Power Plants, 2007, pp. 164–169.
221. Trubitsyn, V.I., Solov’ev, A.I., Consideration of Operator Activity in
Evaluation of Thermal Power Station Unit Performance Reliability, Applied
Energy: Russian Journal of Fuel, Power and Heat Systems, Vol. 31, No. 4,
1993, pp. 95–103.
222. Usher,
D.M.,
Experience
with
Touch-Screens,
IEE
Colloquium
on
Developments in the Man–Machine Interface in Power Stations, Vol. 6,
1986, pp. 1–4.
223. Usher, D.M., Llett, C., Touch-Screen
Techniques:
Performance and
Application in Power Station Control Displays, Displays, Vol. 7, No. 2,
1986, pp. 56–66.
186
Appendix

---


### Page 192

224. Van Cott, H.P., The Application of Human Factors by Doe Nuclear
Facilities, Proceedings of the Human Factors Society Annual Meeting, 1984,
pp. 138–139.
225. Varma,V.,
Maintenance
Training
Reduces
Human
Errors,
Power
Engineering, Vol. 100, No. 8, 1996, pp. 44–47.
226. Varnicar, J.J., Use of Mockups for Control Panel Enhancements, Proceedings
of the IEEE Conference on Human Factors and Power Plants, 1985,
pp. 41–44.
227. Vaurio, J.K., Human Factors, Human Reliability and Risk Assessment in
Licence Renewal of a Nuclear Power Plant, Reliability Engineering and
System Safety, Vol. 94, No. 11, 2009, pp. 1818–1826.
228. Voss, T.J., An Overview of IEEE Human Factors Standard Activities,
Proceedings of the American Nuclear Society International Topical Meeting
on Nuclear Plant Instrumentation, Control and Human Machine Interface
Technology, 2004, pp. 875–880.
229. Wei, L., He, X.H., Zhao, B.Q., Research on the Relationship Between
Nuclear Power Plant Operator’s Reliability and Human Quality, Atomic
Energy Science and Technology, Vol. 38, No. 4, 2004, pp. 312–316.
230. Wenhui, Z., Validation of Control System Speciﬁcations with Abstract Plant
Models, Proceedings of the International Conference on Computer Safety,
Reliability and Security, 2000, pp. 53–62.
231. Whaley, A.M., Boring, R.L., Blackman, H.S., Mc Cabe, P.H., Hallbert, B.P,
Lessons Learned From Dependency Usage in HERA: Implications for
THERP-Related HRA Methods, Proceedings of the IEEE Conference on
Human Factors and Power Plants, 2007, pp. 322–327.
232. Widrig, R.D., Human Factors: A Major Issue in Plant Aging, Proceedings of
the International Conference on Nuclear Power Plant Aging, Availability
Factor, and Reliability Analysis, 1985, pp. 65–68.
233. Wiegmann, D. A., Overbye, T. J., Human Factors Aspects of Three-Dimensional Visualization of Power System Information, Proceedings of the IEEE
Power Engineering Society General Meeting, 2006, pp. 1–7.
234. Williams, A.R., Jr, Seidenstein. S., Goddard, C.J, Human Factors Survey and
Analysis of Electric Power Control Centers, Proceedings of the Human
factors Society Annual Meeting, 1980, pp. 276–279.
235. Williams, J.C., A Data Based Method for Assessing and Reducing Human
Error to Improve Operational Performance, Proceedings of the IEEE
Conference on Human Factors and Power Plants, 1988, pp. 436–450.
236. Wu, T.M., Lee, J.Y., A Large Scale Implementation of Human Factors
Engineering for the Lungmen Nuclear Power Project, Proceedings of the 4th
American Nuclear Society International Topical Meeting on Nuclear Plant
Instrumentation, Controls and Human–Machine Interface Technology, 2004,
pp. 1–10.
237. Yan, X., Milgram, P., Doyle, D.J., Two Classes of Problem Solving Situations
in Managing Complex Systems, Proceedings of the Human Factors and
Ergonomics Society Annual Meeting, 1993, pp. 529–533.
Appendix
187

---


### Page 193

238. Yean-Chuan Y., Lin,T.Z ., Chung, J.S., Der-Yu H., Lessons Learned from
Reviewing
a Plant-Speciﬁc
Reliability
Analysis,
Proceedings
of
the
International Reliability, Availability, Maintainability Conference for the
Electric Power Industry, 1988, pp. 452–457.
239. Yip, W. T., Chan, K.C.C, Uniﬁed Human–Computer Interaction Requirements
Analysis Framework for Complex Socio-technical Systems, International
Journal of Human–Computer Interaction, Vol. 26, No. 1–3, 2010, pp. 1–21.
240. Yoshimura, S., Takayanagi, H., Study on Modeling of Operator’s Learning
Mechanism, Proceedings of the IEEE International Conference on Systems,
Man, and Cybernetics, 1999, pp. 721–726.
241. Yutaka F., Kazuo F., Shunsuke, K, Identiﬁcation of Causes of Human Errors
in Support of the Development of Intelligent Computer-Assisted Instruction
Systems for Plant Operator Training, Reliability Engineering and System
Safety, Vol. 47, 1995, pp. 75–84.
242. Zhao, T., et. al, Based on Multi-Agent Optimize the Operation of the Power
Plant Unit of Assessment Management System, IET Seminar Digest, Vol. 1,
No.3, 2008, pp. 214–219.
243. Zhonaghai, Z, Lin, F., Hongfa, D., Incremental Evaluation Method—An
Integrated Method to Assess Urban Energy System, Proceedings of the
International Conference on Management and Service Science, 2010,
pp. 5–6.
244. Zhuravyov, G.E., Sakov, B.A., Ergonomic and Psychological Provisions of a
Power Plant, Proceedings of the Triennial Congress of the International
Ergonomics Association and the Annual Meeting of the Human Factors and
Ergonomics Association, 2000, pp. 831–834.
245. Zizzo, D., Gutierrez, R., Yu, K., Human Factors Veriﬁcation of the
Advanced Nuclear Plant Control Room Design, Proceedings of the Annual
Joint ISA POWID/EPRI Controls and Instrumentation Conference, 2008,
pp. 252–263.
188
Appendix

---
