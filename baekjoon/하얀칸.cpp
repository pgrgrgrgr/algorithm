#include <iostream>
#include <string>
using namespace std;

int main() {
	string chess[8] = { "", };

	for (int i = 0; i < 8; i++) {
		cin >> chess[i];
	}
	int white_cnt = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 4; j++) {
			if (i % 2 == 0) {
				if (chess[i][2 * j] == 'F') {
					white_cnt += 1;
				}
			}
			else {
				if (chess[i][2 * j + 1] == 'F') {
					white_cnt += 1;
				}
			}
		}
	}
	cout << white_cnt;
	return 0;
}
