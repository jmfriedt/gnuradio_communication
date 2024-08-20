all: ex1_client_stackoverflow ex1_server_stackoverflow

ex1_client_stackoverflow: ex1_client_stackoverflow.c
	gcc -o ex1_client_stackoverflow ex1_client_stackoverflow.c -lzmq

ex1_server_stackoverflow: ex1_server_stackoverflow.c
	gcc -o ex1_server_stackoverflow ex1_server_stackoverflow.c -lzmq

clean:
	rm ex1_client_stackoverflow ex1_server_stackoverflow
