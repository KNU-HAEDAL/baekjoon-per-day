#include <iostream>	
#include <vector>

using namespace std;

const int MAX = 151;

int N, K; //N명, 주인공번호: K, 주인공이 걸려야함
int cnt = 0; //지목횟수, 불가능하면 -1로 출력해야함
vector<int> myGraph[MAX];
bool visited[MAX];

void DFS(int x) { //사이클도는지 확인해야함
	visited[x] = true;
	cnt++;

	for (int i = 0;i < myGraph[x].size();i++) {
		int y = myGraph[x][i];

		if (visited[y] == false) {
			if (y == K)
				return;
			DFS(y);
			return;
		}
	}
	cnt = -1;
}

int main() { //방향 그래프
	int ai;

	cin >> N >> K;

	for (int i = 0;i < N;i++) {
		cin >> ai;

		myGraph[i].push_back(ai); //단방향그래프
	}
	
	DFS(0);

	cout << cnt;

	return 0;
}