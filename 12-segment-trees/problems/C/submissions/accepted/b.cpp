#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fori(n, i) for (int i = 0; i < n; i++)
#define all(x) x.begin(), x.end()
typedef pair<int, int> ii;

typedef struct hatif {
    int l, w, h;
    bool operator<(const struct hatif& o) {
        return tie(l, w, h) < tie(o.l, o.w, o.h);
    }
} hatif;

typedef struct seg {
    int k, sz;
    vector<int> val;

    seg(int n) {
        for (k = 1; k < n; k *= 2)
            ;
        sz = k * 2;
        val.resize(sz, 0);
    }

    void update(int a, int v) {
        a += k;
        val[a] = v;
        for (a /= 2; a; a /= 2) val[a] = max(val[a * 2], val[(a * 2) + 1]);
    }

    int get(int a, int b) {
        a += k, b += k;
        int ma = 0;
        while (a <= b) {
            if (a % 2 == 1) ma = max(ma, val[a++]);
            if (b % 2 == 0) ma = max(ma, val[b--]);
            a /= 2, b /= 2;
        }
        return ma;
    }

} seg;

signed main() {
    int n;
    cin >> n;
    vector<hatif> a(n);
    fori(n, i) cin >> a[i].l >> a[i].w >> a[i].h;
    sort(all(a));

    map<int, int> m;
    int c = 0;
    set<int> t;
    fori(n, i) t.insert(a[i].w);
    for (int v : t) m[v] = c++;

    seg seg(c);
    set<int> ws;

    fori(n, i) {
        auto it = ws.upper_bound(a[i].w);
        int maxh = 0;
        if (it != ws.begin()) {
            it--, maxh = seg.get(0, m[*it]);
        }
        seg.update(m[a[i].w], maxh + a[i].h);
        ws.insert(a[i].w);
    }

    cout << seg.get(0, c - 1) << endl;
}
