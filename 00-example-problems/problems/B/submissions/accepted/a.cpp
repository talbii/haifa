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
    fori(n, i) s[i + 1] = s[i] + p[i];
    // s[i] = sum(p1...pi-1) = sum of first i elements
    fori(q, _) {
        int x, y;
        cin >> x >> y;
        cout << s[n - x + y] - s[n - x] << endl;
    }
}
