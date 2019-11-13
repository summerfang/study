#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main(int argc, char const *argv[])
{
  string tmp, html;
  while(getline(cin, tmp))
  {
    tmp += "\n";
    html += tmp;
  }

  string pattern = "http(s)?://([\\w-]+\\.)+[\\w-]+(/[\\w- ./?%&=]*)?";
  regex re(pattern);

  for (sregex_iterator it(html.begin(), html.end(),re), end;
       it != end;
       ++it
      )
  {
    cout << it->str() << endl;
  }

  return 0;
}
