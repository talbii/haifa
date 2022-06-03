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
    int lo, hi, mi, val = 0;
    seg *left = NULL, *right = NULL;

    seg(int lo, int hi) : lo(lo), hi(hi), mi((lo + hi) / 2) {
        if (lo != hi) {
            left = new seg(lo, mi);
            right = new seg(mi + 1, hi);
        }
    }

    int update(int a, int v) {
        if (a < lo || hi < a) return val;
        if (a == lo && lo == hi) return val = max(val, v);
        if (left) left->update(a, v);
        if (right) right->update(a, v);
        return val = max((left ? left->update(a, v) : 0),
                         (right ? right->update(a, v) : 0));
    }

    int get(int a, int b) {
        if (b < lo || hi < a) return 0;
        if (a <= lo && hi <= b) return val;
        return max((left ? left->get(a, b) : 0),
                   (right ? right->get(a, b) : 0));
    }

} seg;

signed main() {
    int n;
    cin >> n;
    vector<hatif> a(n);
    fori(n, i) cin >> a[i].l >> a[i].w >> a[i].h;
    sort(all(a));

    map<int, int> m;
    int c = -1;
    set<int> t;
    fori(n, i) t.insert(a[i].w);
    for (int v : t) m[v] = ++c;

    seg seg(0, c);
    set<int> ws;

    fori(n, i) {
        auto it = ws.upper_bound(a[i].w);
        int maxh = 0;
        if (it != ws.begin()) it--, maxh = seg.get(0, m[*it]);
        seg.update(m[a[i].w], maxh + a[i].h);
        ws.insert(a[i].w);
    }

    cout << seg.get(0, c) << endl;
}
