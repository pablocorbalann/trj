#include <stdio.h>
#include <stdlib.h>
#include <string.h> // strlen() and all that stuff
#include <arpa/inet.h> // inet_pton() function
#include <sys/socket.h> // Sockets
#include <netinet/in.h> // Adress family (AF_INET)A

#define IP_ADDRESS "127.0.1.1"
#define PORT 4444
/*
int socketStart()
{
  struct sockaddr_in serv;
  int fd, conn; // FD stands for file descriptor (the descriptor of the socket)
  char message [100]; // Stores messages sents from the server 
  // Set up the actual socket and then bind it to the server
  fd = socket(AF_INET, SOCK_STREAM, 0);
  if (fd != 0)
  {
    printf("Can't create the socket...\n");
  }
  else 
    printf("Socket created successfuly...\n");
  serv.sin_family = AF_INET;
  serv.sin_port = htons(4444);
  if ((inet_pton(AF_INET, "127.0.0.1", &serv.sin_addr)) != 0)
  {
    printf("Client can't be binded to the server\n");
  }
  else
    printf("Client binded to the server...\n");
  // Start the chat while loop
  while (1)
  {
    printf("Enter a message to the server: ");
    fgets(message, 100, stdin);
    send(fd, message, strlen(message), 0);
  }
}
*/
int socketTest() 
{
  struct sockaddr_in serv;
  int fd;
  int conn; char message[100] = ""; 
  fd = socket(AF_INET, SOCK_STREAM, 0);
  serv.sin_family = AF_INET;
  serv.sin_port = htons(PORT);
  inet_pton(AF_INET, IP_ADDRESS, &serv.sin_addr); //This binds the client
  connect(fd, (struct sockaddr *)&serv, sizeof(serv)); //This connects the client to the server
  while(1) 
  {
    printf("Enter a message: ");
    fgets(message, 100, stdin);
    send(fd, message, strlen(message), 0);
    //An extra breaking condition can be added here (to terminate the while loop)
  }
}

int main()
{
  // socketStart();
  socketTest();
  return 0;
}
