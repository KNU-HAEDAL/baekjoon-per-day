#include <iostream>
#include <queue>	

using namespace std;

int main(void) {
	queue<int> card;
	int N;
	int tmp;

	cin >> N;

	for (int i = 1;i <= N;i++) {
		card.push(i);
	}

	while (card.size() != 1) {
		card.pop();
		tmp = card.front();
		card.pop();
		card.push(tmp);
	}

	cout << card.front();

	return 0;
}