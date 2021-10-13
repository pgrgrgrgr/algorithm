#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;

	int five = N / 5;
	int three = 0;

	while (five >= 0) {
		int mod;
		mod = N - five*5;
		if (mod == 0) {
			cout << five;
			return 0;
		}
		else {
			while (mod > 0) {
				mod -= 3;
				three++;
			}
			if (mod == 0)break;
		}
		five--;
		three = 0;
	}

	int res = five + three;
	cout << res;

	return 0;
}
