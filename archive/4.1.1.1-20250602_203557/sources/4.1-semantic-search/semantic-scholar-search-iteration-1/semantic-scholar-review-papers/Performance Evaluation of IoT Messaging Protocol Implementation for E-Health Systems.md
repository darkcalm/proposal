

---

Page 1

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
412 | P a g e  
www.ijacsa.thesai.org 
Performance Evaluation of IoT Messaging Protocol 
Implementation for E-Health Systems 
M. Zorkany1 
National Telecommunication 
Institute (NTI) 
Cairo, Egypt 
K.Fahmy2 
Department of Electrical Engineering 
Al-Azhar University, Nasr City 
Cairo, Egypt 
Ahmed Yahya3 
Department of Electrical Engineering 
Al-Azhar University 
Cairo, Egypt 
 
 
Abstract—Now-a-days, e-health and healthcare applications 
in the internet of things are growing rapidly. These applications 
are starting from remote monitoring of patient's parameters in 
home to monitoring patients during his life activities at work, 
transportation, etc. So we can monitor patients at any place 
outside of hospitals and clinical settings. By using this technology, 
we can save lives and reduce the number of emergency visits to 
hospitals. In contemporary time, there are great progress and 
opportunities for the internet of things (IoT) related E-health 
systems. Most IoT e-health platforms consist of three main parts; 
client nodes (patient or doctor), IoT server and IoT 
communication messaging protocol. One of E-health systems 
design over IoT challenge is choosing the most suitable IoT 
messaging protocol for E-health applications. In this paper, IoT 
remote patient and e-Health monitoring system was designed for 
monitoring physiological medical signals of patients based on 
most two famous IoT messaging protocols, MQTT and CoAP. 
These medical signals can be include parameters like heart rate 
signals, electro-cardio graph (ECG), patient temperature, blood 
pressure, etc. This practical comparison between CoAP and 
MQTT is to choose most suitable for e-health systems.  The 
proposed approach was evaluated based on most significant 
protocol parameters like capability, efficiency, communication 
method and message delay. Practical and simulation results show 
the performance of the proposed E-health systems over IoT for 
different 
network 
infrastructure 
with 
different 
losses 
percentages. 
Keywords—E-health; IoT; IoT protocol; CoAP; MQTT and 
remote patient monitoring 
I. 
INTRODUCTION 
IoT (Internet of Things) is an extension of the current 
internet by connecting millions of devices (things) together 
nevertheless the location of each thing. So IoT is a network 
between devices or things through any internet connection 
method (wire, wireless, WiFi, GPRS, 3G, etc). IoT 
applications grow in many applications like transportations, 
medical, shopping, smart home, smart cities etc. To build 
internet of thing platform for any application we need internet 
connections between clients and communication protocol to 
manage these connections through IoT server. 
Nowadays the market of IoT in medical applications espial 
for e-health is growing rapidly ranging from medical smart 
sensors and remote patient monitoring to remote traceability 
and diagnosis of patients. The main objective of e-health over 
IoT is improving the health of patients through better disease 
management and self-help facilities. 
IoT e-health systems can be classified as an Internet of 
Medical Things (IoMT). IoMT is a medical sensors and 
applications connected through IoT network. Also IoMT can 
be use Web Services, to captured patient data and analyzed it. 
The general architecture of e-health system [1] shown in 
Fig. 1 which consists of three main phases: Phase 1 
monitoring the patient to acquire data from medical sensors, 
then this data is gathered and transferred through the internet 
to the application server or clients for data analysis, 
monitoring and investigation in third phase. Also some of data 
processing can be accomplished at patient side and send the 
results to doctor's side directly. 
IoT platform has three main parts: clients, IoT server and 
IoT message protocols. As shown in Fig. 2 E-health 
monitoring system architecture [2] divided into three layers: 
sensing layer. It is a collection of medical sensors. server 
layers It links between the sensing layer "patient" and 
receiving data layer "hospital". Receiving data layer is the 
layer through which patient data are received. In this article, 
rely on the server layer to choose protocol most suitable for 
the electronic health system. 
The messaging protocol is considered the main element in 
the Internet of things. These protocols play a big role to enable 
IoT all over life. One of E-health systems design over IoT is to 
choose the type of IoT messaging protocol. In the Internet of 
things the main factor is the incorporation of many 
technologies, due to the fast growth of the Internet of things 
information sharing has been sophisticated across systems 
where the internet is converted into a comprehensive future 
[3]. Internet of things has a great ability to grow and the main 
engine of this growth is the protocol [4]. So using dedicated 
protocols to the internet of things will increase the efficiency 
and ease of data transfer certified on the environment used. In 
recent years, health care applications have received a lot of 
attention, making researchers discuss the whole structure of 
the healthcare system through IoT and applicability [5]. 
The electronic health system has maintenance medical 
devices, way of managing hospitals and Patients were allowed 
arrival to medical care all hospitals in the world. Many 
hospitals have implemented an electronic health system to 
solve the problems of shortage of doctors, reduce costs for 
patients and increase efficiency [6]. The electronic health 
system aims to progress the health aspect where it monitors 
the organs of the human body and its vital functions, which 
helps to decrease the mortality rate. In the future, health care 


---

Page 2

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
413 | P a g e  
www.ijacsa.thesai.org 
applications across IoT will have a great effectiveness the 
state economy [7]. 
At this time, there is a lot of messaging protocols for IoT, 
some of which are distinguished according to a need for them. 
IoT protocol is divided into: TCP/IP protocol Such as: MQTT, 
SMQTT, AMQP and UDP protocol Such as: CoAP, SNMP, 
SSI. [8] Internet of things has major importance in electronic 
health so it was thought to this part of the application for the 
Internet of things to develop a Special Protocol for E-health to 
increase efficiency and care for patient cases in this paper, 
each protocol will be expounded separately to choose the most 
suitable protocol for health care system.  There shall be a 
practical Comparison amongst the most renowned protocols it 
"MQTT, CoAP". This comparison will be based on the 
Special process components of each protocol. 
In this research, e-health IoT platform will be implemented 
depending on most two famous IoT protocols MQTT (ex. 
TCP) and CoAP (ex. UDP). This practical comparison 
between CoAP and MQTT is to choose the protocol most 
suitable for e-health systems.  The proposed approach was 
evaluated based on most important internet parameters like 
capability, efficiency and message delay. Practical results 
show a performance of E-health systems over it in different 
network infrastructure with different losses percentages. This 
comparison was presented to illustrate the integrity and health 
information towards the protocol most suitable for electronic 
health. 
 
Fig. 1. General Architecture of e-Health System. 
 
Fig. 2. e-Health Monitoring System Architecture. 
This paper is regular as follows: Section 2 presents related 
of work IoT protocol. Section 3 discusses the famous IoT 
protocols. Then, Section 4 Proposed criteria for selecting the 
most protocol appropriate for the E-health application, in 
Section 5 set up scenario and practical results, the concludes 
of this research will be discussed in Section 6. 
II. RELATED WORK 
Most e-health over IoT studies and researches in remote 
monitoring of patients although quite complete but are used 
for individual problems like as ECG or heart rate monitoring. 
Some studies developed for special features as develop 
prototypes for electrocardiography integrated with smart 
phone [9]. In recent years, many researches applied internet of 
things in many e-health applications. To develop these 
applications over IoT they used standard IoT protocols. For 
example, R.N. Kirtana, Y.V. Lokeswari in Paper [10] 
developed Heart Rate Variability (HRV) system to remote 
heart rate monitoring over IoT using MQTT protocol. But this 
system developed to monitoring one medical signal (heart 
rate) only. Antoine Jamin et al. in paper [11] presented an in-
home aggregation IoT platform to monitoring more than one 
medical 
parameters 
(physiological 
and 
thermometer 
parameters). They used standard IoT protocol to implement 
their platform. So they send one message per parameter 
because MQTT is single topic protocol.  In this case if patient 
has more than one emergency parameter in the same time, 
they must send one parameter in one MQTT message, and 
then transmit next parameter in other MQTT message. Which 
cause a delay in some message and occupy more internet 
bandwidth. 
Kaleem Ullah et al. in paper [12] proposed framework for 
e-Health which used smart phone sensors with body sensors to 
monitor patient health. They used different protocol as HTTP 
and HTTPS. But they didn't use most famous IoT protocols 
like MQTT or CoAP. M. Hussein et al. developed IoT 
protocol based on proposed multi-topic IoT protocol which 
can send multi parameters in one message to overcome delay 
of multi messages and save the bandwidth [13]. Also, several 
researchers shared their efforts to develop the health care 
framework across IoT for example: P. Thota and Y. Kim 
compared the famous IoT Protocols MQTT and CoAP based 
on Raspberry-Pi and a temperature sensor [14]. The Pros and 
Cons of each of them in terms of the power consumption and 
data, flows from one node to multiple nodes, safely. CoAP 
more functional in terms of the energy, while the MQTT more 
suitable when data flows from a client to multiple nodes, but 
this consists of only two factors and neglect other factors. 
K. Natarajan et al. used Raspberry Pi in E-health over IoT 
to collect patient data through the sensors, store it and send to 
the doctor [15]. Raspberry Pi is capable to collect diverse 
information from the patient through sensors. Mentioned how 
the data were collected but he did not talk about anything 
concerning the method of sending data over the protocol used 
in IoT. A. Al-Fuqaha et al. provide an overview about IoT, 
basic elements, tools and techniques needed from where 
communication technologies used in IoT like NFC, Z-WAVE, 
LTE-A, Bluetooth LE and RFIC [16]. In addition to the most 
renowned IoT messaging protocols as MQTT, CoAP XMPP, 
 
 


---

Page 3

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
414 | P a g e  
www.ijacsa.thesai.org 
AMQP. Description of different criteria for each protocol and 
explained the using of each of them in detail. Explained how 
to 
collect 
information 
by 
previous 
communication 
technologies and send off them through those protocols to 
achieve the goal of IoT. This paper didn't mention the 
challenges facing the protocols and the differences application 
between all these protocols. Also, they didn't run the protocols 
mentioned in real applications of the IoT, but mentioned in a 
theoretical way only. They didn't address the search of the best 
protocols from where energy and efficiency and the capacity 
to send data. It was necessary to mention the best protocol for 
each part of the different IoT. 
T. Takpor and A. Atayero talked about the dangerous 
matter of integrating E-Health and educational institutions 
across IoT to effectively monitor students' health [17]. 
Because health issues affect students' academic performance, 
so 
exhibited 
a 
technique 
'RFID' 
Radio 
Frequency 
Identification, and use it to know the medical data of students 
such as “blood”. 
There a lot of work on different directions for the 
achievement of that project from sensors used and accuracy 
and how to compile data and keep it and how to transmit data 
Through IoT protocols. In this article Show the effect of IoT 
on improving electronic health, clarifying the communication 
models and protocols used in IoT and health care 
implementation. Today can be applied mobile devices in 
monitoring patients and the elderly and identifying their health 
status. The problem is how to join these devices to the internet 
world while preserving the safety of information. It was 
necessary to have a look at a collection of IoT messaging 
protocols used to solve the problems and to apply the 
application to transmit data [18]. 
From the above survey, we find that most researches didn't 
talk about the best protocols that ability to use in E-health 
applications. In our research, we will do a comparison 
between most IoT famous protocols to select the most 
appropriate protocol for the healthcare system. In the next 
section, clarification the most renowned  IoT protocol will be 
discussed. 
III. IOT MESSAGE PROTOCOL 
IoT message protocols can be divided into TCP/IP and 
UDP protocol. The most popular TCP protocol is "MQTT" 
and one of the most renowned  UDP protocols is "CoAP". 
A. MQTT "Message Queue Telemetry Transport" 
It is a publish-subscribe messaging TCP/IP protocol. The 
messaging style "publish-subscribe" need to IoT server 
"broker". The publish send the message to the broker, the 
broker is accountable for classified messages to interested 
clients relying on the topic of a message as illustrated in the 
Fig. 3. It has many advantages as short massage, minimized 
data packets, faster response and throughput „Speed‟, low 
power usage and lower bandwidth, Other advantages built into 
the MQTT protocol are retained messages and multiple 
subscriptions „multiplexed‟ over one connection. many-to-
many communication protocol for crossing messages between 
multiple clients through the broker. 
 
Fig. 3. General MQTT Architecture. 
MQTT has featured it supports Quality of Service (QoS). 
The Quality of Service (QoS) is a method to secure the 
submission of the message between publisher and subscriber. 
There are three standards of Qualiy of Service (QoS), the 
standard of Quality of Service (QoS) is determined as in paper 
[19] within the scope of the research, it was found that there 
were some letters that showed official models of MQTT as 
well as how to pass messages and analyze them  a constant 
analysis based on indications in paper [20].  MQTT protocol 
has the ability to save the order between the messages by 
adding the mark of the request and SEO which determines 
whether you want to keep the order between the messages or 
not. 
B. CoAP "Constrained Application Protocol" 
It is a "Request/ Response" protocol, it is used as an 
alternative to http in hardware-constrained devices to be 
simple to use with these devices so it is used in IoT. The 
CoAP provides four different types of messages: 
 The message type defines four different method: 
CON Message: refers to the “Confirmable” request. When 
a source node transmits a CON request, the recipient has to 
respond with ACK message. 
NON Message: refers to “Non-Confirmable” request that 
when a source node transmits a non-request, the recipient is 
not required to respond back. 
ACK Message: refer to “Acknowledgement” messages 
which are sent back as a response to a CON message. If 
processing successful, the recipient of the CON message 
should reply back with an ACK message. The ACK message 
can also contain the result of the processing time. 
RST Message: refer to “Reset” message this type of 
messages is sent back when the future of a message 
encounters an error, does not understand the message or is no 
longer interested in the message sender. 
 The message codes define one method: empty message. 
 Request codes define four different methods: 
(GET) This will retrieve the information from a specific 
resource specified by requested URI (POST) display 
information to be processed for a specific resource. The output 
result depends on the targeting resource, usually, results in the 
target resource that is created or updated. (PUT) requests that 
 


---

Page 4

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
415 | P a g e  
www.ijacsa.thesai.org 
resource particular by the URI be created with the carried 
information representation; (DELET) demand that the 
identified resource can be deleted. 
 Response codes define two different methods : 
Success message Contains four messages: CONTENT 
message response for GET message, CONTIUE message 
response for POST message, CREATED message response for 
PUT message, DELETED message response DELETED 
message. 
Client error message Contains different message: such as 
bad request, not found, method not allow. 
General CoAP architecture is exhibit in Fig. 4. 
 
Fig. 4. General CoAP Architecture. 
IV. PROPOSED PERFORMANCE EVALUATION CRITERIA FOR 
E_HEALTH OVER IOT 
The proposed e-health system is An automatic wireless 
health monitoring system which can be used to measure 
patient‟s parameters (like body temperature and heartbeat, 
etc.) by using embedded system technology with internet of 
things.  As shown in Fig. 5, The architecture of proposed 
system divides into five parts: Patient (sensor) node, IoT 
communication protocol, IoT server, application server and 
application node. 
The patient node unit is medical sensors, internet access, 
controller and power and surrounded circuits. Medical sensors 
used to acquire medical parameters from patients. Selection of 
medical sensors depend on two issues decisions: which 
required sensing parameters need monitored, and which 
sampling frequency needed to send theses parameters to 
doctors/Hospital or sending these parameters only when 
required or at abnormal conditions. In order to the patient 
node achieve the objectives of the system; the scope of the 
node is summarized as follow: 
Microcontroller system controls the operation of gathering 
the data from sensors and preparing it to be sent. It is 
integrated with some extra component to increase the 
functionality and execute at high frequency to improve the 
performance of the system so that the system is more reliable 
and efficient. Internet access like Wi-Fi or Bluetooth or 
GSM/GPRS/3G module used to transmit and receive data 
wirelessly in a long distance so the system is portable and easy 
to be operated. 
A. IoT Protocol Architecture 
In order that achieves better healthcare in the Internet of 
things, need to transfer data of patients accurately and 
effectively to remote servers. This paper proposed method to 
select the most convenient messaging protocol for the 
healthcare system. The architecture of the protocol system 
appropriate for electronic health depends on three layers, 
Client receiving data, Gateway / Translation Device 
"Protocols", Sensor data collection "sensing layer" as 
described in Fig. 6. 
The sensing layer consists of many medical sensors such 
as pressure measurement, temperature, heartbeat, ECG, blood 
glucose level and breathing rate. Each sensor measures its own 
patient data and sends it to the doctor through the server layer, 
in this class, the data enable be collected and rerouted. 
 
Fig. 5. Proposed IoT Patient Monitoring System. 
 
Fig. 6. The Proposed Methodology. 
 
 
 


---

Page 5

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
416 | P a g e  
www.ijacsa.thesai.org 
 
Fig. 7.  Remote Health Monitoring. 
In the server layer the focus is on communication 
protocols that authorize the reciprocation of information 
between devices, where the Internet of things is entered in 
many fields, whether industrial or health, where information 
exchange occurs between devices via cloud systems, the link 
in that is many communication protocols Which allow devices 
converse to each other and with the connection of millions of 
devices on the Internet, need for IoT protocols was very 
important such as MQTT, CoAP looking for whichever is 
more compatible for electronic health. 
In the receiving data layer the information is received by 
the doctor that was sent in the sensing layer where the 
information is processed and stored continuously, occur a 
quick reaction to the emergency and other treatment by the 
doctor. Fig. 7 shows these three stages. 
The first phase "The sensing layer" shows the patient's 
specific sensors and how to install it and measure the data. the 
second phase "server layer " describes how to transfer that 
patient-specific data that has been measured through the 
medical sensors via the IoT protocols. The third phase 
"receiving data layer" is the special phase in the hospital 
where the doctor receives the data of the patient was sent in 
the previous phase through special applications. Application 
"client" for each protocol to be the window to transmit data to 
patients Like MQTT FX data is then transferred to the public 
network to select most protocol convenient for transfer data. 
The researchers have made protocols IoT 'internet of things' to 
suit data transfer, enhance efficiency, safety, and energy 
consumption, as the devices used in electronic health often 
operate on batteries, the protocol should be suitable for energy 
saving and easy to use for the customer. 
B. Metrics of the Proposed Method 
The proposed comparison in this article based on three 
aspects metrics as follows: 
1) IoT Success Message "ISM": With this metric, the 
speed of sending messages is evaluated, this is because the 
messages that arrive directly are quicker than the messages 
that need to retransmitting due to loss in the network. This 
measure is the rate of the total number of messages sent from 
client to server without the occurrence of retransmitting it, and 
the gross number of messages sent whether it has to resend or 
not. pronounced in the equation. all message sent M(s) 
consists of: 
The successful message M(succ) from the first time and 
other message happen to be retransmitted  M(re). 
M(s) = M(succ) + M(re) 
 
 
 
         (1) 
    
                          
                                           
         (2) 
2) IoT Average Byte "IAB": With this metric, an medium 
number of bytes used in the message evaluated, because all 
protocol has its own format regardless of the tenor of the 
messages. This measurement is the rate of an average number 
of bytes used in messages sent from the client to the server 
without retransmit, and the medium number of bytes used in 
sent messages, whether resend it or not. 
    
                                    
                                                    
         (3) 
Pronounced in the equation. Packet contains a collection of 
byte it is a byte of payload B(p) and byte of 'fixed, variable' 
header B(h) specific protocol. 
B = B(p) + B(h)  
 
 
 
         (4) 
3) IoT Delay message "IDM": Message delay is evaluated 
in this metric, this is ratio of delay of messages sent from the 
client to the server without retransmission, and delay 
messages sent, whether resend it or not. This is because most 
important in E-health is the speed and size of the sending the 
message and the energy consumption add to the messages lost. 
Pronounced in the equation. 
Delay consists of transmission delay D(t), signal 
processing delay D(s) and queueing delay D(q). 
D = D(t) + D(s) +D(q) 
 
 
 
         (5) 
    
                             
                                             
         (6) 
As the speed of access to patient information to the doctor 
to follow the importance of medical, as well as the number of 
lost messages are a major risk in the diagnosis, the smaller the 
volume of messages sent the faster the access. Fig. 8 shows a 
comparison between most prominent IoT protocols MQTT, 
CoAP. The Patient-specific data "client1" will send to the 
specialist doctor "client2" through the server of the protocol 
used. 
It is distinguished by the MQTT it supports (QoS). The 
Quality of Service (QoS) is to secure the transmission of the 
message between publisher and the future exist three-phases 
of Quality of Service (QoS), the publisher determine the level 
of the service. 
QoS level 0: message sent from publisher to intermediary 
and no acknowledgment is sent to a publisher. This part has 
not been reviewed because it was working on a local network. 
QoS level 1: a message sent by the publisher to the 
intermediary and then the mediator sends an acknowledgment 
to the publisher again until the publisher ensures that do not 
miss the message, this means that transmission is guaranteed. 


---

Page 6

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
417 | P a g e  
www.ijacsa.thesai.org 
 
Fig. 8. The Actual Implementation. 
QoS level 2: The highest level of service, where there is a 
chain of four messages between publisher and mediator to 
confirm sending and confirm receipt. 
V. IMPLEMENTATION OF IOT PROTOCOL AND SET UP 
SCENARIO 
 A typical comparison between CoAP and MQTT and 
evaluated for appropriate selection, each client has a protocol 
and a private server. 
MQTT implementation: have "MQTT FX" as a client and 
"MOSQUITO" server. MQTT FX" CLIENT through which 
the message sent from publisher "patient" and received it by 
subscriber "Doctor"; subscriber and publisher related to the 
server with special IP. MOSQUITO" SERVER mosquito is an 
MQTT broker used for handling data between publisher and 
subscriber. Receives data from publisher and sends it to the 
subscriber certified the subject of the message. 
CoAP implementation:  have "COPPER" client and 
"LIBCoAP "server. "COPPER" CLIENT through which the 
message sent from the patient to his doctor connects to the 
server using the IP of the server. CoAP client use 4 orders 
(GET) that retrieves information from a specific resource that 
is particular by the desired URI. (POST) provides the 
information to be processed to a private resource. The output 
result depends on target resource, usually, results in the base 
resource being created or updated. (PUT) requests to create 
the resource that is particular by the URI or updated with the 
carried information representation. (DELETE) requests that 
identified resource be deleted. "LIBCoAP" SERVER it is a 
special server for CoAP protocol, where data is sent from the 
patient to server using a command "put" and the doctor takes 
the patient's data from a server using a command "get". 
To simulate the loss of network to show the performance 
of the proposed e-health systems over IoT at different network 
infrastructure with different losses percentages, some assisting 
programs were used as WANEM and WIRE SHARK. 
WANEM is an extensive network emulator, designed to 
provide a real network experience. Which can be used to 
simulate WAN properties such as network delay, packet 
damage, packet loss, disconnecting, jitter, reorder of the 
package, etc. WANEM through which we can change the loss 
so as not to result in ideal case the WANEM must mediate 
Client and broker by routing table. 
WIRE SHARK supports large number of the protocol. It 
analyzes the data sent and received through the protocol. 
Through it know: Public packets and subscribe, Timespan, 
Average packet per second, Average packet per size, average 
byte per second. From here we can calculate: IoT Success 
Message "ISM", IoT Average Byte "IAB" and IoT Delay 
message "IDM". 
The scenario through which we have chosen the 
appropriate protocol for electronic health. It appears in Fig. 9. 
The first scenario was executed using an MQTT protocol, 
where we have sent the patient's data from the client "MQTT 
FX" to the attending physician "doctor" through MOSQUITO 
server. Using WIRESHARK We can tracing the MQTT 
messages to know which of these messages received from the 
first time and which of them need re-sent. Through Wireshark, 
we were Managed these MQTT message to calculate the 
average byte used in sent messages and the time need to 
transmitting. All previous measurements in the ideal case, We 
have varied the loss ratio by WANEM server and re-do the 
practical simulations and re-measure an calculate the average 
byte and time to transmitting messages. 
The second scenario was implemented using the CoAP 
protocol. We sent the patient's data from the CoAP client 
"CoPPER" to the doctor by the LIBCoAP server passing with 
WIRESHARK. By tracing the sent data to show which 
messages received at destenation "doctor". Also via 
WIRESHARK analysis we can calculate the average byte used 
to send messages and the user time to transmitte. all the 
previous measurements in the ideal case, then we have change 
the loss ratio using  WANEM simulator and re-measure all the 
previous parameters to study the performance of the protocol 
in different network conditions. 
 
Fig. 9. Set up Scenario. 
 


---

Page 7

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
418 | P a g e  
www.ijacsa.thesai.org 
VI. PRACTICAL AND SIMULATION RESULTS 
The main objective of the practical results and simulation 
is to clarify which protocols "MQTT, CoAP" are more 
suitable for electronic health where the results were evaluated 
by three factors. "ISM, IAB, IBM". From the practical and 
simulation results: 
1) As shown in Fig. 10, the percentage of successful 
messages in case of the MQTT protocol greater than CoAP 
protocol, MQTT has a quality of service so the result is better 
in case of increasing the loss. 
The CoAP protocol is special case of UDP protocol. And 
cannot return lost messages and does not contain QoS, if there 
is a loss of patient data, the data cannot be retrieved and 
therefore cannot be used CoAP protocol in medical cases 
because the doctor need all the patients data without missing 
anything so that he can Correct diagnosis and ensure improved 
health care. 
2) As shown in Fig. 11, the rate of average byte in case 
CoAP greater than MQTT in the case of increasing the loss 
precentage. Despite what appeared in the first curve of the 
defect of the Coap protocol but it appears the second 
drawback is the large increase in the number of bytes used to 
send the message. Increasing the size leads to a large load on 
the network causing some messages to be lost. In spite of QoS 
2 in case MQTT needs to send a series of messages to confirm 
receipt of message it needs a number of bytes less than the 
CoAP, does not mean increasing the size of messages in QoS 
2 for their size in QoS 1 use QoS 1, However, we need to use 
QoS 2 in medical cases to ensure patient data is correct. There 
are also features in MQTT protocol it moves between Quality 
of Services automatically. You choose QoS 2 and the network 
does not allow to use because of a problem in it Selects QoS 1 
so the network service is improved and then the choice is back 
QoS 2 again. 
3) As shown in Fig. 12, The ratio delay of successful 
message in case CoAP greater than MQTT in the case of 
increasing the loss percentage. 
Here is talk about the delay in time, it turns out that the 
delay in QoS2 is greater than QoS1 and CoAP because it 
sends a series of messages to ensure the arrival of the message 
carrying the patient's data. From here we can say that the 
applications that need to be accuracy in sending the message 
do not consider the time delay being used QoS 2, but the 
Applications that care more about time are used QoS 1. In 
both cases, MQTT is more appropriate than CoAP. 
 
Fig. 10. IoT Success Message "ISM". 
 
Fig. 11. IoT Average Byte "IAB". 
 
Fig. 12. IoT Delay Message "IDM". 
 
 
 


---

Page 8

---

(IJACSA) International Journal of Advanced Computer Science and Applications, 
Vol. 10, No. 11, 2019 
419 | P a g e  
www.ijacsa.thesai.org 
VII. CONCLUSION 
This paper presents design and implementation of e-health 
platform over IoT. A reliable e-health monitoring system over 
IoT has been designed and successfully implemented in this 
work based on MQTT and CoAP protocols. Whereas the 
proposed system is based on any type of internet access like 
WIFI, GPRS, 3G, so it is easily reconfigurable and can be 
extended to include more medical sensors and more 
parameters. The proposed e-health system is flexible enough 
to include such kind of modifications. Also, Comparing 
"MQTT & CoAP" protocol to select the best IoT protocol for 
E-health applications is investigated in this paper. In 
particular, it defines real results depending on practical 
simulations to select the best IoT protocol for e-health 
applications. From the practical implementation of these 
protocols, MQTT protocol provided good results than CoAP 
protocol in the delay, the number of messages lost and the 
number of bytes used in messages. Thus decrease the energy 
used, and reduce the needed bandwidth. So from these 
practical and simulation results, MQTT message protocol 
more suitable to design and implementation of e-health 
platform over IoT. 
REFERENCES 
[1] B. Lee, "Healthcare Framework on the IoT open Platform," Service 
Model, Architecture, International Journal of Applied Engineering 
Research, vol. 9, pp. 29783-29792, 2014. 
[2] M.Bhay, M. Pat el and Chin tan Bhatt," Internet of Things (IoT): In a 
Way of Smart World" © Springer Science, Singapore 2016. 
[3] D. Uckelmann, M. Harrison, F. Michahelles "An Architectural 
Approach Towards the Future Internet of Things", Architecting the 
Internet of Things, Springer-Verlag Berlin Heidelberg 2011. 
[4] U. Tandale, Dr. B. Momin and D. P. Seetharam " An Empirical Study of 
Application Layer Protocols for IoT" International Conference on 
Energy, Communication, Data Analytics and Soft Computing (ICECDS-
2017) , IEEE, 2017. 
[5] B. Farahani , F. Firouzi , V. Chang , M. Badaroglu ,N. Constant , K. 
Mankodiya " Towards fog-driven IoT E-Health: Promises and 
challenges of  IoT in medicine and healthcare", Future Generation 
Computer Systems , 2018. 
[6] J. Shah, S. Soni, F. Darji, S. Chandak, A. Shetty "Smart Hospital Using 
Iot "International Conference on Innovative and Advanced Technologies 
in Engineering , IOSR Journal of Engineering (IOSRJEN), Volume 9, 
PP 26-32. 2018. 
[7] C. I. Saidu, A. S. Usman and P. Ogedebe, "Internet of Things: Impact on 
Economy", British Journal of Mathematics & Computer Science, 2015. 
[8] D. B. Ansari, A. Rehman, R. Mughal" Internet of Things (IoT) 
Protocols: A Brief Exploration of MQTT and CoAP",  International 
Journal of Computer Applications (0975 – 8887) Volume 179 – No.27, 
2018. 
[9] Jorge Gómez, Byron Oviedo , Emilio Zhum, " Patient Monitoring 
System Based on Internet of Things", 7th International Conference on 
Ambient Systems, Networks and Technologies (ANT 2016), Published 
by Elsevier, 2016. 
[10] R.N. Kirtana, Y.V. Lokeswari, " An IoT Based Remote HRV 
Monitoring System for Hypertensive Patients", IEEE International 
Conference on Computer, Communication, and Signal Processing 
(ICCCSP), IEEE, 2017. 
[11] Antoine Jamin et al."An aggregation plateform for IoT-based healthcare: 
illustration for bioimpedancemetry, temperature and fatigue level 
monitoring", 2017. 
[12] Kaleem Ullah et al.," Effective Ways to Use Internet of Things in the 
Field of Medical and Smart Health Care", International Conference on 
Intillegent System Engineering, IEEE, 2016. 
[13] M. Hussein, M. Zorkany, N. Abdel Kader, "Design and Implementation 
of IoT Platform for Real Time Systems", International Conference on 
Advanced Machine Learning Technologies and Applications (Springer), 
Egypt, 2018. 
[14] P. Thota, Y. Kim "Implementation and Comparison of M2M Protocols 
for Internet of Things" Intl Conf on Applied Computing and Information 
Technology,© IEEE, 2016. 
[15] K. Natarajan, B. Prasath, P. Kokila "Smart Health Care System Using 
Internet of Things"  Journal of Network Communications and Emerging 
Technologies (JNCET) Volume 6, Issue 3, ISSN: 2395-5317 , 2016. 
[16] A. Al-Fuqaha, M. Guizani, M. Mohammadi, M. Aledhari, Moussa 
Ayyash " Internet of Things: A Survey on Enabling Technologies, 
Protocols, and Applications",  IEEE COMMUNICATION SURVEYS & 
TUTORIALS, VOL. 17, NO. 4, 2015. 
[17] T. Takpor and A. Atayero "Integrating Internet of Things and E-Health 
Solutions Students‟ Healthcare", Proceedings of the World Congress on 
Engineering 2015. 
[18] S. Lee, H. Kim, D. Hong, Hongtaek Ju " Correlation Analysis of MQTT 
Loss and Delay According to QoS Level",  IEEE ICOIN, 2013. 
[19] B. Aziz, " A formal model and analysis of an IoT protocol" Ad Hoc 
Networks, Elsevier B.V. ,2016. 
[20] H. C. Hwang ,J. Park, J. G. Shon," Design and Implementation of a 
Reliable Message Transmission System Based on MQTT Protocol in 
IoT" Wireless Pers Commun, Springer Science, New York ,2016. 
