While a thread can be launched next to a GNU Radio flowgraph to handle the
setters and getters associated with each variable, XMLRPC provides a consistent
framework where a callback function is automagically created for each variable
name, making the flowgraph update easier than writing a custom protocol on a 
TCP/IP socket.

Demonstrations include Python, GNU Octave but even bash communication with
```
$ xmlrpc localhost:8080 set_freq i/200
```
