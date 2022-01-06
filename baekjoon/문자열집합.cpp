#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M;
	cin >> N >> M;

	int cnt = 0;

	map<string, bool> mp;

	for (int i = 0; i < N; i++) {
		string str;
		cin >> str;
		mp[str] = true;
	}

	for (int i = 0; i < M; i++) {
		string str;
		cin >> str;
		if (mp[str])cnt++;
	}

	cout << cnt;
	return 0;
}
