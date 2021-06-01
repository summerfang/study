#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main() {

    string name = "Summer Fang John Smith";
    regex re("ang");

    cout << "regex_match(name, re) = " << regex_match(name, re) << endl;
    return 0;
}