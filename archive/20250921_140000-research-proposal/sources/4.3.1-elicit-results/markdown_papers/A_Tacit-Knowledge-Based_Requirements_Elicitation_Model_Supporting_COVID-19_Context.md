

---

Page 1

---

Received December 28, 2021, accepted February 16, 2022, date of publication February 22, 2022, date of current version March 9, 2022.
Digital Object Identifier 10.1109/ACCESS.2022.3153678
A Tacit-Knowledge-Based Requirements
Elicitation Model Supporting COVID-19 Context
HAMNAH ANWAR
1, SAIF UR REHMAN KHAN
1, JAVED IQBAL
1,
AND ADNAN AKHUNZADA2, (Senior Member, IEEE)
1Department of Computer Science, COMSATS University Islamabad (CUI), Islamabad 45550, Pakistan
2Faculty of Computing and Informatics, Universiti Malaysia Sabah, Kota Kinabalu 88400, Malaysia
Corresponding authors: Adnan Akhunzada (adnan.akhunzada@ums.edu.my) and Hamnah Anwar (hamnah.anwar786@yahoo.com)
ABSTRACT Effective software requirements elicitation plays a vital role in the success or failure of a project.
However, ambiguity in the requirement’s statements indicate the presence of a tacit knowledge, which
ultimately act as a root cause of critical complications in later stages of software development as user’s needs
might remain hidden. Additionally, the existence of numerous stakeholders escalates the problem as their
perceptions may contrast mainly due to their experiences and roles in a speciﬁc application domain. Hence,
witlessness of relevant stakeholder(s) and ambiguous requirements cause the compromise for a product
quality. Eventually, it paves the way towards the failure of a project. Furthermore, COVID-19 has affected all
walks of life, more speciﬁcally requirements elicitation process as it heavily depends on human-to-human
interaction. Motivated by this, current study aims at identifying the requirements elicitation techniques and
challenges through a systematic literature review protocol. Furthermore, we have performed an exploratory
study to identify the traditional elicitation techniques that can be used speciﬁcally for eliciting the tacit
requirements. Additionally, we validate the top 15 critical challenges in a normal and pandemic scenario.
To validate the result’s authenticity and legitimacy, appropriate statistical tests have been applied on the
obtained results. Based on the attained results, it is observed that transfer of tacit knowledge remains a
most crucial challenge. To effectively handle the tacit knowledge challenge, we propose a novel conceptual
model supporting COVID-19 context. Similarly, we employ expert-validation mechanism for empirically
evaluation of the proposed conceptual model. Moreover, the current study provides the guidelines for
the practitioners to mitigate the highlighted effects on the requirements elicitation process during current
pandemic time. Finally, we believe that proposed conceptual model supports the practitioners in effectively
gathering the tacit-knowledge based requirements in the COVID-19 context.
INDEX TERMS Requirements elicitation, challenges, tacit knowledge, tacit knowledge techniques, empir-
ical investigation, systematic literature review, conceptual model.
I. INTRODUCTION
From the last few decades, colossal inﬂation of demand for
software systems has caused expeditious growth in software
development. Hence, software development is getting huge
contemplation of researchers, starting from software systems
to embedded systems, AI, and mobile applications, and so
on. Due to the volatile user requirements, the development
of a software system entails many risks. Due to this fact,
Requirements Engineering (RE) is considered as the most
important step of software development lifecycle [1]. Based
The associate editor coordinating the review of this manuscript and
approving it for publication was Derek Abbott
.
on the previously conducted studies, it has been observed that
almost 60% of failures occur due to poor RE. Notice that RE
mainly concerns with the establishment of goals, constraints,
and properties of the system along with the discovery of
users [2].
RE consists of several activities including requirements
elicitation/ gathering, requirements analysis, requirements
speciﬁcation, requirements validation, and management [3].
Requirements’ elicitation is the ﬁrst activity of the RE
stage. In real scenarios, the requirements elicitation process
is a multi-dimensional in nature, i.e. somehow complex,
and iterative activity that profoundly relies on the require-
ment engineer’s communication skills [4], [5]. Moreover,
VOLUME 10, 2022
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
24481


---

Page 2

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
the cooperation and commitment of other stakeholders also
plays a crucial role during RE process. The communication
barrier is highlighted as one of the main problems faced by
software development project teams [6]. The important point
that needs to be communicated clearly to stakeholders might
remain opaque to them. Generally, this situation goes unno-
ticed during the elicitation process, and this may ultimately
fail a project [7]. The establishment of the system’s goals
by capturing the users’ needs is critical as ‘‘the knowledge
is tacit’’ in most cases [8]. The quality and eminence of
requirements are signiﬁcantly prejudiced by the techniques
used while eliciting the requirements. Elicitation is mainly
concerned with mining and learning users’ actual needs and,
after that, communicating them to the developers [9]. The
requirements elicited from the stakeholders are considered
as basis of engineering the system’s architecture and design,
and development plan [8]. The most common issue in require-
ments elicitation phase is that the stakeholders or customers
have a vague idea about the required/desired functionalities.
To handle this issue, it is suggested that the requirements
engineer must elicit the requirements so that that vague infor-
mation could be turned into a formally documented require-
ments speciﬁcation document [10].
Tacit knowledge in communication is often professed as
a major hurdle or obstacle for knowledge transfer, which
could lead to unclear and incomplete requirements elicitation
process [10], [11]. Ultimately, it plays the prominent role in
the success or failure of project. Thus, eliciting the most accu-
rate requirements from the relevant stakeholders, and also
transfer of ‘‘tacit knowledge’’ remains important for success
of a software project [12]–[14]. However, to the best of our
knowledge, current state-of-the-art lacks in categorization of
the challenges, and providing a control process to mitigate
them in context of transfer of ‘‘tacit knowledge’’. Therefore,
there is need to identify and categorize all the challenges that
negatively affect the software elicitation process. Moreover,
a conceptual model in the context of identiﬁcation of relevant
stakeholder and transfer of tacit knowledge is needed.
COVID-19 pandemic has affected all the human activities
and has evoked an era of agility [15]. As elicitation process
mainly depends on the interaction of requirements engineer
and stakeholders. Notice that the stakeholders are not nec-
essarily the human entities but can be the organizational
surroundings or environment where the intended system is
to be utilized [16]. Evidently, existing work lacks in the
identiﬁcation of challenges that are being highlighted dur-
ing the pandemic time. Therefore, there is a need to iden-
tify the challenges during requirements elicitation process
in COVID-19 scenario and to provide a set of guidelines
effective in mitigate the impact of the identiﬁed challenges
Motivated by this, we have performed Systematic Liter-
ature Review (SLR) to identify the challenges that affect
requirements elicitation process. After identiﬁcation, the
challenges have been categorized and prioritized. To reduce
the biasness of the results, quality-oriented review is per-
formed. Keeping in view of quality, the conducted SLR
observes to the principles of transparency, accountability, and
audibility. Following Research Questions (RQs) are designed
to achieve the objective of current research:
RQ1: What are various requirements elicitation techniques
employed by requirements engineers?
RQ1.1: What are speciﬁc techniques used by the require-
ments engineers to elicit the Tacit Knowledge?
RQ2: What are various challenges which affect negatively
on the elicitation process during software development?
RQ2.1: What is categorization and prioritization of various
challenges that affect the elicitation process?
RQ3: What are various challenges that negatively affect by
COVID-19 Pandemic during requirements elicitation?
RQ4: How the effect of identiﬁed challenges dur-
ing requirements elicitation process can be mitigated in
COVID-19 Pandemic context?
The main contributions of this research work are as
follows:
i. Empirically investigates the tacit-based requirements
elicitation techniques.
ii. Provides a categorization and prioritization of chal-
lenges through frequency analysis.
iii. Presents a conceptual model that unfolds the tacit
knowledge during requirements elicitation process.
iv. Validates the proposed conceptual model through
expert-based validation technique.
v. Highlights the challenges related to requirements elic-
itation process during the COVID-19 pandemic, and
also provide the guidelines for the practitioners to mit-
igate the challenges.
The remaining part of this paper is organized as fol-
lows: Section II provides a detailed overview of research
motivation for current research work. Section III describes
the adopted research methodology; section IV presents the
results concerning the formulated research questions, while
section V describes the discussion on the basis of research
objectives. The proposed conceptual model is presented in
section VI. Section VII provides the validation of proposed
conceptual model, while section VIII illustrates the research
implications. Section IX outlines the threats to validity.
Finally, the conclusion is provided in section X.
II. RESEARCH MOTIVATION
Requirements’ elicitation is considered as intricate, intensive,
and multi-disciplinary process. This is due to the reason
that requirements elicitation aims at gathering the user’s
needs and fulﬁll the stakeholder’s objectives [17]. When
the potential stakeholders try to elaborate their requirements
of intended system, they are basically translating their tacit
knowledge into the explicit knowledge [18]. Notice that tacit
knowledge is basically a kind of knowledge required for
better development of a product, which a client has but unable
to articulate/share with the analyst [4].
Tacit requirements are hard to communicate, related to
domain of the system, user’s own knowledge, and may
change during phases of development [19]. Eliciting tacit
24482
VOLUME 10, 2022


---

Page 3

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 1. Tacit vs. Explicit knowledge [20].
knowledge is similar to the process of gathering tacit require-
ments [20].
Figure 1 illustrates that the knowledge is divided into two
categories: (i) tacit knowledge, and (ii) explicit knowledge.
Tacit knowledge is regarded as hard to document, which
personnel use to perform certain tasks and to take verdicts
or decisions [21]. Experts distributed the knowledge of an
individual with the extensively agreed division of 90% tacit
and 10% explicit [20]. This division of knowledge percentage
evidently creates the problem for requirements engineers to
elicit the precise requirements from stakeholders.
The term ‘‘tacit knowledge’’ was introduced by Polanyi
(1966), who identiﬁed the body of knowledge that is gener-
ally challenging to communicate [13]. The presence of tacit
knowledge can be a root cause of complications in the later
stage of software development as user’s needs might remain
hidden. Additionally, the existence of numerous stakehold-
ers escalates the problem as their perceptions, interests and
expectations may contrast due to their experiences and their
role in the speciﬁc application domain [22].
Whenever a stakeholder expresses the element of informa-
tion, ambiguity occurs as the meaning associated with that
element of information may differ from the meaning intended
by the stakeholder. This ambiguity indicates the presence of
tacit knowledge [23].
It has been observed that traditional methods for elicitation
are failed to expose and discover the critical requirements
as these techniques predominantly focus on technical aspects
only [24], [25]. Some of the traditional elicitation techniques
include interviews, questionnaires, scenarios, and prototypes.
The questionnaire-based survey is considered as one of the
effective techniques used by the requirements analysts to
elicit the data during pandemic era where face-to-face inter-
action is not possible [28].
Evidently, to have a quality product, true requirements are
needed and eliciting the necessary requirements remains a
major challenge in RE context. Some of the core challenges
are communication challenges, lack of stakeholders’ interest,
and capturing authentic users’ needs [26], [27]. It has been
found in one of the reported studies conducted by Yaseen
and Ali [18] that right type of collaborative tool for commu-
nication along with the proper cooperation is mandatory to
capture the proper requirements from stakeholders.
Kania et al. [27] mentioned the challenges that greatly
impacts during requirements elicitation process. The reported
challenges are lack of user’s conﬁdence, and lack of trust
between stakeholders and analysts. The trust between humans
is built due to eye contact [29]. Several studies have been
conducted on lack of contact in case of video calls. The
researchers have also suggested some solutions to improve
it [31].
Knifﬁn et al. [30] pointed out accessibility issues to an
appropriate space for ofﬁce purpose at home. Lack of ded-
icated workspaces at home for ofﬁce work negatively affects
the efﬁciency of employees [32], [33]. During COVID-19
pandemic, the interference in concentration of employees has
caused serious challenges and brought problems in sharing
tacit knowledge [34].
Hence, the facts described above have motivated us to work
on this aspect. Keeping in mind the importance of require-
ments elicitation techniques and challenges, more speciﬁ-
cally in the context of identiﬁcation of relevant stakeholder
and transfer of tacit knowledge, we observed that the lit-
erature has seen limited work on tacit-based requirements
context. Moreover, in current pandemic scenario, no literature
has been found that has raised the effect of pandemic restric-
tions on requirements elicitation process. However, it is of
paramount importance to detect and identify the challenges
of requirements elicitation process and to categorize them,
accordingly. This categorization helps requirements engi-
neers and project managers to mitigate the effect of identiﬁed
challenges. However, the conceptual model in context of
identiﬁcation of relevant stakeholder and unfolding of tacit
knowledge helps the industry practitioners in eliciting the
most accurate requirements.
III. RESEARCH METHODOLOGY
SLR protocol is adopted to answer the targeted research
questions, and to achieve the research objectives. Notice
that process of SLR is different from a normal literature
review process. SLR is useful in gathering the data system-
atically in an arranged and unbiased manner [26]. To per-
form SLR in an efﬁcient way, we followed the guidelines of
Kitchenham et al. [26]. This process consists of three main
phases and each phase consists of different sub-phases. All
these sub-phases are discussed in their respective sections.
Figure 2 displays the detailed research methodology adopted
for this research work. Similarly, Figure 3 illustrates three
main phases of the conducted SLR.
The adopted research methodology consists of ﬁve dif-
ferent phases (Figure 2). In problem formulation phase,
we started with the extensive general literature review to
identify the research gap and formulated of problem state-
ment. Current research targets the problem associated with
VOLUME 10, 2022
24483


---

Page 4

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 2. Detailed research methodology.
FIGURE 3. Three main phases of adopted SLR.
the transfer of tacit knowledge in requirements elicitation
phase during COVID-19 Pandemic era. In data collection
phase, we performed a SLR to obtain data in an organized and
systematic manner. To validate the obtained data, an empir-
ical study was performed targeting the practitioners from
industry. In data analysis phase, we applied various appropri-
ate statistical tests to highlight the most critical challenges.
In the proposed model phase, we presented the conceptual
model according to the obtained ﬁndings and goals. Further-
more, the proposed conceptual model is validated through
expert’s opinion in the validation phase. The following sec-
tions present the main phases of SLR.
A. PLANNING THE REVIEW
The ﬁrst phase of the SLR consists of following activities:
i. Generation of research questions.
24484
VOLUME 10, 2022


---

Page 5

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
ii. Selection of most appropriate data source (search)
repositories.
iii. Generation of search string.
iv. Deﬁning appropriate inclusion and exclusion criterion
for paper selection.
v. Setting and applying quality assessment criteria.
The following sections provide comprehensive discussions
about the above-mentioned activities of planning phase of the
conducted SLR:
1) RESEARCH QUESTIONS
To achieve the targeted research objective, we devised the
following Research Questions (RQs):
RQ1: What are various requirements elicitation techniques
employed by requirements engineers?
RQ1.1: What are speciﬁc techniques used by the require-
ments engineers to elicit the Tacit Knowledge?
RQ2: What are various challenges which affect negatively
on the elicitation process during software development?
RQ2.1: What is categorization and prioritization of various
challenges that affect the elicitation process?
RQ3: What are various challenges that negatively affect by
COVID-19 Pandemic during requirements elicitation?
RQ4: How the effect of identiﬁed challenges dur-
ing requirements elicitation process can be mitigated in
COVID-19 Pandemic context?
2) DATABASE SELECTION
To ﬁnd the relevant studies published in well reputed
peer-reviewed journals, conferences, we selected multiple
database preferences recommended by Arif et al. [37].
We ﬁnalized the total 4 out of 5 databases, as it has been
observed that almost all of the potential studies were retrieved
from Wiley, IEEE Xplore, SpringerLink, and Science Direct.
However, to verify the comprehensiveness of the identiﬁed
primary studies, we cross checked them through Google
Scholar. Hence, the selected databases are Wiley, IEEE
Xplore, SpringerLink and Science Direct.
3) SEARCH STRING
Search string is designed keeping in view of the targeted
research objective and devised RQs. The search string com-
prises of the selected keywords that are being used in the
current research. The keywords and their synonyms were
selected on the basis of already available studies in the context
of current research [26]. The search terms were divided into
ﬁve categories (i) Requirements Elicitation (ii) Challenges
(iii) Techniques (iv) Model or framework and (v) Software
Development. Moreover, the search strings were further cus-
tomized according to the targeted databases due to the differ-
ent searching mechanisms, strategies and restrictions of the
databases. Table 1 highlights the tailored search strings for
each of the selected databases.
4) INCLUSION CRITERIA
A review protocol is incorporated in current research work
for a deﬁnite strategy to search and determine the studies.
TABLE 1. Tailored search string.
Benchmark has applied to the data which is extracted from the
search repositories through designed query [40]. Following
are the inclusion criteria that are implemented in this study.
• IC1: The potential research articles must be written in
English.
• IC2: The research articles should be published in Jour-
nal/conference papers.
• IC3: Research articles consisting of Requirements Elic-
itation Issues or challenges.
• IC4: Research articles consisting of Requirements Elic-
itation Techniques.
• IC5: Research articles should cover the targeted research
objectives.
• IC6: Research articles that have followed appropriate
standard research methodology.
• IC7: Research articles that are not identical of any other
article.
• IC8: Research articles that published after 2016 to date.
5) EXCLUSION CRITERIA
The elimination benchmark has been applied to the studies
that are to be extracted from the database repositories as a
result of query [42]. Papers were included from 2016 to 2021,
and the rest were excluded.
VOLUME 10, 2022
24485


---

Page 6

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
• EC1: Research articles that are written in languages
other than English.
• EC2: Research articles that are published before 2016.
• EC3: Research articles that have irrelevant titles and
abstracts.
• EC4: Research articles containing irrelevant information
in context with research questions.
• EC5: Research articles whose methodology is not
clearly deﬁned.
• EC6: Research articles having unclear data collection
methodology.
• EC7: Research articles possessing ambiguous data vali-
dation methodology.
6) QUALITY ASSESSMENT FOR SELECTED STUDIES
Quality assessment is a compulsory measure of an SLR.
As stated earlier, we have devised a search string for each
database repository to target the potential primary studies
(Table 1). To guarantee the SLR’s overall quality, we have
targeted well known and reliable database repositories, only.
Moreover, the selection criteria itself is a quality measure
consisting of a checklist.
For assessing the overall quality of targeted studies, a qual-
ity assessment checklist was generated. Quality Assessment
Criteria (QAC) allows determining the most relevant articles
inside the idyllic scrutiny space.
The following questions were generated to evaluate the
quality of the selected studies:
QC-1: Does the objectives of the proposed research study
discussed?
QC-2: Is the research methodology used in selected article
clearly deﬁned?
QC-3: Does the study explicitly focus on Requirements
Elicitation Issues?
QC-4: Do the results of the proposed study match the
targeted research objectives and research questions?
QC-5: Does the appropriate methods are used to combine
the studies?
Following are the assessment criteria for the checklist
questions:
i. ‘‘1’’ point for the articles that address the appropriate
answer.
ii. ‘‘0.5’’ points for the articles that address the fractional
answer.
iii. ‘‘0’’ points for articles not addressing the desired
checklist questions.
APPENDIX B illustrates the quality assessment of each
selected primary study.
B. CONDUCTING THE REVIEW
In phase 2 of conducted SLR, we performed the review by
applying the search string query to relevant databases to
ﬁnd the primary studies. The generic process of conducting
the review process is illustrated in Figure 4. To extract the
primary studies, standard approaches were being used. After
the extraction phase, studies were synthesized according to
FIGURE 4. Generic process of the conducted review.
FIGURE 5. Tollgate-based primary study selection process.
TABLE 2. Main phases of paper’s selection process.
the quality criteria. The following sections provide the details
about these activities:
1) PRIMARY STUDY SELECTION
In this section, we gathered numerous research articles from
targeted database repositories through the tailored search
string and passed them through proper analysis process to
ﬁlter out the most relevant papers.
To reﬁne the process of primary study selection, a tollgate
approach was being used that is proposed by Afzal et al. [25].
The employed Tollgate approach comprises of ﬁve different
phases, described in Table 2.
In the ﬁrst phase, a total of 7,883 articles were extracted
from selected databases grounded on the search terms and
keywords. In the second phase, 4,805 articles were selected
on the basis of title and abstract criteria. In the third phase,
2,741 articles were selected based on the introduction and
conclusion sections. In the fourth phase, skimming and
scanning of articles was performed and 299 articles were
24486
VOLUME 10, 2022


---

Page 7

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 3. The details of primary study selection process.
FIGURE 6. Temporal distribution of the selected studies.
ﬁnalized. Finally, in the ﬁfth phase, after applying the
skimming and scanning on full text and removal of dupli-
cate studies, 42 primary studies were ﬁnalized. Figure 5
illustrates the phases of primary study selection process.
Moreover, Table 3 provides the details of primary study
Selection.
2) DATA EXTRACTION
The articles selected (for primary study) were based on the
parameters such as publication year, research methodology
used, author name, and the limitations that are associated with
them. The list of articles selected as primary studies is shown
APPENDIX A. Moreover, to ensure the relevancy of primary
studies, the formulated research questions were cross mapped
with the selected articles.
3) DATA SYNTHESIS
In data synthesis phase, the research articles were being
passed through the phases of tollgate approach for the pur-
pose of synthesizing the data. Moreover, the data gathered
from primary studies were evaluated with the research ques-
tions generated for the research. From total of 42 articles,
40
challenges
and
18
requirements
elicitation
were
identiﬁed.
C. REPORTING THE REVIEW
In third phase of SLR, the primary studies are evaluated
with respect to the quality questions, devised to assess and
maintain the quality of primary studies. This section provides
the details of the temporal distribution of studies to identify
the research trends. The following sections provide the details
of these activities:
FIGURE 7. Expert’s responses.
1) QUALITY ATTRIBUTES
To assess the quality, all the selected primary studies
were reviewed and assessed (mentioned in APPENDIX B).
APPENDIX B consists of quality scores of primary studies
with respect to the generated quality criteria questions. The
average score of each paper is greater than 50% (i.e. 2.5).
Hence, this score depicts that the selected articles have sat-
isﬁed the quality criteria and possesses more relevancy with
the current research work.
2) TEMPORAL DISTRIBUTION OF SELECTED STUDIES
It has been observed that there is signiﬁcant decrease in the
number of publications after year 2019. The rapidly changing
trends and new advancements in the industry demand more
attention towards the quality product. Undoubtedly, quality-
oriented requirements elicitation process provides a base
essential for the success of a software project.
However, the 54.8% (24 out of 42) selected primary stud-
ies were published in well reputed journals, whereas 45.2%
(18 out of 42) were published in conference proceedings.
Figure 6 illustrates the temporal distribution of the selected
primary studies.
IV. RESULTS
This section provides the results and analysis for each of
the formulated research questions. Moreover, for evalua-
tion of the obtained results, empirical assessments are also
performed.
RQ1 (What Are Various Requirements Elicitation Tech-
niques Employed by Requirements Engineers?): Require-
ments are being collected or elicited through the consultation
of end users and stakeholders. However, for different stake-
holders, single method is not enough to demonstrate the infor-
mation about the problem. Moreover, it is almost impossible
to use particular and generic method to elicit the require-
ments due to the changes in situational context during the
elicitation process [15]. To explain the types of techniques,
a total of 29 (out of 42) articles were targeting 18 different
requirements elicitation techniques. Table 4 elaborates dif-
ferent requirements elicitation techniques along with their
references, frequency, and percentage.
To analyze the signiﬁcance of requirements elicitation
techniques, the criteria of frequency having greater than
50% are categorized as important techniques, as followed by
VOLUME 10, 2022
24487


---

Page 8

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 4. Requirements elicitation techniques.
one of the similar studies [4]. Hence, according to above-
mentioned criteria, the important elicitation techniques are
Interviews [ET-1], Questionnaire [ET-2], Prototyping [ET-4],
and Requirements reuse [ET-5], Scenarios [ET-6], Brain-
storming [ET-7], Ethnography [ET-10], and Observation
[ET-11], Similar System [ET-12], Think Aloud [ET-13] and
Active Observation [ET-15].
RQ1.1 (What Are Speciﬁc Techniques Used by the Require-
ments Engineers to Elicit the Tacit Knowledge?): The transfer
of tacit knowledge is considered as the major issue during
eliciting the requirements. The requirements analysts used
different techniques to detect and uncover the tacit knowl-
edge [16]. We performed an empirical study to identify the
existing techniques that might be helpful in uncovering the
hidden tacit knowledge. Figure 7 illustrates the obtained
responses. As depicted by the expert’s responses (Figure 7),
all of the respondents agreed that Prototyping, Scenarios, and
Brainstorming could be used to elicit the tacit requirements.
However, according to the experts, ethnography and Think
Aloud are also being used. Moreover, 50% of the respon-
dents mentioned that ‘‘Storytelling’’ and ‘‘Storyboarding’’
techniques are also useful to uncover the tacit knowledge. The
demographics of experts are shown in Figure 20.
RQ2
(What
Are
Various
Challenges
Which
Affect
Negatively on the Elicitation Process During Software
Development?):
Eliciting the requirements from stakeholders is an early yet
highly precarious stage in RE phase. This stage is more likely
to be affected by the occurrence of error as it comprises of
different important challenges that need to be handled [10].
The identiﬁcation of relevant end users or stakeholders and
ascertaining their actual needs are the basis of success and
failure of requirements elicitation process. Due to the poor
communication between stakeholder and analyst, there are
more chances of occurrence of error which may result in
the utilization of extra resources such as time and cost [24].
There are many other challenges as well which affect the
requirements elicitation process. Hence, to ﬁnd out the
Requirements elicitation challenges, a total of 31 (out of 42)
articles were targeting 40 different requirements elicitation
challenges. APPENDIX C elaborates different requirements
elicitation challenges along with their references, frequency,
and percentage.
To analyze the signiﬁcance of elicitation challenges,
we used the criteria based on their frequency as followed by
one of the similar studies [4].
24488
VOLUME 10, 2022


---

Page 9

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 5. The significance of challenges.
TABLE 6. The expert’s demographics.
The challenges having frequency percentage greater than
50% are considered as high signiﬁcant challenges. That
in this case are Poor Communication [C1], identiﬁcation
of relevant stakeholder [C8], ambiguities among stakehold-
ers [C9], Unawareness of need [C10], Vague information /
implicit knowledge [C14], Experts experience & technical
know-how [C19], Insufﬁcient levels of detail of requirements
(vague requirements) [C28], Communication Issues [C31],
Knowledge is tacit [C33], and Knowledge exchange capa-
bility [C37]. Table 5 illustrates the high, medium, and low
signiﬁcance of challenges.
RQ2.1 (What Is Categorization and Prioritization of Var-
ious Challenges That Affect the Elicitation Process?): For
the categorization and prioritization of identiﬁed challenges,
we used expert judgment method. We approached two
Project Managers and three Requirements Engineers possess-
ing strong industrial and academic background. We catego-
rized and prioritized the challenges on the basis of mutually
agreed mapping from each targeted practitioner. To gather
and analyze the feedback, we conducted total 5 meetings each
consisting of approximately 1 hour. Table 6 represents the
information demographics of targeted expert.
A. CATEGORIZATION OF CHALLENGES
All the challenges identiﬁed from literature are cat-
egorized
into
four
main
categories:
(i)
Communica-
tion, (ii) Organizational, (iii) Analyst, (i) Technical and
Stakeholder (COATS). For this categorization, we selected
the descriptive categories from Zowghi et al. [38] and mapped
the associated challenges. Figure 8 (APPENDIX F) illus-
trates the categorization of all the identiﬁed challenges.
B. PRIORITIZATION OF CHALLENGES
To prioritize the signiﬁcance of elicitation challenges,
we used the criteria based on their frequency as followed
by the study [4]. Challenges having frequency percentage
greater than 50% are considered as high signiﬁcant chal-
lenges. In this case, Poor Communication [C1], identiﬁcation
of relevant stakeholder [C8], ambiguities among stakehold-
ers [C9], Unawareness of need [C10], Vague information /
implicit knowledge [C14], Experts experience & technical
know-how [C19], Insufﬁcient levels of detail of requirements
(vague requirements) [C28], Communication Issues [C31],
Knowledge is tacit [C33], and Knowledge exchange capabil-
ity [C37]. Challenges having frequency percentage between
25% and 50% are considered as medium signiﬁcant chal-
lenges. However, challenges having frequency percentage
less than 25% are considered as low signiﬁcant challenges.
After removing the most likely duplication, identiﬁed chal-
lenges having high and medium signiﬁcance are prioritized
among 5 main categories. Table 7 illustrates the prioritization
of challenges.
1) EMPIRICAL EVALUATION OF CHALLENGES
This section speciﬁes the details concerning the design and
implementation of performed survey analysis through indus-
try practitioners. Furthermore, it includes the investigation
against the prioritized requirements elicitation challenges.
After that a contrast has been drawn among the challenges
from literature and industry.
C. SURVEY DESIGN
To procure the industrial perspective against the top 15 critical
challenges identiﬁed from literature, a survey questionnaire
was premeditated and developed.
Requirements Engineers, Project Managers and Develop-
ers were being targeted as primary respondents. Moreover,
to achieve the legitimacy and validity of results, all the
respondents were targeted who belong to multinational orga-
nizations from all over the globe. To analyze the criticality
of challenges, a 5-Point Likert scale (Strongly agree, Agree,
Neutral, Disagree, Strongly disagree) was sed. Figure 9 pro-
vides the demographics of respondents from the survey. After
obtaining the responses from the targeted audience were
converted into the percentages, and appropriate data analysis
tests were performed.
D. DATA ANALYSIS
For analysis of data, we performed Levene’s test, T-test, and
Spearman Correlation test to validate the result’s authenticity
and legitimacy [44].
VOLUME 10, 2022
24489


---

Page 10

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 7. Prioritization of challenges.
TABLE 8. The results of levene’s test.
1) LEVENE’S TEST
To ensure the consistency of variance between the out-
come of empirical study and SLR, we applied Levene’s test.
Table 8 presents the resultant values of percentages and vari-
ance of data.
2) T-TEST
To analyze the mean differences between Empirical Study
and SLR, we applied t-test. The outcome of t-test was t =
−1.51 and p = 0.04, which clearly indicates that there
is no prominent difference between the outcome of SLR
and the performed empirical study. Top 15 challenges hav-
ing critical and moderate signiﬁcance are being compared.
Table 11 describes the comparison of challenges from indus-
try and literature.
3) SPERSMAN TEST
To evaluate the importance of differences between the ranks
collected from SLR and Empirical Study, we applied spear-
man correlation test.
24490
VOLUME 10, 2022


---

Page 11

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 8. Categorization of challenges.
Notice that in Spearman correlation test, if the value of
coefﬁcient is near or close to +1.0, then it represents the
positive correlation. Notice that if the value of coefﬁcient
is closer to −1.0, then it represents the negative correla-
tion. In the conducted study, the Spearman coefﬁcient was
0.21523651, which clearly indicates the strong positive cor-
relation between the rankings that are obtained from SLR and
Empirical Study results. Table 9 represents the percentage
and ranks of data obtained from SLR and Empirical Study.
RQ3 (What Are Various Challenges That Negatively Affect
by COVID-19 Pandemic During Requirements Elicitation?):
COVID-19 pandemic has affected all of the daily routine
activities and evoked an era of agility [14]. In the conducted
survey, we asked the practitioners whether the requirements
elicitation process in in-house software development is neg-
atively affected due to COVID-19 pandemic or not. 72% of
the practitioners agreed with the statement that this pandemic
era has affected the process of requirements elicitation as it
requires more human to human interaction. Figure 10 illus-
trates the division of percentage of respondents from the
conducted empirical study.
Figure 11 portrays the comparison of impact of critical
challenges before and during COVID-19 pandemic.
Moreover, we calculated the percentage of impact on
each challenge by subtracting the before COVID-19 per-
centage from the percentage obtained during COVID-19.
Table 10 illustrates the percentages and overall impact of
before and during pandemic situation.
Moreover, there are some additional challenges that are
being faced by the practitioners during the COVID-19 pan-
demic situation. It is to be noticed that these challenges are
not deﬁned or highlighted in the literature. The identiﬁed
challenges include team size, response delay, work pressure,
multiple venders’ involvement, and communication infras-
tructure.
E. IC01- TEAM SIZE
Group size is an important challenge when working remotely.
Smaller groups can complete the task more efﬁciently and
effectively as they need to communicate more frequently.
F. IC02- RESPONSE DELAY
Due to the restrictions in pandemic scenario, all work relied
on online collaborative tools. Analysts and stakeholders
communicate through online conferencing tools. Hence, the
delay in response from analyst or stakeholder results in the
VOLUME 10, 2022
24491


---

Page 12

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 9. Demographics of respondents.
TABLE 9. The results of SLR and empirical study.
formation of ambiguities as all the analysts or stakeholders
are collaborating from different surroundings.
FIGURE 10. Division of respondents.
G. IC03- WORK PRESSURE
In the pandemic scenario, the work pressure has increased due
to rapid increase in demand of collaborative software systems
as each activity is shifted to online. The exponential increase
in demand resulted in the increase of work pressure and hence
the analysts lack in having enough time to properly gather the
requirements from stakeholders. Moreover, the stakeholders
need the systems to be built as soon as possible so that less
time might get wasted.
H. IC04- MULTIPLE VENDORS INVOLVEMENT
Involving the multiple vendors during the pandemic times is
challenging, as it needs much time to ﬁnd, manage and com-
municate with them. It is a matter of fact that communication
is badly affected in pandemic scenario and involving mul-
tiple vendors in a project means communicating with more
channels. More communication channels may result in the
poor requirements elicitation process. Furthermore, multiple
vendors might have multiple perspectives, and dealing with
24492
VOLUME 10, 2022


---

Page 13

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 10. Impact of before and during pandemic situation.
FIGURE 11. Comparison of before and during Pandemic.
many perspectives where communication is not up to the
mark might result in the failure of project.
I. IC05- COMMUNICATION INFRASTRUCTURE
It is a matter of fact that communication is badly affected
due to the restrictions in COVID-19 scenario. The commu-
nication channels used by the analysts and stakeholders are
mostly the collaborative tools. The analysts know the usage
of these channels but the stakeholders being the lay persons in
industry do not know how to efﬁciently use these tools unless
FIGURE 12. Five additional challenges.
they are being properly trained for them. This lack of training
might create the communication gap between the analyst and
stakeholder.
Figure 12 illustrates the ﬁve additional challenges being
identiﬁed through Empirical Study.
RQ4 (How the Effect of Identiﬁed Challenges Dur-
ing Requirements Elicitation Process Can be Mitigated in
COVID-19 Pandemic Context?): Elicitation process needs to
be error prone so that the requirements gathered by analyst
are accurate enough to meet the stakeholder’s goal [16]. The
analysts need to identify the relevant stakeholder. Identiﬁca-
tion of relevant stakeholder is very crucial as they will be
the primary source of information and they possess the actual
needs and goals of system to be built [18]. After that, the ana-
lysts need to capture and document the goals and objectives
of stakeholders at an early stage. The analyst needs to be a
good listener and keen observer. The analyst’s assumption
might work as a poison to the system, so analysts need to
conﬁrm the requirements from stakeholders by providing the
prototypes [20].
Requirements Elicitation process is human-centered pro-
cess, so it exclusively depends on the communication
between the analyst and stakeholder. However, in pandemic
scenario, the face-to-face communication has been affected
badly [29]. Therefore, in the conducted empirical study,
we asked the practitioners to provide the guidelines they are
followed to mitigate this effect.
Following are some of the practices/guidelines provided by
the practitioners:
i. Select and create right communication channel such as
MS Teams, Skype.
ii. Perform appropriate inspection time to time while elim-
inating the hurdles.
iii. Target each module of system to be built as a goal and
deﬁne clear timelines.
VOLUME 10, 2022
24493


---

Page 14

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
iv. Involve the stakeholders more frequent than usual to
avoid miscommunication.
v. Quick Prototyping could be used to provide the visuals
among stakeholders and analysts to avoid ambiguity.
vi. Make sure the clariﬁcation in communication at both
stakeholders and analysts ends.
vii. Avoid involving too many resources in the process of
communication.
viii. The communication with stakeholders should be ﬂuent
and fast.
ix. Agile workﬂow management tools such as Asana
Notion and Monday could be used to manage the tasks.
x. Team collaboration amongst cross departmental teams
should be enhanced in order to ensure that the require-
ments are elicited through proper process.
xi. Each step of development should be properly docu-
mented and tracked.
xii. Professional training should be provided to the team to
work online.
xiii. Develop strategies/processes to counter challenges
faced during working.
xiv. Soft skills of both stakeholders and analysts must be
enhanced and training should be provided by company.
V. DISCUSSIONS
The aim of current research work is to identify requirements
elicitation techniques and challenges. Moreover, to identify
the communication issues faced during COVID-19 pandemic.
For this purpose, we performed a SLR to identify the chal-
lenges and to support, we performed an empirical study. The
practitioners were asked the questions to verify the facts that
were found from the literature. In this section, the ﬁndings of
formulated research questions are discussed.
Regarding RQ1, we have identiﬁed different techniques
to be used for elicitation process with the help of SLR.
We have found a total of 42 articles from which 29 targeting
18 different requirements elicitation techniques. After per-
forming the frequency analysis, we analyzed the signiﬁcance
of elicitation techniques. The important elicitation techniques
are Interviews - Open and closed, Questionnaire that is eas-
ily manageable and may target large number of audiences.
Prototyping, easily understandable as it is a visual mockup of
the product that is intended to be built. Moreover, it could be
used to remove the ambiguities among the analysts and stake-
holders. Other important techniques are requirement reuse,
brainstorming, ethnography, observation, similar system and
active observation.
Regarding RQ1. 1, we performed an empirical study to
identify the speciﬁc techniques that could be used to elicit the
tacit requirements. We targeted 12 experts from industry for
this purpose. All of the respondents agreed that Prototyping,
Scenarios, and Brainstorming could be used to elicit the tacit
requirements. 91% of respondents voted for Observation.
However, according to experts, ethnography and Think Aloud
are also being used. Moreover, 50% of the respondents said
that ‘‘Storytelling’’ and ‘‘Storyboarding’’ techniques are also
useful to uncover the tacit knowledge
Regarding RQ2, we performed the SLR to identify the
challenges. A total of 42 articles from which 31 were target-
ing 40 different requirements elicitation challenges.
To analyze the signiﬁcance of elicitation challenges,
we used the criteria based on their frequency as followed
by one of the similar studies [4]. The challenges having
frequency percentage greater than 50% are considered as
high signiﬁcant challenges. That in this case are Poor Com-
munication [F1], identiﬁcation of relevant stakeholder [F8],
ambiguities among stakeholders [F9], Unawareness of need
[F10], Vague information / implicit knowledge [F14], Experts
experience & technical know-how [F19], Insufﬁcient lev-
els of detail of requirements (vague requirements) [F28],
Communication Issues [F31], Knowledge is tacit [F33], and
Knowledge exchange capability [F37]. The division made
it easy to differentiate the challenges and helped us in the
prioritization.
Regarding RQ2.1, we have categorized the challenges into
ﬁve main categories Communication, Organizational, Ana-
lyst, Technical and Stakeholder (COATS). After removing the
most likely duplication, identiﬁed challenges having high and
medium signiﬁcance are prioritized.
Regarding the RQ3, we have identiﬁed that software elici-
tation process is affected negatively due to pandemic restric-
tions. 72% of the practitioners agreed with the statement that
this pandemic era has affected the process of requirements
elicitation as it requires more human to human interaction.
Moreover, we have identiﬁed ﬁve additional challenges that
inﬂuenced the requirements elicitation process during pan-
demic time. The identiﬁed challenges are team size, response
delay, work pressure, multiple venders’ involvement, and
communication infrastructure.
Regarding RQ4, we asked the industrial practitioners to
provide the practices/guidelines they followed to mitigate the
effect of challenges that are highlighted during Pandemic
time.
The suggested practices allow the practitioners to further
investigate and propose the appropriate strategies to help the
practitioners in pandemic era.
VI. PROPOSED CONCEPTUAL MODEL
Based on the outcome of conducted empirical study and
performed SLR, we propose a conceptual model to gather
the unambiguous requirements in the form of veriﬁed tacit
knowledge. To accomplish this, ﬁrst of all, we gathered the
challenges that affect the requirements elicitation process.
With the consultation of industrial practitioners, we catego-
rized and prioritized the requirements elicitation challenges.
The prioritized challenges were then analyzed by the practi-
tioners in the context of normal and pandemic scenario. After
that the practitioners were asked to provide the guidelines
to overcome the effect of challenges during the COVID-19
pandemic scene.
24494
VOLUME 10, 2022


---

Page 15

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 13. High-level view of proposed conceptual model.
In phase 2, we identify the relevant stakeholder(s) from
whom the analysts will communicate to gather the informa-
tion regarding the system to be built. Phase 3 consists of
the steps to unfold the ambiguous statement(s), considering
transfer of tacit knowledge in communication as the most
highlighted challenge. Similarly, in phase 4 of the proposed
model, the obtained tacit/unfolded statements were veriﬁed
using the predicates Accessible, Intelligible, Expressible, Rel-
evant, and Interpretable. Figure 13 illustrates the main phases
of proposed conceptual model.
A. PHASE 2: IDENTIFICATION OF RELEVANT
STAKEHOLDER
In phase 2 of proposed conceptual model, different activities
are performed to identify the relevant stakeholders. In the
beginning, we have a pool consisting of both active and
passive stakeholders. The output of phase 2 is to identify
the active stakeholders and neglect the passive stakeholders
(i.e., their roles are not important for requirements elicita-
tion of a certain system). The ﬁrst and foremost step is to
call a general meeting and involve the pool of all possible
stakeholders. Next, state them the goal or aim of project that
needs to be achieved, provide them a set of role identiﬁcation
criterion [35], [36]. After that we asked them to individu-
ally brainstorm and note down the roles of stakeholders that
might be important to achieve the certain goal. Figure 19
(APPENDIX E) depicts the sample template of role identi-
ﬁcation’s questionnaire.
Afterwards, we make the pairs of stakeholders randomly
and allow them to again brainstorm and discuss roles in pairs.
The role identiﬁcation questionnaire [35], [36] is provided
and asked them to rank the selected roles individually accord-
ing to the provided criterion with justiﬁcation. After pair
brainstorming, group brainstorming is performed. Each pair
is asked to discuss or present their results along with the
provided rankings. At the end, the roles having high ranking
are considered as the active stakeholders that may help to
achieve the certain goal.
Figure 20 (APPENDIX E) presents the sample guideline
questions. Moreover, Figure 14 describes the process of iden-
tiﬁcation relevant stakeholder.
B. PHASE 3: UNFOLDING TACIT KNOWLEDGE
Phase 3 is regarded as the main phase of proposed conceptual
model. When using expert judgment as a knowledge repos-
itory to gather the requirements, the ambiguous statements
from expert stakeholders are to be analyzed. Whenever a
stakeholder expresses the element of information, ambigu-
ity occurs as the meaning associated with that element of
information may differ from the meaning intended by the
stakeholder. This ambiguity indicates the presence of tacit
knowledge [23].
VOLUME 10, 2022
24495


---

Page 16

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 14. PHASE 2 - identification of relevant stakeholder.
For example, Ferrari et al. [43] stated following example of
ambiguity. ‘‘One of our customers is a bio-medical engineer
and wants to develop a system that patients can use to mea-
sure their blood pressure. The system shall include a mobile
application, which sends the data about the blood pressure to
the general practice doctor. When asked how blood pressure
is currently measured, the customer said: There is this device.
Customer uses the device on regular basis but didn’t know
its name, speciﬁcations, and details. The analyst correctly
understood that a speciﬁc device is used. Since, from the
implementation point of view, the analyst thought that a
precise name, or brand, for the device was needed, to develop
an interface between the mobile phone and the device. After
asking, it was clariﬁed that the bio-medical engineer did not
know the name of the device (i.e., blood pressure monitor).’’
To further elaborate the term ‘‘Ambiguity’’, another exam-
ple speciﬁed in study [43] is as follows:
‘‘One of our customers wants to develop a mobile appli-
cation that monitors the use that she makes of her mobile
phone. She said: Maybe the system could give me also some
recommendations. The analyst thought that the term recom-
mendations could have two acceptable meanings: (a) nega-
tive recommendations on applications and mobile features
that she should not use (b) positive recommendations on
applications that could be downloaded and mobile features
that 59 could be used. After clariﬁcation, the ﬁrst meaning
resulted correct.’’
So, considering the ambiguous statement(s) as an input, the
ﬁrst step is to generate the associated goal with that statement
and conﬁrm that goal from the stakeholder. Second step is
to brainstorm and raise the relevant question/s or query/s to
the identiﬁed stakeholders. Afterwards, gather all the per-
spectives from the stakeholders. Each stakeholder might have
multiple perspectives regarding a single query.
After getting the perspectives, evaluate the pros and cons of
each perspective respectively and ask the consequence ques-
tions if need. The analyst could argue against the perspective
and stakeholder could defend the argument using examples.
This process of argumentation and exempliﬁcation is known
as internalization. The analyst(s) could use the techniques
TABLE 11. Criteria and corresponding query.
such as ‘‘Prototyping’’ [45], [46], and ‘‘Storyboarding’’ [47]
to afﬁrm the perspectives when needed. The process contin-
ues until the analysts get the positives and negatives of each
perspective. Keeping in mind the pros and cons, the perspec-
tives is prioritized accordingly. Moreover, the perspectives
having high priority are then compared to the associated goal.
Notice that the perspective possessing most relevancies with
the associated goal is considered as the unfolded statement
or unfolded tacit knowledge from initial ambiguous state-
ment. Figure 15 shows the process of the unfolding tacit
knowledge.
C. PHASE 4: VERIFICATION OF TACIT KNOWLEDGE USING
PREDICATES
The quality of unfolded tacit statement(s) obtained from the
output of phase 3 is veriﬁed in this phase using the ﬁve
predicates [16], [18]. Hence, the sentence would be:
Tacit Knowledge (S) = Accessible ∧Intelligible ∧Inter-
pretable ∧Expressible ∧Relevant
After applying the quality criteria of ‘‘ﬁve’’ predicates,
the quality of unfolded tacit statements is being analyzed
by creating the quality review matrix. Assign scores to the
sentence(s) out of 1 with respect to each predicate. Hence,
the total score of each sentence depicts the attained quality.
However, the process of veriﬁcation of statements is shown
in Figure 16.
24496
VOLUME 10, 2022


---

Page 17

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 12. Primary study references along with their Journal/conference and publication year.
VOLUME 10, 2022
24497


---

Page 18

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 12. (Continued.) Primary study references along with their Journal/conference and publication year.
VII. VALIDATION OF PROPOSED CONCEPRUAL MODEL
This section focuses on validation of the proposed conceptual
model. To validate the proposed model, we adopted two
different approaches: (i) Expert’s judgment/opinion, which
includes initial internal expert’s opinion from academia, and
(ii) Expert’s validation from industry. Initially, the industrial
practitioners reviewed the proposed conceptual model. Con-
sidering the feedback of experts, improvements were being
made. Each subsequent section contains the detailed discus-
sion on the process of validation of proposed model.
24498
VOLUME 10, 2022


---

Page 19

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 12. (Continued.) Primary study references along with their Journal/conference and publication year.
FIGURE 15. PHASE 3 – unfolding the tacit knowledge.
A. INITIAL INTERNAL VALIDATION
Prior getting the expert’s opinion from the industrial prac-
titioners, we performed the initial validation. First version
of the proposed conceptual model was initially evaluated
by the academic experts, Dr. Saif-Ur-Rehman Khan, and
Dr. Javed Iqbal. The considered experts have vast experience
of industry as well as academia and currently employed at
COMSATS University Islamabad (CUI) as Assistant Pro-
fessors. The internal validation of model is carried out by
considering parameters such as readability, logical connectiv-
ity of components and technical aspects. Moreover, novelty
of proposed model was the main target while evaluation.
After the initial internal validation, for further enhancements,
we followed the expert’s validation process. The embraced
process of Expert Validation is described in Figure 17.
FIGURE 16. Verification of the tacit statements.
B. EXPERT VALIDATION
To get the external feedback on proposed conceptual model,
the expert validation method was employed as shown in
Figure 17. First, inclusion criterions were deﬁned to select the
most appropriate practitioners/expert. The selected experts
were requested to review and evaluate the proposed model
according to the provided checklist. The criterion for select-
ing appropriate expert is as follows:
i. The expert must be employed in a Large or Medium
sized organization.
ii. The role of expert in organization must be Project
Manager or Requirements Engineer or both.
iii. The expert must have experience of at least ﬁve years
or more.
We targeted total 12 experts that meet the deﬁned inclusion
criteria. We designed a checklist questionnaire on Google
forms to get the responses. Traits such as design, readability,
VOLUME 10, 2022
24499


---

Page 20

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 13. Quality Assessment of primary studies.
and relevancy of components, logical ﬂow, understandabil-
ity, correctness, practicality, and completeness were cov-
ered. Table 11 provides the criteria and its corresponding
query.
Fortunately, we got positive responses from all the experts,
which clearly depicts that the model we proposed has novelty
and it has potential to positively contribute to the industry.
The general visual demonstrations of expert’s responses are
illustrated in APPENDIX D. In contrast, Figure 18 presents
the expert’s demographics.
VIII. RESERACH IMPLICATIONS
The challenges identiﬁed in current research can be used to
develop and deploy a model that can mitigate their impact
on the process of requirements elicitation. The basic and
eventual goal is to propose the model that mitigates the effect
24500
VOLUME 10, 2022


---

Page 21

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 14. Identified requirements elicitation challenges along with their reference and frequency.
VOLUME 10, 2022
24501


---

Page 22

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 14. (Continued.) Identified requirements elicitation challenges along with their reference and frequency.
FIGURE 17. Expert’s validation process.
of identiﬁcation of relevant stakeholder and the presence of
tacit knowledge in Poor Communication as the transfer of
tacit knowledge in Requirements Elicitation has been the big
issue. Another future direction is to develop a software tool
for the proposed tacit knowledge based conceptual model
which could help the practitioners to effectively elicit the tacit
knowledge-based requirements.
FIGURE 18. The expert’s demographics.
Moreover, this research highlighted the requirements elici-
tation related challenges critical and problematic in pandemic
era in software development. Thus, it seems a great opportu-
nity to develop such strategies or models that may help the
practitioners in pandemic scenarios.
The other possible future research direction is to further
analyze and validate the unfolded tacit statement by analyzing
linguistically the fragments of sentences obtained as the out-
put of phase 3 of proposed conceptual model. For example,
the basic components of any sentence are the subject, the
verb, and (often, but not always) the object. Hence, the valida-
tion could be performed on the tacit statements on the basis of
their structure and presence of these mandatory components.
IX. THREATS TO VALIDITY
The possible validity threat related to current work is that
almost all the authors of primary studies are from academia
24502
VOLUME 10, 2022


---

Page 23

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 15. Visual demonstration of expert’s responses for validation of proposed model.
VOLUME 10, 2022
24503


---

Page 24

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
TABLE 15. (Continued.) Visual demonstration of expert’s responses for validation of proposed model.
24504
VOLUME 10, 2022


---

Page 25

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 19. Sample template of role identification questionnaire.
possessing lack of practical or industrial knowledge. This
might bring hollow gap between the perspective of academia
and software industry. To mitigate this threat, we evaluated
the critical challenges through practitioners from industry.
By doing this, we presented both the academic and industrial
perspectives.
There might be another possible internal threat, that the
acknowledged primary studies have not mentioned the pos-
sible reasons behind the mentioned challenges. Basically,
the literature lacks in the identiﬁcation of origin of these
challenges in requirements elicitation process. We tried to
mitigate its effect by evaluating the challenges from practi-
tioners having real-world experience in industry.
Another validity threat to the current research is that
the selected studies have not targeted both traditional and
in-house development in one context. The requirements’
elicitation challenges are gathered from all the software
development approaches. This threat is mitigated by validat-
ing the critical challenges from the practitioners of software
industry.
The other potential threat is related to the extraction and
evaluation of high number of potential studies. However,
to effectively mitigate this threat, we followed the guidelines
suggested by Kitchenham et al. [26].
Moreover, we analyzed the impact signiﬁcance of
requirements elicitation challenges in context of COVID-19
pandemic scenario. The other possible threat might be that
different people have different perspective towards devel-
opment in the pandemic era. To mitigate its effect, we tar-
geted the global audience essential in acquiring the multiple
perspectives.
X. CONCLUSION
Software requirements’ elicitation is a knowledge-intensive
process of knowing or acquiring the stakeholder’s needs and
goals. The success of requirements elicitation process heavily
grounded on the collaboration, coordination, and most impor-
tantly communication among the analyst and stakeholders.
However, based on the literature review, we realized that little
attention had been paid to the process of transfer of tacit
knowledge in COVID-19 context. Inspired by this, we have
performed a systematic literature review to extensively gather
the requirements elicitation techniques and the challenges
that negatively impacts on the requirements elicitation pro-
cess. After collecting the data from the selected primary
studies, we solicited the industry practitioners to identify
the requirements elicitation techniques employed to elicit the
tacit knowledge explicitly. After that, we categorized and pri-
oritized the challenges by eliminating the possible duplicates
and performed frequency analysis.
To empirically evaluate top 15 identiﬁed challenges from
the literature, we have performed a questionnaire-based sur-
vey. In total, 145 global respondents have participated in the
performed empirical study. Notice that the majority of the
respondents are working in large and medium sized multi-
national organizations as a project manager, requirements
analysts and software developers. Moreover, we have val-
idated the impact of the categorized top 15 challenges in
pandemic scenario context. Finally, we have identiﬁed ﬁve
additional challenges through the performed empirical study.
The major classes of the identiﬁed challenges are team size,
response delay, work pressure, multiple venders’ involve-
ment, and communication infrastructure.
Considering the identiﬁcation of stakeholders and transfer
of tacit knowledge during communication as most challeng-
ing issues, we proposed a conceptual model. The proposed
conceptual model identiﬁes the relevant stakeholder and then
unfolds the tacit knowledge present in the form of ambiguous
statement(s) during elicitation of requirements. To validate
the proposed model, we have performed expert validation
through a survey. Moreover, a set of mitigation guidelines
for the practitioners have been provided, which are useful
VOLUME 10, 2022
24505


---

Page 26

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
FIGURE 20. Sample guideline questions.
in mitigating the highlighted effects on requirements elici-
tation process during the pandemic time. Finally, based on
the attained signiﬁcant results, we believed that proposed
conceptual model supports the practitioners in effectively
eliciting and gathering the tacit-knowledge based require-
ments in the COVID-19 context.
APPENDIX A DEMOGRAPHICS OF THE SELECTED
PRIMARY STUDIES
See Table 12.
APPENDIX B QUALITY ASSESSMENT SCORE ATTAINED
BY PRIMARY STUDIES
See Table 13.
APPENDIX C THE REQUIREMENTS ELICITATION
CHALLENGES
See Table 14.
APPENDIX D MODEL VALIDATION RESPONSES
See Table 15.
APPENDIX E PHASE 2 of Proposed Conceptual Model
See Figures 19 and 20.
APPENDIX F CATEGORIZATION OF CHALLENGES
See Figure 8.
ACKNOWLEDGMENT
This work is related to the Master’s research by Hamnah
Anwar supported by COMSATS University Islamabad (CUI)
Islamabad, Pakistan. The authors are grateful to the members
of Software Reliability Engineering Group (SREG) at CUI
for their continuous support and feedback throughout this
research work. Moreover, they appreciate the project man-
agers and the experts who participated in the survey and
provided their valuable responses.
REFERENCES
[1] G. M. Muketha, L. R. Cherotich, and F. Wabwoba, ‘‘Factors affecting
requirements elicitation for heterogeneous users of information systems,’’
Int. J. Comput. Sci. Eng. Technol. (IJCSET), vol. 5, no. 3, pp. 35–39, 2015.
[2] I. Sommerville, Software Engineering, 9th ed. Boston, MA, USA:
Addison-Wesley, 2010.
[3] L. Wong and D. Mauricio, ‘‘New factors that affect the activities of the
requirements elicitation process,’’ J. Eng. Sci. Technol., vol. 13, no. 7,
pp. 1992–2015, 2018.
[4] H. Dar, M. I. Lali, H. Ashraf, M. Ramzan, T. Amjad, and B. Shahzad,
‘‘A systematic study on software requirements elicitation techniques and
its challenges in mobile application development,’’ IEEE Access, vol. 6,
pp. 63859–63867, 2018.
[5] D. Apšvalka, D. Donina, and M. Kirikova, ‘‘Understanding the problems
of requirements elicitation: A human perspective,’’ in Information Sys-
tems Development: Challenges in Practice, Theory and Education, vol. 1.
Berlin, Germany: Springer, 2009, pp. 211–224.
[6] S. Virendra, D. Pandey, and S. Sankhwar, ‘‘Problems associated with
requirement elicitation process: An overview,’’ Int. J. Adv. Res. Comput.
Sci., vol. 8, no. 5, pp. 2637–2639, 2017.
[7] H. Ferreira Martins, A. Carvalho de Oliveira Junior, E. Dias Canedo,
R. A. Dias Kosloski, R. Ávila Paldês, and E. Costa Oliveira, ‘‘Design
thinking: Challenges for software requirements elicitation,’’ Information,
vol. 10, no. 12, p. 371, Nov. 2019.
24506
VOLUME 10, 2022


---

Page 27

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
[8] C. P. Noraini and A. M. Zin, ‘‘Managing communications challenges in
requirement elicitation,’’ in Software Engineering and Computer Systems
(Communications in Computer and Information Science), vol. 181. 2011,
pp. 803–811.
[9] A. Sutcliffe and P. Sawyer, ‘‘Requirements elicitation: Towards the
unknown unknowns,’’ in Proc. 21st IEEE Int. Requirements Eng. Conf.
(RE), Jul. 2013, pp. 92–104.
[10] J. Coughlan, M. Lycett, and R. D. Macredie, ‘‘Communication issues in
requirements elicitation: A content analysis of stakeholder experiences,’’
Inf. Softw. Technol., vol. 45, no. 8, pp. 525–537, Jun. 2003.
[11] G. Nikita, P. Wora, and S. Kumaresh, ‘‘Managing requirement elicitation
issues using step-wise reﬁnement model,’’ Int. J. Adv. Stud. Comput., Sci.
Eng., vol. 2, no. 5, pp. 27–33, 2013.
[12] S. Asghar and M. Umar, ‘‘Requirement engineering challenges in devel-
opment of software applications and selection of customer-off-the-shelf
(COTS) components,’’ Int. J. Softw. Eng., vol. 1, no. 1, pp. 32–50, 2010.
[13] P. Prasarnphanich, B. D. Janz, and J. Patel, ‘‘Towards a better understand-
ing of system analysts’ tacit knowledge: A mixed method approach,’’ Inf.
Technol. People, vol. 29, no. 1, pp. 69–98, 2016.
[14] A. Ferrari, P. Spoletini, and S. Gnesi, ‘‘Ambiguity and tacit knowledge
in requirements elicitation interviews,’’ Requirements Eng., vol. 21, no. 3,
pp. 333–355, Sep. 2016.
[15] S. Tiwari, S. S. Rathore, and A. Gupta, ‘‘Selecting requirement elicitation
techniques for software projects,’’ in Proc. CSI 6th Int. Conf. Softw. Eng.
(CONSEG), Sep. 2012, pp. 1–10.
[16] Z. Zhang, ‘‘Effective requirements development—A comparison of
requirements elicitation techniques,’’ in Software Quality Management XV:
Software Quality in the Knowledge Society, E. Berki, J. Nummenmaa,
I. Sunley, M. Ross, and G. Staples, Eds. British Computer Society, 2007,
pp. 225–240.
[17] A. Wahbeh, S. Sarnikar, and O. El-Gayar, ‘‘A socio-technical-based pro-
cess for questionnaire development in requirements elicitation via inter-
views,’’ Requirements Eng., vol. 25, no. 3, pp. 295–315, Sep. 2020.
[18] Z. Yaseen, M. Z. Ali, Z. Halabi, A. Karrar, F. Babtain, and M. Aslam,
‘‘Success factors during requirements implementation in global software
development: A systematic literature review,’’ Int. J. Comput. Sci. Softw.
Eng., vol. 8, no. 3, pp. 56–68, 2019.
[19] N. Basir and R. A. Salam, ‘‘Tacit requirements elicitation framework,’’
ARPN J. Eng. Appl. Sci., vol. 10, no. 2, pp. 572–578, 2015.
[20] R. Wikström, ‘‘Fuzzy ontology for knowledge mobilisation and decision
support,’’ Ph.D. dissertation, Dept. Inf. Technol., Åbo Akademi Univ.,
Turku, Finland, 2014.
[21] A. Nour and C. S. Pineda, ‘‘Managing requirements elicitation knowledge
using a spatial hypertext Wiki,’’ in Knowledge Engineering for Software
Development Life Cycles: Support Technologies and Applications. 2011,
pp. 68–83.
[22] K. Olmos-Sánchez, U. Autónoma de Ciudad Juárez, J. Rodas Osollo,
L. Fernández Martínez, V. Morales Rocha, U. Autónoma de Ciudad Juárez,
U. Autónoma de Ciudad Juárez, and U. Autónoma de Ciudad Juárez,
‘‘Requirements engineering based on knowledge: A comparative case
study of the KMoS-RE strategy and the DMS process,’’ Revista Facultad
de Ingeniería Universidad de Antioquia, vol. 77, pp. 88–94, Dec. 2015.
[23] A. Ferrari, P. Spoletini, and S. Gnesi, ‘‘Ambiguity as a resource to disclose
tacit knowledge,’’ in Proc. IEEE 23rd Int. Requirements Eng. Conf. (RE),
Aug. 2015, pp. 26–35.
[24] U. Sajjad and M. Hanif, ‘‘Issues and challenges of requirement elicitation
in large web projects,’’ Ph.D. dissertation, School Comput., Blekinge Inst.
Technol., Karlskrona, Sweden, 2010.
[25] W. Afzal, R. Torkar, and R. Feldt, ‘‘A systematic review of search-based
testing for non-functional system properties,’’ Inf. Softw. Technol., vol. 51,
no. 6, pp. 957–976, 2009.
[26] B. Kitchenham, O. P. Brereton, D. Budgen, M. Turner, J. Bailey, and
S. Linkman, ‘‘Systematic literature reviews in software engineering–A
systematic literature review,’’ Inf. Softw. Technol., vol. 51, no. 1, pp. 7–15,
2009.
[27] M. K. Sabariah, P. I. Santosa, and R. Ferdiana, ‘‘Requirement elicitation
framework for child learning application–A research plan,’’ in Proc. 2nd
Int. Conf. Softw. Eng. Inf. Manage. (ICSIM), 2019, pp. 129–133.
[28] J.-P. Wan, D.-Y. Huang, and D. Wan, ‘‘Knowledge conversion in software
requirement elicitation,’’ in Proc. 1st Int. Conf. Inf. Sci. Eng., Dec. 2009,
pp. 2328–2331.
[29] F. Uebernickel and J. Hehn, ‘‘Towards an understanding of the role of
design thinking for requirements elicitation-ﬁndings from a multiple-case
study,’’ in Proc. Amer. Conf. Inf. Syst. (AMCIS), 2018, pp. 1–10.
[30] K. M. Knifﬁn, J. Narayanan, F. Anseel, J. Antonakis, S. P. Ashford,
A. B. Bakker, P. Bamberger, H. Bapuji, D. P. Bhave, V. K. Choi,
S. J. Creary, E. Demerouti, F. J. Flynn, M. J. Gelfand, L. L. Greer,
G. Johns, S. Kesebir, P. G. Klein, S. Y. Lee, and M. V. Vugt, ‘‘COVID-19
and the workplace: Implications, issues, and insights for future research
and action,’’ Amer. Psychologist, vol. 76, no. 1, pp. 63–77, 2021.
[31] L. S. Bohannon, A. M. Herbert, J. B. Pelz, and E. M. Rantanen, ‘‘Eye
contact and video-mediated communication: A review,’’ Displays, vol. 34,
no. 2, pp. 177–185, Apr. 2013.
[32] A. Jaklič, F. Solina, and L. Šajn, ‘‘User interface for a better eye contact in
videoconferencing,’’ Displays, vol. 46, pp. 25–36, Jan. 2017.
[33] B. Wang, Y. Liu, and S. K. Parker, ‘‘Achieving effective remote working
during the COVID-19 pandemic: A work design perspective,’’ Appl. Psy-
chol., vol. 70, no. 1, pp. 16–59, 2021.
[34] O. Király, M. N. Potenza, D. J. Stein, and D. L. King, ‘‘Preventing problem-
atic internet use during the COVID-19 pandemic: Consensus guidance,’’
Comprehensive Psychiatry, vol. 100, Jul. 2020, Art. no. 152180.
[35] Job
Analysis
Questionnaire
by
Kansas
State
University.
Accessed: May 24, 2021. [Online]. Available: https://www.k-state.edu/
hcs/docs/Job-Analysis-Questionnaire.pdf
[36] Job Analysis Questionnaire by Tennessee Technological University.
Accessed: Apr. 5, 2021. [Online]. Available: https://www.tntech.edu/
hr/pdf/JAQ.pdf
[37] F. Hayat, A. U. Rehman, K. S. Arif, K. Wahab, and M. Abbas, ‘‘The
inﬂuence of agile methodology (Scrum) on software project management,’’
in Proc. 20th IEEE/ACIS Int. Conf. Softw. Eng., Artif. Intell., Netw. Paral-
lel/Distributed Comput. (SNPD), Jul. 2019, pp. 145–149.
[38] D. Zowghi and C. Coulin, ‘‘Requirements elicitation: A survey of tech-
niques, approaches, and tools,’’ in Engineering and Managing Software
Requirements, A. Aurum and C. Wohlin, Eds. Berlin, Germany: Springer,
2005.
[39] W. Alsaqaf, M. Daneva, and R. Wieringa, ‘‘Quality requirements chal-
lenges in the context of large-scale distributed agile: An empirical study,’’
Inf. Softw. Technol., vol. 110, pp. 39–55, Jun. 2019.
[40] V. Gervasi, R. Gacitua, M. Rounceﬁeld, P. Sawyer, L. Kof, L. Ma, P. Piwek,
A. D. Roeck, A. Willis, H. Yang, and B. Nuseibeh, ‘‘Unpacking tacit
knowledge for requirements engineering,’’ in Managing Requirements
Knowledge. Berlin, Germany: Springer, 2013, pp. 23–47.
[41] K. Kenz, P. Soffer, and I. Hadar, ‘‘The role of domain knowledge in
requirements elicitation via interviews: An exploratory study,’’ Require-
ments Eng., vol. 19, pp. 143–159, Sep. 2014.
[42] B. Kitchenham, ‘‘Procedures for performing systematic reviews,’’ Keele
Univ., Keele, U.K., Tech. Rep. 33-2004, 2004, pp. 1–26.
[43] A. Ferrari, P. Spoletini, and S. Gnesi, ‘‘Ambiguity cues in requirements
elicitation interviews,’’ in Proc. IEEE 24th Int. Requirements Eng. Conf.
(RE), Sep. 2016, pp. 56–65.
[44] C.-H. Chang, N. Pal, and J.-J. Lin, ‘‘A revisit to test the equality of vari-
ances of several populations,’’ Commun. Statist.-Simul. Comput., vol. 46,
no. 8, pp. 6360–6384, Sep. 2017.
[45] S. Rueda, J. I. Panach, and D. Distante, ‘‘Requirements elicitation methods
based on interviews in comparison: A family of experiments,’’ Inf. Softw.
Technol., vol. 126, Oct. 2020, Art. no. 106361.
[46] T. Spijkmanb, B. Wintera, S. Bansidhara, and S. Brinkkempera, ‘‘Concept
extraction in requirements elicitation sessions: Prototype and experimenta-
tion,’’ in Proc. CEUR Workshop. Utrecht, The Netherlands: Utrecht Univ.,
Department of Information and Computing Sciences, 2021.
[47] S. Ayob and M. F. Omidire, ‘‘Storyboards as a qualitative method
of exploring learners’ experience with the use of a multilingual
support strategy,’’ Int. J. Qualitative Methods, vol. 20, Aug. 2021,
Art. no. 16094069211034391.
HAMNAH ANWAR received the B.S. degree in
software engineering from COMSATS University
Islamabad, in 2017, where she is currently pursu-
ing the master’s degree. She has two years of expe-
rience in project management and successfully
completed many software projects. Her research
interests include software project management,
software requirements engineering, and software
process improvement.
VOLUME 10, 2022
24507


---

Page 28

---

H. Anwar et al.: Tacit-Knowledge-Based Requirements Elicitation Model Supporting COVID-19 Context
SAIF UR REHMAN KHAN received the bache-
lor’s degree in computer science and the master’s
degree in software and system engineering from
Mohammad Ali Jinnah University (MAJU), Islam-
abad, Pakistan, in 2005 and 2007, respectively, and
the Ph.D. degree in software engineering from the
University of Malaya, Kuala Lumpur, Malaysia,
in 2018. He has been a Faculty Member with the
Computer Science Department, COMSATS Uni-
versity Islamabad (CUI), Islamabad, since 2005.
He has more than 20 years of teaching, development, and research experi-
ence. He has published numerous research articles in high-impact journals
and peer-reviewed conferences. He has been in several expert review panels,
both locally and internationally. His research interests in software engi-
neering include veriﬁcation and validation, search-based software engineer-
ing, cyber-physical systems, requirements engineering, and software project
management. He was a recipient of the Best Paper Presentation Award from
the University of Malaya, in 2014, and a Certiﬁcate of Outstanding Con-
tribution in Reviewing from Future Generation Computer Systems journal,
in 2018.
JAVED IQBAL received the Ph.D. degree in com-
puter science from the University of Malaya,
Kuala Lumpur, Malaysia, in 2016. He is cur-
rently an Assistant Professor with the Department
of Computer Science, COMSATS University
Islamabad, Pakistan. He has more than 19 years
of experience in research and development.
His research interests include software process
improvement, requirements engineering, software
development outsourcing, and machine learning.
ADNAN AKHUNZADA (Senior Member, IEEE)
is currently serving as an Associate Professor
with the Faculty of Computing and Informatics,
Universiti Malaysia Sabah, Malaysia. His expe-
rience as an educator and a researcher is diverse
that includes an Assistant Professor at COMSATS
University Islamabad (CUI); a Senior Researcher
at RISE SICs Vasteras AB, Sweden; a Research
Fellow and a Scientiﬁc Lead at DTU Compute,
The Technical University of Denmark (DTU); the
Course Director of Ethical Hacking at The Knowledge Hub Universities
(TKH), Coventry University, U.K.; a visiting professor having mentorship
of graduate students; and a supervision of academic and research and devel-
opment projects both at UG and PG levels. He has also been involved in
international accreditation, such as Accreditation Board for Engineering
and Technology (ABET), and curriculum development according to the
guidelines of ACM/IEEE. He is a principal investigator of national and a
co-principal investigator of several Swedish and Horizon 2020 EU funded
projects. He has a proven track record of high impact published research
and commercial products. His research interests include cyber security,
secure future internet, artiﬁcial intelligence, such as machine learning, deep
learning, and reinforcement learning, large scale distributed systems, such
as edge, fog, cloud, and SDNs, the IoT, industry 4.0, and the Internet of
Everything (IoE). He is a member of technical program committee of varied
reputable conferences, journals, and editorial boards. He is also a Profes-
sional Member of ACM with extensive 13 years of research and development
(R&D) experience both in ICT industry and academia.
24508
VOLUME 10, 2022
