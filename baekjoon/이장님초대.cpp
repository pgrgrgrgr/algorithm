#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;

	int* trees = new int[N];
	int* trees_growth = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> trees[i];
	}
	
	sort(trees, trees + N);

	for (int i = 0; i < N; i++) {
		trees_growth[i] = (trees[i]-i);
	}

	int max = trees_growth[0];
	for (int i = 1; i < N; i++) {
		if (max < trees_growth[i]) {
			max = trees_growth[i];
		}
	}

	cout << max + N + 1;

	return 0;
}
