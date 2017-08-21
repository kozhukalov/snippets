#include <stdio.h>
#include <stdlib.h>

struct my
{
  int a;
  struct my *next;
};

struct my *p = NULL;

void put(const struct my *my_p)
{
  printf("Put element: 0x%x\n", my_p);
  if (p == NULL){
    printf("Empty list\n");
    p = my_p;
    return;
  }
  struct my *cur = p;
  while (1){
    printf("cur:       0x%x\n", cur);
    printf("cur->next: 0x%x\n", cur->next);
    if (cur->next == NULL)
      break;
    cur = cur->next;
  }
  cur->next = my_p;
  printf("set cur->next: 0x%x\n", cur->next);
}

struct my *get(int a)
{
  if (p == NULL){
    printf("There are no elements\n");
    return NULL;
  }
  struct my *cur = p;
  while (1){
    printf("Current element: %d\n", cur->a);
    if (cur->a == a){
      return cur;
    }
    printf("Next: 0x%x\n", cur->next);
    if (cur->next != NULL)
      cur = cur->next;
    else
      return NULL;
  }
}

int main(int argc, char** argv)
{

  struct my *my_p;
  for (int i = 0; i < 10; i++){
    my_p = (struct my *)malloc(sizeof(struct my));
    my_p->a = i;
    put(my_p);
  }

  struct my *s = get(5);
  printf("s: %d\n", s->a);



  return 0;
}
