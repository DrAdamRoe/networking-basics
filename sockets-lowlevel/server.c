// a low-level server using sockets
// adapted from https://www.tutorialspoint.com/unix_sockets/index.htm
// lots of details here: http://www.cs.rpi.edu/~moorthy/Courses/os98/Pgms/socket.html

#include <stdio.h>
#include <stdlib.h>

#include <netdb.h>
#include <netinet/in.h>

#include <unistd.h>

#include <string.h>

int main( void) {

  // the things we'll need
   int newsockfd;
   unsigned int client_addr_length;
   char buffer[256];
   struct sockaddr_in serv_addr, cli_addr;
   int transmission_error;

   int port_number = 5001;

   /* Initialize socket structure. Explicitly clears out memory at the
       address of the server
   */
   bzero((char *) &serv_addr, sizeof(serv_addr));

   /* the server's address struct, an instance of sockaddr_in
   http://pubs.opengroup.org/onlinepubs/7908799/xns/netinetin.h.html
   */
   serv_addr.sin_family = AF_INET; //IPv4
   serv_addr.sin_addr.s_addr = INADDR_ANY; //all local interfaces
   serv_addr.sin_port = htons(port_number); // porty in network byte order

   /* define the socket's network attributes, and open the socket
        AF_INET: Use an IPv4 Address
        SOCK_STREAM: TCP
        0: use the IP protocol
   */
   int sockfd = socket(AF_INET, SOCK_STREAM, 0);

   if (sockfd < 0) {
      perror("ERROR opening socket");
      exit(1);
   }

   /* Now that the socket is open and the address is defined,
    we can bind the socket to the port, and capture any errors
    manual at http://man7.org/linux/man-pages/man2/bind.2.html
   */
   if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
      perror("ERROR on binding");
      exit(1);
   }

   //TODO: unhack this, get actual host address
   printf("server started at address 127.0.0.1 on port %i\n", port_number);


   /* Now start listening for a client on the bound port.
      the process will go in sleep mode and will wait for the incoming connection.
      only one connection is allowed at a time (backlog is set to 0).
   */

   listen(sockfd,0);
   client_addr_length = sizeof(cli_addr);

   /* Accept actual connection from the client */
   newsockfd = accept(sockfd, (struct sockaddr *)&cli_addr, &client_addr_length);

   if (newsockfd < 0) {
      perror("ERROR on accept");
      exit(1);
   }

   //TODO: get client address from accepted connection
   //printf("Client connected from: ", address)

   /* If connection is established, then start communicating */
   bzero(buffer,256);
   transmission_error = read( newsockfd,buffer,255 );

   if (transmission_error < 0) {
      perror("ERROR reading from socket");
      exit(1);
   }

   printf("message from client: %s\n",buffer);

   /* respond to client */
   //TODO: msg_response = "server got your message: " + data.decode()
   transmission_error = write(newsockfd,"server got your message: ",128);

   if (transmission_error < 0) {
      perror("ERROR writing to socket");
      exit(1);
   }

   return 0;
}
