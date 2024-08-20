all: string_client string_server vector_client

string_client: string_client.c
	gcc -o string_client string_client.c -lzmq

string_server: string_server.c
	gcc -o string_server string_server.c -lzmq

vector_client: vector_client.c
	gcc -o vector_client vector_client.c -lzmq
clean:
	rm string_client string_server
