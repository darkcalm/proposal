

---

Page 1

---

arXiv:2504.07472v2  [cs.SE]  29 May 2025
HACMony: Automatically Detecting Hopping-related
Audio-stream Conflict Issues on HarmonyOS
Jinlong He
Technology Center of Software
Engineering, Institute of Software,
Chinese Academy of Sciences
Beijing, China
hejinlong@otcaix.iscas.ac.cn
Binru Huang
Hangzhou Institute for Advanced
Study, University of Chinese
Academy of Sciences
Hangzhou, China
huangbinru24@mails.ucas.ac.cn
Changwei Xia
Hangzhou Institute for Advanced
Study, University of Chinese
Academy of Sciences
Hangzhou, China
xiachangwei24@mails.ucas.ac.cn
Hengqin Yang
Hangzhou Institute for Advanced
Study, University of Chinese
Academy of Sciences
Hangzhou, China
yanghq@ios.ac.cn
Jiwei Yan∗
Technology Center of Software
Engineering, Institute of Software,
Chinese Academy of Sciences
Beijing, China
yanjiwei@otcaix.iscas.ac.cn
Jun Yan
Technology Center of Software
Engineering, Institute of Software,
Chinese Academy of Sciences
Beijing, China
yanjun@ios.ac.cn
Abstract
HarmonyOS is emerging as a popular distributed operating sys-
tem for diverse mobile devices. One of its standout features is app-
hopping, which allows users to switch apps seamlessly across differ-
ent HarmonyOS devices. However, when apps play audio-stream-
hop between different devices, they can easily trigger Hopping-
related Audio-stream Conflict (HAC) scenarios. Improper resolu-
tion of HAC will lead to significant HAC issues, which are hard
to detect comprehensively due to the unclear semantics of Har-
monyOS’s app-hopping mechanism and the lack of effective multi-
app hopping testing methods. To fill the gap, this paper introduces
an automated and efficient approach to detecting HAC issues. We
formalized the operational semantics of HarmonyOS’s app-hopping
mechanism for audio streams for the first time. Leveraging this for-
malization, we designed an Audio-stream-aware State Transition
Graph (ASTG) to model the behaviors of audio-streams during win-
dow transitions and proposed a model-based approach to detect
HAC issues automatically. Our techniques were implemented in a
tool, HACMony, and evaluated on 20 real-world HarmonyOS apps.
Experimental results reveal that 12 of the 20 apps exhibit HAC is-
sues. Among the 53 HAC issues detected, a total of 18 unique HAC
issues were manually confirmed. Additionally, we summarized the
detected issues into two typical types, namely MoD and MoR, and
analyzed their characteristics to assist and guide both app and OS
developers.
Keywords
HarmonyOS, Audio-Stream Conflict, App-Hopping, Mobile Testing,
Large Language model
1
Introduction
The use of audio-stream is prevalent in mobile applications, cov-
ering a range of use cases from simple music playing to complex
audio processing and interaction. When more than one apps use
audio streams on a single device, their audio streams may conflict
∗*
and require proper handling. For example, users may launch a mu-
sic app to play a song first and then switch to a movie app to play
a video, both of which involve audio streams. However, if neither
the music app nor the movie app handles the played audio streams
according to the scenario, i.e., just let the two started audios play
at the same time, users may feel confused and uncomfortable.
When there are conflicts on multiple audio-streams, there are
specific coping solutions according to experience. In this example,
users usually expect the music-playing can be paused automatically
to ensure the normal playing of the newly launched video. To
enhance users’ experience, existing mobile systems typically offer
an audio-focus feature to resolve such Audio-stream Conflicts (ACs).
When an app attempts to play an audio, the system requests focus
for the audio stream. Only the audio stream that gains the focus can
be played, i.e., if the request is rejected, the audio stream cannot be
played. If an audio stream is interrupted by another one, it loses
audio focus and is expected to take actions like pause, stop, or lower
volume to avoid unexpected AC-related issues.
As we can see, handling multiple audio app interaction scenar-
ios on a single device is inherently complex. Fortunately, as apps
undergo iterative updates, most app developers have made efforts
to design proper and effective conflict-handling solutions for their
apps. Nowadays, with the rise of multi-device distributed operating
systems [16], applications can not only be used on a single device
but can also be migrated to other devices through hopping opera-
tions. These emerging operating systems aim to enhance users’ ex-
perience, but they also make audio app interactions scenarios much
more complex. In such a context, the existing conflict-handling
solutions designed for single-device scenarios often lose effective-
ness. Thus, when developing apps working on distributed operating
systems, the audio-stream conflict handling scenarios on multiple
devices should be comprehensively tested.
In recent years, as the most representative distributed mobile
operating system, HarmonyOS has achieved remarkable success
and is running on more than one billion devices [38]. Developed
by Huawei, HarmonyOS is a distributed platform designed for
seamless integration across smartphones, tablets, smart TVs, and
more. A standout feature of HarmonyOS is app-hopping [25], a


---

Page 2

---

Conference’17, July 2017, Washington, DC, USA
He et al.
distributed operation mode that plays a fundamental role in its
ecosystem. This functionality allows users to seamlessly transfer
apps across different devices, enhancing convenience and flexibility.
However, this innovation also complicates the resolution of ACs due
to the increased interplay between devices. Through a preliminary
investigation, we found that many users had complained about poor
experiences caused by Hopping-related Audio-stream Conflict
(HAC) issues [1, 2], where the audio-stream conflicts that occur
during HarmonyOS’s app-hopping are improperly handled. Given
the significant disruption HAC issues cause to the user experience
during app-hopping across multiple HarmonyOS devices, this paper
focuses on how to detect HAC issues automatically and efficiently,
alongside analyzing existing HAC issues to provide deeper insights.
To achieve that, it is crucial first to understand how HarmonyOS’s
app-hopping mechanism operates and design an efficient test gen-
eration approach tailored for app-hopping scenarios. The first
major challenge lies in the lack of semantics for the app-
hopping mechanism. Through an investigation of the official
documentation, we found that existing materials focus on high-
lighting the benefits of app-hopping but lack detailed descriptions
of the underlying mechanism. This lack of clarity significantly
complicates the design of effective testing approaches for app-
hopping. Specifically, it increases the difficulty of determining when
and how to perform hopping operations that are more likely to
trigger HAC issues. Moreover, this omission also impedes other
hopping-related research efforts. The second challenge is lack-
ing hopping-specific models designed for efficient testing.
Although there are various models designed for mobile apps’ GUI
testing [11, 14, 20, 23, 24, 31, 36, 37, 39–43], there is no HAC-specific
model, that describes the behaviors of audio streams of an app and
can guide a compact test case generation. Without such a model, it
would be difficult to design an effective testing strategy to detect
HAC issues.
To address Challenge 1, we meticulously picked several rep-
resentative HarmonyOS native apps, designed and conducted a
group of semantic experiments on app-hopping operations, and
summarized the behaviors of app-hopping operations according
to the experimental results. Based on that, we first present the
formalized operational semantics of HarmonyOS’s app-hopping
mechanism in the aspect of audio stream. To address Challenge
2, we propose an extended FSM [43] called Audio-stream-aware
State Transition Graph (ASTG) to describe the behaviors of audio
streams. Its node, Audio-Stream-aware State (ASS), denotes the
window and its audio stream status in a running app; while its edge
describes the transition rule between ASSs with the label of GUI
events. To accurately and efficiently construct ASTG model, we pro-
pose an ASS-targeted and LLM-driven model exploration approach,
which adopts LLM to identify and prioritize GUI events capable of
triggering audio-stream interactions, then utilizes this information
to guide the dynamic exploration of the app under test. As this
exploration approach can only explore the audio-stream statuses
without multiple apps’ interaction, we also propose an ASS-guided
enhancement approach to simulate the multi-app environment
for extracting the extra ASSs and then construct a more precise
ASTG. Based on both the operational semantics of HarmonyOS’s
app-hopping mechanism and the fine-grained ASTG model, we can
finally generate targeted test cases and execute them to detect HAC
issues.
We implemented our proposed techniques into a tool called HAC-
Mony (Hopping-related Audio-stream Conflict issues for HarMonyOS)
and evaluated it on 20 real-world popular HarmonyOS apps. The ex-
perimental results demonstrate that the proposed testing approach
can efficiently detect HAC issues. Among the 20 apps, 12 were found
to have HAC issues. Among the 53 HAC issues detected, there are
18 unique HAC issues, which are all manually confirmed. Through
issue analysis, we categorized the identified HAC issues into two
types: Misuse of Device (MoD) and Misuse of Resolution (MoR).
We further summarized their characteristics and possible causes to
provide deeper insights for both application and OS developers.
The main contributions of this work are summarized as follows:
• We present the first formal semantics of the HarmonyOS app-
hopping mechanism, which serves as a foundation for HAC issue
testing and could inspire further research.
• We design the ASTG model to describe the transitions of ASSs
in HarmonyOS apps and propose a LLM-driven dynamic ex-
ploration approach to construct ASTG models. The approach
is implemented into a tool HACMony 1, which is evaluated on
20 real-world apps and successfully discovered 18 unique HAC
issues.
• We summarize two typical types of HAC issues, namely MoD
and MoR, and analyze their possible causes. These findings can
assist and guide both app and OS developers in improving the
apps’ quality on distributed mobile systems.
2
Background
This section introduces the basic concepts around HarmonyOS apps
and audio streams. We also give a motivating example to illustrate
the behavior of a real HAC issue.
2.1
HarmonyOS: Architecture and Application
HarmonyOS is designed with a layered architecture, which from
bottom to top consists of the kernel layer, system server layer, frame-
work layer, and application layer. Figure 1 illustrates the layered
architecture of HarmonyOS [13, 26]. The application layer is com-
posed of Android (AOSP) apps and HarmonyOS native (OpenHar-
mony) apps, which achieves binary compatibility. In the framework
layer, the ABI-compliant Shim (application binary interface com-
pliant layer) redirects Linux syscalls into IPCs, channeling them
towards appropriate OS services. This mechanism effectively ad-
dresses compatibility issues with AOSP and OpenHarmony, as
noted in [13]. The system service layer offers a comprehensive
set of capabilities crucial for HarmonyOS to provide services to
applications. It consists of a basic system capability subsystem, a
basic software service subsystem, an enhanced software service
subsystem, and a hardware service subsystem. The kernel layer,
through its core kernel, furnishes memory management, file system
management, process management, and native driver functionality.
With this architecture, especially the design of ABI-compliant
shim, HarmonyOS can support both AOSP [19] (for Android apps)
and OpenHarmony [17] (for native apps). Notably, the distributed
1Available at https://github.com/SQUARE-RG/hacmony


---

Page 3

---

HACMony: Automatically Detecting Hopping-related Audio-stream Conflict Issues on HarmonyOS
Conference’17, July 2017, Washington, DC, USA
Application Layer
Android/Harmony native App Binary Compatible
AOSP/OpenHarmony
Framework Layer
ABI-compliant Shim
Kernel Layer
System Server Layer
IPC…
Linux Syscall
Basic system 
capability
Hardware 
service
Basic software 
service
Enhanced 
software service
IPC
Core Kernel
Proc. Mgr.
Mem
Mgr.
File
System
…
Native Driver
Figure 1: HarmonyOS Architecture
operation app-hopping is implemented within the basic system ca-
pability subsystem, which transports Android and HarmonyOS
native apps to another HarmonyOS device through the distributed
soft bus in the same way. In this paper, we take both of the two
supported types of apps on HarmonyOS as HarmonyOS apps.
2.2
Audio Stream
Audio streaming is a technology that allows users to transmit and
receive audio data in real-time over the internet. Audio streaming
is commonly used in online music services, internet radio, pod-
casts, and other applications that require instant audio content
transmission.
In general, an app typically has three fundamental audio-stream
statuses when no other app is playing audio stream, i.e., STOP,
PAUSE, and PLAY. In real-world scenarios, audio streams are prone
to conflicts when apps interact. When such conflicts occur, the
behavior of the audio playback in an app becomes more complex.
To mitigate the interference impact of the conflict on users, the
app will often temporarily lower the volume or pause the audio
stream to avoid simultaneous playback. As a consequence, during
the occurrence of these conflicts, an app has two extra audio-stream
statuses, i.e., PLAY↓and PLAY∥. Specifically, when an app play to-
gether with another app, PLAY↓signifies one app lower the volume,
and PLAY∥signifies one app pause the playback and play again
when the conflict disappears. As shown in Table 1, we consider the
listed five audio stream statuses in this paper.
Table 1: Description of Audio Stream Statuses
Audio-stream Status
Description
STOP
stop the playback
PAUSE
pause the playback
PLAY
play the playback
PLAY↓
lower the volume,
restore after conflict disappear
PLAY∥
pause the playback,
play after conflict disappear
Furthermore, HarmonyOS adopt audio focus to manage audio
streams from different apps to reconcile the audio-stream conflicts.
When an audio stream requests or releases audio focus, the system
manages focus for all streams based on predefined audio focus
policies. These policies determine which audio stream can operate
normally and which must be interrupted or subjected to other
actions. The system’s default audio focus policy primarily relies on
the type of audio stream and the order in which the audio streams
are initiated [29]. In HarmonyOS, “StreamUsage" is an enumeration
type to define audio stream categories. It plays a crucial role in audio
playback and management. The commonly used values include
STREAM_USAGE_MUSIC (MUSIC), STREAM_USAGE_MOVIE
(MOVIE), STREAM_USAGE_NAVIGATION (NAVIG), and STREA
M_USAGE_VOICE_COMMUNICATION (COMMU) [30].
Table 2 lists typical resolutions for solving ACs based on audio
stream types by HarmonyOS, where app “pre" plays audio streams
first and then app “post" plays at a later time. Although these reso-
lutions are recommended ones, HarmonyOS also allows developers
to handle conflicts on their own. This leads to different proper
resolutions for solving conflicts for real-world apps in practice.
Table 2: Typical Resolutions for Solving the ACs, where
:
app “pre" lowers the volume, after app “post" releases the
audio focus, app “pre" restores the volume.
: app “post"
lowers the volume, after app “pre" releases the audio focus,
app “post" restores the volume.
: app “pre" and “post" play
together. : app “pre" pauses the playback, after app “post"
releases the audio focus, app “pre" plays again.
: app “pre"
stops the playback.
Type of app “post"
MUSIC
MOVIE
NAVIG
COMMU
Type
of
app
“pre"
MUSIC
MOVIE
NAVIG
COMMU
2.3
Motivating Example
To show the motivation for this work, we use a navigation app,
AMap [3], running on a phone, and a music app, Kugou Music [6],
running on a tablet for illustration. As shown in Figure 2, the initial
scenario is depicted in 1○, where both apps, AMap and Kugou Music,
play their audio streams at normal volume. When the user launches
Amap on the tablet and navigating in 1○, the app AMap plays the
audio stream with the normal volume, but Kugou Music lowers the
volume to avoid the audio-stream conflict, whose status is displayed
in 2○. When the user clicks the “recent" button on the phone in
1○, the interface on the phone changes the interface for selecting
the hopping app and target device, which is shown in 3○. When
the user drags the app Amap to the tablet on the phone in 3○, the
app Amap will be hopped to the tablet. However, in this situation,
both AMap and Kugou Music play their audio streams at normal
volume on the tablet, which is not expected. Since Kugou Music fails
to lower its volume, users may have difficulty hearing navigation
instructions from AMap. In the context of in-vehicle infotainment
systems, such conflicts could even pose safety risks.


---

Page 4

---

Conference’17, July 2017, Washington, DC, USA
He et al.
1h 30km
1h 30km
1h 30km
1h 30km
1h 30km
Launch Amap
on the tablet 
& navigate
Click the “recent” button
on the  phone
Drag Amap
to the tablet
tablet
3
4
1
2
Amap plays audio
Kugou Music plays audio
Kugou Music lowers the volume
Amap plays audio
Amap plays audio
Amap plays audio
Kugou Music plays audio
Kugou Music plays audio
Amap plays audio
Figure 2: Motivating Example
To uncover hidden vulnerabilities that can be triggered by the
app-hopping operation on HarmonyOS, two key tasks must be
accomplished. First, it is essential to understand the operational se-
mantics of HarmonyOS’s app-hopping mechanism. Besides, an effi-
cient test generation approach tailored specifically for app-hopping
scenarios should be designed.
3
The Operational Semantics of App-Hopping
Mechanism on HarmonyOS
In this section, we describe the overview of the app-hopping mech-
anism and specify the mechanism as an operational semantics.
3.1
The Overview of App-Hopping
HarmonyOS provides the Virtual Super Device (Super Device) to
integrate multiple physical devices and allow one device to share
data and apps among devices with distributed communication ca-
pabilities. App-hopping is the fundamental feature of the Super
Device to share the apps among devices [25].
When hopping an app 𝑎from device 𝑑to device 𝑑′, the app 𝑎
will seamlessly transfer from device 𝑑to 𝑑′, i.e., it will be displayed
on the screen of device 𝑑′ only. Users could end a hop at any time
when there is an app hop in the super device. Ending the hop of
app 𝑎will let app 𝑎return to device 𝑑. To obtain HarmonyOS’s
hopping mechanism, We picked several representative HarmonyOS
native apps to explore the behavior of app-hooping among multiple
devices. By checking the official documents as well as conducting a
group of experiments, we found that there is at most one app hop
held in the super device in HarmonyOS. That is, if app 𝑎has been
hopped from device 𝑑to device 𝑑′ and the users hop another app
𝑎′ in the super device, the hop of app 𝑎will be ended automatically.
Furthermore, when considering the audio stream of apps, the be-
haviors of starting a hop and ending a hop will be more complicated.
When starting a hop of app 𝑎that is playing music on device 𝑑to
another device 𝑑′, then app 𝑎will play music on device 𝑑′. If there
is another app playing music on device 𝑑′ before the hop of app 𝑎,
the audio-stream conflict will occur on the device 𝑑′, which should
be carefully addressed to avoid HAC issue happen.
3.2
The operational Semantics of App-Hopping
According to our literal and experimental investigation, we first
summarize the formal semantics of HarmonyOS’s app-hopping
mechanism. In this part, we specify its operational semantics to help
users to better understand the app-hopping behaviors. Figure 3 de-
fines domains, stacks, and operations to describe the operational
semantics. We write 𝑎for an app name, and 𝑑for a device name. An
app instance is a pair of its activity name, and audio stream status
(𝑎, 𝜇). An app stack 𝛼is a sequence of app instances. A device in-
stance is a pair of its device name and its app stack (𝑑, 𝛼). A device
stack 𝛽is a sequence of device instances. A hopping relation 𝑟is
either a triple of source device name, app name and target device
name (𝑑,𝑎,𝑑′), or a dummy symbol 𝜖representing no hop exists in
the super device.
The operational semantics are defined as the relation of the
form ⟨𝛽,𝑟⟩
𝐶
⊢−→⟨𝛽′,𝑟′⟩, where the current devices stack is 𝛽and
the current hopping relation is 𝑟, the operation 𝐶resulting in the
new devices stack 𝛽′ and the new hopping relation 𝑟′. The typical
behaviors of StartHop and EndHop operations are as follows:
𝛽= 𝛽1 :: (𝑑𝑠, 𝛼𝑠) :: 𝛽2 :: (𝑑𝑡, 𝛼𝑡) :: 𝛽3
𝛼𝑠= 𝛼1 :: (𝑎, 𝜇) :: 𝛼2
𝐴= (𝑎, 𝜇)
𝑟= (𝑑𝑠,𝑎,𝑑𝑡)
𝛼′𝑠= rmv(𝐴, 𝛼𝑠)
𝛼′
𝑡= add(𝐴, 𝛼𝑡)
⟨𝛽,𝜖⟩
𝑑𝑠.StartHop(𝑎,𝑑𝑡)
⊢−−−−−−−−−−−−−−−→⟨𝛽1 :: (𝑑𝑠, 𝛼′𝑠) :: 𝛽2 :: (𝑑𝑡, 𝛼′
𝑡) :: 𝛽3,𝑟⟩
𝛽= 𝛽1 :: (𝑑𝑠, 𝛼𝑠) :: 𝛽2 :: (𝑑𝑡, 𝛼𝑡) :: 𝛽3
𝛼𝑡= 𝛼1 :: (𝑎, 𝜇) :: 𝛼2
𝐴= (𝑎, 𝜇)
𝑟= (𝑑𝑠,𝑎,𝑑𝑡)
𝛼′𝑠= add(𝐴, 𝛼𝑠)
𝛼′
𝑡= rmv(𝐴, 𝛼𝑡)
⟨𝛽,𝑟⟩
EndHop
⊢−−−−−−→⟨𝛽1 :: (𝑑𝑠, 𝛼′𝑠) :: 𝛽2 :: (𝑑𝑡, 𝛼′
𝑡) :: 𝛽3,𝜖⟩
The first specifies that if a user hops an app when there is no hop
in the super device, the app will be moved to the target device, and
the other apps in the source (resp. target) device will change the
audio stream status according to the function rmv (resp. add). The
second describes that if a user ends a hop of an app, the behavior
of this operation is dual to that of the first.
Intuitively, the function rmv(𝐴, 𝛼) (resp. add(𝐴, 𝛼)) indicates the
behaviors of removing (resp. adding) an app instance 𝐴from (resp.
into) a given app stack 𝛼. Moreover2,
2Due to the space limitation, we describe the remaining rules and helper functions in
a companion report [22].
𝑎
∈
App
application name
𝑑
∈
Device
device name
𝜇
∈
Audio
=
{PLAY, PAUSE, STOP, PLAY↓, PLAY∥}
𝑟
∈
HopRelation
=
Device × App × Device ∪{𝜖}
𝐴
∈
AppInst
=
App × Audio
𝐷
∈
DeviceInst
=
Device × AppStack
𝛼
::= 𝜖| 𝐴:: 𝛼
∈
AppStack
𝛽
::= 𝜖| 𝐷:: 𝛽
∈
DeviceStack
𝐶
::= EndHop
|
𝑑.StartHop(𝑎,𝑑)
Figure 3: Domains, Stacks, and Operations


---

Page 5

---

HACMony: Automatically Detecting Hopping-related Audio-stream Conflict Issues on HarmonyOS
Conference’17, July 2017, Washington, DC, USA
(𝑎!,PLAY)
d1
(𝑎", PLAY)
d2
(𝑎#, PLAY)
d3
(𝑎$, PLAY)
d1
(𝑎", PLAY↓)
d2
(𝑎#, PLAY)
d3
𝑎!
d1
d2
d3
𝑎#
(𝑎!,PLAY)
(𝑎$, PLAY)
d1
(𝑎", PLAY)
d2
(𝑎#, PLAY)
d3
𝑎!
𝑠𝑑!
𝑠𝑑"
𝑠𝑑#
𝑠𝑑$
𝑑!.StartHop(𝑎!, 𝑑$)
𝑑". StartHop(𝑎#, 𝑑$)
(𝑎!,PLAY)
(𝑎#, PLAY)
𝑑!. StartHop(𝑎!,𝑑")
(𝑎$, PLAY↓)
(𝑎$, PLAY↓)
(𝑎", PLAY‖)
(𝑎!,PALY)
EndHop
EndHop
EndHop
Figure 4: Example of HarmonyOS’s App-Hopping Mecha-
nism
• if app instance 𝐴is in the status PLAY, and there exists another
app instance 𝐴′ in the status PLAY↓or PLAY∥, rmv(𝐴, 𝛼) will let
𝐴′ turn into PLAY,
• if 𝐴is in the status of {PLAY, PLAY↓, PLAY∥}, and there exists
another app instance 𝐴′ in the status PLAY, add(𝐴, 𝛼) will lead
to the audio-stream conflict, the status of app instance 𝐴′ will
change according to the resolution to solve the conflicts (refer to
Section 4.3.3).
Multiple-Device App-Hopping Example. In the following,
we use an example to illustrate the operational semantics of the
HarmonyOS app-hopping mechanism. Suppose that there are three
devices 𝑑1,𝑑2,𝑑3 in the super device, and four apps 𝑎1,𝑎2,𝑎3,𝑎4
running on these devices. The types of audio streams used for each
app are as follows, 𝑎1 : NAVIG, 𝑎2 : MOVIE, 𝑎3 : MUSIC, and
𝑎4 : COMMU. To simplify the complicated process, we suppose all
the resolutions to solve audio stream conflicts following the typical
resolutions listed in Table 2. As shown in Figure 4, there are four
cases of the super device 𝑠𝑑1,𝑠𝑑2,𝑠𝑑3,𝑠𝑑4. For each 𝑖∈[1, 4], we
let 𝑠𝑑𝑖= ⟨𝛽𝑖,𝑟𝑖⟩where 𝛽𝑖= (𝑑1, 𝛼𝑖,1) :: (𝑑2, 𝛼𝑖,2) :: (𝑑3, 𝛼𝑖,3). For
instance, 𝛼1,1 = (𝑎1, PLAY) :: (𝑎2, PLAY↓) is the app stack of the
device 𝑑1 in the super device 𝑠𝑑1. The semantics of the app-hopping
mechanism are illustrated by the following cases.
• When the operation𝑑1.StartHop(𝑎1,𝑑2) is applied to 𝑠𝑑1, the app
instance (𝑎1, PLAY) will be removed from 𝛼1,1 = (𝑎1, PLAY) ::
(𝑎2, PLAY↓). Since the audio stream status of 𝑎2 is PLAY↓, it will
turn to PLAY , resulting in 𝛼2,1 = (𝑎2, PLAY). Moreover, the app
instance (𝑎1, PLAY) will be added into the device 𝑑2, and request
the audio focus of device 𝑑2, then app instance of 𝑎3 will turn to
PLAY↓, resulting in 𝛼2,2 = (𝑎1, PLAY) :: (𝑎3, PLAY↓).
• When the operation EndHop is applied to 𝑠𝑑2, since there is
already a hop 𝑟2 = (𝑑1,𝑎1,𝑑2), the app instance (𝑎1, PLAY) will
be moved back to device 𝑑1 from 𝑑2. Moreover, (𝑎1, PLAY) will
be removed from 𝛼2,2 = (𝑎1, PLAY) :: (𝑎3, PLAY↓). Since the
audio stream status of 𝑎3 is PLAY↓, it will then turn to PLAY,
resulting in 𝛼1,2 = (𝑎3, PLAY). Then the app instance (𝑎1, PLAY)
will be added into the device 𝑑1, and request the audio focus of
device 𝑑1, then app instance of 𝑎2 will turn to PLAY↓, resulting
in 𝛼1,1 = (𝑎1, PLAY) :: (𝑎2, PLAY↓).
Main
STOP
Player
PLAY
Click song
Player
PAUSE
Click “Play”
Click “Play”
Main
PAUSE
Back
Click song
Main
STOP
Player
PLAY
Click song
Player
PAUSE
Click “Play”
Click “Play”
Main
PAUSE
Back
Click song
Player
DUCK
Player
PAUSE*
Start app1
Start app2
1. ASS-Targeted LLM-Driven Model Exploration
2. ASS-Guided Model Enhancement
App Under Test
Initial ASTG Model
Multi Audio-associated Apps
ASTG Model
Phase 1. Model Construction
3. Test Generation
4. Test Execution
5. Issue Detection
Issue Report
Multi Devices
Test Cases
Phase 2. Model-Based Testing
LLM
Figure 5: HACMony’s Workflow
• When the operation 𝑑3.StartHop(𝑎4,𝑑2) is applied to 𝑠𝑑2, since
there is already a hop 𝑟2 = (𝑑1,𝑎1,𝑑2), it will end the previous
hop first. That is, the case turns to 𝑠𝑑1. Then it will hop 𝑎4 from
device 𝑑3 to device 𝑑2. Since the audio stream conflict resolution
for app pair (pre:𝑎3, post:𝑎1) is different from pair (pre:𝑎3, post:𝑎4)
according to their types, the audio stream status of 𝑎3 is PLAY∥
instead of PLAY↓in this case.
• When the operation 𝑑1.StartHop(𝑎1,𝑑3) is applied to 𝑠𝑑2, it is
similar to the previous case.
It shows that during the app-hopping, audio-stream conflicts
may arise between the hopping app and audio-stream-using apps
on both original device and target device, thereby altering their
audio-stream statuses.
4
Model-based Testing Approach for HAC Issue
Detection
In this section, we present the overview and design details of the
model-based testing approach for automatically detecting HAC
issues.
4.1
Approach Overview
Based on the knowledge of the HarmonyOS’s app-hopping mech-
anism, we design a model-based automatic testing approach for
HAC issue detection. Figure 5 presents an overview of HACMony’s
architecture and workflow, which has two key phases.
Phase 1: Model Construction. To obtain the GUI events that
can influence the statuses of audio streams in further audio-directed
testing, we designed a new model called Audio-stream-aware State
Transition Graph (ASTG). The node, Audio-Stream-aware State
(ASS), of ASTG denotes a pair of the window and its associated
audio-stream status. This binding arises from the fact that audio
stream utilization is normally achieved through windows within an
app, where multiple windows may coexist to manage audio streams.
Therefore, we employ ASSs to explicitly define the audio-stream
statuses of these windows, with the aim of testing HAC issues.
To construct ASTG model, We first employ a dynamic ASS-
targeted app exploration strategy enhanced by large language
model (LLM) analysis to identify and prioritize GUI events capable


---

Page 6

---

Conference’17, July 2017, Washington, DC, USA
He et al.
of triggering audio-stream interactions. Specifically, for each single
app, the LLM-driven analysis examines its window components
and corresponding event handlers to identify events that may acti-
vate audio streams (e.g., play buttons, volume sliders). This refined
process of identifying events is then used to construct the initial
ASTG model (step 1, details in Section 4.2.1). As the single-app ex-
ploration misses the audio-stream statuses (e.g., PLAY↓and PLAY∥)
that happen during the interaction of multiple apps, we enhance the
initial ASTG model by collaborating with multiple apps to explore
extra ASSs (step 2, details in Section 4.2.2).
Phase 2: Model-Based Testing. To generate the compact test
suite for audio-aware hopping behavior testing, we select the ASSs
that are in the PLAY-like statuses (called ASSPLAY) from the ASTG
model constructed by Phase 1, and configure the devices according
to different app-hopping operations (step 3, details in Section 4.3.1).
Then we execute the test cases on multiple devices to detect whether
there are HAC issues (step 4, details in Section 4.3.2). Finally, by
analyzing the resolution to solve the audio-stream conflicts during
hopping and checking whether it is consistent with the resolution
on a single device, HACMony can automatically report HAC issues
(step 5, details in Section 4.3.3).
4.2
ASTG Model Construction
To generate the test case for detecting the HAC issues, we define an
extended FSM, Audio-stream-related State Transition Graph
(ASTG), to represent the audio-stream-level behavior of an app. An
ASTG model is a triple 𝐺= (𝑆,𝑇,𝑠0), where
• 𝑆is a finite set of app’s Audio-Stream-related States (ASSs). A
state 𝑠∈𝑆is a pair ⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩where 𝑤𝑖𝑛denotes the GUI win-
dow, which contains the screenshot as well as the element hierar-
chical tree, 𝑠𝑡𝑎𝑡∈Audio denotes audio-stream status, and 𝑠0 ∈𝑆
is the initial ASS of the app.
• 𝑇denotes the set of transitions. An element 𝜏∈𝑇is a triple
⟨𝑠,𝑒,𝑡⟩representing the transition from the source ASS 𝑠to the
destination ASS 𝑡caused by a GUI event 𝑒, e.g., click or drag.
4.2.1
ASS-Targeted and LLM-Driven Model Exploration. To con-
duct more effective ASS-targeted GUI exploration, we utilize an
LLM-driven analysis to comprehensively understand the tested app
to obtain the available audio-stream types, e.g. MUSIC, and the
semantics of GUI components to pick the optimal event that can en-
able the app to play the audio stream corresponding to the available
type. After identifying the optimal audio-related event in current
window, we proceed to execute the event on the device and collect
the information about the changes (e.g., GUI window changes). If
the app has deviated from the exploration goal after previous event
execution, the LLM will re-evaluate the identified event and select
an alternative event that are more likely to lead the app towards
playing the audio stream. This iterative process of event identifica-
tion, execution, information collection, and verification continues
until the app successfully plays the audio stream.
Algorithm 1 describes the ASS-targeted LLM-driven exploration
approach. The input of the approach is the tested_app to be ex-
plored and the empty ASTG 𝐺, the output is the ASTG 𝐺of the
tested_app. First, it initializes the variable feedback, which indicates
the feedback of the event execution, as empty (line 1). It also ob-
tains the audio-stream types audios available for the tested_app via
UnderstandApp() function (line 2). Then, for each audio to explore
from the available audios, it repeats the following process until the
variable feedback.terminated becomes True, i.e., the app successfully
play audio (lines 3-19).
(1) Obtain the current ASS = (𝑤𝑖𝑛,𝑠𝑡𝑎𝑡) via the function GetASS(),
and pass the current window 𝑤𝑖𝑛to the LLM for understand-
ing, so as to obtain a set of GUI elements containing semantic
information via UnderstandWin() function (lines 6-7).
(2) Send the audio to explore, the current GUI elements, the current
ASTG 𝐺, and the 𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘of the previous event execution, to
the LLM. The LLM then selects the “optimal” event from all
possible events based on the goal of enabling the app to play
the audio stream (line 8). Then it execute the “optimal” event
event (line 9).
(3) Obtain the current ASS = (𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′) after executing the “opti-
mal” event via GetASS() again (line 10), then update the ASTG
𝐺(lines 11-13).
(4) Verify whether the “optimal” event deviates from the explo-
ration goal and whether the current exploration can be termi-
nated, and record such information in the feedback. If it does
deviate from the goal, then restart the test_app to conduct a
more target-directed exploration (lines 14-17).
Algorithm 1: Exploration()
input :𝐺= (𝑆,𝑇,𝑠0),𝑡𝑒𝑠𝑡𝑒𝑑_𝑎𝑝𝑝
1 𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘←[];
2 𝑎𝑢𝑑𝑖𝑜𝑠←UnderstandApp(𝑡𝑒𝑠𝑡𝑒𝑑_𝑎𝑝𝑝);
3 for each 𝑎𝑢𝑑𝑖𝑜in 𝑎𝑢𝑑𝑖𝑜𝑠do
4
𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘.𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑡𝑒𝑑←𝐹𝑎𝑙𝑠𝑒;
5
while 𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘.𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑡𝑒𝑑= 𝐹𝑎𝑙𝑠𝑒do
6
⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩←GetASS();
7
𝑒𝑙𝑒𝑚𝑒𝑛𝑡𝑠←UnderstandWin(𝑤𝑖𝑛);
8
𝑒𝑣𝑒𝑛𝑡←GetOptimalEvent(
𝑎𝑢𝑑𝑖𝑜,𝑒𝑙𝑒𝑚𝑒𝑛𝑡𝑠,𝐺, 𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘);
9
𝑒𝑣𝑒𝑛𝑡.execute();
10
⟨𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′⟩←GetASS();
11
𝑆←𝑆∪{⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩, ⟨𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′⟩};
12
𝜏←⟨⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩,𝑒𝑣𝑒𝑛𝑡, ⟨𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′⟩⟩;
13
𝑇←𝑇∪{𝜏};
14
𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘←Verify(𝑠𝑡𝑎𝑡′,𝑒𝑣𝑒𝑛𝑡,𝑤𝑖𝑛,𝑤𝑖𝑛′);
15
if 𝑓𝑒𝑒𝑑𝑏𝑎𝑐𝑘.𝑣𝑎𝑙𝑖𝑑𝑖𝑡𝑦= False then
16
Restart the 𝑡𝑒𝑠𝑡𝑒𝑑_𝑎𝑝𝑝;
17
end
18
end
19 end
LLM Prompt construction: The prompts used for interaction
with the LLM in each exploration step are presented in Table 3,
which will be elaborated as follows.
• UnderstandWin. This prompt asks LLM to understand the
semantics of each GUI element and specifies the output for-
mat. The LLM describes each element’s function based on
screenshots and individual element images. Each element


---

Page 7

---

HACMony: Automatically Detecting Hopping-related Audio-stream Conflict Issues on HarmonyOS
Conference’17, July 2017, Washington, DC, USA
Table 3: The Simplified LLM Prompt Templates for ASS-Targeted Exploration
UnderstandWin
GetOptimalEvent
Verify
Prompt:
Based on the information of the pro-
vided screenshot of a mobile app in-
terface and images of clickable compo-
nents, complete the task of analyzing
each component image in order to de-
scribe its function. Note that, return
the answer as a Python list; each de-
scription should be concise and func-
tional.
Prompt:
Based on the information of the current
screen, clickable elements, and previous feed-
back, complete the task of determining the
next event. Note that, focus on functional-
ity and adapt to the current screen; choose
the most appropriate element with the same
purpose; avoid repeating previous events; re-
spond only in JSON format.
Prompt:
Based on the information of the screenshots
and elements changes before and after the event,
complete the task of evaluating whether the
event follows previous steps and progresses to-
ward the exploration goal. Note that, check if
the played audio stream type matches the explo-
ration type; assess whether to terminate based
on the audio stream type and status; provide
suggestions for the next step.
Example outputs:
["Return button", "Search box",
"Settings button", "Add device"]
Example outputs:
{"event_type": "click", "id": 3}
{"event_type":
"input",
"id":
2,
"text": "music"}
Example outputs:
{"validity": true/false,
"terminated": true/false,
"suggestion":
"Select
the
"Search"
button"}
is numbered to ensure descriptions are in order and no de-
scriptions are missed, preventing parsing errors.
• GetOptimalEvent. This prompt asks the LLM to generate
the next event based on the current app state (GUI elements
and the step for exploration goal). The LLM selects the opti-
mal event, considering previous steps and feedback to avoid
repetition.
• Verify. This prompt asks LLM to validate the executed event
to checks if the event meets the exploration goal and causes
GUI changes. It analyzes deviations, screen changes, and
completion. It also suggests the next step to guide future
event selection, and determine whether the audio-stream
with the current audio type is played.
4.2.2
ASS-Guided Model Enhancement. As mentioned in Section 2.2,
the audio stream statuses PLAY↓and PLAY∥occur only when there
is another app requesting the audio stream focus. To explore the
extra audio stream statuses, we need to launch another app and
execute specific events to make it use the audio stream and cause
audio-stream conflicts. For different audio stream statuses, the col-
laborating apps may be different in general, so we select a set of
representative apps that use different types of audio streams to
explore these statuses. The principle of the collaborating apps se-
lection is primarily based on the typical resolutions for solving
the ACs (see Table 2). For example, the app with the type NAVIG
(resp. COMMU) is more likely to be selected to explore PLAY↓(resp.
PLAY∥) status for the app with MUSIC type.
Algorithm 2 describes the ASS-guided model enhancement ap-
proach. It takes the previously constructed ASTG 𝐺= (𝑆,𝑇,𝑠0) by
Algorithm 1, the previously tested app tested_app and an audio-
associated app set enhanced_apps as inputs, and takes the ASTG
𝐺enhanced with extra ASSs as output. First, for the tested_app,
it finds out all the ASSs in its ASTG where 𝑠𝑡𝑎𝑡= PLAY as the
target ASSs. Then for each target ASS, according to the ASTG 𝐺, it
obtains and executes the events to switch the tested_app to the ASS
status (lines 1-3). For each enhanced_app in the audio-associated
apps set enhanced_apps, it launches enhanced_app and switches
enhanced_app to PLAY status to make its audio stream conflict with
the explored app (lines 4-6). Finally, if the target app reaches a new
ASS, we add the new ASS as well as the corresponding transition
into the ASS set 𝑆and transition set 𝑇, respectively (lines 7-13).
Algorithm 2: Enhancement()
input :𝐺= (𝑆,𝑇,𝑠0),𝑡𝑒𝑠𝑡𝑒𝑑_𝑎𝑝𝑝,𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝𝑠
1 for each ⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩in S do
2
if 𝑠𝑡𝑎𝑡= PLAY then
3
Switch to ⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩;
4
for each 𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝in 𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝𝑠do
5
Launch 𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝and switch
𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝to PLAY status;
6
⟨𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′⟩←GetASS();
7
if 𝑠𝑡𝑎𝑡≠𝑠𝑡𝑎𝑡′ then
8
𝑆←𝑆∪{⟨𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′⟩};
9
𝑒←launch 𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝and execute
𝑒𝑛ℎ𝑎𝑛𝑐𝑒𝑑_𝑎𝑝𝑝;
10
𝜏←⟨⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩,𝑒, ⟨𝑤𝑖𝑛′,𝑠𝑡𝑎𝑡′⟩⟩;
11
𝑇←𝑇∪{𝜏};
12
end
13
End 𝑡𝑒𝑠𝑡𝑒𝑑_𝑎𝑝𝑝and switch back to ⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩;
14
end
15
end
16 end
4.3
Model-Based HAC Issue Detection
Upon ASTG model construction, this section presents our model-
based testing approach for detecting HAC issues3.
3We mainly consider the two-device hopping testing scenario as it is the most basic
and common scenario and can cover many basic HAC issues.


---

Page 8

---

Conference’17, July 2017, Washington, DC, USA
He et al.
4.3.1
HAC-Directed Test Generation. As we have two typical app-
hopping commands StartHop and EndHop, two types of hopping-
related test cases TestStartHop and TestEndHop should be gener-
ated for each tested app. The basic test generation idea is to select
ASSPLAY, the ASSs in the PLAY-like statuses in the ASTG model,
and configure the devices according to different app-hopping op-
erations. For an ASTG 𝐺= (𝑆,𝑇,𝑠0), an ASS = ⟨𝑤𝑖𝑛,𝑠𝑡𝑎𝑡⟩∈𝑆is
an ASSPLAY, if 𝑠𝑡𝑎𝑡∈{PLAY, PLAY↓, PLAY∥}. Intuitively, ASSPLAY
indicates the audio stream status of the window is PLAY or will
turn to PLAY after other apps release the focus.
Generate TestStartHop. A test case TestStartHop is to perform
the process of hopping the tested app where the window is in
the PLAY-like status to another device that is utilizing the audio
stream. With a tested app 𝑎and an audio-associated app 𝑎′, for
each ASSPLAY 𝑠in the ASTG of app 𝑎, we can get the following test
case, 𝐸𝑠:: 𝐸𝑎′ :: 𝑑1.StartHop(𝑎,𝑑2), where
• 𝐸𝑠is the event sequence that should be executed on device 𝑑1 to
let app 𝑎reach ASSPLAY 𝑠from the initial ASS 𝑠0.
• 𝐸𝑎′ is the event sequence that should be executed on device 𝑑2
to let app 𝑎′ reach an ASS whose status is PLAY from 𝑠0.
• 𝑑1.StartHop(𝑎,𝑑2) is the event that hopping the tested app 𝑎
from device 𝑑1 to 𝑑2.
Generate TestEndHop. A test case TestEndHop is to perform
the process of ending a hop of the tested app where a window is
in the PLAY-like status to another device that is utilizing the audio
stream. Generating the test case TestEndHop is more complicated
than TestStartHop, since before ending a hop, we need to construct
a hop between these two devices. Similarly, a test case TestEndHop
generated can be formally defined as 𝐸𝑠:: 𝐸𝑎′ :: EndHop, where
• 𝐸𝑠could be divided into three parts: (1) the event that starts app
𝑎on the device 𝑑1; (2) the StartHop event that transfers app 𝑎
from the device 𝑑1 to the device 𝑑2; (3) the event sequence should
be executed on device 𝑑2 to let app 𝑎reach ASSPLAY 𝑠from the
initial ASS 𝑠0.
• 𝐸𝑎′ is the event sequence that should be executed on device 𝑑1
to let app 𝑎′ reach an ASS which status is PLAY from 𝑠0.
• EndHop is the event that ending the hop of 𝑎between 𝑑1 and 𝑑2.
4.3.2
HAC-Directed Test Execution. After test generation, HAC-
Mony connects two devices 𝑑1 and 𝑑2 via HarmonyOS Device
Connector [27] (HDC) or Android Debug Bridge [18] (ADB) to
automatically execute the test cases for the target HarmonyOS
app. For general click events or the EndHop operation, HACMony
directly invokes the click command in HDC (or ADB) to execute
the event. Note that, the EndHop operation can also be regarded
as a click event. The StartHop operation could be regarded as a
sequence of events, HACMony needs to click the “Recent" button,
and then drag the current app to the target device. Finally, HAC-
Mony records the ASSs of the tested app 𝑎and the conflicting app
𝑎′.
4.3.3
HAC Issue Detection. After each test execution, HACMony
will analyze the recorded ASSs, and report how the hopping-related
audio-stream conflict between apps is resolved, i.e., the conflict
resolution. To detect the HAC issues, our key idea is that the conflict
resolutions that show up in the multiple-device scenario, i.e., the
“hopping" resolutions, should be consistent with the ones in the
single-device scenario, i.e., the “normal" resolutions. Thus, for each
target app 𝑎and its collaborating app 𝑎′ in app-hopping testing,
for each ASS 𝑠= ⟨𝑤𝑖𝑛, PLAY⟩(resp. 𝑠′ = ⟨𝑤𝑖𝑛′, PLAY⟩) in the
ASTG, we perform the following operations to obtain the “normal"
resolutions:
(1) Start app 𝑎on the device, and execute it to the ASS 𝑠;
(2) Start app 𝑎′ on the device, and execute it to the ASS 𝑠′;
(3) Obtain the current ASSs for app 𝑎and 𝑎′.
We compare the “normal" resolutions with the “hopping" resolu-
tions obtained by HACMony’s test execution. If there is any incon-
sistency, a HAC issue will be reported.
5
Evaluation
To evaluate the effectiveness of our approach, we raise several
research questions as follows:
• RQ1 (ASTG Construction) Is the ASTG construction process
effective and efficient?
• RQ2 (HAC Issue Detection) To what extent can HACMony
detect real-world HAC issues?
• RQ3 (HAC Issue Analysis) What are the categories and char-
acteristics of the detected HAC issues?
5.1
Evaluation Setup
To answer these research questions, we collect 20 real-world Har-
monyOS apps from Huawei AppGallery [28]. More specifically, we
take four categories associated with audio, i.e., Music, Video, Navi-
gation, and Social, into account, which are respectively have the
highest possibility of using the audio stream type MUSIC, MOVIE,
NAVIG, and COMMU. For each type, we download its top five apps
that support app-hopping as well as available for both phone and
tablet versions. Table 4 lists the detailed information of these ex-
perimental apps. All of the following experiments are done on a
phone HUAWEI P40 Pro and a tablet HUAWEI Matepad, both with
HarmonyOS 4.2.
5.2
RQ1: ASTG Construction
Table 4 shows the results of the ASTG model of each experimental
app constructed by HACMony. The fifth column gives the number
of audio-stream types that are analyzed by LLM (#Audio-Type).
The sixth and seventh columns give the statistics of the ASS: the
number of ASSs that are detected by exploration (#ASS-Init), and
the number of the extra ASSs (#ASS-Extra) extracted by collabo-
rating with multiple apps. Besides, the number of total ASSs, the
edges in the model, and the dynamical exploration time are shown
in the last three columns.
As we can see, HACMony can successfully explore all apps with
an average of 1.4 audio-stream types and 6.1 ASSs in an average of
72 seconds. Additionally, 7 (35%) apps with Music or Social category
have discovered 2 audio-stream types, and the types of these apps
additionally found are all MOVIE type. Among all categories, the
Navigation apps require more exploration time, which typically
explore around 4 ASSs (GUI windows). This is because Navigation
app usually involves complex events such as selecting a destina-
tion and means of transportation before starting navigation. This
observation also demonstrates the effectiveness of the LLM-based
exploration approach. Furthermore, the number of the extra ASSs


---

Page 9

---

HACMony: Automatically Detecting Hopping-related Audio-stream Conflict Issues on HarmonyOS
Conference’17, July 2017, Washington, DC, USA
Table 4: Experimental Apps and Model Size
App name
Categories
Size(MB)
Version
#Audio-Type
#ASS-
Init
#ASS-
Extra
#ASS
#Edge
Time(s)
Kugou Music
Music
156.6
12.4.2
2
4
4
8
7
95
QQ Music
Music
188.7
13.9.0.8
2
5
4
9
8
121
Kuwo Music
Music
181.4
11.0.0.0
2
4
4
8
7
85
Fanqie
Music
71.5
7.41.18
1
2
2
4
3
27
Kuaiyin
Music
75.8
5.57.11
1
2
2
4
3
25
Tencent Video
Video
145.9
8.11.71
1
2
2
4
3
40
Xigua Video
Video
65.6
8.8.6
1
1
2
3
2
22
Youku Video
Video
123.5
11.0.99
1
2
2
4
3
38
Mangguo TV
Video
133.2
8.13.0
1
2
2
4
3
41
HaoKan Video
Video
49.5
7.64.0.10
1
2
2
4
3
22
AMap
Navigation
254.9
15.01.0
1
4
1
5
4
135
Baidu Map
Navigation
171.5
20.7.30
1
4
1
5
4
59
Tencent Map
Navigation
162
10.11.1
1
4
1
5
4
62
Petal Maps
Navigation
83.9
4.5.0.303
1
5
1
6
5
74
Beidouniu
Navigation
59.1
3.3.1
1
4
1
5
4
61
Douyin
Social
271.9
31.4.0
2
6
3
9
8
106
Soul
Social
158.5
5.40.0
2
7
3
10
9
120
Xiaohongshu
Social
164
8.52.0
2
7
3
10
9
192
Zhihu
Social
87.8
10.22.0
1
3
2
5
4
53
Momo
Social
127
9.13.10
2
6
3
9
8
107
Avg./Max.
-
136.6/271.9
-
1.4/2
3.8/7
2.3/4
6.1/10
5.1/9
72/192
extracted by the ASS-guided enhancement is twice the number of
the audio-stream types in all apps with the Music or Video cat-
egories, indicating that these apps all discovered the PLAY↓and
PLAY∥statuses during the enhancement process.
5.3
RQ2: HAC Issue Detection
Table 5 displays information of the real-world HAC issues detected
by HACMony. Columns #Test Cases and Avg. L show the num-
ber of test cases and their average length. Columns #HAC and
#Unq. HAC show the number of the total and unique HAC issues
detected. And the column Time shows the time of testing.
In total, with the ASTG model, HACMony generates an average
of 137 test cases for each app, with an average length of 6.1 events.
There are 12 out of 20 (60%) apps detected to have HAC issues,
which involve a total of 18 unique HAC issues out of 53 HAC issues.
This indicates that HAC issues are relatively likely to occur during
the HarmonyOS app-hopping. The video demonstrations of HAC
issues found by HACMony can be viewed [21].
Recall that during the exploration phase, we leverage large mod-
els to explore multiple audio-stream types (MT) within apps, while
in the enhancement phase, we utilize other apps to explore mul-
tiple audio-stream statues (MS), e.g., PLAY↓and PLAY∥, with the
aim of discovering as many PLAY-like ASSs as possible to detect
more HAC issues. To validate the effectiveness of MT and MS in
our approach, we conducted additional experiments, as shown in
Table 6. The second to fifth columns shows the number of HAC
issues and unique HAC issues of each configuration, specifically,
• The Base column represents the baseline configuration without
using either MS or MT.
• The MT column denotes the configuration using only multi
audio-type (without MS).
• The MS column denotes the configuration using only multi audio-
status (without MT).
• The MT+MS column represents the full configuration that com-
bines both MS and MT.
The results demonstrate that the full configuration (MT+MS) outper-
forms all other configurations, with a 35.9% increase in detection of
the HAC issues and a 12.5% increase in detection of the unique HAC
issues compared to the baseline. Individually, MT and MS improve
the detection of the HAC issues by 25.6% and 7.7% over the baseline,
respectively, but show limited improvement in the detection of the
unique HAC issues (only one new unique HAC issue each). This
reflects that both the MT- and MS-aware exploration are important
in achieving comprehensive HAC issues detecting. Testers should
focus their efforts on generating test cases for different audio-types
and audio-statuses to detect HAC issues.
5.4
RQ3: HAC Issue Analysis
To assist both the developer of Harmony apps and OS better un-
derstanding the real-world HAC issues. We category issues and
perform case studies to investigate their characteristics.
First, we summarize the specific behaviors of the apps where
HAC issues occur and category issues into two types, Misuse of
Device (MoD) and Misuse of Resolution (MoR). MoD issue
refers to the situation where, during the hopping of an app, the
usage of the audio streams fails to be transferred to the target device
along with the app. The MoR issue refers to the situation where,
during the hopping of an app, an audio-stream conflict occurs on


---

Page 10

---

Conference’17, July 2017, Washington, DC, USA
He et al.
Table 5: Detected HAC Issues by HACMony
App name
#Test
Cases
Avg. L
#HAC
#Unq.
HAC
Time(s)
Kugou Music
228
5.7
0
0
2891
QQ Music
228
6.7
3
1
3402
Kuwo Music
228
6.2
5
1
3202
Fanqie
114
5.2
0
0
1407
Kuaiyin
114
6.2
0
0
3221
Tencent Video
114
5.2
5
2
1337
Xigua Video
114
6.2
0
0
1634
Youku Video
114
5.2
5
1
1367
Mangguo TV
114
5.4
0
0
1417
HaoKan Video
114
5.2
4
1
2793
AMap
76
7.3
7
3
1241
Baidu Map
76
7.3
5
2
1375
Tencent Map
76
8.4
2
2
1187
Petal Maps
76
7.3
5
2
1793
Beidouniu
76
7.1
3
1
1857
Douyin
190
5.6
0
0
1450
Soul
190
5.4
0
0
1415
Xiaohongshu
190
5.4
3
1
1453
Zhihu
114
5.4
0
0
1417
Momo
190
6.2
5
1
1572
Avg.
137
6.1
2.7
0.9
1872
Table 6: Impact of Multi Audio-Type (MT) and Multi Audio-
Status (MS) on HAC Detection
App name
#HAC (Unq.)
Base
MT
MS
MT+MS
QQ Music
2 (1)
2 (1)
3 (1)
3 (1)
Kuwo Music
5 (1)
5 (1)
5 (1)
5 (1)
Tencent Video
3 (1)
3 (1)
5 (2)
5 (2)
Youku Video
5 (1)
5 (1)
5 (1)
5 (1)
HaoKan Video
4 (1)
4 (1)
4 (1)
4 (1)
AMap
4 (3)
7 (3)
4 (3)
7 (3)
Baidu Map
3 (2)
5 (2)
3 (2)
5 (2)
Tencent Map
2 (2)
2 (2)
2 (2)
2 (2)
Petal Maps
3 (2)
5 (2)
3 (2)
5 (2)
Beidouniu
3 (1)
3 (1)
3 (1)
3 (1)
Xiaohongshu
0 (0)
3 (1)
0 (0)
3 (1)
Momo
5 (1)
5 (1)
5 (1)
5 (1)
Sum.
39 (16)
49 (17)
42 (17)
53 (18)
the target device, but the “normal" resolution to solve the conflict
is not applied. In our experiments, HACMony detected four apps
with MoD issues and nine apps with MoR issues.
Then, we count the number of HAC issues of different app cate-
gories. As shown in Figure 6(a), the MoD issues are more likely to oc-
cur in the Video applications, while the MoR issues are more likely
to occur in the Navigation applications. Furthermore, we count the
number of HAC issues of different types of test cases. As shown in
Figure 6(b), all the MoD issues are detected through the test cases
in the form of TestStartHop, and few (26%) MoR issues are detected
through the test cases in the form of TestEndHop. Although most
of the HAC issues are detected through the TestStartHop test cases,
there are still some issues identified by the TestEndHop test cases,
this indicates that it is necessary to consider different operations
when generating test cases (See Section 4.3.1). Therefore, Naviga-
tion apps trigger more HAC issues than all other types. They suffer
severe MoR issues, especially in the process of StartHop operation.
Besides, Video apps are easier to trigger MoD issues. Testers and
developers can perform testing/developing according to the type of
the target app.
1
2
9
1
1
2
1
1
0
1
2
3
4
5
6
7
8
9
10
Music
Movie
Navigation
Social
Number
Category
Unq. MoD Issues
Unq. MoR Issues
1
(a) Issue-related apps and unique issues
5
9
3
5
2
3
15
2
1
2
4
1
0
2
4
6
8
10
12
14
16
18
20
Music
Movie
Navigation
Social
Number
Category
MoD Issues of StartHop
MoD Issues of EndHop
MoR Issues of StartHop
MoR Issues of EndHop
1
(b) Issues triggered with different ops
Figure 6: Number of HAC Issues
To further study the characteristics of HAC issues, we analyze
the two types of HAC issues with case studies, respectively.
5.4.1
Misuse of Device: MoD issues. According to Finding 2, we
pick a Video app to investigate the characteristic of MoD issue.
Case study 1: MoD. When Youku Video [10] is playing a video
normally on the mobile phone, if the user hop it to the tablet, the
video continues to play on the tablet, but the audio is still playing on
the mobile phone. It leads to the audio-visual inconsistency problem
which makes it difficult for the users to focus on the video content
and affects users’ understanding and enjoyment of the video.
Analysis: We noticed that, the MoD issues may not occur in
all test cases of the same app, i.e., sometimes the issue do not occur.
Thus, we infer that such sporadic issues may be caused by the
lack of synchronization of commands and data between devices,
which prevents the new device from taking over audio playback in
a timely manner, so the audio playback on the original device does
not stop. Moreover, since the MoD issues are only detected though
the TestStartHop test cases, it indicates that the handling process
between StartHop operation and EndHop operation is different.
EndHop operation may force all resources related to the hopping
app in the target device to be transferred back to the original device.
5.4.2
Misuse of Resolution: MoR issues. As MoR issues involve
more statuses, we categorize them into three sub-types according


---

Page 11

---

HACMony: Automatically Detecting Hopping-related Audio-stream Conflict Issues on HarmonyOS
Conference’17, July 2017, Washington, DC, USA
to the status changes, namely PLAY↓→PLAY, PLAY↓→STOP, and
STOP→PLAY. The first (resp. second) issue refers to the situation
where the “hopping” resolution for solving audio-stream conflict
changes from lowering the volume to playing (resp. stopping) com-
pared to the “normal” one. The third issue refers to the situation
where the “hopping” resolution for solving audio-stream conflict
changes from stopping to playing. Table 7 shows the sub-types of
MoR issues HACMony have detected. Next, we pick two Navigation
apps and a Video app as the case study hopping apps to investigate
the characteristic of MoR issue.
Table 7: Sub-types of the App that Detected MoR Issues
App name
#PLAY↓→PLAY
#PLAY↓→STOP
#STOP→PLAY
QQ Music
★
Tencent Video
★
AMap
★
★
★
Baidu Map
★
★
Tencent Map
★
★
Petal Maps
★
★
Xiaohongshu
★
Case study 2: PLAY↓→PLAY type MoR. When Baidu Map [4]
is running on the mobile phone and navigating, the user hops it to
the tablet for further navigation, on which Kuaiyin [5] is playing
music. The expected behaviour is that Kuaiyin lower the volume.
However, in this situation, both Baidu Map and Kuaiyin play their
audio streams at normal volume on the tablet. As a result, it makes
difficult for users to clearly hear the navigation instructions or
information from Baidu Map, which brings inconvenience or safety
risks to their travels.
Case study 3: PLAY↓→STOP type MoR. When Petal Map [7] is
running on the mobile phone and navigating, the user hops it to
the tablet for further navigation, on which QQ Music [8] is playing
music. The expected behaviour is that QQ Music lower the volume.
However, QQ Music stops its audio stream. On the one hand, it ruins
the user’s immersive music-listening experience, where the sudden
interruption breaks the continuity of the music. On the other hand,
the unexpected stop of the music may force the user to interrupt
other ongoing operations to check and resume the music playback,
distracting the user’s attention from using Petal Map for navigation
or other tasks.
Case study 4: STOP→PLAY type MoR. When Tencent Video [9]
is playing the video on the mobile phone, the user hops it to the
tablet for further playing, on which Kugou Music is playing music.
The expected behaviour is that Kugou Music stops playing. How-
ever, both Tencent Video and Kugou Music play their audio streams
at normal volume on the tablet. As a result, users can’t clearly
distinguish the dialogue in the video from the music, leading to
extreme auditory discomfort and ruining the original audio-visual
enjoyment.
Analysis: After conducting all the experiments, we observed
that while Kuaiyin and Kugou Music exhibit MoR issues as the “pre”
apps in hopping, no HAC issues were detected when they served as
the “post” apps, i.e., the hopped apps. Although an STOP→PLAY
issue was detected in QQ Music as shown in Table 7, it occurred in
the audio-stream conflict with Kugou Music, not with Tencent Video.
This shows that MoR issues are generally asymmetric, meaning
that a change in the order of audio-stream conflict can influence
the occurrence of MoR issues. Thus, we infer that such asymmetric
MoR issues may be caused by the fact that apps using different
types of audio-streams adopt different priorities for handling audio-
stream conflict. This indicates that the MoR issues are related to
the resolution of conflicts between two apps, which are generally
asymmetric. Testers should not design test cases merely based on
the conventional symmetric assumption.
6
Discussion
This section primarily discusses the threats to the validity (including
limited generalizability due to restricted app sampling and version
dependency on HarmonyOS) and proposes future research direc-
tions (testing in multi-device scenarios, generating test cases with
complex hopping operations, and root-cause analysis combining
static analysis).
6.1
Threats to Validity
There are two main threats to the validity of our study.
⋆The representativeness of selected benchmarks can affect the
fidelity of our conclusions. To mitigate this threat, we have se-
lected 20 real-world apps from Huawei AppGallery, which are:
(1) Highly popular (Ranked within the top 5 in their respective
categories); (2) Diverse in categories (Specifically aligned with
audio-stream types, e.g., music players, video platforms, live
streaming apps); (3) Large-scale (An avarage of 136.6 MB size).
Future work could expand the app sample to include diverse cat-
egories and low-download apps, ensuring a more comprehensive
assessment of the approach’s robustness.
⋆The version of HarmonyOS, e.g., 3.1, 4.2, Next, etc., may affect
the semantics of app-hopping mechanism. Besides, the latest
HarmonyOS version currently faces challenges in experimental
validation due to limited device support and a scarcity of avail-
able apps, which restricts our ability to assess the framework’s
compatibility with emerging system architectures. To mitigate
this, we selected the version HarmonyOS 4.2, which is the most
widely used version of HarmonyOS up to now, as well as has a
large number of available HarmonyOS apps.
6.2
Directions for Further Research
According to the previous investigation, we will provide several
directions for further researches.
⋆Testing hopping behaviours by generating more complex
test cases. In this paper, the test cases designed are restricted to
incorporating only a single hopping operation. However, users
may frequently perform multiple consecutive hopping opera-
tions. To account for this real-world behavior, more complex
test cases should be generated in the future, aiming to more
comprehensively detect HAC issues.
⋆Combining static analysis technique to make in-depth root
cause analysis. In this paper, the cause of HAC issues are an-
alyzed solely based on their phenomena. However, to uncover
the root causes of issues, in-depth analysis of the application is
required using static analysis techniques to figure out the au-
dio stream related code patterns. Future research works could


---

Page 12

---

Conference’17, July 2017, Washington, DC, USA
He et al.
combine static analysis technique, e.g., data-flow, control-flow,
to analyze the root cause of HAC issues.
7
Related work
This section introduces the research works related to HarmonyOS
and model-based testing.
7.1
Analysis and Testing for HarmonyOS
Since HarmonyOS is an emerging system, there are few research
works of analysis and testing for it. Ma et al. [35] are the first to
provide an overview of HarmonyOS API evolution to measure the
scope of situations where compatibility issues might emerge in
the HarmonyOS ecosystem. Zhu et al. [44] propose the HM-SAF
framework, a cross-layer static analysis framework specifically
designed for HarmonyOS applications. The framework analyzes
HarmonyOS applications to identify potential malicious behaviors
in a stream and context-sensitive manner. Chen et al. [12] design
a framework ArkAnalyzer for OpenHarmony Apps. ArkAnalyzer
addresses a number of fundamental static analysis functions that
could be reused by developers to implement OpenHarmony app
analyzers focusing on statically resolving dedicated issues such
as performance bug detection, privacy leaks detection, compati-
bility issues detection, etc. These works are all static analyses of
HarmonyOS apps and do not focus on the ACs studied in this paper.
7.2
Model-Based Testing of GUI
Model-based testing (MBT) technique is commonly used in auto-
mated GUI testing for applications. Existing woks mainly extract
models through static analysis, dynamic analysis and hybrid analy-
sis. FSM [43] is the first to model the GUI behaviors of Android apps
using static analysis for MBT. WTG [42], an extension of FSM with
back stack and window transition information, is a relatively classic
model in MBT. Based on WTG, some models [14, 20, 23, 24, 36, 37]
which can be considered as a finer-grained WTG, are built by dy-
namic analysis. There are also some works [11, 15, 31, 40, 41] that
extend the WTG through a hybrid technique of static and dynamic
analysis. With the rise of large language models (LLMs), the GUI
exploration methods based on LLMs are capable of extracting the
WTG more quickly and accurately. This new approach leverages
the powerful language understanding and generation capabilities of
LLMs, which can effectively analyze the complex interactions and
transitions within the GUI [32–34]. However, the models proposed
in these works are almost used to describe the transitions of GUIs.
They do not take into account information related to audio streams,
nor do they consider the interactions among multiple applications.
These two factors are the key points that ASTG takes into account.
8
Conclusion
Hopping-related audio-stream conflict (HAC) issues are common
on the distributed operating system HarmonyOS. To test them au-
tomatically and efficiently, we design the Audio Service Transition
Graph (ASTG) model and propose a model-based testing approach.
To support it, we also present the first formal semantics of the
HarmonyOS’s app-hopping mechanism. The experimental results
show that, with the help of the formal semantics of the app-hopping
mechanism and the ASTG model, the HACMony can detect real-
world HAC issues effectively and efficiently. For the detected issues,
we also analyze their characteristics to help app and OS developers
improve apps’ quality on distributed mobile systems.
Acknowledgement
This project was partially funded by the Strategic Priority Re-
search Program of the Chinese Academy of Sciences (Grant No.
XDA0320102), National Natural Science Foundation of China (Grant
No. 62132020), and Major Project of ISCAS (ISCAS-ZD-202302).
References
[1] 2021. HarmonyOS Developer Issue. https://developer.huawei.com/consumer/cn/
forum/topic/0202700699545450014?fid=0101587866109860105.
[2] 2021. HarmonyOS Developer Issue. https://developer.huawei.com/consumer/cn/
forum/topic/0202646978991840491?fid=0101591351254000314.
[3] 2025. AMap. https://url.cloud.huawei.com/tXaf6tZ5sY.
[4] 2025. Baidu Map. https://url.cloud.huawei.com/tXQg34wJXy.
[5] 2025. Kuaiyin. https://url.cloud.huawei.com/u2T5hQKLjW.
[6] 2025. Kugou Music. https://url.cloud.huawei.com/tXafXtrfyM.
[7] 2025. Petal Map. https://url.cloud.huawei.com/tXRdtLucnu.
[8] 2025. QQ Music. https://url.cloud.huawei.com/tXRhftsDPW.
[9] 2025. Tencent Video. https://url.cloud.huawei.com/tXRhNDqDWo.
[10] 2025. Youku Video. https://url.cloud.huawei.com/tXLQZi7oZi.
[11] Tanzirul Azim and Iulian Neamtiu. 2013. Targeted and depth-first exploration
for systematic testing of android apps. In Proceedings of the 2013 ACM SIGPLAN
International Conference on Object Oriented Programming Systems Languages &
Applications, OOPSLA 2013, part of SPLASH 2013, Indianapolis, IN, USA, October
26-31, 2013, Antony L. Hosking, Patrick Th. Eugster, and Cristina V. Lopes (Eds.).
ACM, 641–660. https://doi.org/10.1145/2509136.2509549 https://doi.org/10.1145/
2509136.2509549.
[12] Haonan Chen, Daihang Chen, Yizhuo Yang, Lingyun Xu, Liang Gao, Mingyi Zhou,
Chunming Hu, and Li Li. 2025. ArkAnalyzer: The Static Analysis Framework for
OpenHarmony. arXiv:2501.05798 [cs.SE] https://arxiv.org/abs/2501.05798.
[13] Haibo Chen, Xie Miao, Ning Jia, Nan Wang, Yu Li, Nian Liu, Yutao Liu, Fei Wang,
Qiang Huang, Kun Li, Hongyang Yang, Hui Wang, Jie Yin, Yu Peng, and Fengwei
Xu. 2024. Microkernel Goes General: Performance and Compatibility in the
HongMeng Production Microkernel. In 18th USENIX Symposium on Operating
Systems Design and Implementation, OSDI 2024, Santa Clara, CA, USA, July 10-12,
2024, Ada Gavrilovska and Douglas B. Terry (Eds.). USENIX Association, 465–485.
https://www.usenix.org/conference/osdi24/presentation/chen-haibo.
[14] Taolue Chen, Jinlong He, Fu Song, Guozhen Wang, Zhilin Wu, and Jun Yan.
2018. Android Stack Machine. In Computer Aided Verification - 30th International
Conference, CAV 2018, Held as Part of the Federated Logic Conference, FloC 2018,
Oxford, UK, July 14-17, 2018, Proceedings, Part II (Lecture Notes in Computer Science,
Vol. 10982), Hana Chockler and Georg Weissenbacher (Eds.). Springer, 487–504.
https://doi.org/10.1007/978-3-319-96142-2_29 https://doi.org/10.1007/978-3-319-
96142-2_29.
[15] Zhuo Chen, Jie Liu, Yubo Hu, Lei Wu, Yajin Zhou, Yiling He, Xianhao Liao,
Ke Wang, Jinku Li, and Zhan Qin. 2023. DeUEDroid: Detecting Underground
Economy Apps Based on UTG Similarity. In Proceedings of the 32nd ACM SIGSOFT
International Symposium on Software Testing and Analysis, ISSTA 2023, Seattle,
WA, USA, July 17-21, 2023, René Just and Gordon Fraser (Eds.). ACM, 223–235.
https://doi.org/10.1145/3597926.3598051 https://doi.org/10.1145/3597926.3598051.
[16] Huawei Community. 2024. Huawei’s HarmonyOS Gains Market Share. https:
//consumer.huawei.com/en/community/details/topicId-225051/.
[17] OpenAtom Foundation. 2025.
OpenHarmony Project.
https://gitee.com/
openharmony/docs/blob/master/en/OpenHarmony-Overview.md.
[18] Google. 2024. Android Debug Bridge (adb). https://developer.android.com/tools/
adb.
[19] Google. 2025. Android Open Source Project. https://source.android.com/.
[20] Tianxiao Gu, Chengnian Sun, Xiaoxing Ma, Chun Cao, Chang Xu, Yuan Yao,
Qirun Zhang, Jian Lu, and Zhendong Su. 2019. Practical GUI testing of Android
applications via model abstraction and refinement. In Proceedings of the 41st
International Conference on Software Engineering, ICSE 2019, Montreal, QC, Canada,
May 25-31, 2019, Joanne M. Atlee, Tevfik Bultan, and Jon Whittle (Eds.). IEEE /
ACM, 269–280. https://doi.org/10.1109/ICSE.2019.00042 https://doi.org/10.1109/
ICSE.2019.00042.
[21] HACMony. 2025. HAC Issues Detected by HACMony. https://www.youtube.
com/playlist?list=PL9InyCjzL53mWIbPP5ixylr7Qwd-kzUTa.
[22] HACMony. 2025. Operational Semantics of App-Hopping Mechanism on Har-
monyOS. https://github.com/SQUARE-RG/hacmony/blob/main/Semantics_of_
HarmonyOS_App_Hopping.pdf.


---

Page 13

---

HACMony: Automatically Detecting Hopping-related Audio-stream Conflict Issues on HarmonyOS
Conference’17, July 2017, Washington, DC, USA
[23] Jinlong He, Taolue Chen, Ping Wang, Zhilin Wu, and Jun Yan. 2019. Android
Multitasking Mechanism: Formal Semantics and Static Analysis of Apps. In
Programming Languages and Systems - 17th Asian Symposium, APLAS 2019, Nusa
Dua, Bali, Indonesia, December 1-4, 2019, Proceedings (Lecture Notes in Computer
Science, Vol. 11893), Anthony Widjaja Lin (Ed.). Springer, 291–312. https://doi.org/
10.1007/978-3-030-34175-6_15 https://doi.org/10.1007/978-3-030-34175-6_15.
[24] Jinlong He, Zhilin Wu, and Taolue Chen. 2024. Formalization of Android Activity-
Fragment Multitasking Mechanism and Static Analysis of Mobile Apps. Form.
Asp. Comput. (Dec. 2024).
https://doi.org/10.1145/3708562 https://doi.org/10.
1145/3708562.
[25] Huawei. 2024. Hopping Overview. https://developer.huawei.com/consumer/en/
doc/design-guides-V1/service-hop-overview-0000001089296748-V1.
[26] Huawei. 2025. About HarmonyOS. https://developer.huawei.com/consumer/en/
doc/harmonyos-guides-V3/harmonyos-overview-0000000000011903-V3.
[27] Huawei. 2025. hdc. https://developer.huawei.com/consumer/en/doc/harmonyos-
guides-V5/hdc-V5.
[28] Huawei. 2025.
Huawei Appgallery.
https://consumer.huawei.com/en/
mobileservices/appgallery/.
[29] Huawei. 2025.
Processing Audio Interruption Events.
https:
//developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/audio-
playback-concurrency-V5.
[30] Huawei. 2025. StreamUsage. https://developer.huawei.com/consumer/en/doc/
harmonyos-references-V13/js-apis-audio-V13#streamusage.
[31] Changlin Liu, Hanlin Wang, Tianming Liu, Diandian Gu, Yun Ma, Haoyu Wang,
and Xusheng Xiao. 2022. PROMAL: Precise Window Transition Graphs for An-
droid via Synergy of Program Analysis and Machine Learning. In 44th IEEE/ACM
44th International Conference on Software Engineering, ICSE 2022, Pittsburgh, PA,
USA, May 25-27, 2022. ACM, 1755–1767. https://doi.org/10.1145/3510003.3510037
https://doi.org/10.1145/3510003.3510037.
[32] Zhe Liu, Chunyang Chen, Junjie Wang, Mengzhuo Chen, Boyu Wu, Xing Che,
Dandan Wang, and Qing Wang. 2024. Make LLM a Testing Expert: Bringing
Human-like Interaction to Mobile GUI Testing via Functionality-aware Deci-
sions. In Proceedings of the 46th IEEE/ACM International Conference on Software
Engineering, ICSE 2024, Lisbon, Portugal, April 14-20, 2024. ACM, 100:1–100:13.
https://doi.org/10.1145/3597503.3639180 https://doi.org/10.1145/3597503.3639180.
[33] Zhe Liu, Chunyang Chen, Junjie Wang, Mengzhuo Chen, Boyu Wu, Yuekai Huang,
Jun Hu, and Qing Wang. 2024. Unblind Text Inputs: Predicting Hint-text of Text
Input in Mobile Apps via LLM. In Proceedings of the CHI Conference on Human
Factors in Computing Systems, CHI 2024, Honolulu, HI, USA, May 11-16, 2024,
Florian ’Floyd’ Mueller, Penny Kyburz, Julie R. Williamson, Corina Sas, Max L.
Wilson, Phoebe O. Toups Dugas, and Irina Shklovski (Eds.). ACM, 51:1–51:20.
https://doi.org/10.1145/3613904.3642939 https://doi.org/10.1145/3613904.3642939.
[34] Zhe Liu, Chunyang Chen, Junjie Wang, Mengzhuo Chen, Boyu Wu, Yuekai
Huang, Jun Hu, and Qing Wang. 2024. Unblind Text Inputs: Predicting Hint-text
of Text Input in Mobile Apps via LLM. CoRR abs/2404.02706 (2024).
https:
//doi.org/10.48550/ARXIV.2404.02706 arXiv:2404.02706 https://doi.org/10.48550/
arXiv.2404.02706.
[35] Tianzhi Ma, Yanjie Zhao, Li Li, and Liang Liu. 2023. CiD4HMOS: A Solution to
HarmonyOS Compatibility Issues. In 38th IEEE/ACM International Conference
on Automated Software Engineering, ASE 2023, Luxembourg, September 11-15,
2023. IEEE, 2006–2017.
https://doi.org/10.1109/ASE56229.2023.00134 https:
//doi.org/10.1109/ASE56229.2023.00134.
[36] Yun Ma, Yangyang Huang, Ziniu Hu, Xusheng Xiao, and Xuanzhe Liu. 2019.
Paladin: Automated Generation of Reproducible Test Cases for Android Apps. In
Proceedings of the 20th International Workshop on Mobile Computing Systems and
Applications, HotMobile 2019, Santa Cruz, CA, USA, February 27-28, 2019, Alec
Wolman and Lin Zhong (Eds.). ACM, 99–104. https://doi.org/10.1145/3301293.
3302363 https://doi.org/10.1145/3301293.3302363.
[37] Ting Su, Guozhu Meng, Yuting Chen, Ke Wu, Weiming Yang, Yao Yao, Geguang
Pu, Yang Liu, and Zhendong Su. 2017. Guided, stochastic model-based GUI testing
of Android apps. In Proceedings of the 2017 11th Joint Meeting on Foundations of
Software Engineering, ESEC/FSE 2017, Paderborn, Germany, September 4-8, 2017,
Eric Bodden, Wilhelm Schäfer, Arie van Deursen, and Andrea Zisman (Eds.).
ACM, 245–256. https://doi.org/10.1145/3106237.3106298 https://doi.org/10.1145/
3106237.3106298.
[38] Global Times. 2024. China’s first fully home-grown mobile operating system
HarmonyOS NEXT launched. https://www.globaltimes.cn/page/202410/1321670.
shtml.
[39] Tianyong Wu, Xi Deng, Jun Yan, and Jian Zhang. 2019. Analyses for specific
defects in android applications: a survey. Frontiers Comput. Sci. 13, 6 (2019), 1210–
1227. https://doi.org/10.1007/S11704-018-7008-1 https://doi.org/10.1007/s11704-
018-7008-1.
[40] Jiwei Yan, Hao Liu, Linjie Pan, Jun Yan, Jian Zhang, and Bin Liang. 2020.
Multiple-entry testing of Android applications by constructing activity launch-
ing contexts. In ICSE ’20: 42nd International Conference on Software Engineer-
ing, Seoul, South Korea, 27 June - 19 July, 2020, Gregg Rothermel and Doo-
Hwan Bae (Eds.). ACM, 457–468.
https://doi.org/10.1145/3377811.3380347
https://doi.org/10.1145/3377811.3380347.
[41] Jiwei Yan, Tianyong Wu, Jun Yan, and Jian Zhang. 2017. Widget-Sensitive
and Back-Stack-Aware GUI Exploration for Testing Android Apps. In 2017 IEEE
International Conference on Software Quality, Reliability and Security, QRS 2017,
Prague, Czech Republic, July 25-29, 2017. IEEE, 42–53. https://doi.org/10.1109/
QRS.2017.14 https://doi.org/10.1109/QRS.2017.14.
[42] Shengqian Yang, Hailong Zhang, Haowei Wu, Yan Wang, Dacong Yan, and
Atanas Rountev. 2015. Static Window Transition Graphs for Android (T). In
30th IEEE/ACM International Conference on Automated Software Engineering, ASE
2015, Lincoln, NE, USA, November 9-13, 2015, Myra B. Cohen, Lars Grunske, and
Michael Whalen (Eds.). IEEE Computer Society, 658–668.
https://doi.org/10.
1109/ASE.2015.76 https://doi.org/10.1109/ASE.2015.76.
[43] Wei Yang, Mukul R. Prasad, and Tao Xie. 2013. A Grey-Box Approach for Auto-
mated GUI-Model Generation of Mobile Applications. In Fundamental Approaches
to Software Engineering - 16th International Conference, FASE 2013, Held as Part
of the European Joint Conferences on Theory and Practice of Software, ETAPS
2013, Rome, Italy, March 16-24, 2013. Proceedings (Lecture Notes in Computer Sci-
ence, Vol. 7793), Vittorio Cortellessa and Dániel Varró (Eds.). Springer, 250–265.
https://doi.org/10.1007/978-3-642-37057-1_19 https://doi.org/10.1007/978-3-642-
37057-1_19.
[44] Yukun Zhu, JiChao Guo, FengHua Xu, RuiDong Chen, XiaoSong Zhang, Shen
Yi, and Jia Yu. 2023. HM-SAF: Cross-Layer Static Analysis Framework For
HarmonyOS. In 2023 IEEE Smart World Congress (SWC). 1–10. 10.1109/SWC57546.
2023.10449022.
