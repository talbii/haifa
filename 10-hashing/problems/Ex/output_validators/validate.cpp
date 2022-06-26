#include "validate.hpp"

#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::string;
using std::vector;

const int MAXQ = 25000;
const string VALID_CHARS = "ATGC";

bool validate_query_str(int n, const string& str) {
    if (str.size() > n) return false;
    if (str.size() < 1) return false;
    for (char c : str) {
        bool found = false;
        for (char k : VALID_CHARS)
            if (c == k) found = true;
        if (!found) return false;
    }
    return true;
}

bool is_prefix(const string& all, const string& pref) {
    for (int i = 0; i < pref.size(); i++)
        if (all[i] != pref[i]) return false;
    return true;
}

int main(int argc, char** argv) {
    init_io(argc, argv);

    int n;
    if (!(judge_in >> n)) judge_error("can't parse judges input n\n");
    cout << n << endl;

    string str;
    if (!(judge_in >> str)) judge_error("can't parse judges string\n");

    for (int q = 1; q <= MAXQ; q++) {
        string pref;
        if (!(author_out >> pref))
            wrong_answer("can't parse author's query string\n");
        if (!validate_query_str(n, pref))
            wrong_answer("invalid query #%d\n", q);
        if (is_prefix(str, pref)) {
            cout << "YES" << endl;
            if (pref.size() == n) accept();
        } else {
            cout << "NO" << endl;
        }
    }

    wrong_answer("no queries left\n");
}
