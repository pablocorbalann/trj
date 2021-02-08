#include <stdio.h>
#include <stdlib.h>

int main()
{
  char c[1000];
  FILE *f;
  if ((f = fopen("configuration.yaml", "r")) == NULL)
  {
    printf("Error opening the file...\n");
    exit(1);
  }
  // reads the file until newline is encountered
  fscanf(f, "%[^client]", c);
  printf("Data from the file:\n%s", c);
  fclose(f);
  return 0;  
}
