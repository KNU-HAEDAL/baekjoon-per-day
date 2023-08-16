#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string tmp[5];

	for (int i = 0;i<5;i++) {
		cin >> tmp[i];
	}

	for (int i = 0;i < 15;i++)
		for (int j = 0;j < 5;j++) {
			if (i<tmp[j].size())
				cout << tmp[j][i];
		}

	return 0;
}