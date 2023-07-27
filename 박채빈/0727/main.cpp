#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1001;

vector<int> myGraph[MAX];
bool visited[MAX];

//그래프연결시키기
void DFS(int x) {
	visited[x] = true;

	for (int i = 0;i < myGraph[x].size();i++) {
		int y = myGraph[x][i];

		if (visited[y] == false)
			DFS(y);
	}
}

int main() {
	int N, M; //N:정점개수, M:간선개수
	int count = 0;

	cin >> N >> M;

	//단방향 그래프 작성
	for (int i = 0;i < M;i++) {
		int u, v;

		cin >> u >> v;

		//무방향 그래프
		myGraph[u].push_back(v);
		myGraph[v].push_back(u);
	}

	for (int i = 1;i <= N;i++) {
		if (visited[i] == false) {
			count++;
			DFS(i);
		}
	}

	cout << count;

	return 0;
}