// https://usaco.org/index.php?page=viewproblem2&cpid=1203

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

void add_elements_2(vector<int>& lst, int i, int ii1) {
    lst[i] = ii1;
    lst.erase(lst.begin() + i + 1);
}

bool all_elements_same(const vector<int>& lst) {
    for (int i = 1; i < lst.size(); ++i) {
        if (lst[i] != lst[0]) return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n_pers;
        cin >> n_pers;
        vector<int> times_sleep(n_pers);
        for (int i = 0; i < n_pers; ++i) {
            cin >> times_sleep[i];
        }

        vector<int> times_sleep_original = times_sleep;
        int total_sleep = accumulate(times_sleep.begin(), times_sleep.end(), 0);
        int sleep_aim = *max_element(times_sleep.begin(), times_sleep.end());
        int at = 0;

        while (!all_elements_same(times_sleep)) {
            if (total_sleep % sleep_aim != 0) {
                sleep_aim++;
                at = 0;
                times_sleep = times_sleep_original;
                continue;
            }

            if (times_sleep[at] == sleep_aim) {
                at++;
                if (at >= times_sleep.size() - 1) {
                    sleep_aim++;
                    at = 0;
                    times_sleep = times_sleep_original;
                }
                continue;
            }

            if (at < times_sleep.size() - 1) {
                int ii1 = times_sleep[at] + times_sleep[at + 1];
                if (ii1 > sleep_aim) {
                    sleep_aim++;
                    at = 0;
                    times_sleep = times_sleep_original;
                    continue;
                }

                add_elements_2(times_sleep, at, ii1);
            } else {
                sleep_aim++;
                at = 0;
                times_sleep = times_sleep_original;
            }
        }

        cout << n_pers - times_sleep.size() << endl; // joins = len_i - len_f
    }

    return 0;
}
