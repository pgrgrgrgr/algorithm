#include <iostream>
#include <stack>
using namespace std;

int main() {
	stack<int> nums;
	stack<char> outputs;

	int N;
	cin >> N;
	cin.ignore();

	int input;
	int idx = 1;

	do
	{
		cin >> input;
		if (!(nums.size())) {
			for (int i = 1; i <= input; i++) {
				nums.push(i); outputs.push('+');
				idx++;
			}
			nums.pop(); outputs.push('-');
		}
		else if (nums.top() < input) {
			for (int i = idx; i <= input; i++) {
				nums.push(i); outputs.push('+');
				idx++;
			}
			nums.pop(); outputs.push('-');
		}
		else if (nums.top() == input) {
			nums.pop(); outputs.push('-');
		}
		else {
			cout << "NO";
			return 0;
		}
	} while (nums.size());

	

	return 0;
}
