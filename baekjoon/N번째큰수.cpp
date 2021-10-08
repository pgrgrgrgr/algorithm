#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	int A[10] = { 0, };
	for (int k = 0; k < T; k++) {
		for (int i = 0; i < 10; i++)cin >> A[i];
		for (int i = 9; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (A[j] > A[j + 1]) {
					int tmp = A[j + 1];
					A[j + 1] = A[j];
					A[j] = tmp;
				}
			}
		}
		cout << A[7] << endl;
	}
	return 0;
}
