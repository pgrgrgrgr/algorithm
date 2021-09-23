#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	cin >> N;

	int x[50] = { 0, };
	int y[50] = { 0, };
	int rank = 1;

	for (int i = 0; i < N; i++) {
		cin >> x[i] >> y[i];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (x[i] < x[j] && y[i] < y[j])
				rank++;
		}
		cout << rank << ' ';
		rank = 1;
	}

	return 0;
}
