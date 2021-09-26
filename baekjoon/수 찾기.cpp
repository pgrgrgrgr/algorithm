#include <iostream>
#include <algorithm>
using namespace std;

int N;
int M;
int A[100000] = { 0, };

void binary_search(int a) {
	int start = 0;
	int end = N - 1;
	int mid;

	while (end >= start) {
		mid = (start + end) / 2;
		
		if (A[mid] == a) {
			cout << 1 << "\n";
			return;
		}
		else if (A[mid] < a) {
			start = mid + 1;
		}
		else {
			end = mid - 1;
		}
	}
	cout << 0 << "\n";
	return;
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> N;
	int tmp;

	for (int i = 0; i < N; i++) {
		cin >> tmp;
		A[i] = tmp;
	}

	sort(A, A + N);

	cin >> M;

	for (int i = 0; i < M; i++) {
		cin >> tmp;
		binary_search(tmp);
	}

	return 0;
}
