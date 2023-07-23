#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
	stack<int> s;
	vector<int> ori;
	vector<char> out;
	int c = 0, n;
	int temp;

	cin >> n;

	for (int i = 0;i < n;i++) {
		cin >> temp;
		ori.push_back(temp);
	}

	for (int i = 1;i <= n;i++) {
		out.push_back('+');
		s.push(i);
		for (int j = i;j > 0;j--) {
			if (!s.empty()) {
				temp = s.top();
				if (ori[c] == temp) {
					s.pop();
					out.push_back('-');
					c = c + 1;
				}
				else {
					break;
				}
			}
		}
	}

	if (s.empty()) {
		for (int i = 0;i < 2 * n;i++)
			cout << out[i] << "\n";
	}
	else
		cout << "NO";

	return 0;
}