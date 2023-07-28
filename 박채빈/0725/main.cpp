#include<iostream>
#include<vector>

using namespace std;

const int MAX = 101;

int cnt = 0;
vector<int> myGraph[MAX];
bool visited[MAX];

void DFS(int x) {
	visited[x] = true;

	for (int i = 0;i < myGraph[x].size();i++) {
		int y = myGraph[x][i];

		if (visited[y] == false) {
			cnt++;
			DFS(y);
		}
	}
	if(x==1)
		cout << cnt;
}

int main() {
	int N, M; //N:정점개수, M:간선개수

	cin >> N >> M;

	for (int i = 0;i < M;i++) {
		int u, v;
		cin >> u >> v;

		myGraph[u].push_back(v);
		myGraph[v].push_back(u);
	}

	DFS(1);
	
	return 0;
}