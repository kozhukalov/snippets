#include <stdio.h>
#include <sys/types.h>
#include <syslog.h>
#include <time.h>



int main(int argc, char** argv)
{
  openlog(NULL, LOG_PID, LOG_USER);

  time_t t = time(NULL);
  syslog(LOG_INFO, "Hello log world: %s", asctime(localtime(&t)));

  return 0;
}
