#include <iostream>
#include <string>
using namespace std;

string VPS(string ps) {
	int opencnt = 0;
	int closecnt = 0;
	int cnt = 0;

	while (!((opencnt + closecnt > 1) && (opencnt == closecnt))) {
		if (cnt == ps.length()) {
			if (opencnt != closecnt)return "NO";
			else return "YES";
		}
		if (ps[0] == ')' || ps.length()%2!=0) return "NO";

		if (ps[cnt] == '(')opencnt++;
		else closecnt++;

		cnt++;
	}

	string tmp = "";
	for (int i = cnt; i < ps.length(); i++) {
		tmp += ps[i];
	}

	return VPS(tmp);
}

int main() {
	int T;
	cin >> T;

	string* testlist = new string[T];
	for (int i = 0; i < T; i++) {
		cin >> testlist[i];
		cout << VPS(testlist[i]) << endl;
	}

	return 0;
}
