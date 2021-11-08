#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	cin >> N;

	string qs;
	int difficulty;

	cin >> qs >> difficulty;
	for (int i = 0; i < N - 1; i++) {
		int tmp;
		string strtmp;

		cin >> strtmp >> tmp;
		if (difficulty > tmp) {
			qs = strtmp;
			difficulty = tmp;
		}
	}

	cout << qs;
}
