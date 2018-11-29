// a low-level client using sockets
// adapted from https://www.tutorialspoint.com/unix_sockets/index.htm
// more documentation in server.c

#include <stdio.h>
#include <stdlib.h>

#include <netdb.h>
#include <netinet/in.h>

#include <unistd.h>

#include <string.h>

int main(void) {
   int port_number, transmission_error;
   struct sockaddr_in serv_addr;
   struct hostent *server;
   char buffer[256]; // for receiving messages

   port_number = 5001;

   /* Create a socket point */
   int sockfd = socket(AF_INET, SOCK_STREAM, 0);

   if (sockfd < 0) {
      perror("ERROR opening socket");
      exit(1);
   }

   server = gethostbyname("127.0.0.1");

   //TODO: document better
   bzero((char *) &serv_addr, sizeof(serv_addr));
   serv_addr.sin_family = AF_INET;
   bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
   serv_addr.sin_port = htons(port_number);

   /* Now connect to the server */
   if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
      perror("ERROR connecting");
      exit(1);
   }

   // message to be send to the server
   char msg[26] = "Hello, this is the client";

   /* Send message to the server, and capture any errors*/
   transmission_error = write(sockfd, msg, strlen(msg));

   if (transmission_error < 0) {
      perror("ERROR writing to socket");
      exit(1);
   }

   // Now read server's response into buffer, and capture any errors
   bzero(buffer,256);
   transmission_error = read(sockfd, buffer, 255);

   if (transmission_error < 0) {
      perror("ERROR reading from socket");
      exit(1);
   }

   printf("Received from server: %s\n",buffer);
   return 0;
}
