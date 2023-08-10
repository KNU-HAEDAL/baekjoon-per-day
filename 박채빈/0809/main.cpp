#include <iostream>
#include <algorithm>

using namespace std;


int main(void) {
	ios_base::sync_with_stdio(0);cin.tie(0);
	int A[100001];
	int N, M;
	int tmp;

	cin >> N;

	for (int i = 0;i < N;i++) {
		cin >> A[i];
	}

	sort(A, A + N); //정렬
	int newSize = unique(A, A + N) - A;

	cin >> M;

	for (int i = 0;i < M;i++) {
		cin >> tmp;
		cout << binary_search(A, A + newSize, tmp) << "\n";
	}

	return 0;
}