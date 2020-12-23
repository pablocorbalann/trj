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
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int start(int argc , char *argv[])
{
  int sock;
  struct sockaddr_in server;
  char message[1000] , server_reply[2048];

  /* To actually start the client, we have to create
   * a socket using socket() and then connect it to the 
   * server.
   * */
  sock = socket(AF_INET , SOCK_STREAM , 0);
  if (sock == -1)
  {
  	printf("[E]: Can't create a socket\n");
  }
  printf("Socket created successfully\n");
  server.sin_addr.s_addr = inet_addr("127.0.1.1");
  server.sin_family = AF_INET;
  server.sin_port = htons(3330);
  if (connect(sock, (struct sockaddr*) &server, sizeof(server)) < 0)
  {
    printf("[E]: Can't connect to the server...\n");
    return 1;
  }
  
  while(1)
  {
    if (recv(sock, server_reply, 2000, 0) < 0)
    {
      printf("[E]: Fatal, can't recive the msg from the server");
      break;
    }
    printf("[SERVER]: %s\n", server_reply);
    // Send a confirmation from the client to the server
    char message[] = "Reply recived at client";
    if (send(sock , message , strlen(message) , 0) < 0)
    {
      printf("[E]: Can't send a message to the server");
      return 1;
    }
  }
  
  close(sock);
  return 0;
}
