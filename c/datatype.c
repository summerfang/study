#include <stdio.h>

int main(int argc, char** argv){

    // integer
    int i_smallest = -32768;
    int i_largest = 32767;

    unsigned ui_smallest = 0;
    unsigned ui_largest = 65525;

    long l_smallest = -2147483648;
    long l_largest = 2147483647;

    short st_smallest = -32768;
    short st_largest = 32767;

    // character
    char c_smallest = -128;
    char c_largest = 127;

    unsigned char uc_smallest = 0;
    unsigned char uc_largest = 127;
    
    // Float
    float f = 0.123456;
    double d = 0.1234567890123;
    long double ld = 0.1234567890123456789;


    // point
    int *pi = NULL;
    int *pc = NULL;

    // Enumerator
    enum COLORS {RED, GREEN, BLUE};
    enum COLORS color;

    // Arrary
    int a_int[10];
    char a_char[10];

    struct Person
    {
        char Name[100];
        unsigned short age;
        bool is_female;
    };
    
    return 0;
}