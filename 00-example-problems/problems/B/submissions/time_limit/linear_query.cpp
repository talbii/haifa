#include <bits/stdc++.h>
using namespace std;
#define int long long
#define all(x) x.begin(), x.end()
#define fori(n, i) for (int i = 0; i < n; i++)
typedef vector<int> vi;
signed main() {
    int n, q;
    cin >> n >> q;
    vi p(n), s(n + 1);
    fori(n, i) cin >> p[i];
    sort(all(p));
    fori(q, _) {
        int x, y;
        cin >> x >> y;
        int s = 0;
        for (int i = n - x; i < n - x + y; i++) s += p[i];
        cout << s << endl;
    }
}
