#include <iostream>
#include <vector>

using namespace std;

int main() {
	string tmp;
	char pha[100];
	int result = 1;

	cin >> tmp;

	for (int i = 0;i < tmp.length();i++)
		pha[i] = tmp[tmp.length()-i-1];

	for (int i = 0;i < tmp.length();i++) {
		if (pha[i] != tmp[i])
			result = 0;
	}

	cout << result;

	return 0;
}