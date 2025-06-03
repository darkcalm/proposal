

---

Page 1

---

Feeding the Coffee Habit: A Longitudinal Study of a Robo-Barista
Mei Yii Lim1, David A. Robb1, Bruce W. Wilson1 and Helen Hastie1
Abstract— Studying Human-Robot Interaction over time can
provide insights into what really happens when a robot becomes
part of people’s everyday lives. “In the Wild” studies inform
the design of social robots, such as for the service industry, to
enable them to remain engaging and useful beyond the novelty
effect and initial adoption. This paper presents an “In the Wild”
experiment where we explored the evolution of interaction
between users and a Robo-Barista. We show that perceived trust
and prior attitudes are both important factors associated with
the usefulness, adaptability and likeability of the Robo-Barista.
A combination of interaction features and user attributes are
used to predict user satisfaction. Qualitative insights illuminated
users’ Robo-Barista experience and contribute to a number of
lessons learned for future long-term studies.
I. INTRODUCTION
Social robots are expected to increasingly become part of
our everyday lives. They are designed to interact socially
with humans and have made appearances in various public
and domestic venues including schools [1], malls [2], restau-
rants [3] and homes [4]. When these robots are ensconced
in our daily lives, the relationship between the human and
robot will evolve over time [5]. Therefore, understanding
people’s attitude towards, and relationship with, embedded
technological artifacts will be key. As a result, it is important
to understand how trust and acceptance change over long
periods in human-robot interaction (HRI).
To date, most HRI studies focus on short-term interactions
between humans and robots, as conducting a longitudinal
study in natural settings imposes various methodological
and empirical challenges [6], [7] and requires much effort.
However, such short-term studies do not generalise well to
everyday life environments and interactions, within which the
robots need to operate. Furthermore, robots are subject to the
novelty effect - initial excitement surrounding the interaction
that fades after a certain period of time. They do not capture
the difficulty of sustaining engagement and high interaction
quality long-term. Repeated interactions are required in many
real-world robot applications for deployment (e.g. in homes,
hospitals, receptions and for hospitality). This affords us
the opportunity to investigate relationship-building and what
leads to acceptance over a period of time.
In this paper, we present a longitudinal “In the Wild”
experiment with a Robo-Barista in a natural setting. A Furhat
robot1 (Figure 1) was set up in an academic department com-
For the purpose of open access, the author has applied a Creative
Commons Attribution (CC BY) license to any Author Accepted Manuscript
version arising.
1School of Mathematical and Computer Sciences, Heriot-Watt University,
EH14 4AS, UK m.lim@hw.ac.uk, d.a.robb@hw.ac.uk,
bww1@hw.ac.uk, h.hastie@hw.ac.uk
1https://furhatrobotics.com/ (last assessed: Mar 27, 2023)
mon room to interact with people and serve up the requested
coffee via natural language interaction. This emulates a robot
that you might find in a caf´e, acting as a barista, with whom
regular customers would interact periodically over a long
period of time.
Fig. 1.
The Robo-Barista installation. Top left: inside the booth. Top
Right: the booth situated in our departmental common room. Bottom: a
user interacting with the Robo-Barista
We explored the evolution of interaction between users
and the Robo-Barista over 6 weeks. We focused on various
social robots acceptance factors, namely perceived useful-
ness [8], likeability [9], perceived trustworthiness [10] and
perceived adaptability [8]. We took into consideration users’
prior dispositions, specifically their negative attitude towards
robots [11] and propensity to trust robots [12], as well as
usage patterns and user satisfaction. In this study, we aim to
answer the following research questions:
• RQ1: What factors play a role in the long-term user
perceptions of the Robo-Barista?
• RQ2: Did user attitude towards robots change over the
study period?
• RQ3: What lessons are learned for a long-term study
in the wild?
II. RELATED WORK
Long-term effects exist in the use of technology and
different interaction patterns have been observed over time
and after the novelty effect wears off [6], [13]. To understand
how people perceive technology, we need to study their
reasons for adopting or not adopting it [14]. Kidd and
Breazeal [15] posit three important factors in creating a
arXiv:2309.02942v1  [cs.RO]  6 Sep 2023


---

Page 2

---

long-term relationship between humans and robots, which
we took into consideration in our study design. These are i)
motivation to use the system, ii) engagement of the user, and
iii) trustworthiness of the system. In order for any system to
be used, users must be motivated to play an active part. The
ability to draw a person into an interaction is an important
first step for the user to carry out and test the abilities of a
robot [16]. Once interaction occurs, the user must be willing
to carry on regular interactions and must have continuous
belief that the robot is capable of performing its tasks over
the course of the relationship.
With regards to engagement and relationship-building, we
are interested in how interactions between users and the
Robo-Barista evolve, the type of relationship users build and
factors that are important to the relationship. According to
Sung et al. [6], there are 4 stages of interaction: pre-adoption,
adoption, adaptation, use and retention. Based on a 6 months
study of Roomba2 in 30 households, their study shows that
users began to view the robots as social agents after the initial
interaction and showed higher satisfaction in all categories
of user experiences during the adoption phase. Adaptation
occurs when the users make necessary changes to enable
the technology to be incorporated, leading to reaffirmation
or rejection of further use. De Graff et al. [4] extended the
acceptance phases to include identification, which happens
when the technology becomes a personal object for making
status claims. Their study revealed that there was an initial
drop in user experience before rising again when the robot
was used over a longer period of time.
In a 3 months study with severe cognitively impaired
children, a seal robot PARO acted as a mediator for social
interaction and was able to drive changes in people’s be-
haviour [17]. The interaction was successful because people
viewed the robots as social agents with affection rather than
a mere object. Several studies observed decreased interaction
over time due to unmet initial expectations such as the
case with Pleo3 [7] and novelty effects wearing off [18].
Although Tanaka et al. [18] observed a lost of interest in the
robot QRIO4 over time, they also witnessed an improvement
in interaction quality towards the end of their study when
children hugged and pulled the robot’s hand asking it to
go for a walk with them. A similar pattern was observed
with a dancing Robovie, despite decreased interest, children
collectively created an information board and shared their
knowledge about the robot towards the end of the study [1].
In the service industry context, Berardinis et al. [19]
applied different supervised learning techniques for coffee
recommendations based on users’ preferences. Recently,
Irfan et al. [20] carried out a real-world study of fully au-
tonomous interaction, evaluating the potential of data-driven
approaches in generic and personalised long-term HRI. They
generated two datasets5 for a barista, one containing generic
interactions between customers and a barista and one with
2https://www.irobot.co.uk/, last assessed: Mar 29, 2023
3https://robots.ieee.org/robots/pleo/, last assessed: Mar 29, 2023
4https://robots.ieee.org/robots/qrio/, last assessed: Mar 29, 2023
5https://github.com/birfan/BaristaDatasets, last assessed: Mar 29, 2023
personalised long-term interaction, where the barista would
learn and recognise the users and recall their preferences.
The authors argue that long-term interactions require re-
membering users and their preferences continuously, for a
personalised experience.
Rossi and Rossi [21] also stressed that effective cus-
tomer retention is possible only when the robot is able
to personalise the interaction to the user’s needs. They
found that customers’ attitude towards the robot positively or
negatively affects their trust and satisfaction in the service.
Earlier studies have also shown that incremental learning and
adaptation are vital for life-like HRI [22], [23]
Besides user engagement, trustworthiness is key to the
acceptance of the robots [15], [24]. A robot must be seen as
dependable and trustworthy for a person to use or collaborate
with it for completing a task. Trust formation begins prior
to the interaction with an automated system and different
layers of trust are built up sequentially [10]. Hancock et al.
[25] found that robot-related, human-related and contextual
factors are predictors of trust. Inappropriate levels of robot
trust could not only result in a frustrating experience but
misuse (overly high trust) or disuse (overly low levels of
trust) of the robot [26].
III. SETUP
The Robo-Barista was located at a departmental Common
Room frequented by staff and postgraduate students. Its
setup consists of a Furhat robot, linked up to a high-end
coffee machine, Jura, via Bluetooth. The interaction starts
when the Robo-Barista detects and greets a user. If the user
is a first timer, it refers them to the registration signage,
otherwise it asks to scan their loyalty card using its QR
code scanning capability. After identifying the user, it makes
order suggestions based on the user’s past preferences (refer
to Figure 2 for an example) or if the user is ordering for
the first time, it asks for an order, which can be a type of
coffee or tea. It then confirms the request and asks if the user
would like it to detect whether a stronger coffee is needed.
If the user agrees, it uses its tiredness detector component
developed by Cisco6 - a vision component based on Google
Cloud Vision API and the Microsoft Azure Face API - to
detect the user’s fatigue level from their facial features. If
the level is high, it suggests an extra shot of coffee [27].
The verbal interaction is implemented using an open-
source conversational AI platform, RASA7. The DIET model
was employed [28] for Natural Language Understanding. It
handles both user intent classification and entity recognition
in a single transformer architecture and allows for the use
of pre-trained embedding models, such as BERT [29]. For
the dialogue management, the RASA TED Policy [30] is
used in combination with a set of dialogue handwritten
rules. The TED Policy applies a machine learning policy
that can generalise patterns from example conversations and
uses context from previous user utterances to perform well
in a non-linear conversation.
6https://www.cisco.com, last assessed: Mar 27, 2023
7https://rasa.com/, last assessed: Mar 27, 2023


---

Page 3

---

Fig. 2. An excerpt of the conversation between a user and the Robo-Barista
User identification is important for relationship establish-
ment [5]. Unfortunately, current visual and auditory sensing
technologies cannot identify users with certainty. To combat
this problem, we introduced the loyalty card scheme, which
is not uncommon in a caf´e setting, to accurately identify a
user for both data recording and interaction management.
While user questionnaires for study recruitment and exit
were prompted by signage (see Section IV), periodic user
feedback was requested by the robot. To reduce participation
burden this was collected periodically. Specifically, for every
third interaction with each user, it asks them to fill in a short
feedback questionnaire before going into idle mode. Once the
order is ready, the Robo-Barista informs the user and engages
them in small talk (Fig. 2), including various topics such as
weather, jokes and hobbies. It then asks the user to rate their
satisfaction level on the interaction and whether they received
the drink they ordered before ending the conversation.
As mentioned in Section II, adaptation is important for
personalised interaction. The Robo-Barista remembers users’
previous interactions and makes suggestions for orders based
on their most frequent choices. Additionally, it exhibits
shared attention with the user through non-verbal behaviour
and adapts the small talk to each user avoiding topics
repetition. It also adapts its remarks based on the user’s
satisfaction response, for example, “I am glad to hear that”
when the user gave a rating above average.
IV. EXPERIMENT
The main aim of the experiment is to explore factors that
lead to the acceptance of the Robo-Barista. We investigate
how various factors change over time and if there are
correlations between them. These factors are: prior attitude
towards robots, perceived usefulness, likeability, perceived
trustworthiness, perceived adaptability, user satisfaction and
usage pattern. Throughout the following sections, we present
lessons learned as they emerge from the discussion.
Before we begin the detailed description of the study, a
brief word about nomenclature: As the different collection
instruments are described and measures are introduced we
label the measures with the concepts that they measure. Later,
to help distinguish at what stage a measure is collected, we
adopt a policy of prefixing our measure labels with the study
stage at which they were collected. For example, RecruitAge
is collected on recruitment.
The procedure was ethically approved by Heriot-Watt
University School of Mathematical and Computer Sciences’
ethics board. The Robo-Barista was situated in the School
Common Room. Users were recruited through signage
placed beside the Robo-Barista. In order to participate, they
were required to bring their own mug and have an internet
connected smart phone so that they could access the online
questionnaires (all questionnaires were accessible via QR
codes). To sign up, they were given a loyalty card with
a unique customer number as identification. These cards
were in envelopes and could be picked up from a dispenser
marked “Customer Cards” below the signage. Figure 3 shows
the various input and feedback we elicited from the users
throughout the interaction period. Table I gives the descrip-
tive statistics for all the continuous measures (descriptions
to follow) captured in Figure 3.
Fig. 3.
Questionnaires and user feedback flow
TABLE I
DESCRIPTIVE STATISTICS FOR ALL NUMERIC MEASURES (RECRUIT AND
EXIT N=21, INTERACTIONS (INT) N=112). INTTIME-TAKEN IS IN
MINS:SECS.
Measure
Mean
Med
SD
Max
Min
RecruitAge
35.6
34.5
13.50
23.5
74.5
RecruitNARS
2.39
2.40
0.48
1.67
3.47
RecruitPTT
3.42
3.33
0.65
2.33
4.50
ExitNARS
2.40
2.67
0.43
1.67
3.13
ExitTrust
4.88
5.00
0.87
3.00
6.14
ExitUsefulness
4.20
4.33
1.64
1.00
6.67
ExitAdaptability
4.28
4.33
0.94
2.67
6.00
ExitLikeability
63.3
61.8
15.2
32.0
88.6
IntUsat
7.25
7.00
2.33
1
10
IntTime-taken
2:38
2:33
0:34
1:35
4:50
IntTurns-user
9.00
8.00
2.77
5
21
IntTurns-robot
11.14
11.00
3.09
6
25
IntRobot-apologies
1.10
1.00
1.53
0
10
A. Recruitment Questionnaire
After giving consent for their participation at the start
of the ‘Recruitment Questionnaire’, the users entered their


---

Page 4

---

customer number and some demographic information about
themselves specifically: Age Group (18-29, 30-39, 40-49,
up to 80-89 then 90 or above); Gender (Male, Female,
Non-binary/third gender, Prefer not to say, Other); and their
Coffee drinking habits (How often do you drink coffee?:
More than 1 cup per day, A cup per day, A few cups per
week but not daily, None at all). They were also asked about
their prior dispositions towards robots using the following
measures:
• 14-item Negative Attitude Towards Robots (NARS)
questionnaire [11], and
• 6-item Propensity to Trust Technology (PTT) ques-
tionnaire [12], which measures stable characteristics in
individuals, attitudes towards technology and whether
people were likely to collaborate with technology.
Both questionnaires use a 5-point Likert scale ranging
from strongly disagree (1) to strongly agree (5). Prior work
has shown that adapting the PTT to interaction context
enhances the reliability of the measure, and hence the pre-
dictability of perceived trustworthiness [12]. Therefore, we
adapted the PTT questionnaire to our scenario with the word
“technology” being replaced by “robot”. We also added an
additional question to the NARS specific to our scenario -
“I would feel uneasy if I had to order a drink from robots”.
Once the users signed up, they could start ordering drinks
from the Robo-Barista. They were being offered up to one
cup of free coffee or tea a day. The interaction is as described
in Section III. Audio, but not video, was recorded throughout
the interaction.
B. Each Interaction Evaluation
After each Interaction, the users provided a self report of
a) their satisfaction rating (IntUsat) to the question “On a
scale from 1 to 10, with 10 being the highest, how satisfied
with this interaction were you today?”; and b) whether
they received the correct coffee (IntCoffee-Correct): True,
False, Walked-Away (before being asked or answering), Ask-
Repeat (Asked robot to repeat the question). In addition, we
recorded the following interaction data: Interaction duration
(IntTime-taken), number of user and robot turns (IntTurns-
user and IntTurns-robot) and number of robot apologies
(IntRobot-apologies).
Lesson 1: Don’t expect users to patiently complete
interactions In the wild, users can get interrupted,
leave unexpectedly, and do not necessarily hang around
politely until the robot has completed every step of its
programmed interaction.
C. Periodic Questionnaire
Users were prompted, after every three coffees, to give
feedback on their experience through the ‘Periodic Ques-
tionnaire’, where they rated the following:
• Perceived trustworthiness - their level of trust in the
Robo-Barista using an adapted LETRAS-G (Trust)
[10], a subset of the empirically determined scale of
trust in automated systems [31],
• Perceived usefulness (Usefulness) of the Robo-Barista
[8]
• Perceived Adaptability (Adaptability) of the Robo-
Barista [8] and
• Likeability from the portion of the Godspeed question-
naire (Likeability) [9]
The Trust, Adaptability (e.g. “I think the robot will only
do what I need at that particular moment”) and Usefulness
items were rated using 7-point Likert scales ranging from
Strongly Disagree (1) to Strongly Agree (7). Likert scales
allow only integer responses and may fail to capture the
subtle effects evoked by individual variability [32]. In order
to allow for a more fine-grained measure and more robust
detection of subtle individual differences, sliders ranging
from 0 to 100 were used for the rating of the Likeability
items. Additionally, a general open question, “Any other
comments?”, was asked allowing the users to give worded
feedback on aspects or issues.
D. Exit Questionnaire
At the end of the study, users were asked to fill out an ‘Exit
Questionnaire’. After entering their customer number, users
were given the NARS, Trust, Usefulness, Adaptability
and Likeability items to rate. Finally, the open questions
listed below were asked to help us understand better users’
perception of the Robo-Barista and provide guidelines for
future refinements.
1) Would you continue using the Robo-Barista? Why?
2) If you have the opportunity, which features would you
add to the Robo-Barista?
3) Which aspects (negative/positive) regarding the Robo-
Barista could you highlight?
4) What is the Robo-Barista to you? (A tool to perform
task, A social mediator among common room visitors,
A social agent or A status symbol [4], [6])
5) Any other comments?
V. DATA COLLECTED
In this section, we describe the actual data collected,
detailing how the numbers of responses, missing values and
the need to recode some categorical fields, led to the final
populations of responses included in analysis.
On recruitment, 53 users gave consent and provided the
information detailed in Subsection IV-A. During the study,
186 interactions were recorded, 136 included responses to
the in-dialogue questions for user satisfaction (IntUsat) and
task performance (IntCoffee-Correct). Of those 136, 8 were
by users, who had not completed the online recruitment
form (i.e. no consent) and were set aside. Only 12 ‘Periodic
Questionnaire’ responses were recorded from just 8 users
(one without providing consent).
Furthermore, only 22 Exit responses were collected. One
user had not recorded their consent (thus the response was
set aside). This left 21 valid responses, where participants
did both the recruitment and exit surveys (referred to as
Thru-Study users). Of the 21 Thru-Study users, 15 identified
as Male, 4 as Female, 1 as non-binary, and 1 preferred


---

Page 5

---

not to say. This was representative of the Common Room
population during this early post-pandemic period.
We decided that, while the Recruitment and Exit returns
of the 21 Thru-Study users could give a useful picture of
the start and end of the study, the low number of Periodic
returns were too few to usefully characterise Robo-Barista
use during the course of the study. However, the interaction
data itself was numerous enough and this is what we analyse
to explore what transpired between Recruitment and Exit.
Of the 21 Thru-Study users, one had no fully recorded
interactions with a IntUsat rating, four had only one, and
16 had two or more interactions. An average (IntMeanUsat)
was calculated for users with at least one user satisfaction
rating, else IntMeanUsat was coded as missing.
Lesson 2: Unexpected use patterns People may use
your installation in ways you had not expected: e.g.
We had some users who used coffee “loyalty” cards to
access the robot and get coffee but who did not visit the
online recruitment form to sign up and give consent, as
per instructions on the installation signage.
Lesson 3: Attrition Rate Be prepared for users to drop
out from an “In the Wild” study. Motivation is needed
to prompt better return rates for periodic feedback (e.g.
extra cups of coffee).
VI. DATA ANALYSIS METHOD
The experiment was essentially an observational study,
rather than variable manipulation. Users interacted with the
Robo-Barista. We asked them questions, and recorded their
interactions and responses. Our methods, described below,
were chosen to exploit the observational nature of the data.
A. Correlation
We were able to explore possible associations between the
measures collected in the study through bi-variate correlation
[33]. In Section VII, we report statistically significant corre-
lations between various factors, such as users’ PTT and the
likeability of the robot.
B. Multiple Linear Regression (MLR)
We probe the influences on users’ in-dialogue self-reported
satisfaction (IntUsat) using Univariate Multiple Linear Re-
gression (MLR). This helps to understand what combina-
tion of interaction variables contribute to user satisfaction,
inspired by the PARADISE framework [34]. To allow a
regression analysis, the variables need to be either numeric
or categorical but with only two categories [33].
On initial modeling, we found that the interaction data
(described in Subsection IV-B and in the bottom part of
Table I) alone were not yielding effective models. So to
explore whether user attributes might account for some of
the variability in IntUsat, we added demographic attributes
gathered by the Recruitment questionnaire (see Subsection
IV-A and top part of Table I), with some recoding of the
categorical data into two categories.
The MLR was run excluding missing values listwise.
This meant that starting with 136 full interactions, dropping
the 8 without recruitment consent, those not identifying as
Male/Female re-coded as missing RecruitGender values,
and IntCoffee-Correct (Walked-Away, Ask-Repeat) values
being re-coded as missing, 112 interactions remained and
were included in the MLR, the results of which are reported
in Subsection VII-A.
C. Qualitative Analysis
The qualitative questionnaire items were collected. A
codebook was created using an inductive approach similar
to grounded theory and open coding [35]. Two coders met
to discuss the codebook, and unitisation policy [36]. They
then independently coded all the data. The average agreement
across all codes was 95.8% with a Cohen’s Kappa of 0.77.
Themes were developed based on the coding [37]. The
themes and contributing codes are described in the next
section along with the qualitative results.
VII. RESULTS AND DISCUSSION
Firstly, we examine quantitative results, addressing their
bearing on RQ1 and RQ2, then the qualitative results, as
they related to RQ1 alone, and finally we focus on RQ3
and lessons learned.
TABLE II
SIGNIFICANT CORRELATIONS: SHOWING EACH BI-VARIATE
CORRELATION, WITH PEARSON’S r AND TWO-TAILED p-VALUES BY RQ.
Row No
RQ
Variable pair
r
p
1
1
ExitTrust v. ExitUsefulness
.765
<.001
2
1
ExitTrust v. ExitAdaptability
.616
.003
3
1
ExitTrust v. ExitLikeabilty
.535
.012
4
1
RecruitPTT v. ExitUsefulness
.600
.004
5
1
RecruitPTT v. ExitAdaptability
.569
.007
6
1
IntMeanUsat v. ExitUsefulness
.567
.009
7
1
IntMeanUsat v. ExitAdaptability
.547
.013
8
2
RecruitNARS v. ExitNARS
.699
<.001
9
2
RecruitPTT v. ExitNARS
-.631
.002
A. Quantitative Results
RQ1: What factors play a role in the long-term user
perceptions of the Robo-Barista?
As illustrated in Table II, trust was a clear factor. Specifi-
cally, there were strong8 positive correlations between the
trust in the robot after the final interaction (ExitTrust)
and
perceived
usefulness (ExitUsefulness),
adaptability
(ExitAdaptability) and general likeability (ExitLikeabilty).
(Table II rows 1 to 3). This is evidence that trust is either
influenced by or is influencing views on those three accep-
tance measures. There were also strong positive correlations
between users’ propensity to trust (RecruitPTT) and both
usefulness and adaptability (Table II rows 4 and 5). This is
another indication that trust is an active factor here.
8Pearson’s r of 0.5 and over equates to “strong”, while 0.3 to 0.5 equates
to “medium” [33]


---

Page 6

---

Additionally, there was a strong positive correlation be-
tween user satisfaction (IntMeanUsat) and both ExitUseful-
ness and ExitAdaptability (Table II rows 6 and 7), which
was not surprising as prior work found that users’ perception
of the robot contributes to their interaction satisfaction [21].
Finding 1: Trust is important in perceptions of
the Robo-Barista Perceived trust of the robot and an
individual’s propensity to trust affect the perceptions of
usefulness, adaptability and likeability of the robot.
MLR analysis allowed a deep dive into factors that af-
fected user satisfaction. Table III gives the variables used in
this model in order of influence, as given by the Standardized
Beta coefficient. The model has R2 = .339, which indicates
that 33.9% of the variability in IntUsat is explained by these
seven variables.
TABLE III
THE MULTIPLE LINEAR REGRESSION RESULTS. THE INFLUENCE ON
INTUSAT OF EACH VARIABLE IN THE MODEL AS REVEALED BY THEIR
STANDARDIZED BETA COEFFICIENT.
Variable
Standardized Beta coefficient
IntCoffee-Correct
.270
RecruitGender
.251
RecruitAge
-.232
RecruitNARS
-.210
RecruitCoffeeHabit
-.210
IntTurns-user
-.166
IntTime-taken
-.116
Table III can be interpreted as follows: IntUsat was
higher: when a user identified as female (RecruitGender),
when users’ were younger (RecruitAge), when their negative
attitude to robots was lower (RecruitNARS), when the user’s
coffee habit was low (RecruitCoffeeHabit), when the robot
dispensed the correct coffee (IntCoffee-Correct), when they
took fewer turns in an interaction (IntTurns-user), and when
their interaction was shorter (IntTime-taken).
Finding 2: Interaction features and user attributes
predict user satisfaction
Gender, age, attitude to
robots, and their coffee habits all contribute to user
satisfaction, as well as, whether they got the right coffee
and how long it took.
RQ2: Did user attitude towards robots change over the
study period?
Given that we had measured NARS at recruitment and
exit, we were able to compare users’ negative attitudes to
robots at the the start and end of the study. A paired sample
t-test, (RecruitNARS Mean, 2.39, ExitNARS Mean, 2.40,
N=21, t(20)=−.122, sig two-tailed p=0.904) revealed no
statistically significant difference between the two measures.
This shows that users’ negative attitudes to robots did not
change through the study, confirming NARS as a relatively
stable characteristic measure. By way of confirming the t-
test result, there is also a strong positive correlation of
RecruitNARS with ExitNARS (Table II row 8).
We also report here the strong negative correlation be-
tween Propensity to Trust (RecruitPTT) and users’ neg-
ative attitude to robots after completing the experiment
(ExitNARS) (Table II row 9). This confirms users with low
Propensity to Trust are also likely to have a high negative
attitude to robots, as seen in prior work [38].
Finding 3: Negative attitudes to robots did not
change during the study NARS did not change from
start to end of the study, reflecting that NARS is a
reliable measure of a stable trait, confirming prior work.
B. Qualitative Results
Returning to RQ1: What factors play a role in the long-
term user perceptions of the Robo-Barista?
The views expressed in the qualitative responses of the 21
Thru-Study users (mostly yielded from the Exit question-
naire) give some interesting insights into how users viewed
the Robo-Barista and contribute to our understanding of
RQ1. The one closed question in the ‘Exit questionnaire’
- “What is the Robo-Barista to you?” - was overwhelmingly
answered by choosing “A tool to perform tasks” (N=18)
with 2 users answering “A social agent” and one, “A social
mediator among common room visitors”. Although this
mostly utilitarian view is reflected in the analysis of the
open responses below with the majority focusing on practical
aspects of the Robo-Barista service, a proportion of the views
did focus on aspects such as the Robot’s appearance, the
quality of the Robot’s conversation, and their enjoyment of
the experience.
The analysis (described in Subsection VI-C) led to the
development of themes expressed by the users. In our de-
scription of those views, we also indicate the percentage of
the total 21 Thru-Study users who express them. The most
popular themes are summarised in Table IV.
TABLE IV
THEMES EXPRESSED AND THEIR PERCENTAGE POPULARITY AMONG
THE 21 THRU-STUDY USERS (N).
Theme
Example codes
Expressed
by % of N
Dialogue
Repetition,
Conversation
flow,
Pitch
86%
Coffee
Free, Selection, Quality
67%
Feelings
Interest,
Enjoyment,
Boredom,
Comfort
62%
Service
Reliability, Benefits
57%
Physical Interface
Cup placement, ID card reading
52%
Pace
Duration, Speed
38%
Being Understood
Accents, Background noise
29%
Robot
Appearance, Demeanor
19%
Users were asked whether or not they would continue
using the Robo-Barista. The majority, 71%, said they would,
24% said they wouldn’t and one (5%) gave a conditional
view “Probably not, unless the coffee remains free” [P9].
Indeed 24% mentioned free coffee being a motivating fac-
tor. Other reasons expressed for wishing to continue using
the service included coffee quality, and the enjoyment and
interest of the experience.


---

Page 7

---

Beyond the majority stating they viewed the robot as
a tool, other indications of this utilitarian view are that,
although the robot introduced itself as “Alex”, only two
(10%) referred to it by name in their feedback responses
and only two made any comparison with human baristas.
The “Dialogue” theme, perhaps unsurprisingly with a
conversational robot, was the most popular. Users wished for
more flexible and free flowing chat (14%) from the Robo-
Barista and less repetition from one interaction to the next
(29%). Some found the interaction initially challenging but it
seems they may have adapted, something expressed by P11:
“I have adapted to the robot. I know where to stand ... how
to speak to it”. This finding is inline with prior work [39]
stating that users will over time adapt to and come up with
workarounds for possible shortcomings to fulfill their needs.
This leads on to another aspect of the Robo-Barista service
in that for the duration of the study it was a feature of
the common room, and it seems that others perhaps found
it an entertaining feature beyond its coffee function. Here
one user’s feedback is perhaps alluding to the idiosyncrasies
of the Robot’s conversations when overheard from outside
the booth: “I enjoyed the interaction, the coffee, and had a
good laugh hearing Alex talk to its customers” [P19]. Some
feedback mentioned the tiredness detector feature which
was greeted both positively and negatively: “I loved the
suggestion to add caffeine too, it was quite funny” [P17]
and ”Always gives the same suggestions for extra dose, do i
constantly look tired ?” [P4].
Users could have a nuanced view of the robot e.g. P17
(quoted above) began their answer stating, “I was quite
impressed by what it could do and understand.”, but when
describing their desired feature wrote “Add some functional-
ity to make it shut up :D as harsh as that sounds, sometimes
you just want to have a coffee”. Another new functionality
suggestion was for visual display to show what the robot
was seeing, which when taken in conjunction with one user
expressing doubt as to whether the tiredness detector was
simply random [P15], we can see that more visual feedback
could perhaps help with transparency.
C. Lessons Learned
RQ3: What lessons are learned for a long-term study in
the wild?
Throughout this paper, we have presented a number of
lessons learned. Other challenges were mostly around logis-
tics, some of which were expected (e.g. booting up at the start
of day), but there were also unforeseen technical challenges
(e.g. the coffee machine doing unexpected cleans). These
had to be met by the four-person on-site support team, which
included two departmental support staff and two researchers,
one taking the role of “robot wrangler” [40], while the other
fielded user emails and coordinated support.
The Robo-Barista needed routine check-ups at the start and
the end of each day, to clean, provision the coffee machine,
to boot up and shut down the system. This duty was shared
among the team on a rota. Aside from the challenge of coping
with the sometimes noisy environment around the booth the
most intractable technical challenge was in the unpredictable
nature of the coffee machine’s cleaning activity, a 20 second
automated action. If the coffee machine initiated this rinsing
procedure during a user interaction, it would cause the
machine to report a “service unavailable” error to the system.
This would a) prevent the system properly responding to user
requests and b) cause the system to generate an email alert to
the support team. Unfortunately, there was no way to predict
or control this behaviour of the coffee machine.
Lesson 4: Expect technical and support challenges:
Supporting a robot installation “In the Wild” may
require more time and resources than you originally
think might be needed.
The “Feelings and Dialogue-Interface” themes revealed
that users often wish for a service that would adapt more
to their individual use and offer more variety in interaction.
e.g. “I do not need the robot to tell me, every day, where
to put my loyalty card.”[P11], and “Chat should perhaps
be a bit more flexible. Having to go through the same
questions again with it feels redundant” [P6]. Indeed, the
MLR results indicate that user attributes, including age and
gender, influence IntUsat and thus show that this would be
a good direction to explore further.
Lesson 5: Flexibility, adaptability and variety in
long-term study Aim to offer more flexibility, adapt-
ability and variety in the robot interactions, as previous
research suggested [21], [41], [42], with the possibility
of developing interaction features to appeal to different
user groups.
VIII. CONCLUSION AND FUTURE WORK
This paper presents an exploratory longitudinal “In the
Wild” study of social robot acceptance to better understand
users’ perceptions of such robots over time, which can
help to better shape future design and implementation. It
has uncovered several important lessons and findings. The
unexpected challenges occurring at various stages of the
deployment perhaps is not surprising due to the uncertainties
in the environment and the heterogeneous group of users
[42]. Additional effort in terms of usability, flexibility and
adaptation will be necessary in future studies. Ethics approval
for a less formal engagement of users will be useful in such
installation. In terms of findings, trust has been shown to
play a key role in influencing acceptance of the robot. It is
also interesting to see that users’ satisfaction with the robot
depends on individual differences, confirming previous find-
ings [38], [43]. Thus, personalisation should be an important
part of interaction design for these types of long term studies.
IX. ACKNOWLEDGEMENTS
We would like to thank Jose David Aguas Lopes for his
work on the original Robo-Barista. Special thanks go to
Claire Porter and Jennifer Hurley for their indispensable sup-
port with the maintenance and upkeep of the Robo-Barista.
This work was funded and supported by the UKRI Node


---

Page 8

---

on Trust (EP/V026682/1) https://trust.tas.ac.uk
and EPSRC CDT on Robotics and Autonomous Systems
(EP/S023208/1).
REFERENCES
[1] T. Kanda, R. Sato, N. Saiwaki, and H. Ishiguro, “A two-month field
trial in an elementary school for long-term human-robot interaction,”
IEEE Trans. Robot, vol. 23, no. 5, pp. 962–971, 2007.
[2] T. Kanda, M. Shiomi, Z. Miyashita, H. Ishiguro, and N. Hagita, “A
communication robot in a shopping mall,” IEEE Trans. Robot, vol. 26,
pp. 897–913, 2010.
[3] S.
Prideaux,
“Robot
host
welcomes
guests
at
new
dubai
mall
restaurant,”
The
National,
Jan
2019.
[Online].
Available:
https://www.thenational.ae/lifestyle/food/
robot-hostwelcomes-guests-at-new-dubai-mall-restaurant-1.813177,
Lastaccessed:28Feb2022
[4] M. M. de Graaf, S. Ben Allouch, and J. A. van Dijk, “A phased
framework for long-term user acceptance of interactive technology in
domestic environments,” vol. 20, no. 7, pp. 2582––2603, 2018.
[5] R. A. Hinde, Ed., Individuals, relationships and culture: Links between
ethology and the social sciences.
England: Cambridge University
Press., 1988.
[6] G. R. Sung J, Christensen HI, “Robots in the wild: understanding
long-term use,” in Proc of HRI ’09.
New York: ACM, 2009, pp.
245–252.
[7] Y. Fernaeus, M. H˚akansson, M. Jacobsson, and S. Ljungblad, “How
do you play with a robotic toy animal?: A long-term study of pleo.”
in Proc. of the 9th international conference on interaction design and
children.
New York: ACM, 2010, pp. 39–48.
[8] M. Heerink, B. Kr¨ose, V. Evers, , and B. Wielinga, “Assessing
acceptance of assistive social agent technology by older adults: the
almere model,” Int. J. Soc. Robot, vol. 2, pp. 361–375, 2010.
[9] C. Bartneck, D. Kuli´c, E. Croft, and S. Zoghbi, “Measurement
instruments for the anthropomorphism, animacy, likeability, perceived
intelligence, and perceived safety of robots,” vol. 1, pp. 71–81, 2009.
[10] J. M. Kraus, “Psychological processes in the formation and calibration
of trust in automation,” Ph.D. dissertation, Ulm University, Germany,
2020.
[11] T. Nomura, T. Suzuki, T. Kanda, and K. Kato, “Measurement of neg-
ative attitudes toward robots,” Interaction Studies: Social Behaviour
and Communication in Biological and Artificial Systems, vol. 7, no. 3,
pp. 437–454, 2006.
[12] S. A. Jessup, T. Schneider, G. Alarcon, T. Ryan, and A. Capiola,
“The measurement of the propensity to trust automation,” in Virtual,
Augmented and Mixed Reality. Applications and Case Studies. HCII
2019. Lecture Notes in Computer Science, C. J. and F. G., Eds. Cham:
Springer, 2019, vol. 11575.
[13] K. Koay, D. Syrdal, M. Walters, and K. Dautenhahn, “Living with
robots: investigating the habituation effect in participants’ preferences
during a longitudinal human-robot interaction study,” in Proc. of RO-
MAN 2007.
New York: IEEE, 2007, pp. 564–569.
[14] J. E. Young, R. Hawkins, E. Sharlin, and T. Igarashi, “Toward
acceptable domestic robots: applying insights from social psychology,”
vol. 1, no. 1, pp. 95–108, 2009.
[15] C. D. Kidd and C. Breazeal, “Effect of a robot on user perceptions,”
in 2004 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), vol. 4.
IEEE, 2004, pp. 3559–3564.
[16] D. Bohus and E. Horvitz, “Dialog in the open world: platform and
applications,” in Proceedings of the 2009 international conference on
Multimodal interfaces, 2009, pp. 31–38.
[17] P. Marti, A. Pollini, A. Rullo, and T. Shibata, “Engaging with artificial
pets,” in Proc of EACE ’05.
New York: ACM, 2005, pp. 99–106.
[18] F. Tanaka, J. Movellan, B. Fortenberry, and K. Aisaka, “Daily hri
evaluation at a classroom environment: reports from dance interaction
experiments,” in Proc of HRI ’06.
New York: ACM, 2006, pp. 3–9.
[19] J. De Berardinis, G. Pizzuto, F. Lanza, A. Chella, J. Meira, and
A. Cangelosi, “At your service: Coffee beans recommendation from
a robot assistant,” in Proceedings of the 8th International Conference
on Human-Agent Interaction, Virtual Event, NSW, Australia, 2020,
pp. 257––259.
[20] B. Irfan, M. Hellou, and T. Belpaeme, “Coffee with a hint of
data: Towards using data-driven approaches in personalised long term
interactions,” Front. Robot. AI, vol. 8, no. 676814, 2021.
[21] A. Rossi and S. Rossi, “Engaged by a bartender robot: Recommenda-
tion and personalisation in human-robot interaction,” in Proceedings
of the 29th ACM Conference on User Modeling, Adaptation and
Personalization.
New York: ACM, 2021, pp. 115–119.
[22] G. Castellano, R. Aylett, K. Dautenhahn, A. Paiva, P. McOwan, and
S. Ho, “Long-term affect sensitive and socially interactive compan-
ions,” in Proc of the 4th international workshop on human computer
conversation, 2008.
[23] M. Y. Lim, R. Aylett, P. A. Vargas, W. C. Ho, and J. a. Dias, “Human-
like memory retrieval mechanisms for social companions,” in Proc
of The 10th International Conference on Autonomous Agents and
Multiagent Systems - Volume 3, AAMAS ’11.
Taipei, Taiwan: ACM,
2005, pp. 1117–1118.
[24] J. J. Lee, B. Knox, J. Baumann, C. Breazeal, and D. DeSteno,
“Computationally modeling interpersonal trust,” vol. 4, no. 893, 2013.
[25] P. A. Hancock, T. T. Kessler, A. D. Kaplan, J. C. Brill, and J. L.
Szalma, “Evolving trust in robots: Specification through sequential
and comparative meta-analyses,” Human factors, vol. 63, no. 7, pp.
1196–1229, 2021.
[26] J. D. Lee and K. A. See, “Trust in automation: Designing for
appropriate reliance,” Human Factors: The Journal of the Human
Factors and Ergonomics Society, vol. 46, pp. 50–80, 2004.
[27] M. Y. Lim, J. D. A. Lopes, D. A. Robb, B. W. Wilson, M. Moujahid,
and H. Hastie, “Demonstration of a robo-barista for in the wild
interactions,” in 2022 17th ACM/IEEE International Conference on
Human-Robot Interaction (HRI).
IEEE, 2022, pp. 1200–1201.
[28] T. Bunk, D. Varshneya, V. Vlasov, and A. Nichol, “Diet: Lightweight
language
understanding
for
dialogue
systems,”
arXiv
preprint
arXiv:2004.09936, 2020.
[29] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
training of deep bidirectional transformers for language understand-
ing,” in Proceedings of NAACL, Jun. 2019, pp. 4171–4186.
[30] V. Vlasov, J. E. Mosig, and A. Nichol, “Dialogue transformers,” arXiv
preprint arXiv:1910.00486, 2019.
[31] J.-Y. Jian, A. Bisantz, and C. Drury, “Foundations for an empirically
determined scale of trust in automated systems,” International J. of
Cognitive Ergonomics, vol. 4, pp. 53–71, 2000.
[32] C. Imbault, D. Shore, and V. Kuperman, “Reliability of the sliding
scale for collecting affective responses to words,” Behav Res 50, pp.
2399––2407, 2018.
[33] A. Field, Discovering Statistics Using SPSS, 3rd ed.
London: Sage,
2009.
[34] M. A. Walker, D. J. Litman, C. A. Kamm, and A. Abella, “Paradise: a
framework for evaluating spoken dialogue agents,” in Association for
Computational Linguistics, 1997, pp. 271–280.
[35] N. McDonald, S. Schoenebeck, and A. Forte., “Reliability and inter-
rater reliability in qualitative research: Norms and guidelines for cscw
and hci practice,” in Proc. ACM Human Computer Interaction, no. 39,
November 2019.
[36] J. L. Campbell, C. Quincy, J. Osserman, and O. K. Pedersen, “Coding
in-depth semistructured interviews: Problems of unitization and inter-
coder reliability and agreement,” Sociological methods & research,
vol. 42, no. 3, pp. 294–320, 2013.
[37] J. Corbin and A. Strauss, Basics of qualitative research: Techniques
and procedures for developing grounded theory.
Sage, 2008.
[38] M. Y. Lim, J. D. A. Lopes, D. A. Robb, B. W. Wilson, M. Moujahid,
E. De Pellegrin, and H. Hastie, “We are all individuals: The role of
robot personality and human traits in trustworthy interaction,” in 2022
31st IEEE International Conference on Robot and Human Interactive
Communication (RO-MAN).
IEEE, 2022, pp. 538–545.
[39] H. H and E. KS, “Fetch-and-carry with cero: observations from a long-
term user study with a service robot,” in Proc. of RO-MAN ’02.
New
York: IEEE, 2002, pp. 158–163.
[40] L. Takayama, “Putting human-robot interaction research into de-
sign practice,” in 2022 17th ACM/IEEE International Conference on
Human-Robot Interaction (HRI), 2022, pp. 1–1.
[41] A. Langer, R. Feingold-Polak, O. Mueller, P. Kellmeyer, and S. Levy-
Tzedek, “Trust in socially assistive robots: Considerations for use in
rehabilitation,” vol. 104, pp. 231–239, 2019.
[42] I. Leite, C. Martinho, and A. Paiva, “Social robots for long-term
interaction: A survey,” vol. 5, no. 2, pp. 291–308, 2013.
[43] M. Lewis, K. Sycara, and P. Walker, “The role of trust in human-robot
interaction.” Foundations of Trusted Autonomy, 2018.
