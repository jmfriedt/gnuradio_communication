0MQ, ZeroMQ or Zero-MQ is a TCP/IP wrapper making transactions of complex
structures (complex such as real and imaginary part, or vectors) easier.

Publish-Subscribe (PUBSUB) behaves like a UDP communication, where the server
keeps on running and streaming even if no client is connected.

Request-Reply (REQREP) behaves like a TCP communication, where each transaction
must be acknowledged.

For most purposes, PUBSUB seems most appropriate for streaming IQ data collected
by SDR. With GNU/Octave, the only way I could find to reset the queue was to close
the socket and open again for each new request, making sure not to receiver
obsolete data.
