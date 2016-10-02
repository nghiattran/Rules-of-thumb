## Chapter 1

### 1.1 Computer security concepts

* **Information Security**: is about how to prevent attacks, or failing that, to detect attacks on information-based systems
* **Computer Security**: generic name for the collection of tools designed to protect data and to thwart hackers
* **Network Security**: measures to protect data during their transmission
* **Internet Security**: measures to protect data during their transmission over a collection of interconnected networks

Three key objectives of computer security:

1. **Confidentiality**:
  * **Data confidentiality**: assures that private or confidential infomation is not made available or disclosed to unauthorized individuals.
  * **Privacy**: Assures that individuals control or influence what information related to them may be collected and stored.
2. **Integrity**:
  * **Data integrity**: Assures that information and programs are changed only in a specified and authorized manner.
  * **System integrity**: Assures that a system performs its intended function in an unimpaired manner.
3. **Availability**: Assures that systems work promptly abd service us not denied to authorized users.

These are called **CIA triad**.

Definitions of a loss for each category:

* **Confidentiality**: Unauthorized disclosure of information.
* **Integrity**: Unauthorized modification or destruction of information.
* **Availability**: The disruption of access to or ues of information or information system.

#### Computer Security Challenges

1. not simple
2. must consider potential attacks
3. procedures used counter-intuitive
4. involve algorithms and secret info
5. must decide where to deploy mechanisms
6. battle of wits between attacker / admin
7. not perceived on benefit until fails
8. requires regular monitoring
9. too often an after-thought
10. regarded as impediment to using system

#### Computer Security vs. Network Security

**Computer Security**: deals with protecting a single machine.
**Network Security**: deals with protecting the communication and all participants in it.

### 1.2 The OSI security architerture

* **Threat**: a potential for violation of security; a possible danger that might exploit a vulnerability.
* **Attack**: an assault on system security that derives from an intelligent threat.

**Security Architecture**:
* Security Attack: Any action that compromises the security of information.
* Security Mechanism: A mechanism that is designed to detect, prevent, or recover from a security attack.
* Security Service: A service that enhances the security of data processing systems and information transfers. A security service makes use of one or more security mechanisms.

### 1.3 Security Attacks

![alt tag](http://www.open.edu/openlearnworks/pluginfile.php/70189/mod_page/content/1/T823_1_002i.jpg)

Attacks:

1. **Passive attack** : attempts to learn or make use of information from the system but does not affect system resource.
 
 * **Release of the message contents**: read the contents of the message
 * **Traffic analysis**: observe the pattern of the massage
2. **Active attack**: attempts to alter system resources or affect their operation
 * **Masquerade**: one entity pretends to be a different entity
 * **Replay**: involves the passive capture of a data unit and its subsequent retransmission to produce an unauthorized effect
 * **Modification of message**: some portion of a legitimate message is altered, or that messages are delayed or reordered.
 * **The denial of service**: prevents or inhibits the normal use or management of communications facilities

![alt tag]()

* **Interruption**: This is an attack on availability
* **Interception**: This is an attack on confidentiality
* **Modification**: This is an attack on integrity
* **Fabrication**: This is an attack on authenticity

### 1.4 Security Services

* **Authentication**: assurance that the communicating entity is the one claimed
 * **Peer entity authentication**
 * **Data origin authentication**
* **Access control**: the ability to limit and control the access to host systems and application via links.
* **Confidentiality**: the protection of transmitted data from passive attacks
 * **Trafic flow**: the protection of traffic flow, prevents hacker from knowing message's source and destination.
* **Integrity**: assures that messages are received as sent with no duplication, insertion, modification, reordering, or replays.
* **Nonrepudiation**: prevents either sender or receiver from denying a transmitted message.
* **Availability**

### 1.5 Security Mechanisms

* **Encipherment**
* **Digitial Signature**
* **Access control**
* **Data Integrity**
* **Authentication Exchange**
* **Traffice Padding**: the insertion of bits into gaps in data stream to frustrate traffic analysis attemps;
* **Routing Control**: enable selections of physical secure routes.
* **Notarization**: the use of trusted third party to assure center properties for data exchange.

### 1.6 Network Security Model

![alt tag](http://image.slidesharecdn.com/dnslec1-130403040340-phpapp01/95/data-network-security-40-638.jpg?cb=1364961883)

Four basic tasks in designing a security service:

1. Design a suitable algorithm for the security transformation
2. Generate the secret information (keys) used by the algorithm
3. Develop methods to distribute and share the secret information
4. Specify a protocol enabling the principals to use the transformation and secret information 

#### Network Access Security

![alt tag](http://image.slidesharecdn.com/cns-13f-lec01-overview-130905003004-/95/network-security-1st-lecture-44-638.jpg?cb=1378341083)


1. Select appropriate gatekeeper functions to identify users
2. Implement security controls to ensure only authorised users access designated information or resources 

## Chapter 2

### Terminologies

* **Plaintext** - original message
* **Ciphertext** - coded message
* **Cipher** - algorithm for transforming plaintext to ciphertext
* **Key** - info used in cipher known only to sender/receiver
* **Encipher** (encrypt) - converting plaintext to ciphertext
* **Decipher** (decrypt) - recovering ciphertext from plaintext
* **Cryptography** - study of encryption principles/methods
* **Cryptanalysis** (codebreaking) - study of principles/ methods of deciphering ciphertext without knowing key
* **Cryptology** - field of both cryptography and cryptanalysis

### 2.1 Symmetric Encryption Principles

![alt tag](https://notes.shichao.io/cnspp/figure_2.1.png)

Five ingredients for a symmetric encryption scheme:

1. **Plaintext**: original data.
2. **Encryption algorithm**
3. **Secret key**
4. **Ciphertext**: encrypted output from above three ingredient.
5. **Decryption algorithm**

Two requirements for secure use of symmetric encryption:

1. A strong encryption algorithm
2. Sender and receiver muse have obtained copies of secret keys in a secure fashion.

#### Cryptography

Three indepentdent dimemsions of cryptography:

1. The type of operations used for transforming plaintext to ciphertext:
 * **Substitution**: each element in the plaintext is mapped into another element.
 * **Transposition**: elements in plaintext is rearraged.
2. Number of keys used
 * One-key: symmetric, single-key, secret-key, or conventional encryption.
 * Multiply keys: asymmetric, two-key, or public-key encryption.
3. The way in which the plaintext is processed
 * **Block cipher**: one block at a time.
 * **Stream cipher**: 

#### Cryptanalysis

1. **Brute-force attack**: Eve has caught a ciphertext and will try every
 * Possible key to try to decrypt it. This can be made infinitely hard by choosing a large keyspace.
2. **Cryptanalytic attacks**
 * **Cyphertext-only attack**: Eve can gather and analyze C’s to learn K2
  * Encryption algorithm is known
  * Ciphertext to be decoded is known
 * **Known-plaintext attack**
  * Encryption algorithm is known
  * Ciphertext to be decoded is known
  * One or more plaintext-ciphertext pairs formed with the secret key are known
 * **Chosen-plaintext attack**: Mallory can feed chosen messages M into encryption algorithm and look at resulting ciphertexts C. Thus she can attempt to learn either K2 or messages M that produce C.
  * Encryption algorithm is known
  * Ciphertext to be decoded is known
  * Purported message chosen by cryptanalyst, together with its corresponding ciphertext generated with the secret key
 * **Chosen-ciphertext attack**
  * Encryption algorithm is known
  * Ciphertext to be decoded is known
  * Purported ciphertext chosen by cryptanalyst, together with its corresponding decrypted plaintext generated with the secret key
 * **Chosen-text attack**:
  * Encryption algorithm is known
  * Ciphertext to be decoded is known
  * Plaintext message chosen by cryptanalyst, together with its corresponding ciphertext generated with the secret key
  * Purported ciphertext chosen by cryptanalyst, together with its corresponding decrypted plaintext generated with the secret key
3. **Man-in-the-middle attack**:
 * Mallory can modify messages
 * So that they have different meaning – Mallory can drop messages
 * Mallory can replay messages to Alice, Bob or the third party
 
