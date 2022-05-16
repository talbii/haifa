#include "validate.hpp"

#include <string>
#include <vector>

const int maxn = 2e5 + 5;
std::vector<int> g[maxn];

void ancestor_dfs(int u, std::vector<int>& parent, std::vector<int>& groups,
                  std::vector<bool>& seen) {
    if (seen[groups[u]]) wrong_answer("bad party exists!\n");
    seen[groups[u]] = true;
    for (int v : g[u]) ancestor_dfs(v, parent, groups, seen);
    seen[groups[u]] = false;
}

int main(int argv, char** argc) {
    init_io(argv, argc);

    int n;
    if (!(judge_in >> n)) judge_error("can't parse judges n\n");
    if (n > 2e5) judge_error("n is too large\n");

    std::vector<int> b(n + 1);
    for (int i = 2; i <= n; i++) {
        int par;
        if (!(judge_in >> par)) judge_error("can't parse judges b_%d\n", i);
        g[par].push_back(i);
    }

    int ans_g, author_g;
    if (!(judge_ans >> ans_g)) judge_error("can't parse judges g\n");
    if (!(author_out >> author_g)) wrong_answer("can't parse authors g\n");

    if (ans_g != author_g)
        wrong_answer("expected g=%d, got %d\n", ans_g, author_g);

    std::vector<int> person_to_g(n + 1, 0);
    int seen = 0;
    for (int gi = 1; gi <= ans_g; gi++) {
        int g_size;
        if (!(author_out >> g_size))
            wrong_answer("cant parse size of group %d\n", gi);
        if (g_size < 1 || g_size >= n)
            wrong_answer("group size %d out of range\n", g_size);

        seen += g_size;
        if (seen >= n) wrong_answer("group sizes larger then n\n");

        for (int i = 1; i <= g_size; i++) {
            int a;
            if (!(author_out >> a))
                wrong_answer("cant parse person %d in group %d", i, gi);
            if (a < 2 || n < a) wrong_answer("person out of range\n");

            if (person_to_g[a] != 0)
                wrong_answer("person %d in more then one group\n", a);

            person_to_g[a] = gi;
        }
    }

    if (seen != n - 1)
        wrong_answer("total people placed in parties is %d, expected %d\n",
                     seen, n - 1);

    std::string trash;
    if (author_out >> trash) wrong_answer("output overflow\n");

    std::vector<bool> seens(ans_g + 1, false);
    ancestor_dfs(1, b, person_to_g, seens);
    accept();
}
