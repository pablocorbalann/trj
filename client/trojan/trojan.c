/* This is the file that contains the trojan horse for the 
 * trj horse.
 *
 * It uses a socket to connect to the server and give access 
 * to the system.
 *
 * For more information:
 *
 *    https://github.com/pblcc/trj
 * */
#include <stdio.h>	
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdbool.h>

#define MAX 200

int socketCreate(void) {
  /*
   * This function creates a sockets using a short
   * data type and the socket():func
   * */
  int sock;
  printf("Creating the socket...\n");
  sock = socket(AF_INET, SOCK_STREAM, 0);
  return sock;
}

int socketConnect(short int sock)
{
  /*
   * This function connects the client to a remote server using a tct 
   * protocol
   *
   * Parameters:
   *  sock -> The socket
   * */
  int ret = -1;
  unsigned int port = 3330;
  struct sockaddr_in server = {0};
  // Configuration of the socket itself
  server.sin_addr.s_addr = inet_addr("127.0.1.1"); // localhost
  server.sin_family = AF_INET;
  server.sin_port = htons(port);
  ret = connect(sock, (struct sockaddr *)&server, sizeof(struct sockaddr_in));
  return ret;
}

int socketSend(short int sock, char * msg, int lmsg)
{
  /* 
   * This function takes a socket and sends a message to 
   * the server.
   *
   * Parameters:
   *  sock -> The socket
   *  mgs -> The message to send
   *  lmsg -> The len of the message
   * */
  int ret = -1;
  struct timeval tv;
  tv.tv_sec = 20; // 20 seconds timeout
  tv.tv_usec = 0;
  if (setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, (char *)&tv, sizeof(tv)) < 0)
  {
    printf("[E]: Socket timeout\n");
    return -1;
  }
  ret = send(sock, msg, lmsg, 0);
  return ret;
}

int socketReceive(int sock, char * msg, int lmsg)
{
  /*
   * This function receives a message from a server using a
   * socket tcpt
   *
   * Parameters:
   *  sock -> The socket
   *  msg -> The message that the socket gets
   *  lmsg -> The len of the message
   * */
  int ret = -1;
  struct timeval tv;
  tv.tv_sec = 20; // 20 seconds timeout
  tv.tv_usec = 0;
  if (setsockopt(sock, SOL_SOCKET, SO_SNDTIMEO, (char *)&tv, sizeof(tv)) < 0)
  {
    printf("[E]: Socket timeout\n");
    return -1;
  }
  // Receive the message itself
  ret = recv(sock, msg, lmsg, 0);
  printf("[S]: %s\n", msg);
  return ret;
}

int socketClose(int sock)
{
  int ret = 0;
  close(sock);
  for (short int i = 0; i < 3; i++)
  {
    shutdown(sock, i);
  }
  return ret;
}

int start()
{
  int sock, serverReplySize;
  struct sockaddr_in server;
  // receive and send arrays
  char sendMsg[100] = {0};
  char serverReply[200] = {0};
  // Start tctp
  sock = socketCreate();
  if (sock == -1)
  {
    printf("[E]: Can't create the socket...\n");
    return 1;
  }
  printf("Socket created successfully\n");
  // Connect the socket to the remote server using tct
  if (socketConnect(sock) < 0) 
  {
    printf("[E]: Socket connection error\n");
    return 1;
  }
  printf("Socket connected to the server\n");
  // Start a loop for receiving and sending messages
  while (1) {
    // Set the buffer reply to 0 (like cleaning the cache)
    serverReplySize = NULL;
    serverReplySize = socketReceive(sock, serverReply, 200);
    printf("SERVER: %s\n", serverReply);
    // Send a msg to the server
    printf(">>> ");
    gets(sendMsg);
    socketSend(sock, sendMsg, strlen(sendMsg));
  }
  if (socketClose(sock) < 0)
  {
    printf("[E]: Can't close the socket...");
    return -1;
  }
  printf("Socket closed...");
  return 0;
}

