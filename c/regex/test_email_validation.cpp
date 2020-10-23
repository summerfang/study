#include <iostream>

#include "email_validation.cpp"

using namespace std;

int main(int argc, char const *argv[])
{
    string strEmail = "summerfang@gmail.com";

    if(is_email_valid(strEmail))
    {
        cout << "Valid" << endl;
    }
    else
    {
        cout << "Invalid" << endl;
    }
    
    return 0;
}
