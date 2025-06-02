

---

Page 1

---

David C. Wyld et al. (Eds): ICDIPV, CBIoT, ICAIT, WIMO, NC, CRYPIS, ITCSE, NLCA, CAIML -2023    
pp. 113-125, 2023. CS & IT - CSCP 2023                                                               DOI: 10.5121/csit.2023.131309 
 
VERIFIABLE DATA SHARING SCHEME FOR 
DYNAMIC MULTI-OWNER SETTING 
 
Jing Zhao and Qianqian Su 
 
Department of Computer Science and Technology, Qingdao University, 
Qingdao, China 
 
ABSTRACT 
 
One of scenarios in data-sharing applications is that files are managed by multiple owners, and 
the list of file owners may change dynamically. However, most existing solutions to this problem 
rely on trusted third parties and have complicated signature permission processes, resulting in 
additional overhead. Therefore, we propose a verifiable data-sharing scheme (VDS-DM) that 
can support dynamic multi-owner scenarios. We introduce a management entity that combines 
linear secret-sharing technology, multi-owner signature generation, and an aggregation 
technique to allow multi-owner file sharing. Without the help of trusted third parties, VDS-DM 
can update file signatures for dynamically changing file owners, which helps save 
communication overhead. Moreover, users independently verify the integrity of files without 
resorting to a third party. We analyze the security of VDS-DM through a security game. Finally, 
we conduct enough simulation experiments and the outcomes of experimental demonstrate the 
feasibility of VDS-DM. 
 
KEYWORDS 
 
Security, Data Sharing, Dynamic Multi-Owner, Verification 
 
1. INTRODUCTION 
 
Thanks to the fast growth of cloud computing [1, 2, 3, 4], companies and individuals are able to 
store files on cloud servers for easy sharing. Although cloud computing offers many 
conveniences, it also brings several security risks [5, 6]. First, there is a danger of file privacy 
leakage since files may contain sensitive information and cloud servers cannot be completely 
trusted. Second, when file is kept in the cloud, the file owner loses physical control over the file, 
increasing the risk of illegal access. Naturally, file confidential can be achieved via traditional 
symmetric and asymmetric encryption techniques. However, these methods enable one-to-one 
access control rather than flexible and controlled authorized access. In addition, when there are 
many files, these methods suffer from drawbacks such as multiple copies of ciphertext, high 
encryption overhead and complicated key management [7, 8]. Fortunately, a potential solution to 
the above problems has emerged with the emergence of the ciphertext-policy attribute-based 
encryption (CP-ABE) scheme [9]. In CP-ABE, the file owner determines the set of authorized 
users by establishing an attribute-based access policy. Only users whose attributes satisfy the 
access policy can achieve decryption of the ciphertext. To achieve multi-user-oriented sharing in 
CP-ABE, the file owner just has to encrypt the file once. Therefore, CP-ABE can leverage 
attributes to achieve one-to-many access control by performing only one time encrypt operation 
[10, 11, 12, 13]. 
 


---

Page 2

---

114 
       
 
Computer Science & Information Technology (CS & IT) 
Most of CP-ABE based file sharing schemes are designed for single-file-owner setting, where the 
files are owned and managed by a single user [14, 15, 16, 17]. However, a multi-owner setting, in 
which files are managed by many owners, is equally typical. In contrast to single-file-owner, 
sharing files under a multi-owner setting require everyone’s signature for permission. Obviously, 
schemes designed for single-file-owner setting are not suitable for multi-owner setting. This is 
due to the fact that the latter has to address not just the issue of dynamic user changes, but also 
whether permissions are obtained from all file owners. One option to address the above issues is 
to appoint a multi-owner representative as manager with the responsibility of defining file access 
policies and ensuring file confidentiality. Different from the single-file-owner scenario, the multi-
owner scenario will face new problems. First, the manager must obtain each owner’s approval 
before the file shared. After that, the ciphertext and permissions can be uploaded to the cloud. To 
reduce storage and communication overhead, the manager has to aggregate multiple permissions 
into one. Second, the file owners may leave or join, both of which have an impact on the 
permission of the file. Therefore, the manager needs to perform file updates with the least amount 
of overhead as possible. Third, during the access phase, the user expects the file supplied by the 
cloud server to be correct. However, the cloud server could give the user incomplete or incorrect 
file due to factors like software, hardware, or interest, [18, 19, 20, 21]. Therefore, the user needs 
to have the ability to check the integrity of the results.  
 
Due to the prevalence of multi-owner setups, researchers are increasingly interested in how to 
design solutions for multi-owner scenarios. After in-depth research, we found that although 
related work has been proposed, there are still some problems that have not been well solved well. 
First, when the membership of file owner’s changes (such as join or leave), most existing 
solutions require the manager to complete file updates with the assistance of a trusted third party. 
To enable the renewal of multi-user signatures, the third party needs to redistribute the public and 
private keys for the manager. This method increases additional communication overhead [20]. 
Second, most of the existing schemes utilize the integrity proof method for file integrity 
verification, which is complex and requires the help of a third party [20, 21]. 
 
1.1. Our Contribution 
 
Motivated by the above issues, we design a verifiable data sharing scheme based on CP-ABE 
with dynamically multi-owner setting (shorted as VDS-DM). We introduce a management entity 
that combines linear secret-sharing technology, multi-owner signature generation, and an 
aggregation technique to allow multi-owner file sharing. Without the help of trusted third parties, 
VDS-DM can update file signatures for dynamically changing file owners, which helps save 
communication overhead. For the verifiability of the shared file, users can independently verify 
the integrity of the shared file without resorting to a trusted third party. Additionally, we analyze 
the security of VDS-DM through a formal security game. Finally, we carry out enough 
simulation experiments and the outcomes of experimental demonstrate the feasibility of VDS-
DM. 
 
2. RELATED WORK 
 
Waters and Sahai [22] proposed the first attribute-based encryption (ABE) scheme, which is 
considered as an extension of identity-based encryption (IBE) [23]. In ABE schemes, a set of 
attributes is used as the user’s identity. Only users whose attributes satisfy the specified access 
policy can obtain the plaintext of the encrypted file. This property of ABE has led to its 
increasing interest in data sharing applications. Later, Goyal et al. [24] proposed the first key-
policy ABE (KP-ABE) scheme and Bethencourt et al. [9] proposed the first ciphertext-policy 


---

Page 3

---

Computer Science & Information Technology (CS & IT)                                        115 
ABE (CP-ABE) scheme. Due to the fact that CP-ABE supports data owners to set access policies, 
most of the subsequent studies on data sharing schemes are conducted based on CP-ABE.  
 
In the next section, we mainly consider the data sharing schemes in the multi-owner scenario. In 
CP-ABE schemes that support multi-owner setting, Miao et al. [25] designed a verifiable 
keyword search scheme for encrypted data using multiple signature techniques. Miao et al. [26] 
proposed a CP-ABKS scheme based on privacy protection and implemented the traceability 
function of malicious users. Moreover, Zhang et al. [21] achieved multi-keyword search and 
verifiability of search results with guaranteed efficiency. However, the above schemes are 
implemented in static multi-owner setting, without considering dynamic multi-owner setting. In 
other words, the above schemes cannot be used directly to solve the problem if the file owners 
are added or deleted. Recently, Miao et al. [20] proposed a verifiable fine-grained keyword 
search scheme that supports dynamic multi-owner setting. However, their scheme requires 
interaction with a trusted third-party entity when performing update operation, which increases 
the time overhead. 
 
Another issue in multi-owner data sharing is that the cloud service is in practice an incomplete 
trusted entity. Cloud servers may return incomplete or incorrect search results to users due to 
interest issues or software and hardware failures. Sun et al. [27] implemented the search result 
verification function to some extent by using Bloon filters. Due to the high false positive rate of 
the Bloon filter, the search results will not be verified accurately. Miao et al. [20] and Zhang et al. 
[21] used signatures of files to achieve verification of the integrity of search results, but the 
process of forming signatures is complicated and requires interaction with the cloud service at the 
time of verification. 
 
3. PRELIMINARIES 
 
3.1. Bilinear pairing 
 
Let 𝔾,𝔾𝕋 be two multiplicative cyclic groups of prime order 𝑝, and 𝑔 is the generator of 𝔾. The 
bilinear mapping function 𝑒: 𝔾× 𝔾→𝔾𝕋 has the following three properties:  
 
1) Bilinearity: 𝑒(𝜇1
𝜑1, 𝜇2
𝜑2) = 𝑒(𝜇1, 𝜇2)𝜑1𝜑2 for all 𝜇1, 𝜇2 ∈𝔾, 𝜑1, 𝜑2 ∈ℤ𝑝. 
2) Non-degeneracy: For all 𝜇1, 𝜇2 ∈𝔾,𝑒(𝜇1, 𝜇2) ≠1. 
3) Computability: For all 𝜇1, 𝜇2 ∈𝔾,𝑒(𝜇1, 𝜇2) can be computed efficiently. 
 
3.2. Access structure 
 
𝐴= {𝐴1, 𝐴2, ⋯, 𝐴𝑛} is the set of n attributes. 𝔸 represents an access structure. For any 𝐵, 𝐶, if 
𝐵⊆𝐴 and 𝐵⊆𝐶, then 𝐶∈𝔸, then the collection 𝔸⊆2𝐴 is monotone. We can say that the 
collection 𝔸 of non-empty subsets of 𝐴 is a monotone access structure. The set in 𝔸 is called an 
authorized set and the opposite is called an unauthorized set. 
 
3.3. Decisional parallel bilinear Diffie-Hellman exponent assumption 
 
Let 𝔾 be a group with order 𝑝 and 𝑔 is the generator of 𝔾. Choose 𝑎, 𝑠, 𝑏1,⋯, 𝑏𝑞∈ℤp. Given a 
tuple: 
𝑦⃗= (𝑔, 𝑔𝑠,𝑔𝑎, ⋯, 𝑔𝑎𝑞, 𝑔𝑎𝑞+2, ⋯, 𝑔𝑎2𝑞, ∀1≤𝑗≤𝑞𝑔𝑠𝑏𝑗, 
𝑔𝑎/𝑏𝑗, ⋯, 𝑔𝑎𝑞/𝑏𝑗, 𝑔𝑎𝑞+2/𝑏𝑗, ⋯, 𝑔𝑎2𝑞/𝑏𝑗, ∀1≤𝑘,𝑗≤𝑞,𝑘≠𝑗 𝑔𝑎𝑠𝑏𝑘/𝑏𝑗,⋯, 𝑔𝑎𝑞𝑠𝑏𝑘/𝑏𝑗). 


---

Page 4

---

116 
       
 
Computer Science & Information Technology (CS & IT) 
There does not exist any probabilistic polynomial-time algorithm ℬ that distinguishes with non-
negligible probability between 𝑒(𝑔, 𝑔)𝑎𝑞+1 ∈𝔾𝑇 and a random element 𝑅∈𝔾𝑇. The algorithm 
ℬ, which returns the result 𝑧∈{0,1}, has advantage 𝜖 in solving the q-parallel BDHE problem in 
𝔾 if |Pr [ℬ(𝑦⃗,𝑒(𝑔, 𝑔)𝑎𝑞+1𝑠) = 0] −Pr [ℬ(𝑦⃗,𝑅) = 0]| ≥𝜖. 
 
3.4. Linear secret sharing scheme (LSSS) 
 
Let (𝕄,𝜌) indicates an access policy 𝔸, where 𝕄 is a shared generator matrix with 𝑙 rows and 𝑛 
columns. The function 𝜌(𝑖)(𝑖∈[1, 𝑙]) maps the 𝑖-th row in 𝕄 to an attribute in 𝔸. The linear 
secret sharing scheme consists of two parts: share generation and secret reconstruction. 
 
1) Share generation. Secret 𝑠∈ℤ𝑝∗, choose 𝑦2,⋯, 𝑦𝑛∈ℤ𝑝∗ at random. Set a vector 𝑣⃗=
(𝑠, 𝑦2,⋯, 𝑦𝑞)  to compute 𝜆𝑖= 𝕄𝑖⋅𝑣⃗.  𝜆𝑖 is the valid shared value of the secret 𝑠 
corresponding to 𝜌(𝑖). 
2) Secret reconstruction. Any authorized set 𝑆∈𝔸, 𝐼⊂{1,2, ⋯, 𝑙} is defined as 𝐼= {𝑖: 𝜌(𝑖) ∈
𝑆}. There exists a set of constants {𝜔𝑖∈ℤ𝑝}𝑖∈𝐼 that can be found in polynomial time. By 
computing ∑𝑖∈𝐼 𝜔𝑖𝜆𝑖= 𝑠 can recover the secret 𝑠. 
 
4. PROBLEM FORMULATION 
 
In this section, we present the system model, algorithm definition, security model and design 
goals of the proposed scheme. 
 
4.1. System Model 
 
As shown in Figure 1, the system model consists of five entities: Trusted Authorization (TA), 
Date Manager (DM), Data Owners (DOs), Cloud Service Provider (CSP), Data User (DU). The 
details of each entity are as follows: 
 
 
TA is a trusted authorization center. TA is responsible for initializing the system and 
generating the secret key for each DU (Step (1)). 
 
DOs is the owner of data. Each DO generate the signature to indicate approval of the file and 
sends the signature to 𝐃𝐌 (Step (2)). 
 
DM is a representative of all DOs. DM has own public/private key pair. DM first encrypts 
the file with the symmetric encryption method, then DM sets the access policy and uses to 
encrypt the symmetric key. After receiving the signatures of all DOs, DM aggregates them 
into a single signature. Finally, DM sends the file ciphertext, the key ciphertext, and the 
aggregated signature to CSP (Step (3)). When the number of DOs changes, DM issues an 
update key to CSP to update the aggregated signature (Step (8)). 
 
CSP is a semi-honest cloud server provider, which provides storage, search and update 
services. CSP stores the ciphertext sent by DM. When DU sends search request to it, CSP 
returns the search results to DU (Step (5)). Besides, CSP implements the signature update 
operation by using the update key sent by DM. 
 
DU is the user of data. DU first sends a file search request to CSP (Step (4)), then DU 
verifies the search results returned by CSP (Step (6)). If the verification fails, DU will no 
longer execute the decryption algorithm. Otherwise, the ciphertext can be decrypted only if 
the attributes of DU meet the access policy (Step (7)). 


---

Page 5

---

Computer Science & Information Technology (CS & IT)                                        117 
 
 
Figure 1. The system model of VDS-DM 
 
4.2. Algorithm definition 
 
Our proposed scheme includes the following algorithms: 
 
−𝐒𝐞𝐭𝐮𝐩 (1𝜅). Given a secure parameter 𝜅, TA runs this algorithm to output the public key 𝑃𝐾 
and the master key 𝑀𝑆𝐾. 
−𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼(𝑃𝐾, 𝑀𝑆𝐾, 𝑆). Given the public key 𝑃𝐾, the master key 𝑀𝑆𝐾 and DU's attribute set 
𝑆, TA runs this algorithm to output DU's secret key 𝑆𝐾𝑢. 
−𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴(𝑃𝐾, 𝒪). Given the public key 𝑃𝐾 and DO's set 𝒪= {𝑂1, ⋯, 𝑂𝑑}, DM outputs own 
public/private key pair (𝑃𝐾𝑚, 𝑆𝐾𝑚) and parameter 𝑦𝑡(𝑡∈[1, 𝑑]) for each DO. 
−𝐄𝐧𝐜(𝑃𝐾, (𝕄,𝜌), 𝐹). Given the public key 𝑃𝐾, matrix access structure 𝕄, the function 𝜌 maps 
each row of the 𝕄 to a attribute and file F, DM outputs file ciphertext 𝐶𝐹 and key ciphertext 
𝐶𝑇1. 
−𝐒𝐢𝐠𝐧(𝐶𝐹, 𝑦𝑡). Given file ciphertext 𝐶𝐹 and parameter 𝑦𝑡,𝐃𝐎𝒕 outputs signature 𝜎𝑡. 
−𝐀𝐠𝐠 ({𝜎𝑡}). Given all DOs's signature set {𝜎𝑡}, DM outputs an aggregated signature 𝜎 and 
uploads the ciphertext 𝐶𝑇= {𝐶𝐹, 𝐶𝑇1, 𝜎} to CSP. 
−𝐕𝐞𝐫𝐢𝐟𝐲(𝑃𝐾, 𝐶𝑇∗, 𝑃𝐾𝑚). Given the public key 𝑃𝐾, the ciphertext 𝐶𝑇∗ sent from CSP and DM's 
public key 𝑃𝐾𝑚, 𝐃𝐔 validates the integrity of 𝐶𝑇∗. 
−𝐃𝐞𝐜 (𝐶𝑇∗, 𝑆𝐾𝑢). Given the ciphertext 𝐶𝑇∗ and 𝐃𝐔 's secret key 𝑆𝐾𝑢, Only 𝐃𝐔 whose attributes 
satisfy the access policy can use the secret key 𝑆𝐾𝑢 to decrypt successfully. Authorized DU 
outputs the file 𝐹. 
−𝐔𝐩𝐝𝐚𝐭𝐞(𝑆𝐾𝑚). Given DM's private key 𝑆𝐾𝑚, 𝐃𝐌 outputs the update key 𝑈𝑃𝐾. DM sends it to 
CSP to implement the signature update operation. 
 
4.3. Security Model 
 
We require that the proposed scheme is secure against selected plaintext attacks in a selective 
model. We describe the security model by designing a security game played by the adversary 𝒜 
and the challenger 𝒞. 
 
Initialization: 𝒜 selects a challenge access policy 𝑃∗ and sends 𝑃∗ to 𝒞. 
Setup: 𝒞 executes the 𝐒𝐞𝐭𝐮𝐩 algorithm to obtain the public key 𝑃𝐾 and the master secret key 
𝑀𝑆𝐾. Then, it sends the public key 𝑃𝐾 to 𝒜. 


---

Page 6

---

118 
       
 
Computer Science & Information Technology (CS & IT) 
Phase 1: 𝒜 makes a key generation query to 𝒞, 𝒞 executes the 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼algorithm to generate 
a key 𝑆𝐾𝑢 and sends it to 𝒜. It is noted that the attribute set 𝑆 of attributes of 𝒜 does not satisfy 
𝑃∗. 
 
Challenge: 𝒜 submits two messages of the same length 𝑀0, 𝑀1 to 𝒞. Then, 𝒞 chooses a random 
bit 𝑏∈{0,1} and runs the 𝐄𝐧𝐜 algorithm to generate the ciphertext 𝐶𝑇𝑏
∗ under the challenge 
access policy 𝑃∗. Finally, 𝒞 sends 𝐶𝑇𝑏
∗ to 𝒜. 
 
Guess: 𝒜 outputs a guess 𝑏′ ∈{0,1}. 
The advantage of the adversary 𝒜 to winning this game is defined as: 
𝐴𝑑𝑣𝒜
𝐶𝑃𝐴= |Pr [𝑏′ = 𝑏] −
1
2|. 
 
Definition 1. If there does not exist any probabilistic polynomial-time adversary 𝒜 that can 
break the above selectively safe game with non-negligible probability, then VDS-DM is 
selectively safe. 
 
4.4. Design goals 
 
File integrity. If CSP returns an incomplete result to 𝐃𝐔, 𝐃𝐔 can detect the error with a non-
negligible probability. 
File privacy. If and only if the attributes of DU satisfy the access policy set by DM, DU can 
decrypt the ciphertext. 
Update Correctness. If the number of DOs changes, the ciphertext and owner's permission 
information can be updated correctly. 
 
5. THE PROPOSED VDS-DM 
 
In this section, after presenting the overview flow of the VDS-DM scheme, we describe in detail 
the algorithm construction involved in VDS-DM. Finally, we prove the security of the VDS-DM 
scheme. 
 
5.1. Overview 
 
As shown in Figure 2, TA runs Setup algorithm to realize system initialization and runs 
𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼 algorithm to generate the secret key for each DU. Each DO execute Sign algorithm 
to generate a signature to achieve approval of the file. DM runs 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴 algorithm to 
generate public/private key pair and publishes public key. DM performs symmetric encryption on 
the file and sets the access policy. DM uses the access policy to encrypt the symmetric key under 
𝐄𝐧𝐜 algorithm. Then DM aggregates all signatures into one signature by executing 𝐀𝐠𝐠 
algorithm. Finally, DM uploads the file ciphertext, the key ciphertext, and the aggregated 
signature to CSP. DU sends a search request to CSP, and 𝐂𝐒𝐏 returns results to DU. Then DU 
executes 𝐕𝐞𝐫𝐢𝐟𝐲 algorithm to verify the integrity of the results. If the verification passes, only 
DU whose attributes match the access policy can use 𝐃𝐞𝐜 algorithm to decrypt successfully. 
When the number of DOs changes, DM runs 𝐔𝐩𝐝𝐚𝐭𝐞 algorithm to generate an update key 
without the help of a third party and uploads it to CSP. CSP uses the update key to complete the 
signature update operation. 


---

Page 7

---

Computer Science & Information Technology (CS & IT)                                        119 
 
 
Figure 2. The system flow of VDS-DM 
 
5.2. Construction of VDS-DM 
 
The detailed algorithms of the VDS-DM are described as follows: 
 
−𝐒𝐞𝐭𝐮𝐩 (1𝜅) . Given a global public parameter 𝑝𝑝= (𝔾, 𝔾𝑇,𝑝, 𝑒, 𝑔) , TA randomly selects 
elements 𝛼, 𝛽∈ℤ𝑝, and computes 𝑒(𝑔, 𝑔)𝛼 and 𝑔𝛽. TA defines a system attribute set 𝐴, and 
selects a random element ℎ𝑥∈𝔾 for each attribute 𝑥∈𝐴. TA chooses a anti-collision hash 
function 𝐻2:{0,1} →𝔾. TA outputs public key 𝑃𝐾= (𝑝𝑝,𝐻2, 𝑒(𝑔, 𝑔)𝛼, 𝑔𝛽) and the master 
key 𝑀𝑆𝐾= (𝑔𝛼,{ℎ𝑥}𝑥∈𝐴). 
−𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼(𝑃𝐾, 𝑀𝑆𝐾, 𝑆). TA issues a set of attributes for each DU and randomly selects an 
element 𝑣∈ℤ𝑝, and computes 𝐾1 = 𝑔𝛼⋅𝑔𝑣𝛽, 𝐾2 = 𝑔𝑣, 𝐾𝑥= ℎ𝑥𝑣(𝑥∈𝑆). TA issues 𝑆𝐾𝑢=
(𝐾1, 𝐾2, {𝐾𝑥}𝑥∈𝑆) to DU. 
−𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴(𝑃𝐾, 𝒪) . DM randomly selects an element 𝑐∈ℤ𝑝, and computes 𝑃𝐾𝑚=
𝑔𝑐 and 𝑆𝐾𝑚= 𝑐 as own public/private key pair. Given multiple owners 𝒪= {𝑂1, ⋯, 𝑂𝑑}, DM 
outputs a (𝑑−1)-dimensional polynomial 𝑓(𝑥) = 𝑎0 + 𝑎1𝑥+ ⋯+ 𝑎𝑑−1𝑥(𝑑−1), where 𝑎𝑖∈
ℤ𝑝(𝑖∈[1, 𝑑−1]) , 𝑎0 = 𝑐. Then, 𝐃𝐌 selects 𝑑 points {(𝑥1, 𝑦1), ⋯, (𝑥𝑑, 𝑦𝑑)}  according to 
𝑓(𝑥) and sends 𝑦𝑡(𝑡∈[1, 𝑑]) to each DO. 
−𝐄𝐧𝐜(𝑃𝐾, (𝕄,𝜌), 𝐹). Given a file 𝐹, 𝐃𝐌 encrypts the file 𝐹 into 𝐶𝐹 by using the symmetric 
secret key 𝐾∈𝔾𝑇. DM encrypts 𝐾 by a matrix 𝕄𝑙×𝑞 associate with the access policy, the 
function 𝜌(𝜏) maps each row 𝕄𝜏(𝜏∈[1, 𝑙]) of the 𝕄𝑙×𝑞 to an attribute, and DM randomly 
chooses a vector 𝑣⃗= (𝑠, 𝑦2,⋯, 𝑦𝑞) to compute 𝜆𝜏= 𝕄𝜏⋅𝑣⃗. DM randomly chooses 𝑟1, ⋯, 𝑟𝑙∈
ℤ𝑝. The ciphertext of 𝐾 is: 
𝐶𝑇1 = ((𝕄, 𝜌), 𝐶1 = 𝐾⋅𝑒(𝑔, 𝑔)𝑠𝛼, 𝐶2 = 𝑔𝑠,{𝐶𝜏= 𝑔𝛽𝜆𝜏ℎ𝜌(𝜏)
−𝑟𝜏,𝐷𝜏= 𝑔𝑟𝜏}
𝜏∈[1,𝑙]). 
−𝐒𝐢𝐠𝐧 (𝐶𝐹, 𝑦𝑡). Each DO can generate the signature 𝜎𝑡= 𝐻2(𝐶𝐹)𝑦𝑡 on the file after receiving 𝑦𝑡 
from the DM. 


---

Page 8

---

120 
       
 
Computer Science & Information Technology (CS & IT) 
−𝐀𝐠𝐠 ({𝜎𝑡}). When DM receives the signatures of all DOs, DM computes the aggregated 
signature 𝜎= ∏𝑡=1
𝑑
 𝜎𝑡
𝐿𝑡(0) = (𝐻2(𝐶𝐹))
𝑐, where 𝐿𝑡(0) = ∏𝜄=1,𝜄≠𝑡
𝑑
 
−𝑥𝜄
𝑥𝑡−𝑥𝜄. DM uploads the 
ciphertext 𝐶𝑇= {𝐶𝐹, 𝐶𝑇1, 𝜎} to CSP. 
−𝐕𝐞𝐫𝐢𝐟𝐲(𝑃𝐾, 𝐶𝑇∗, 𝑃𝐾𝑚). When DU receives the ciphertext 𝐶𝑇∗ from CSP, DU calculates ℎ∗=
𝐻2(𝐶𝐹
∗). If 𝑒(𝑔, 𝜎) = 𝑒(𝑃𝐾𝑚, ℎ∗)  , DU executes the decryption operation. Otherwise, the 
algorithm will return ⊥. 
−𝐃𝐞𝐜 (𝐶𝑇∗, 𝑆𝐾𝑢). DU first needs to obtain the symmetric secret key 𝐾. If the attributes of DU 
satisfy the access policy embedded in the ciphertext, 𝐾 can be computed. Let 𝐼⊂{1,2, ⋯, 𝑙} be 
defined as 𝐼= {𝜏: 𝜌(𝜏) ∈𝑆}, {𝜆𝜏} is a reasonable share of 𝑠, and there exists a set of constants 
{𝜔𝜏∈ℤ𝑝}𝜏∈𝐼 satisfying ∑𝜏∈𝐼 𝜔𝜏𝜆𝜏= 𝑠.  DU computes 𝐴=
𝑒(𝑐2,𝑘1)
∏𝜏∈𝐼 (𝑒(𝑐𝜏,𝑘2)𝑒(𝐷𝜏,𝐾𝜌(𝜏)))
𝜔𝜏, 𝐾=
𝐶1/𝐴. Finally, DU transforms the ciphertext 𝐶𝐹
∗ into 𝐹 by the symmetric key 𝐾. 
−𝐔𝐩𝐝𝐚𝐭𝐞(𝑆𝐾𝑚). When 𝑚 new DOs join, 𝑑∗= 𝑑+ 𝑚. DM recalls 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴 algorithm to 
generate 𝑃𝐾𝑚∗= 𝑔𝑐∗, 𝑆𝐾𝑚∗= 𝑐∗. DM rechooses a (𝑑∗−1) dimensional-polynomial 𝑓∗(𝑥) =
𝑎0
∗+ 𝑎1
∗𝑥+ ⋯+ 𝑎𝑑∗−1𝑥(𝑑∗−1), where 𝑎𝑖′∗∈ℤ𝑝, 𝑎0
∗= 𝑐∗, (𝑖′ ∈[1, 𝑑∗−1]). DM reselects 𝑑∗ 
points {(𝑥1
∗, 𝑦1
∗), ⋯, (𝑥𝑑∗
∗, 𝑦𝑑∗
∗)} on 𝑓∗(𝑥) and sends 𝑦𝑡
∗(𝑡∈[1, 𝑑∗]) to each DO. Finally, DM 
computes the update key 𝑈𝑃𝐾= 𝑐∗/𝑐 and uploads it to CSP. The new signature can be 
computed by 𝜎∗= 𝜎𝑈𝑃𝐾; When 𝑛 DOs leave, 𝑑∗= 𝑑−𝑛, 𝐃𝐌 recalls the 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴 
algorithm to generate a new public/private key pair and reselects a (𝑑∗−1) dimensional-
polynomial 𝑓∗(𝑥). After that, the DM performs a process similar to the join operation. 
 
5.3. Security analysis 
 
5.3.1. Correctness analysis 
 
1) The correctness of Verify can be derived in the following way:  
𝑒(𝑔, 𝜎) = 𝑒(𝑔𝑐,𝐻2(𝐶𝐹)) = 𝑒(𝐺𝑃𝐾, ℎ∗). 
2) The correctness of Dec can be derived by: 
 
𝐴
 =
𝑒(𝐶2, 𝐾1)
∏
 
𝜏∈𝐼 (𝑒(𝐶𝜏, 𝐾2)𝑒(𝐷𝜏,𝐾𝜌(𝜏)))
𝜔𝜏
 =
𝑒(𝑔𝑠,𝑔𝛼⋅𝑔𝑣𝛽)
∏
 
𝜏∈𝐼 𝑒(𝑔𝛽𝜆𝜏ℎ𝜌(𝜏)
−𝑟𝜏, 𝑔𝑣)
𝜔𝜏𝑒(𝑔𝑟𝜏, ℎ𝜌(𝜏)
𝑣
)
𝜔𝜏
 = 𝑒(𝑔, 𝑔)𝑠𝛼
𝐶1
𝐴
 = 𝐾⋅𝑒(𝑔, 𝑔)𝑠𝛼
𝑒(𝑔, 𝑔)𝑠𝛼
= 𝐾
 
 
5.3.2. Security proof 
 
Theorem 1: If the decisional q-parallel BDHE assumption holds, VDS-DM scheme is secure 
against selected plaintext attacks in the selection model. 
Proof 1: Suppose there exists a probabilistic polynomial-time adversary that can compromise the 
security of the VDS-DM scheme with non-negligible probability, then there exists an algorithm 
ℬ that can solve the decisional q-parallel BDHE assumption. 
Initialization: 𝒜 selects an access policy 𝑃∗, 𝕄∗ is a matrix of 𝑙∗× 𝑞∗ associated with the access 
policy, 𝒜 sends (𝕄∗, 𝜌∗) to ℬ. 


---

Page 9

---

Computer Science & Information Technology (CS & IT)                                        121 
Setup: ℬ selects an element 𝛼′ and sets 𝑒(𝑔, 𝑔)𝛼= 𝑒(𝑔𝛽,𝑔𝛽𝑞)𝑒(𝑔, 𝑔)𝛼′ , here sets 𝛼= 𝛼′ +
𝛽𝑞+1.  ℬ chooses 𝑣𝑥∈ℤ𝑝 at random for each attribute 𝑥. Let 𝜏 denotes the row number of the 
matrix 𝕄∗, 𝑋 denotes a set with index 𝜏, and 𝜌∗(𝜏) = 𝑥. Then ℬ computes ℎ𝑥=
𝑔𝑣𝑥∏𝜏∈𝑋 𝑔𝛽𝕄𝜏,1
∗/𝑏𝜏𝑔𝛽2𝕄𝜏,2
∗/𝑏𝜏⋯𝑔𝛽
𝑞∗𝕄𝜏,𝑞∗
∗
/𝑏𝜏. 
Phase 1: Suppose ℬ receives a key query request for a set of attributes 𝑆, where 𝑆 does not 
satisfy the access policy 𝑃∗. ℬ selects a vector 𝑣⃗∗= {𝑣1
∗, 𝑣2
∗,⋯, 𝑣𝑞∗
∗} ∈ℤ𝑝∗, where 𝑣1
∗= −1. For 
every 𝜏∈𝑋, 𝜌∗(𝜏) ∈𝑆, there is 𝕄𝜏∗𝑣⃗∗= 0. ℬ randomly chooses 𝑟∈ℤ𝑝 and computes: 
 
𝑣
 = 𝑟+ 𝑣1
∗𝛽𝑞+ 𝑣2
∗𝛽𝑞−1 + ⋯+ 𝑣𝑞∗
∗𝛽𝑞−𝑞∗+1;
𝐾2
 = 𝑔𝑟∏ 
𝑞∗
𝜏=1
 (𝑔𝛽𝑞−𝜏+1)
𝑣𝜏∗
= 𝑔𝑣;
𝐾1
 = 𝑔𝛼′𝑔𝛽𝑟∏ 
𝑞∗
𝜏=2
 (𝑔𝛽𝑞−𝜏+2)
𝑣𝜏∗
= 𝑔𝛼𝑔𝑣𝛽.
 
 
For each attribute 𝑥∈𝑆, if there is no 𝜏 such that 𝜌∗(𝜏) = 𝑥, ℬ sets 𝐾𝑥= 𝐾2
𝑣𝑥; Otherwise, ℬ sets  
 
𝐾𝑥= 𝐾2
𝑣𝑥∏𝜏∈𝑋 ∏𝑗=1
𝑞∗ (𝑔
𝑟𝛽𝑗
𝑏𝜏∏𝑘=1,𝑘≠𝑗
𝑞∗
 (𝑔𝛽𝑞+1+𝑗−𝑘/𝑏𝜏)
𝑣𝑘
∗
)
𝕄𝜏,𝑗
∗
= ℎ𝑥𝑣. 
 
Challenge: 𝒜 submits two equal-length messages 𝑀0, 𝑀1 to ℬ, ℬ selects a random bit 𝑏∈
{0,1}  and computes 𝐶1
∗= 𝐾𝑏𝑇𝑒(𝑔𝑠,𝑔𝛼′), 𝐶2
∗= 𝑔𝑠. ℬ randomly chooses 𝑦2
′, ⋯, 𝑦𝑞∗
′ ∈ℤ𝑝 and 
sets 𝑣⃗′ = (𝑠, 𝑠𝛽+ 𝑦2
′,𝑠𝛽2 + 𝑦3
′,⋯, 𝑠𝛽𝑞∗−1 + 𝑦𝑞∗
′ ). Let 𝑌 denotes a set of 𝜏, where 𝜏∈[1, 𝑙] and 
satisfies 𝜌∗(𝜏) = 𝜌∗(𝑘)(𝑘≠𝜏). ℬ randomly chooses 𝑟1
′, ⋯, 𝑟𝑙
′ ∈ℤ𝑝 and computes:  
 
𝐷𝜏∗= 𝑔−𝑟𝜏′−𝑠𝑏𝜏; 
 
𝐶𝜏∗= ℎ𝜌∗(𝜏)
𝑟𝜏′
(𝑔𝑠𝑏𝜏)−𝑣𝜌∗(𝜏) ∏
(𝑔𝛽)𝑦𝑗
′𝕄𝜏,𝑗
∗
𝑞∗
𝑗=2
∏
∏
(𝑔
𝛽𝑗𝑠𝑏𝜏
𝑏𝑘)𝕄𝜏,𝑗
∗
𝑞∗
𝑗=1
𝑘∈𝑌
. 
 
Guess: 𝒜 outputs a guess 𝑏′ ∈{0,1}. 
If 𝑏′ = 𝑏, ℬ can guess that 𝑇= 𝑒(𝑔, 𝑔)𝛽𝑞+1𝑠, we have Pr [ℬ(𝑦⃗,𝑇= 𝑒(𝑔, 𝑔)𝛽𝑞+1𝑠) = 0] =
1
2 +
𝐴𝑑𝑣𝒜
𝐶𝑃𝐴. Otherwise, 𝑇 is a random element in 𝔾𝑇, we have Pr [ℬ(𝑦⃗, 𝑇= 𝑅) = 0] =
1
2. The 
advantage that ℬ can solve the decisional q-parallel BDHE assumption is negligible, then the 
VDS-DM scheme is selectively secure. 
 
6. PERFORMANCE ANALYSIS 
 
In this section, we evaluate the VDS-DM scheme from both theoretical and experimental aspects. 
 
6.1. Theoretical analysis 
 
We analyze the storage and calculation cost of the VDS-DM scheme theoretically. In storage 
cost, we set |𝔾𝑇|,|𝔾| and |ℤ𝑝| to denote the length of element in 𝔾𝑇, 𝔾 and ℤ𝑝. In calculation 
cost, we set the bilinear pairing operation 𝑃, the exponentiation operation 𝐸(𝐸𝑇) in group 𝔾 (𝔾𝕋). 


---

Page 10

---

122 
       
 
Computer Science & Information Technology (CS & IT) 
We ignore the hash operation which is more efficient compared to the above operations. We set 𝑑 
to denote the number of DOs, 𝑛𝑠 to denote the number of attributes in the system, 𝑛𝑎 to denote 
the number of attributes in the access structure, 𝑛𝑢 to denote the number of DU's attributes, and 
“-” to denote not applicable. Table 1 shows the calculation and storage cost of our scheme.  
 
As shown in Table 1, in 𝐒𝐞𝐭𝐮𝐩 algorithm, TA publishes a value for each system attribute. 
Therefore, the storage cost of this algorithm is affected by the number of system attributes. TA 
issues a set of attributes for DU and sends a secret key for DU according to attributes. Thus, the 
storage cost of 𝐊𝐞𝐲𝐆𝐞𝐧𝐃𝐔 algorithm is related to the number of DU's attributes. The 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴 
algorithm stores only two values fixedly, so its storage cost is constant. The ciphertext is related 
to the access policy, so the storage cost of 𝐄𝐧𝐜 algorithm is affected by the number of attributes 
in the access policy. In the multi-owner setting, the storage cost of 𝐒𝐢𝐠𝐧 algorithm is related to 
the number of owners. The 𝐀𝐠𝐠 algorithm outputs an aggregated signature belonging to 𝔾, so the 
storage cost is |𝔾|. The signature verification process does not store information, but only to 
perform verify operation, so the storage cost of 𝐕𝐞𝐫𝐢𝐟𝐲 algorithm is not considered. DU needs to 
store the results of three linear pairing operations when executing Dec algorithm. Therefore, the 
storage cost is 3|𝔾𝑇|. 
 
Table 1. Storage and calculation cost 
 
 
Storage cost 
Calculation cost 
𝐒𝐞𝐭𝐮𝐩 
(3 + 𝑛𝑠)|𝔾| + |𝔾𝑇| 
𝑃+ 2𝐸 
𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼 
(2 + 𝑛𝑢)|𝔾| 
(2 + 𝑛𝑢)𝐸 
𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴 
|𝔾| + |ℤ𝑝| 
𝐸 
𝐄𝐧𝐜 
|𝔾𝑇| + (2𝑛𝑎+ 1)|𝔾| 
𝑃+ (2𝑛𝑎+ 1)𝐸 
𝐒𝐢𝐠𝐧 
𝑑|𝔾| 
𝐸 
𝐀𝐠𝐠 
|𝔾| 
𝐸 
𝐕𝐞𝐫𝐢𝐟𝐲 
− 
2𝑃 
𝐃𝐞𝐜 
3|𝔾𝑇| 
(2𝑃+ 𝐸𝑇)𝑛𝑎+ 𝑃 
 
In the calculation cost, the cost of 𝐒𝐞𝐭𝐮𝐩 algorithm is not affected by the number of system 
attributes. In the composition of DU's secret key, TA performs corresponding operation on the 
value corresponding to each attribute of DU. Therefore, the calculation cost of 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼 
algorithm is related to the number of attributes of DU. DM obtains the public/private key pair 
through an exponentiation operation 𝐸 under 𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑴 algorithm. In 𝐒𝐢𝐠𝐧 algorithm, each DO 
only perform an exponentiation operation 𝐸 to complete the signature, which reduces the 
calculation burden of resource-limited DOs. The calculation cost of 𝐀𝐠𝐠 algorithm is 
independent of the number of DO. In 𝐕𝐞𝐫𝐢𝐟𝐲 algorithm, the results of two bilinear pairing 
operation 𝑃 need to be judged. Thus, the calculation cost is 2𝑃. The calculation cost of 𝐄𝐧𝐜 and 
𝐃𝐞𝐜 are related to the number of attributes in the access policy. 
 
6.2. Experimental simulation 
 
We test the performance of the VDS-DM scheme through experiment. Our experiment is 
implemented on a 64-bit Windows 10 operating system with an 11th Gen Intel(R) Core (TM) i7-
11700T @ 1.40GHz1.39GHz processor. The experiment uses Java language and JPBC-1.2.1, and 
uses a-type curves based on 160-bit elliptic curve group on a super singular curve 𝑦2 = 𝑥3 + 𝑥 
over a 512-bit finite field. we set |ℤ𝑝| = 160bit, |𝔾| = |𝔾𝑇| = 1024bit, 𝑑∈[2,10], 𝑛𝑠, 𝑛𝑎,
𝑛𝑢∈[10,100].  
 


---

Page 11

---

Computer Science & Information Technology (CS & IT)                                        123 
We set the unit of storage cost to KB and the unit of calculation cost to ms. As shown in Figure 3, 
the storage cost of 𝐒𝐞𝐭𝐮𝐩 is influenced by the number of system's attributes. Figure 4 shows the 
storage cost of 𝐊𝐞𝐲𝐆𝐞𝐧𝐷𝑈 algorithm increases linearly with the number of DU's attributes. From 
Figure 5, and compared with other algorithms, the storage cost of 𝐄𝐧𝐜 algorithm is larger and 
increases with the number of attributes in the access structure. As shown in Figure 6, the 
calculation cost of the 𝐊𝐞𝐲𝐆𝐞𝐧𝐷𝑈 algorithm is proportional to the number of DU's attributes. In 
𝐊𝐞𝐲𝐆𝐞𝐧𝑫𝑼 algorithm, it takes about 339ms at 𝑛𝑢= 50 . Figure 7 and Figure 8 show the 
calculation cost of 𝐄𝐧𝐜 and 𝐃𝐞𝐜, both of which are linearly related to the number of attributes in 
the access structure. Among them, the 𝐄𝐧𝐜 algorithm is more time consuming. Through 
experiments we found that each 𝐃𝐎 takes about 7ms to generate a signature by executing 𝐒𝐢𝐠𝐧 
algorithm in our experiment setting. The experiment shows that our scheme is feasible and 
efficient in solving the problem of verifiable data sharing in dynamic multi-owner setting. 
 
 
 
          Figure 3. Storage cost in 𝑺𝒆𝒕𝒖𝒑                         Figure 4. Storage cost in 𝑲𝒆𝒚𝑮𝒆𝒏𝐷𝑈 
 
 
 
             Figure 5. Storage cost in 𝑬𝒏𝒄                           Figure 6. Calculation cost in 𝑲𝒆𝒚𝑮𝒆𝒏𝐷𝑈 
 
 
 
          Figure 7. Calculation cost in 𝑬𝒏𝒄                        Figure 8. Calculation cost in 𝑫𝒆𝒄 
 


---

Page 12

---

124 
       
 
Computer Science & Information Technology (CS & IT) 
7. CONCLUSION 
 
In this paper, we propose a verifiable data sharing scheme (called VDS-DM) that can support 
dynamic multi-owner scenarios, which can ensure the confidentiality of files and the privacy of 
user identities while achieving the verifiability of shared files. The proposed scheme can 
complete the update of the file permission signature without the assistance of a third party, 
addressing the update issue brought by the dynamic change of the file owners. This method 
reduces the communication overhead. Additionally, users can verify the integrity of shared files 
by themselves without resorting to a third party. We demonstrate the security of VDS-DM 
through a formal security game. Finally, we conduct sufficient simulation experiments, and the 
experimental results demonstrate the feasibility of VDS-DM. 
 
ACKNOWLEDGEMENTS 
 
The authors would like to thank for the support from the Natural Science Foundation of 
Shandong Province under Grant No. ZR2022QF102.  
 
REFERENCES 
 
[1]  A. Sunyaev, “Cloud computing,” in Internet computing. Springer, 2020, pp. 195–236.  
[2]  C. Ge, W. Susilo, Z. Liu, J. Xia, P. Szalachowski, and L. Fang, “Secure keyword search and data 
sharing mechanism for cloud computing,” IEEE Transactions on Dependable and Secure Computing, 
vol. 18, no. 6, pp. 2787–2800, 2020.  
[3]  J. Li, S. Wang, Y. Li, H. Wang, H. Wang, H. Wang, J. Chen, and Z. You, “An efficient attribute-
based encryption scheme with policy update and file update in cloud computing,” IEEE Transactions 
on Industrial Informatics, vol. 15, no. 12, pp. 6500–6509, 2019.  
[4]  S. Xu, J. Ning, Y. Li, Y. Zhang, G. Xu, X. Huang, and R. Deng, “Match in my way: Fine-grained 
bilateral access control for secure cloud-fog computing,” IEEE Transactions on Dependable and 
Secure Computing, 2020.  
[5]  X. Lu, Z. Pan, and H. Xian, “An integrity verification scheme of cloud storage for internet-of-things 
mobile terminal devices,” Computers & Security, vol. 92, p. 101686, 2020.  
[6]  X. Gao, J. Yu, Y. Chang, H. Wang, and J. Fan, “Checking only when it is necessary: Enabling 
integrity auditing based on the keyword with sensitive information privacy for encrypted cloud data,” 
IEEE Transactions on Dependable and Secure Computing, 2021.  
[7]  D. Boneh, G. D. Crescenzo, R. Ostrovsky, and G. Persiano, “Public key encryption with keyword 
search,” in International conference on the theory and applications of cryptographic techniques. 
Springer, 2004, pp. 506–522. 
[8]  R. Chen, Y. Mu, G. Yang, F. Guo, and X. Wang, “Dual-server publickey encryption with keyword 
search for secure cloud storage,” IEEE transactions on information forensics and security, vol. 11, no. 
4, pp. 789–798, 2015.  
[9]  J. Bethencourt, A. Sahai, and B. Waters, “Ciphertext-policy attributebased encryption,” in 2007 IEEE 
symposium on security and privacy (SP’07). IEEE, 2007, pp. 321–334.  
[10]  Y. Miao, J. Ma, X. Liu, J. Weng, H. Li, and H. Li, “Lightweight finegrained search over encrypted 
data in fog computing,” IEEE Transactions on Services Computing, vol. 12, no. 5, pp. 772–785, 2018.  
[11] B. Waters, “Ciphertext-policy attribute-based encryption: An expressive, efficient, and provably 
secure realization,” in International workshop on public key cryptography. Springer, 2011, pp. 53–70.  
[12] Z. Zhang, J. Zhang, Y. Yuan, and Z. Li, “An expressive fully policyhidden cipher text policy attribute-
based encryption scheme with credible verification based on blockchain,” IEEE Internet of Things 
Journal, 2021.  
[13] M. Xiao, H. Li, Q. Huang, S. Yu, and W. Susilo, “Attribute-based hierarchical access control with 
extendable policy,” IEEE Transactions on Information Forensics and Security, 2022.  
[14] Y. Miao, J. Ma, X. Liu, X. Li, Q. Jiang, and J. Zhang, “Attributebased keyword search over 
hierarchical data in cloud computing,” IEEE Transactions on Services Computing, vol. 13, no. 6, pp. 
985–998, 2017.  


---

Page 13

---

Computer Science & Information Technology (CS & IT)                                        125 
[15] Z. Ying, W. Jiang, X. Liu, S. Xu, and R. Deng, “Reliable policy updating under efficient policy hidden 
fine-grained access control framework for cloud data sharing,” IEEE Transactions on Services 
Computing, 2021.  
[16] D. Han, N. Pan, and K.-C. Li, “A traceable and revocable cipher text policy attribute-based encryption 
scheme based on privacy protection,” IEEE Transactions on Dependable and Secure Computing, 
2020.  
[17] N. Chen, J. Li, Y. Zhang, and Y. Guo, “Efficient cp-abe scheme with shared decryption in cloud 
storage,” IEEE Transactions on Computers, vol. 71, no. 1, pp. 175–184, 2020.  
[18] J. Lai, R. H. Deng, C. Guan, and J. Weng, “Attribute-based encryption with verifiable outsourced 
decryption,” IEEE Transactions on information forensics and security, vol. 8, no. 8, pp. 1343–1354, 
2013.  
[19] B. Qin, R. H. Deng, S. Liu, and S. Ma, “Attribute-based encryption with efficient verifiable 
outsourced decryption,” IEEE Transactions on Information Forensics and Security, vol. 10, no. 7, pp. 
1384–1393, 2015.  
[20] Y. Miao, R. H. Deng, K.-K. R. Choo, X. Liu, J. Ning, and H. Li, “Optimized verifiable fine-grained 
keyword search in dynamic multi-owner settings,” IEEE Transactions on Dependable and Secure 
Computing, vol. 18, no. 4, pp. 1804–1820, 2019.  
[21] Y. Zhang, T. Zhu, R. Guo, S. Xu, H. Cui, and J. Cao, “Multi-keyword searchable and verifiable 
attribute-based encryption over cloud data,” IEEE Transactions on Cloud Computing, 2021.  
[22] A. Sahai and B. Waters, “Fuzzy identity-based encryption,” in Annual international conference on the 
theory and applications of cryptographic techniques. Springer, 2005, pp. 457–473.  
[23] A. Shamir, “Identity-based cryptosystems and signature schemes,” in Workshop on the theory and 
application of cryptographic techniques. Springer, 1984, pp. 47–53.  
[24] V. Goyal, O. Pandey, A. Sahai, and B. Waters, “Attribute-based encryption for fine-grained access 
control of encrypted data,” in Proceedings of the 13th ACM conference on Computer and 
communications security, 2006, pp. 89–98.  
[25] Y. Miao, J. Ma, X. Liu, J. Zhang, and Z. Liu, “Vkse-mo: verifiable keyword search over encrypted 
data in multi-owner settings,” Science China Information Sciences, vol. 60, no. 12, pp. 1–15, 2017.  
[26] Y. Miao, X. Liu, K.-K. R. Choo, R. H. Deng, J. Li, H. Li, and J. Ma, “Privacy-preserving attribute-
based keyword search in shared multi-owner setting,” IEEE Transactions on Dependable and Secure 
Computing, vol. 18, no. 3, pp. 1080–1094, 2019.  
[27] W. Sun, S. Yu, W. Lou, Y. T. Hou, and H. Li, “Protecting your right: Verifiable attribute-based 
keyword search with fine-grained ownerenforced search authorization in the cloud,” IEEE 
Transactions on Parallel and Distributed Systems, vol. 27, no. 4, pp. 1187–1198, 2014.  
 
AUTHORS  
 
Jing Zhao received the B.S. degree from the College of Electronic Information, Shandong Modern 
University, Jinan, China, in 2021. She is currently a graduate student in the College of Computer Science 
and Technology, Qingdao University, Qingdao, China. Her field of study is Attribute-Based Encryption.  
 
Qianqian Su received the B.S. and M.S. degrees from the College of Computer Science and Technology, 
Qingdao University, Qingdao, China, in 2015 and 2018, respectively. She received a Ph.D. degree from the 
State Key Laboratory of Information Security, Institute of Information Engineering, Chinese Academy of 
Sciences, Beijing, China, in 2021. She is currently working in the School of Computer Science and 
Technology, Qingdao University, Qingdao, China. Her research interests include cloud computing security, 
blockchain, and data security. 
 
 
 
© 2023 By AIRCC Publishing Corporation. This article is published under the Creative Commons 
Attribution (CC BY) license. 
