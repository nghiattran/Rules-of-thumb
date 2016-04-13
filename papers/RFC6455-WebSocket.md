
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

