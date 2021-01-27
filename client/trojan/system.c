#include <stdlib.h> // system
#include <stdio.h> // basic functions
#include "system.h"

/*
 * This function is used to execute a command in the system of
 * the client.
 *
 * Parameters
 * ----------
 * command: The command to be executed
 */
int systemExecute(char *command)
{
  if (command[0] == '\0')
  {
    // The string is empty so we can't execute the command.
    return 1;
  }
  system(command);
  return 0;
}

/*
 * Runs a small test for checking if the systemExecute function
 * actually works. (Just for running this file in local)
 */
int systemTest()
{
  printf("Executing ls...");
  systemExecute("ls");
  printf("Executing tree...");
  systemExecute("tree");
  printf("Executing ping google.com...");
  systemExecute("ping google.com");
}
