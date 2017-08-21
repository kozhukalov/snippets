#include <stdio.h>

/* This function calculates checksum of a set of 16 bit words
   That is why we cast to poiter to unsigned short */
unsigned short checksum(unsigned short *ptr, int nbytes)
{
  unsigned long sum;
  unsigned char tmp;

  sum = 0;
  while (nbytes > 1)
    {
      sum += *(ptr++);
      nbytes -= 2;
    }

  /* If originally there was an odd number of bytes */
  if (nbytes == 1)
    {
      tmp = *(u_char *)ptr;
      sum += tmp;
    }

  sum = (sum >> 16) + (sum & 0x0000ffff);
  sum = sum + (sum >> 16);
  return (unsigned short)~sum;
}


int main(int argc, char **argv)
{
  unsigned char *ptrc;
  printf("unsigned char: %d\n", sizeof(unsigned char));
  ptrc = malloc(sizeof(unsigned char) * 3);
  ptrc[0] = (unsigned char)0xff;
  ptrc[1] = (unsigned char)0xff;
  ptrc[2] = (unsigned char)0xff;

  return 0;
}
