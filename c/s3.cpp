#include <iostream>
#include <string>

using std::string;
using std::cout;

int main(int argc, char const *argv[]) {
  string str("This is the small world!");

  str.Format("{1}-{2}-{3}", 10, 20, 30);

  std::cout << str << '\n';
  return 0;
}
