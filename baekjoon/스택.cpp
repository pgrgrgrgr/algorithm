#include <iostream>
#include <string>
using namespace std;

int stack[10001];
int idx = 0;

void push(int a) {
	stack[idx] = a;
	idx += 1;
}

void pop() {
	if (idx == 0)cout << -1 << endl;
	else {
		cout << stack[idx - 1] << endl;
		idx -= 1;
	}
}

void size() {
	cout << idx << endl;
}

void empty() {
	if (idx) cout << 0 << endl;
	else cout << 1 << endl;
}

void top() {
	if (idx) cout << stack[idx - 1] << endl;
	else cout << -1 << endl;
}

int main() {
	int N;
	cin >> N;
	cin.ignore();

	string* instructions = new string[N];
	for (int i = 0; i < N; i++) {
		getline(cin, instructions[i]);
	}

	for (int i = 0; i < N; i++) {
		if (instructions[i][1] == 'u') {
			string tmp = "";
			for (int j = 5; j < instructions[i].length(); j++)tmp += instructions[i][j];
			int a = stoi(tmp);
			push(a);
		}

		else if (instructions[i][1] == 'o' && instructions[i][0] != 't')pop();
		else if (instructions[i][1] == 'i')size();
		else if (instructions[i][1] == 'm')empty();
		else if (instructions[i][0] == 't' && instructions[i][1] == 'o')top();
	}
}

