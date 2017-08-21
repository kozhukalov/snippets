#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int errno;

int main(int argc, char** argv)
{
  const char *pathname = "/tmp/file.txt";
  int flags = O_RDONLY;
  int fd;
  char buf[1024];
  char *read_data;
  int read_size;

  fd = open(pathname, flags);
  if (fd == -1) {
    fprintf(stderr, "Error %d occured while opening file %s\n", errno, pathname);
    return 1;
  }
  read_size = read(fd, buf, 1024);
  if (read_size == -1) {
    fprintf(stderr, "Error %d occured while reading file %s\n", errno, pathname);
    return 1;
  }
  read_data = (char *)malloc(read_size);
  memcpy(read_data, buf, read_size);
  printf("Read from file:\n%s", read_data);
  return 0;
}
