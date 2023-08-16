#include <iostream>
#include <vector>

using namespace std;

vector<int> my_Graph[100001];
int parent[100001];

void DFS(int x) {

	for (int i = 0;i < my_Graph[x].size();i++) {
		int y = my_Graph[x][i];

		if (!parent[y]) {
			parent[y] = x;
			DFS(y);
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int N;
	int a, b;

	cin >> N;

	for (int i = 0;i < N-1;i++) {
		cin >> a >> b;

		my_Graph[b].push_back(a);
		my_Graph[a].push_back(b);
	}

	DFS(1);

	for (int i = 2;i <= N;i++) {
		cout << parent[i] << endl;
	}

	return 0;
}