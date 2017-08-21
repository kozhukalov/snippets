#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
  char *ptr[5];

  ptr[0] = "zero";
  ptr[1] = "one";
  ptr[2] = "two";
  ptr[3] = "three";
  ptr[4] = "four";
  for (int i = 0; i < 5; i++)
    printf("%s\n", ptr[i]);

  return 0;
}
