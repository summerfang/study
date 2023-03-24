#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(int argc, const char* argv[]){
	list<string> lst;
	lst.push_front("test");
	lst.push_front("test2");

	lst.push_front("test3");
	lst.push_front("test4");



	list<string>::iterator it;

	for (it = lst.begin(); it != lst.end(); ++it)
		cout << *it << endl;

}
