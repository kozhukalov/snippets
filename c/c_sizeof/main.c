#include <stdio.h>

int main(int argc, char** argv)
{
  char a;
  char *b;
  char c[3];
  a = "a";
  b = "abc";
  c[0] = "d";
  c[1] = "e";
  c[2] = "f";
  printf("sizeof(char) = %d\n", sizeof(char));
  printf("sizeof(a) = %d\n", sizeof(a));
  printf("sizeof(b) = %d\n", sizeof(b));
  printf("sizeof(*b) = %d\n", sizeof(*b));
  printf("sizeof(c) = %d\n", sizeof(c));
  return 0;
}
