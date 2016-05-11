
### 1.3. Opening Handshake

#### Client

The client send handshaking request with header
```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: http://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

`GET /chat HTTP/1.1`: The request URI is the endpoint of websocket connection

`Host: server.example.com` :The client includes the hostname in the |Host| header field of its handshake as per, so that both the client and the server can verify that they agree on which host is in use.

Additional header fields are used to select options in the WebSocket Protocol:
* `Sec-WebSocket-Protocol`: subprotocol selector
* `Sec-WebSocket-Extensions`: list of extensions support by the client
* `Sec-WebSocket-Protocol`: indicate what subprotocols are acceptable to the client

The server selects one or none of the acceptable protocols and echoes that value in its handshake to indicate that it has selected that protocol.

`Origin: http://example.com`: used to protect against unauthorized cross-origin use of a WebSocket server by scripts using the WebSocket API in a web browser

Finally, the server has to prove to the client that it received the client’s WebSocket handshake, so that the server doesn’t accept connections that are not WebSocket connections

To prove that the handshake was received, the server has to take two pieces of information and combine them to form a response:
* `Sec-WebSocket-Key` in header field in the client handshake

For this header field, the server has to take the value (as present in the header field, e.g., the base64-encoded [RFC4648] version minus any leading and trailing whitespace) and concatenate this with the Globally Unique Identifier (GUID, [RFC4122]) "258EAFA5-E914-47DA-95CA-C5AB0DC85B11" in string form, which is unlikely to be used by network endpoints that do not understand the WebSocket Protocol. A SHA-1 hash (160 bits) [FIPS.180-3], base64-encoded (see Section 4 of [RFC4648]), of this concatenation is then returned in the server’s handshake (`Sec-WebSocket-Accept` see page 8 RFC6455).

#### Server

Handshake header
```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

`HTTP/1.1 101 Switching Protocols`: Any status code other than 101 indicates that the WebSocket handshake has not completed and that the semantics of HTTP still apply. The headers follow the status code.

The `Connection` and `Upgrade` header fields complete the HTTP Upgrade.

`Sec-WebSocket-Accept` header field indicates whether the server is willing to accept the connection

The connection will not be established if one of these occurs
* `Sec-WebSocket-Accept` value does not match the expected value
* the header field is missing
* the HTTP status code is not 101

Server can also send additional header like `Sec-WebSocket-Protocol: chat`

### 1.4. Closing Handshake

###1.5.  Design Philosophy

Conceptually, WebSocket is really just a layer on top of TCP that does the following:

* adds a web origin-based security model for browsers

* adds an addressing and protocol naming mechanism to support multiple services on one port and multiple host names on one IP address

* layers a framing mechanism on top of TCP to get back to the IP packet mechanism that TCP is built on, but without length limits

* includes an additional closing handshake in-band that is designed to work in the presence of proxies and other intermediaries

By default, the WebSocket Protocol uses port 80 for regular WebSocket connections and port 443 for WebSocket connections tunneled over Transport Layer Security (TLS)


##3.  WebSocket URIs

ws-URI = "ws:" "//" host [ ":" port ] path [ "?" query ]
wss-URI = "wss:" "//" host [ ":" port ] path [ "?" query ]

##4.  Opening Handshake

###4.1.  Client Requirements

There must be only one running websocket connection for a host (identified by host name and port number). Multiple connections have to be serialized.

0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                               |Masking-key, if MASK set to 1  |
+-------------------------------+-------------------------------+
| Masking-key (continued)       |          Payload Data         |
+-------------------------------- - - - - - - - - - - - - - - - +
:                     Payload Data continued ...                :
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|                     Payload Data continued ...                |
+---------------------------------------------------------------+

FIN:  1 bit

  Indicates that this is the final fragment in a message.  The first
  fragment MAY also be the final fragment.

RSV1, RSV2, RSV3:  1 bit each

  MUST be 0 unless an extension is negotiated that defines meanings
  for non-zero values.  If a nonzero value is received and none of
  the negotiated extensions defines the meaning of such a nonzero
  value, the receiving endpoint MUST _Fail the WebSocket
  Connection_.
Opcode:  4 bits

   Defines the interpretation of the "Payload data".  If an unknown
   opcode is received, the receiving endpoint MUST _Fail the
   WebSocket Connection_.  The following values are defined.

   *  %x0 denotes a continuation frame

   *  %x1 denotes a text frame

   *  %x2 denotes a binary frame

   *  %x3-7 are reserved for further non-control frames

   *  %x8 denotes a connection close

   *  %x9 denotes a ping

   *  %xA denotes a pong

   *  %xB-F are reserved for further control frames

Mask:  1 bit

   Defines whether the "Payload data" is masked.  If set to 1, a
   masking key is present in masking-key, and this is used to unmask
   the "Payload data" as per Section 5.3.  All frames sent from
   client to server have this bit set to 1.

Payload length:  7 bits, 7+16 bits, or 7+64 bits

   The length of the "Payload data", in bytes: if 0-125, that is the
   payload length.  If 126, the following 2 bytes interpreted as a
   16-bit unsigned integer are the payload length.  If 127, the
   following 8 bytes interpreted as a 64-bit unsigned integer (the
   most significant bit MUST be 0) are the payload length.  Multibyte
   length quantities are expressed in network byte order.  Note that
   in all cases, the minimal number of bytes MUST be used to encode
   the length, for example, the length of a 124-byte-long string
   can't be encoded as the sequence 126, 0, 124.  The payload length
   is the length of the "Extension data" + the length of the
   "Application data".  The length of the "Extension data" may be
   zero, in which case the payload length is the length of the
   "Application data".

Masking-key:  0 or 4 bytes

  All frames sent from the client to the server are masked by a
  32-bit value that is contained within the frame.  This field is
  present if the mask bit is set to 1 and is absent if the mask bit
  is set to 0.  See Section 5.3 for further information on client-
  to-server masking.

Payload data:  (x+y) bytes

  The "Payload data" is defined as "Extension data" concatenated
  with "Application data".

Extension data:  x bytes

  The "Extension data" is 0 bytes unless an extension has been
  negotiated.  Any extension MUST specify the length of the
  "Extension data", or how that length may be calculated, and how
  the extension use MUST be negotiated during the opening handshake.
  If present, the "Extension data" is included in the total payload
  length.

Application data:  y bytes

  Arbitrary "Application data", taking up the remainder of the frame
  after any "Extension data".  The length of the "Application data"
  is equal to the payload length minus the length of the "Extension
  data".

5.4.  Fragmentation

Why:
* For sending message without knowing. Without fragmentation, server must have a buffer to store entire message. Without fragmentation, server and choose a resonable buffer size and when it is reach the fragmentation is put into the network.
* For multiplexing, where it is desirable to split the message into smaller fragments and send through multiple channel.

Rules for fragmentation:
* An unfragmented message has FIN bit set and opcode other than 0.
* A fragmented message has FIN bit clear and opcode other than 0, followed by 0 or more frames with FIN bit clear and the opcode set to 0, and terminated by a single frame with the FIN bit set and an opcode of 0.
* Control frames (see Section 5.5) MAY be injected in the middle of a fragmented message.  Control frames themselves MUST NOT be fragmented.
* Message fragments MUST be delivered to the recipient in the order sent by the sender.
* The fragments of one message MUST NOT be interleaved between the fragments of another message unless an extension has been negotiated that can interpret the interleaving.
* An endpoint MUST be capable of handling control frames in the middle of a fragmented message.
* A sender MAY create fragments of any size for non-control messages.
* Clients and servers MUST support receiving both fragmented and unfragmented messages.
* As control frames cannot be fragmented, an intermediary MUST NOT attempt to change the fragmentation of a control frame. (???)
* An intermediary MUST NOT change the fragmentation of a message if any reserved bit values are used and the meaning of these values
is not known to the intermediary.
* An intermediary MUST NOT change the fragmentation of any message
in the context of a connection where extensions have been negotiated and the intermediary is not aware of the semantics of the negotiated extensions.  Similarly, an intermediary that didn't see the WebSocket handshake (and wasn't notified about its content) that resulted in a WebSocket connection MUST NOT change the fragmentation of any message of such connection.
* As a consequence of these rules, all fragments of a message are of the same type, as set by the first fragment's opcode.  Since control frames cannot be fragmented, the type for all fragments in a message MUST be either text, binary, or one of the reserved opcodes.

5.5.  Control Frames

Control frames are identified by opcodes where the most significant bit of the opcode is 1.  Currently defined opcodes for control frames include 0x8 (Close), 0x9 (Ping), and 0xA (Pong).  Opcodes 0xB-0xF are reserved for further control frames yet to be defined.

Control frames are used to communicate state about the WebSocket. Control frames can be interjected in the middle of a fragmented message.

All control frames MUST have a payload length of 125 bytes or less and MUST NOT be fragmented.

5.5.1.  Close

The Close frame contains an opcode of 0x8.

The Close frame MAY contain a body (the "Application data" portion of the frame) that indicates a reason for closing.

If there is a body, the first two bytes of the body MUST be a 2-byte unsigned integer representing a status code in Section 7.4. Following the 2-byte integer, the body MAY contain UTF-8-encoded data with value /reason/ (could be not readable)

Close frames sent from client to server must be masked.

The application MUST NOT send any more data frames after sending a Close frame.

If an endpoint receives a Close frame and did not previously send a Close frame, the endpoint MUST send a Close frame in response.

5.5.2.  Ping

The Ping frame contains an opcode of 0x9.

A Ping frame MAY include "Application data".

5.5.2.  Ping

The Pong frame contains an opcode of 0xA.

A Pong frame sent in response to a Ping frame must have identical
"Application data" as found in the message body of the Ping frame being replied to.

5.6.  Data Frames

Data frames (e.g., non-control frames) are identified by opcodes where the most significant bit of the opcode is 0.  Currently defined opcodes for data frames include 0x1 (Text), 0x2 (Binary).  Opcodes 0x3-0x7 are reserved.

Data frames carry application-layer and/or extension-layer data.The opcode determines the interpretation of the data:

Text
  The "Payload data" is text data encoded as UTF-8.  Note that a
  particular text frame might include a partial UTF-8 sequence;
  however, the whole message MUST contain valid UTF-8.  Invalid
  UTF-8 in reassembled messages is handled as described in
  Section 8.1.

Binary
  The "Payload data" is arbitrary binary data whose interpretation
  is solely up to the application layer.