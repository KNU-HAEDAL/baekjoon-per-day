#include <iostream>
#include <string>

using namespace std;

double change(string grade) {
	if (grade == "A+")return 4.5;
	if (grade == "A0")return 4.0;
	if (grade == "B+")return 3.5;
	if (grade == "B0")return 3.0;
	if (grade == "C+")return 2.5;
	if (grade == "C0")return 2.0;
	if (grade == "D+")return 1.5;
	if (grade == "D0")return 1.0;
	if (grade == "F")return 0.0;
	
	return 0.0;
}
int main() {
	char subject_name[51];
	string grade;
	double credit;
	int cnt=0;
	double sum = 0.0;

	for (int i = 0;i < 20;i++) {
		cin >> subject_name >> credit >> grade;
		if(grade!="P")
			cnt += credit;
		sum += credit * change(grade);
	}

	cout << sum / cnt;

	return 0;
}