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

* **Unconditional security**:  no matter how much computer power or time is available, the cipher cannot be broken since the ciphertext provides insufficient information to uniquely determine the corresponding plaintext.
* **Computational security**: given limited computing resources (eg time needed for calculations is greater than age of universe), the cipher cannot be broken.

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

### 2.2 Ciphers

#### Polyalphabetic Ciphers (Substitution)

**Polyalphabetic Ciphers** a substitution cipher in which the cipher alphabet changes during the encryption process. It  use uses a key to select which alphabet is used for each letter of the message and repeats from start until end of key is reached.

##### Vigenère Cipher

**Vigenère Cipher** is the simplest polyalphabetic substitution cipher:

* Having multiple letters long key, K = k<sub>1</sub> k<sub>2</sub> ... k<sub>i</sub> where i<sup>th</sup> letter specifies i<sup>th</sup> alphabet to use.

Example:
```
 key:       deceptivedeceptivedeceptive

 plaintext: wearediscoveredsaveyourself

 ciphertext:ZICVTWQNGRZGVTWAVZHCQYGLMGJ
```

##### One-Time Pad

If a truly random key as long as the message is used, the cipher will be secure since ciphertext bears no statistical relationship to the plaintext.

If only one of these rules is disregarded, the cipher is no longer unbreakable:

1. The key is at least as long as the message or data that must be encrypted.
2. The key is truly random (not generated by a simple computer function or such)
3. Key and plaintext are calculated modulo 10 (digits), modulo 26 (letters) or modulo 2 (binary)
4. Each key is used only once, and both sender and receiver must destroy their key after use.
5. There should only be two copies of the key: one for the sender and one for the receiver (some exceptions exist for multiple receivers)

#### Transposition Ciphers

Transposition Cipher's properties:

* Rearranging letters order without altering the actual letters used in plaintext.
• Can be recognized since it has the same frequency distribution as the original text.

##### Rail Fence cipher

**Rail Fence cipher**: write message letters out diagonally over a number of rows then read off cipher row by row

Example: 

```
Plaintext: MEETMEAFTERTHETOGAPARTY

Cipher process:
m e m a t r h t g p r y

 e t e f e t e o a a t
 
Ciphertext: MEMATRHTGPRYETEFETEOAAT
```

##### Row Transposition Ciphers

**Row Transposition Ciphers** procedure:

1. Write letters of message out in rows over a specified number of columns.
2. Reorder the columns according to some key before reading off the rows.

```
Key: 
            6 3 2 4 1 5
Plaintext: 
            W E A R E D
            I S C O V E 
            R E D F L E 
            E A T O N C 
            E Q K J E U 
Ciphertext: EVLNE ACDTK ESEAQ ROFOJ DEECU WIREE
```

### 2.2 Symmetric Block Encryption Algorithm

**Diffusion**: dissipates statistical structure of plaintext over bulk of ciphertext.
**Confusion**: makes relationship between ciphertext and key as complex as possible.

#### Feistel Cipher Structure

![alt tag](http://images.slideplayer.com/9/2613295/slides/slide_13.jpg)

**Feistel Cipher Structure** partitions input block into two halves, LE<sub>0</sub> and RE<sub>0</sub>
1. Each round *i* has has as inputs LE<sub>i-1</sub> and RE<sub>i-1</sub> from previous round as well as K<sub>i</sub> derived from K and a subkey generator algorithm.
2. A substitution is performed on the left half by applying a *round function* F to the right half and then taking the XOR kf the output of that function and the left half.
3. Permutation is performed which is consists of the interchange of the 2 halves.

All block ciphers used **Feistel Cipher Structure** as a general structure. Parameters for feature design:

* Block size: the larger the more secured. Common size: 128 bits.
* Key size: the larger the more secured. Common size: 128 bits.
* Number of rounds: the larger the more secured. Common size: 10-16 rounds.
* Subkey generation algorithm: the more complex the more secured.
* Round function: same as above.

Other considerations:

* Fast software en/decryption
* Ease of analysis

#### Data Encryption Standard

**Data Encryption Standard***:

* Used 64-bit data blocks
* 56-bit key, but only subkey is only 48 bits since 8 bits are for bit check function.
* 16 rounds processing
* Has initial and final permutation

![alt tag](https://www.tutorialspoint.com/cryptography/images/des_structure.jpg)

![alt tag](https://www.tutorialspoint.com/cryptography/images/initial_and_final_permutation.jpg)

Single round of DES

![alt tag](https://www.cybrary.it/wp-content/uploads/2016/01/des-enc3.jpg)

Single round structure of DES:

* Uses two 32-bit L & R halves
* As for any Feistel cipher can describe as: 
 L<sub>i</sub> = R<sub>i–1</sub>
 R<sub>i</sub> = L<sub>i–1</sub> ⊕ F(R<sub>i–1</sub>, K<sub>i</sub>)
* F takes 32-bit R half and 48-bit subkey:
 * Expands R to 48-bits using permutation E
 * Ddds to subkey using XOR
 * Passes through 8 S-boxes to get 32-bit result
 * Finally permutes using 32-bit perm P

**Avalanche Effect**:

1. The output changes significantly (e.g., half the output bits flip) as a result of a slight change in input (e.g., flipping a single bit)
2. In "quality" block ciphers, such a small change in either the key or the plaintext should cause a strong change in the ciphertext.

#### Double-DES

Use 2 DES encrypts on each block: C = E<sub>K2</sub>(E<sub>K1</sub>(P))

##### Issue

Since X = E<sub>K1</sub>(P) = D<sub>K2</sub>(C), hackers can attack by encrypting P with all keys and store and then decrypt C with keys and match X value.

Only takes twice as long to break double DES using brute force => 2<sup>57</sup>

#### Triple-DES with Two-Keys

**Triple-DES with Two-Keys** uses 3 encryptions and 2 keys in sequence  E-D-E.

C = E<sub>k1</sub>(D<sub>k2</sub>(E<sub>k1</sub>(P)))

k1 must differ from k2 since if so, D<sub>k2</sub>(E<sub>k1</sub>(P)) = D<sub>k1</sub>(E<sub>k1</sub>(P)) = P

**Triple-DES with Three-Keys**

Similar to **Triple-DES with Two-Keys** but uses 3 keys

C = E<sub>k3</sub>(D<sub>k2</sub>(E<sub>k1</sub>(P)))

#### Advanced Encryption Standard (AES)

**AES** properties:

* Secret key symmetric block cipher.
* 128-bit data, 128/192/256-bit keys.
* Stronger & faster than Triple-DES.

![alt tag](fillin)

![alt tag](https://www.kullabs.com/uploads/AES_structure.png)

**AES** specifications:

* AES does not use Feistel structure.
* Data block of 4 columns of 4 bytes is state.
* Key is expanded to an array of 44 words. 4 of them make up a round key.
* Both cipher and decipher begin with **Add round key** stage.
* Has 9/11/13 rounds in which state undergoes:
 * Byte substitution (1 S-box used on every byte)
 * Shift rows (permute bytes between groups/columns) mix columns (subs using matrix multipy of groups)
 * Mix columns: a substitution that alters each byte in a column as a function of all of the bytes in the column.
 * Add round key (XOR state with key material).
* Last round only has 3 stages.

#### Other Symmetric Block Ciphers

**International Data Encryption Algorithm**

* 128-bit key
* Used in PGP
 
**Blowfish**

* High execution speed 
* Run in less than 5K of memory

**RC5**

* Suitable for hardware and software
* Fast, simple
* Adaptable to processors of different word lengths
* Variable number of rounds
* Variable-length key
* Low memory requirement
* High security
* Data-dependent rotations

### 2.4 Stream Ciphers

Stream cipher properties:

* The longer the period of repeat, the more secured
* Statistically random.
* Depends on large enough key.

#### RC4

![alt tag](http://flylib.com/books/3/190/1/html/2/images/06fig09.jpg)

**RC4** outline:

1. Initial State of **S**(state vector, initialized from key) and **T** (temporary vector)
 
 * **S**: a permutation of 8-bit numbers from 0 to 255.
```
/* Initialization of S and T */
for i = 0 to 255 do
 S[i] = i
 T[i] = K[i mod keylen])
```

2. Initial permutation of S

```
j = 0
for i = 0 to 255 do
 j = (j + S[i] + T[i]) mod 256
 swap (S[i], S[j])
```

3. Stream generation

```
/*stream generation */
i = j = 0
for i = 0 to 255 do
 j = (j + S[i]) mod 256
 swap(S[i], S[j])
 t = (S[i] + S[j]) mod 256
 k = S[t]
 
 Ci = Pi XOR k     // cipher
 Di = Ci XOR k     // or decipher
```

To encrypt, XOR the value k with the next byte of plaintext. To decrypt, XOR it with the next byte of the ciphertext.

Key is only used in first step
 
### 2.5 Cipher Block Modes of Operation

#### 1. Electronic Codebook (ECB)

Message is broken into independent blocks which are encrypted with same key.

Each block is encoded independently of the other blocks. C<sub>i</sub> = DES<sub>K1</sub>(P<sub>i</sub>)

**Codebook**: for a given, there is an unique ciphertext for b-bit block of plaintext.

If the same b-bit block appear repeatively, it always produce same ciphertext.

Uses: secure transmission of single values

#### 2. Cipher Block Chaining (CBC) 

![alt tag](http://flylib.com/books/3/190/1/html/2/images/06fig04.jpg)

Same key is used for all blocks.

The input to the encryption is the XOR of the current plaintext abd the preceding ciphertext. Therefore, repeating patterns of b-bit are not exposed.

**Initial vector (IV)** must be known by sender and receiver and should be protected as well as key. 

#### 3. Cipher FeedBack (CFB)

Using **Cipher FeedBack**, a block cipher can be transmitted to stream cipher.

![alt tag](http://flylib.com/books/3/190/1/html/2/images/06fig05.jpg)

#### 4. Counter (CTR)

![alt tag](http://edulabs.drupalgardens.com/sites/g/files/g1751726/f/styles/large/public/201410/Counter%20Mode%20block.png?itok=h2oUJGeb)

### 2.6 Placement of Encryption

Two major placement alternatives:

1. Link encryption
 * Encryption occurs independently on every link 
 * Implies must decrypt traffic between links
 * Requires many devices and keys
2. End-to-end encryption
 * Encryption occurs between original source and final destination
 * Need devices at each end with shared keys
 * Must leave headers in clear so network can correctly route information
 * Hence although contents protected, traffic pattern flows are not

Therefore, link encryption occurs at layers 1 or 2, end-to-end can occur at layers 3, 4, 6, 7
