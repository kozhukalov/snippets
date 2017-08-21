#include <stdio.h>
#include <sys/types.h>


void foo(int a, int b)
{
  printf("a = %d\n", a);
  printf("b = %d\n", b);
}

void bar(void (*callback)(int, int))
{

  callback(1, 2);
}

int main(int argc, char** argv)
{
  bar(&foo);

  return 0;
}
