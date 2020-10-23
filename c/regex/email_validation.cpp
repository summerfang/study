#include <iostream>
#include <regex>

using namespace std;

bool is_email_valid(string& strEmaiAddress) {
    regex pattern("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");

    return regex_match(strEmaiAddress, pattern);
}