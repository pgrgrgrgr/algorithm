#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	cin >> N;

	string names[150] = { "", };
	int alphabets[27] = { 0, };

	for (int i = 0; i <= N; i++) {
		getline(cin, names[i]);
	}

	for (int i = 1; i <= N; i++) {
		alphabets[int(names[i][0] - 'a' + 1)]++;
	}

	int cnt = 0;
	for (int i = 1; i <= 26; i++) {
		if (alphabets[i] >= 5) {
			cout << char(i+'a' - 1);
			cnt++;
		}
	}
	if (cnt == 0) {
		cout << "PREDAJA";
	}
	return 0;
}
