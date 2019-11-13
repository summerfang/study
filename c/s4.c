#include <stdio.h>
#include <string.h>
#include <regex.h>

#define SUBSLEN 10
#define EBULEN 128
#define BUFLEN 1024

int main(int argc, char const *argv[]) {
  size_t len;
  regex_t re;
  regmatch_t subs[SUBSLEN];
  char matched[BUFLEN];
  char errbuf[EBULEN];

  int err, i;
  char src[] = "111 <title>Hello World</title>222";
  char pattern[] = "<title>(.*)</title>";

  printf("String: %s\n", src);

  printf("Pattern:\"%s\"\n");

  err = regcomp(&re, pattern, REG_EXTENDED);
  if(err) {
    len = regerror(err, &re, errbuf, size(errbuf));
    printf("error:regcomp: %s\n", errbuf);
    return 1;
  }
  return 0;
}
