#include <iostream>>
#include <vector>

using namespace std;

vector<long> get_collatz_sequence(long l);

int main(int argc, char const *argv[])
{
    /* code */
    for (long l = 1; l <= 100; l++){
        vector<long> cs = get_collatz_sequence(l);
        for(auto i = cs.begin(); i != cs.end(); ++i)
            cout << *i << " ";
        cout << "\n";
    }
    return 0;
}

vector<long> get_collatz_sequence(long l) {
    vector<long> v_collatz;

    while (l != 1)
    {
        v_collatz.push_back(l);

        if (l % 2 == 0) {
            l = l / 2;
        } else {
            l = 3 * l + 1;
        }
    }

    v_collatz.push_back(1L);
    return v_collatz;
}
