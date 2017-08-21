#include <stdio.h>
#include <sys/types.h>

typedef struct
{
  u_int8_t a;
} my_nested_t;

typedef struct
{
  u_int8_t a;
  my_nested_t my_nested;
  u_int8_t b[0];
} __attribute__ ((packed)) my_t;


int main(int argc, char** argv)
{
  int i;
  u_int8_t buffer[1024];
  memset(buffer, 0, 1024);

  my_t *my_p;
  my_p = (my_t *)buffer;

  u_int8_t *tmp;
  int tmp_len = 16;

  tmp = malloc(tmp_len);
  memset(tmp, 0xff, tmp_len);

  my_p->a = 0;
  memcpy(my_p->b, tmp, tmp_len);

  for (i = 0; i < 32; i++)
    printf("%04d :: 0x%02x\n", i, buffer[i]);

  printf(":::::::::::\n");

  for (i = 0; i < 32; i++)
    printf("%04d :: 0x%02x\n", i, *(((u_int8_t *)my_p) + i));

  /* printf("sizeof(my_t) = %d\n", sizeof(my_t)); */

  return 0;
}
