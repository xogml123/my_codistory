#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <netinet/in.h>//unix
#include <sys/socket.h>
#include <sys/wait.h>
#define PORT 3490
#define BACKLOG 10           
/*
how many pending connections
queue will hold*/

//server
struct sockaddr_in {
	short sin_family;
	unsigned short sin_port;
	struct in_addr sin_dddr;

};

void main() {
	int sockfd, new_fd;

	struct sockaddr_in my_addr;
	struct sockaddr_in their_addr;
	int sin_size;
	//socket()
	if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
		perror("socket");
		exit(1)
	}

	my_addr.sin_family = AF_INET;
	my_addr.sin_port = htons(MYPORT);

	my_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	//bind()
	if (bind(sockfd, (struct sockaddr*)&my_addr, sizeof(struct sockaddr)) == -1) {
		perror("bind");
		exit(1);
	}
	//listen(),accept()
	while (1) {
		sin_size = sizeof(struct sockaddr_in);
		if ((new_fd = accept(sockfd, (struct sockaddr*)&their_addr, &sin_size)) == -1) {
			perror("accept");
			continue;
		}
		printf("server: got connection from %s\n", inet_ntoa(their_addr.sin_addr));
	}

	//Client
	if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {
		perror("socket");
		exit(1);
	}
	their_addr.sin_family = AF_INET;
	their_addr.sin_port = htons(Server_Portnumber);
	their_addr.sin_addr = htonl(Server_IP_address);

	if (connect(sockfd, (struct sockfaddr *)&their_addr, sizeof(struct sockaddr)) == -1) {
		perror("connect");
		exit(1);
	}

}