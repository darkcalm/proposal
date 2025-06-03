

---

Page 1

---

Human-AI Collaboration in Decision-Making: Beyond Learning to Defer
Diogo Leit˜ao 1 2 3 Pedro Saleiro 1 M´ario A. T. Figueiredo 2 3 Pedro Bizarro 1
Abstract
Human-AI collaboration (HAIC) in decision-
making aims to create synergistic teaming be-
tween human decision-makers and AI systems.
Learning to defer (L2D) has been presented as a
promising framework to determine who among
humans and AI should make which decisions in
order to optimize the performance and fairness of
the combined system. Nevertheless, L2D entails
several often unfeasible requirements, such as the
availability of predictions from humans for every
instance or ground-truth labels that are indepen-
dent from said humans. Furthermore, neither L2D
nor alternative approaches tackle fundamental is-
sues of deploying HAIC systems in real-world
settings, such as capacity management or dealing
with dynamic environments. In this paper, we
aim to identify and review these and other limita-
tions, pointing to where opportunities for future
research in HAIC may lie.
1. Introduction
With the advent of machine learning (ML), artiﬁcial intelli-
gence (AI) is now fast, scalable, and, in several applications,
very accurate. As a result, AI is increasingly present in
decision-making processes previously conducted solely by
humans, such as in healthcare (Esteva et al., 2017), or in
criminal justice (Kirchner & Larson, 2017). The AI may
take on a pure advisory role, providing the human decision-
maker with a prediction, a score, or explanations. However,
in several applications, the volume of cases is so large that it
is impractical or even economically unfeasible to solely rely
on human decision-making. This is the case in fraud detec-
tion (Youseﬁet al., 2019), and credit scoring (Burrell, 2016).
Because AI models are able to process large volumes of
information, they offer superior operational efﬁciency and
statistical precision to that of humans, who are known to
1Feedzai 2Instituto Superior T´ecnico, Universidade de Lisboa
3Instituto de Telecomunicac¸˜oes. Correspondence to: Diogo Leit˜ao
<diogo.leitao@feedzai.com>.
Presented at the ICML 2022 Workshop on Human-Machine Col-
laboration and Teaming. Copyright 2022 by the authors.
struggle in this regard (Meehl, 1954). With that said, hu-
mans are capable of swiftly learning from few data points,
and can leverage information that the AI cannot grasp, either
because it cannot be converted to symbolic representation,
or because it originates from accrued experience. As such,
often the ideal system consists neither of AI alone, nor of
humans alone, but rather of a collaboration between the two.
A key challenge in human-AI collaboration (HAIC) is to
determine who makes which decisions. An ideal HAIC sys-
tem is capable of identifying the strengths and weaknesses
of humans and AI in order to optimally assign instances
to decision-makers. This encompasses modelling not only
predictive performance, but also fairness. ML models are
known to be capable of producing biased decisions against
protected groups (Angwin et al., 2016; Buolamwini & Ge-
bru, 2018). Humans, too, can be prejudiced, especially when
information correlated with protected attributes is available
to them. HAIC systems have the opportunity to reduce un-
fairness by optimizing assignments to mitigate group-wise
disparities.
The current state-of-the-art approach for performance- and
fairness-aware assignments in HAIC is learning to defer
(L2D) (Madras et al., 2018; Mozannar & Sontag, 2020;
Keswani et al., 2021). L2D frames the assignment problem
as a classiﬁcation task, providing a supervised method to
ﬁnd the best decision-maker for each given instance. Never-
theless, L2D exhibits structural limitations: it requires pre-
dictions from every human decision-maker for every in-
stance in the training set, and trades off robustness for spe-
cialization. Additionally, capacity management in teams
of humans is disregarded: L2D aims to ﬁnd the optimal
assignment given an individual instance, instead of aiming
to ﬁnd the optimal set of assignments for a set of instances
given a team of humans with limited capacity.
Settings where decisions inﬂuence outcomes are also usually
not considered. A particularly ubiquitous problem is selec-
tive labels (Lakkaraju et al., 2017). For instance, in criminal
justice, rearrest can only take place if bail is ﬁrst granted; in
credit scoring, failing to repay a loan can only happen if a
loan is granted. Lastly, a key issue still unaddressed in the
literature is dealing with dynamic environments, which
may entail addressing concept drift (Gama et al., 2014) and
feedback loops (Dalvi et al., 2004; Perdomo et al., 2020).
arXiv:2206.13202v2  [cs.LG]  13 Jul 2022


---

Page 2

---

Human-AI Collaborative Decision-Making: Beyond Learning to Defer
To avoid performance degradation, HAIC systems must
account for non-stationary factors, or at least be updated
with new data. However, L2D offers no solution to learn
from partial, non-random data, and neither do alternative
contributions.
In short, HAIC systems have the opportunity to optimize
performance and fairness beyond that of individual contrib-
utors. Although L2D provides a valid framework to this
end, it entails several structural limitations that inhibit its
adoption in real-world use-cases and disregards other key
challenges. The goal of this paper is to clearly deﬁne these
challenges and limitations, while shedding light on possible
avenues of future research to bring us closer to performant,
fair, and practical human-AI collaboration.
2. Learning to Defer
The simplest approach to manage assignments in HAIC is
to defer based on model conﬁdence. This approach is drawn
from learning with a reject option, a framework ﬁrst studied
by Chow (1970), where the goal is to optimize the perfor-
mance of the non-rejected predictions by rejecting to predict
in cases of high uncertainty. The baseline for uncertainty
estimation is to take the predicted probability score(s) as a
measure of conﬁdence (Hendrycks & Gimpel, 2016), while
more sophisticated techniques range from ensemble meth-
ods (Gal & Ghahramani, 2016; Lakshminarayanan et al.,
2017) to auxiliary models (Corbi`ere et al., 2019). In HAIC
systems, these uncertainty estimation techniques can be
leveraged to defer low model conﬁdence cases to humans.
Madras et al. (2018) introduced learning to defer (L2D)
as an improvement upon conﬁdence-based deferral in the
context of HAIC systems with a single human expert. The
authors argue that conﬁdence-based deferral is suboptimal,
as it fails to consider the downstream human decision-maker.
In some instances of high model uncertainty, they may be
just as inaccurate as the model; as such, it may be preferable
to defer to them other lower uncertainty instances where
they are able to outperform the model. To model these dif-
ferences, Madras et al. (2018) expand upon the framework
of learning with a reject option. In particular, they adapt the
work of Cortes et al. (2016), who incorporated the reject
option into the learning algorithm, allowing the classiﬁer
to reject to predict, incurring instead in a constant, label-
independent cost. To account for the performance of the
human decision-maker, L2D adds a variable cost of deferral
to this setup:
Lsystem( ˆYM, ˆYH, s) =
X
i
[(1 −si)LCE(Yi, ˆYM,i)
+ siL0-1(Yi, ˆYH,i) + siγdefer]
The system loss depends on the choice to defer (s = 1) or
not to defer (s = 0) to the human decision-maker H. If the
human decision-maker is chosen, the system loss is the 0-1
loss between ground-truth label Y and human prediction
ˆYH, plus a constant penalty term γdefer. Conversely, if the
decision is not deferred, the system loss corresponds to the
cross-entropy loss of model M’s prediction ˆYM.
Madras et al. (2018) propose a learning scheme consist-
ing of two separate neural networks that are jointly trained
to minimize the system loss. The main model focuses on
the classiﬁcation task at hand; the deferral model decides
whether to assign the decision to the model or to the human
decision-maker. During training, the output of the deferral
model is taken as a Bernoulli probability, with both net-
works backpropagating on the expected value of the system
loss. Consequently, the deferral model learns to choose the
decision-maker with best expected performance, and the
main classiﬁer is allowed to specialize on the cases that are
not deferred, disregarding the rest.
An additional concern of Madras et al. (2018) is that both
the human decision-maker and the ML model may be biased
against certain protected groups. To allow the L2D system
to mitigate these biases, the authors propose a regularized
loss with an additional penalty term for error-rate disparities
between protected groups. We will further develop on the
topic of fairness in HAIC in Section 3.6.
Others authors have since joined the effort of expanding and
improving learning to defer. Mozannar & Sontag (2020)
generalize L2D to multi-class settings and introduce a con-
sistent surrogate loss to be used in a single classiﬁer capable
of deferral. Verma & Nalisnick (2022) elaborate upon their
work, proposing a loss calibrated for human correctness.
Keswani et al. (2021) expand L2D to model multiple human
decision-makers. Lastly, some authors propose different
methodologies (Wilder et al., 2020; Gao et al., 2021), or
different end-goals (Bansal et al., 2021). In the next section,
we will shed light on the limitations of L2D, as well as
unaddressed challenges by this and alternative frameworks.
3. Challenges and Limitations
To help illustrate the shortcomings of L2D, we will take
the domain of online merchant fraud detection as a running
example. In this use-case, ML models and human fraud
analysts work in tandem to identify and stop fraud in streams
of thousands of daily purchases. As such, the AI is used
to process the majority of purchases, while humans, due
to limited capacity, only intervene on a small fraction (e.g.
5%) of the most difﬁcult instances.
3.1. Learning from data without human predictions
Learning to defer entails a fundamental, structural limita-
tion: it requires predictions from human decision-makers


---

Page 3

---

Human-AI Collaborative Decision-Making: Beyond Learning to Defer
for every training instance. This implies an additional effort
that goes much beyond what is strictly necessary in regular
operations. One cannot expect a team of fraud analysts hired
to intervene only on the most difﬁcult cases to be able to
review all the instances necessary to train an ML model.
Mozannar & Sontag (2020) consider this problem, and sug-
gest an imputation scheme where the behavior of the human
decision-makers is modelled from the complete data and
replicated on the incomplete data. However, that method
fails when the complete and incomplete data are not identi-
cally distributed, as the basis for generalization falters. This
will be the case whenever the collected data stems from a
non-random assignment system. In real-world use-cases,
this is to be expected, as aforementioned techniques such as
deferring low-conﬁdence instances to the human decision-
makers already bring substantial performance gains. In
fraud detection, analysts do not review random cases; they
review cases where the ML model is less conﬁdent.
As such, L2D cannot be implemented as an improvement to
an existing deferral system. In fact, if a L2D system needs
to be updated to keep up with changing trends in the data,
the framework cannot be reused to perform this update, as
non-deferred instances will lack a human prediction, and
will be distributed differently from deferred instances. We
will revisit this point in Section 3.7, elaborating on why
model updating will, in fact, be necessary in most settings.
Future research should focus on being able to learn from
data with and without human predictions, as that is its natu-
ral state in HAIC settings. An interesting approach would be
to resort to reinforcement learning techniques, where partial
and biased information is the norm. Choices of decision-
maker could be framed as actions, with the environment
being the features and any other relevant information.
3.2. Joint learning: losing robustness and advisory
One of the proposed beneﬁts of L2D is that, by jointly train-
ing the main classiﬁer with the deferral model, the former is
allowed to specialize on non-deferred instances, in detriment
of those that are deferred (Madras et al., 2018; Mozannar
& Sontag, 2020). However, by design, specialization ren-
ders the main classiﬁer useless in the instances likely to
be deferred, as gradients are stopped from backpropagat-
ing into it. As such, learning to defer is unsuitable in do-
mains where the AI advises the human decision-makers.
In such use-cases, the ML model may provide the human
decision-maker with a tentative prediction, a score, or a set
of explanations, that they will then combine with their own
accrued experience and analysis of the instance at hand. In
fraud detection, the ML model score is one of the pieces of
information considered by analysts when making a predic-
tion (Jesus et al., 2021). This would not be possible if the
classiﬁer specialized away from the deferred instances.
Furthermore, specialization makes the system brittle: by
trading off generalization for specialization, the AI is not
robust to post-deployment changes on human capacity for
review. If fraud analysts become temporarily unavailable,
the AI will not be capable of deciding on a fraction of
instances, seriously harming performance.
A promising avenue of research could be to develop an
alternative approach to L2D that follows a sequential learn-
ing setup instead of joint learning. This option is brieﬂy
considered by Madras et al. (2018), when the authors sug-
gest stopping system error from backpropagating to the
main classiﬁer; however, results of this alternative setup
are not shown, and it has not been considered in posterior
contributions. A HAIC assignment system trained sequen-
tially would solely focus on ﬁnding the best assignment
policy given the pre-trained classiﬁer and the set of human
decision-makers. This approach would not only avoid the
aforementioned drawbacks of altering the main classiﬁer,
but also eliminate the need for human predictions for every
instance, which, as mentioned in Section 3.1, is often an
unfeasible demand.
3.3. Deferral to multiple decision-makers
Madras et al. (2018) introduce learning to defer in the con-
text of deferral to a single human decision-maker. How-
ever, in several applications, teams may be composed of
several people, and they may have different biases and types
of expertise. For example, fraud analysts may be specialized
in speciﬁc fraud patterns.
Keswani et al. (2021) propose a L2D method that accounts
for the diversity of human decision-makers, modelling each
available expert individually. However, to this end, they re-
quire not only human predictions for every instance — as in
single-human L2D — but also predictions from every con-
sidered decision-maker. This data will rarely be available
in real-world use-cases, as it is inefﬁcient for individuals
in teams of human experts to review each other’s decisions.
If every fraud analyst in a team with n elements starts re-
viewing every deferred instance, the capacity for reviews
decreases by a factor of n, harming the system’s perfor-
mance. Keswani et al. (2021) posit that missing predictions
may be imputed; however, the robustness of that method is
not discussed. If the data reﬂects non-random assignments,
then generalization may not be possible.
Future work should focus on modelling several decision-
makers without requiring concurrent predictions, as those
will rarely be available without additional effort. As men-
tioned in Section 3.1, this could be accomplished with rein-
forcement learning techniques, where partial information is
the norm.


---

Page 4

---

Human-AI Collaborative Decision-Making: Beyond Learning to Defer
3.4. Capacity management
Learning to defer frames deferral as a classiﬁcation task:
given a speciﬁc instance, the goal is to ﬁnd which decision-
maker is expected to be the most accurate and less biased.
However, in the presence of capacity constraints, the best
decision-maker may not be the optimal choice. For example,
if a fraud analyst is universally better than the rest of the
team, then, ideally, they would decide on only the hardest
cases where others are most likely to err.
Current L2D methods would simply assign them to every in-
stance, disregarding capacity constraints. While this may be
acceptable in use-cases where the hiring process is fully ﬂex-
ible, such as with Amazon Mechanical Turk, in human-AI
teams with stricter arrangements, such extreme assignments
are unfeasible. As a result, for an optimal deferral solution,
capacity must be managed explicitly. We believe this to be
a blind spot and an opportunity for future research.
3.5. Selective labels
Human-AI decision-making teams often operate in envi-
ronments where actions can inﬂuence outcomes. In fraud
detection, a purchase may only be found to be fraudulent if
it is not declined. Lakkaraju et al. (2017) refer to this as the
selective labels problem. L2D is incapable of dealing with
selective labels, as it requires ground-truth labels to evaluate
human decision-makers on.
Gao et al. (2021) propose an alternative method anchored
not on predictions and ground-truth labels, but rather actions
and rewards. For instance, in fraud detection, the reward of
past declined purchases is always zero, regardless of the (un-
observable) ground-truth label, as no revenue or loss occurs.
On the other hand, predicted negatives either have a negative
reward — the cost of accepting a fraudulent purchase —, or
a positive reward — the revenue of a legitimate purchase.
(Gao et al., 2021) propose using this bandit feedback to
learn both a decision-making model and a routing model,
leveraging counterfactual risk minimization (Swaminathan
& Joachims, 2015). Despite modelling rewards instead of
labels, their approach still requires human predictions for
every training instance.
Alternatively, selective labels can also be directly addressed.
Imputation techniques may be used, leveraging expert con-
sensus when available (De-Arteaga et al., 2018; Keswani
et al., 2022). Furthermore, selective labels do not com-
pletely eliminate relevant signal, as predicted negatives will
still result in either true or false negatives. Consequently,
performance can be compared on the basis of the trade-off
between predicted positive prevalence and false negative
prevalence (Lakkaraju et al., 2017). A HAIC system based
on these signals could still be beneﬁcial, without requiring
additional data.
3.6. Fairness
As mentioned in Section 1, both humans and ML models
are capable of bias against protected groups (Angwin et al.,
2016; Buolamwini & Gebru, 2018). When introducing learn-
ing to defer, Madras et al. (2018) were keen on building a
framework that optimizes not only for performance, but also
for fairness. Considering the ML model’s biases, as well
as those of humans, allows the deferring system to mitigate
existing biases. On the contrary, introducing customized
deferral systems without considering fairness may result in
aggravating existing biases, as demonstrated by Jones et al.
(2020) in the context of learning with rejection.
Fairness in HAIC represents not only an opportunity, but
also a threat, and should thus always be considered. While
most contributions on L2D do consider fairness (Madras
et al., 2018; Keswani et al., 2021), other contributions inside
and outside L2D do not (Mozannar & Sontag, 2020; Gao
et al., 2021; Bansal et al., 2021). With AI being increasingly
used to support decision-making in key societal sectors, fu-
ture research should aim to maintain fairness at the forefront
of human-AI collaboration.
3.7. Dynamic environments
Lastly, a key unaddressed issue is dealing with dynamic
environments. The underlying data distribution may change
due to new trends, resulting in concept drift (Gama et al.,
2014). Furthermore, in performative prediction settings
(Perdomo et al., 2020), the actions of the system may inﬂu-
ence the environment. In adversarial classiﬁcation settings
(Dalvi et al., 2004), it may even elicit a response (e.g. fraud-
sters changing strategies as a response to fraud detection
systems). The system’s decision-makers may also change
their behavior, as they learn new concepts, update beliefs,
or are inﬂuenced by exogenous factors. HAIC systems must
account for all these non-stationary factors, or at least be
updated with new data to avoid performance degradation.
L2D does not endogenously model any of the aforemen-
tioned non-stationarity factors, and it cannot be updated
with new data naturally obtained from the HAIC environ-
ment (see Section 3.1). Future research should focus on
developing HAIC systems that do not have this limitation.
4. Conclusion
In this paper, we shed light on the structural limitations and
unaddressed challenges of the state-of-the-art method for
managing assignments in human-AI collaborative decision-
making — learning to defer. Our goal is to motivate research
moving towards a holistic human-AI collaboration system
that learns to optimize performance and fairness from the
available data, while managing existing capacity constraints,
and keeping up with dynamic environments.


---

Page 5

---

Human-AI Collaborative Decision-Making: Beyond Learning to Defer
References
Angwin, J., Larson, J., Mattu, S., and Kirchner, L. Machine
bias risk assessments in criminal sentencing. ProPublica,
May, 23, 2016.
Bansal, G., Nushi, B., Kamar, E., Horvitz, E., and Weld,
D. S. Is the most accurate ai the best teammate? optimiz-
ing ai for teamwork. In Proceedings of the AAAI Con-
ference on Artiﬁcial Intelligence, volume 35, pp. 11405–
11414, 2021.
Buolamwini, J. and Gebru, T. Gender shades: Intersec-
tional accuracy disparities in commercial gender classi-
ﬁcation. In Conference on fairness, accountability and
transparency, pp. 77–91. PMLR, 2018.
Burrell, J. How the machine ‘thinks’: Understanding opacity
in machine learning algorithms. Big Data & Society, 3
(1):2053951715622512, 2016.
Chow, C. K.
On optimum recognition error and reject
tradeoff. IEEE Trans. Inf. Theory, 16:41–46, 1970.
Corbi`ere, C., Thome, N., Bar-Hen, A., Cord, M., and P´erez,
P. Addressing failure prediction by learning model con-
ﬁdence.
Advances in Neural Information Processing
Systems, 32, 2019.
Cortes, C., DeSalvo, G., and Mohri, M. Learning with
rejection. 2016.
Dalvi, N., Domingos, P., Sanghai, S., and Verma, D. Ad-
versarial classiﬁcation. In Proceedings of the tenth ACM
SIGKDD international conference on Knowledge discov-
ery and data mining, pp. 99–108, 2004.
De-Arteaga, M., Dubrawski, A., and Chouldechova, A.
Learning under selective labels in the presence of expert
consistency. arXiv preprint arXiv:1807.00905, 2018.
Esteva, A., Kuprel, B., Novoa, R. A., Ko, J., Swetter, S. M.,
Blau, H. M., and Thrun, S. Dermatologist-level classiﬁ-
cation of skin cancer with deep neural networks. Nature,
542(7639):115–118, 2017.
Gal, Y. and Ghahramani, Z. Dropout as a bayesian ap-
proximation: Representing model uncertainty in deep
learning. In Balcan, M. F. and Weinberger, K. Q. (eds.),
Proceedings of The 33rd International Conference on Ma-
chine Learning, volume 48 of Proceedings of Machine
Learning Research, pp. 1050–1059, New York, New York,
USA, 20–22 Jun 2016. PMLR.
Gama, J., ˇZliobait˙e, I., Bifet, A., Pechenizkiy, M., and
Bouchachia, A. A survey on concept drift adaptation.
ACM computing surveys (CSUR), 46(4):1–37, 2014.
Gao, R., Saar-Tsechansky, M., De-Arteaga, M., Han, L.,
Lee, M. K., and Lease, M. Human-AI collaboration with
bandit feedback. arXiv preprint arXiv:2105.10614, 2021.
Hendrycks, D. and Gimpel, K. A baseline for detecting
misclassiﬁed and out-of-distribution examples in neural
networks. arXiv preprint arXiv:1610.02136, 2016.
Jesus, S. M., Bel´em, C., Balayan, V., Bento, J., Saleiro,
P., Bizarro, P., and Gama, J. How can I choose an ex-
plainer? An application-grounded evaluation of post-hoc
explanations. CoRR, abs/2101.08758, 2021.
Jones, E., Sagawa, S., Koh, P. W., Kumar, A., and Liang,
P. Selective classiﬁcation can magnify disparities across
groups. arXiv preprint arXiv:2010.14134, 2020.
Keswani, V., Lease, M., and Kenthapadi, K. Towards unbi-
ased and accurate deferral to multiple experts. In Proceed-
ings of the 2021 AAAI/ACM Conference on AI, Ethics,
and Society, pp. 154–165, 2021.
Keswani, V., Lease, M., and Kenthapadi, K.
Design-
ing closed human-in-the-loop deferral pipelines. arXiv
preprint arXiv:2202.04718, 2022.
Kirchner,
L.
and
Larson,
J.
How
we
ana-
lyzed the compas recidivism algorithm.
2017.
URL
https : / / www.propublica.org /
article/how- we- analyzed- the- compas-
recidivism-algorithm.
Lakkaraju, H., Kleinberg, J., Leskovec, J., Ludwig, J., and
Mullainathan, S. The selective labels problem: Evalu-
ating algorithmic predictions in the presence of unob-
servables. In Proceedings of the 23rd ACM SIGKDD
International Conference on Knowledge Discovery and
Data Mining, pp. 275–284, 2017.
Lakshminarayanan, B., Pritzel, A., and Blundell, C. Simple
and scalable predictive uncertainty estimation using deep
ensembles. Advances in neural information processing
systems, 30, 2017.
Madras, D., Pitassi, T., and Zemel, R. Predict responsi-
bly: Improving fairness and accuracy by learning to defer.
In Proceedings of the 32nd International Conference on
Neural Information Processing Systems, NIPS’18, pp.
6150–6160, Red Hook, NY, USA, 2018. Curran Asso-
ciates Inc.
Meehl, P. E. Clinical versus statistical prediction: A theoret-
ical analysis and a review of the evidence. 1954.
Mozannar, H. and Sontag, D. Consistent estimators for learn-
ing to defer to an expert. In Proceedings of the 37th In-
ternational Conference on Machine Learning, ICML’20.
JMLR.org, 2020.


---

Page 6

---

Human-AI Collaborative Decision-Making: Beyond Learning to Defer
Perdomo, J., Zrnic, T., Mendler-D¨unner, C., and Hardt, M.
Performative prediction. In International Conference on
Machine Learning, pp. 7599–7609. PMLR, 2020.
Swaminathan, A. and Joachims, T. Counterfactual risk
minimization: Learning from logged bandit feedback.
In International Conference on Machine Learning, pp.
814–823. PMLR, 2015.
Verma,
R. and Nalisnick,
E.
Calibrated learning
to defer with one-vs-all classiﬁers.
arXiv preprint
arXiv:2202.03673, 2022.
Wilder, B., Horvitz, E., and Kamar, E. Learning to comple-
ment humans. arXiv preprint arXiv:2005.00582, 2020.
Youseﬁ, N., Alaghband, M., and Garibay, I. A compre-
hensive survey on machine learning techniques and user
authentication approaches for credit card fraud detection.
arXiv preprint arXiv:1912.02629, 2019.
