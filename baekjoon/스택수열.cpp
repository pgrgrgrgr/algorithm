#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
	stack<int> nums;
	string outputs = "";

	int N;
	cin >> N;
	cin.ignore();

	int input;
	int idx = 1;

	for (int i = 0; i < N; i++) {
		cin >> input;

		while (idx <= input) {
			nums.push(idx);
			idx += 1;
			outputs += '+';
		}

		if (nums.top() == input) {
			nums.pop();
			outputs += '-';
		}
		else {
			cout << "NO";
			return 0;
		}
	}

	for (int i = 0; i < outputs.length(); i++) {
		cout << outputs[i] << "\n";
	}

	

	return 0;
}
