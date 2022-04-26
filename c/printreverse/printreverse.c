# include <stdio.h>
# include <string.h>

void printreverse(const char* pcString);

int main(int argc, char** argv){
    const char* s = "Hello World";
    printreverse(s);
    printf("\n");
    return 0;
};

void printreverse(const char* pcString){
    if(!*pcString)
        return;
    else
        printreverse(pcString + 1);
        putchar(*pcString);
}
