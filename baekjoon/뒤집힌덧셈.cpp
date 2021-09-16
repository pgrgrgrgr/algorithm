#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int Rev(int x);
int Rev(int x) {
	int revnum;

	string tmp = to_string(x);
	reverse(tmp.begin(), tmp.end());

	revnum = stoi(tmp);
	return revnum;
}

int main() {
	int x, y;
	cin >> x >> y;
	cout << (Rev(Rev(x) + Rev(y)));

	return 0;
}
