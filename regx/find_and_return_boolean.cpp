#include <iostream>
#include <regex>
#include <string>

using namespace std;

int main() {
    string pattern_string = "Lee";
    string string_be_search = "An Lee is a famous director";

    regex re(pattern_string);
    
    if (regex_match(string_be_search, regex("Lee"))) {
        cout << "String patter is found!";
    } else {
        cout << "String patter is not found!";
    }

}