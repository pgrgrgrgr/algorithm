#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;

	int n_mod, n_div;
	n_mod = n % 14;
	n_div = n / 14;

	if (n_mod == 1 || n_mod == 13)	cout << "baby" << endl;
	else if (n_mod == 2 || n_mod == 14 || n_mod == 0)	cout << "sukhwan" << endl;
	else if (n_mod == 5)	cout << "very" << endl;
	else if (n_mod == 6)	cout << "cute" << endl;
	else if (n_mod == 9)	cout << "in" << endl;
	else if (n_mod == 10)	cout << "bed" << endl;
	else {
		if (n_mod == 3 || n_mod == 7 || n_mod == 11) {
			if (n_div < 3) {
				cout << "tururu";
				for (int i = 1; i <= n_div; i++)
					cout << "ru";
			}
			else {
				cout << "tu+ru*" << (n_div + 2);
			}
		}
		else if (n_mod == 4 || n_mod == 8 || n_mod == 12) {
			if (n_div < 4) {
				cout << "turu";
				for (int i = 1; i <= n_div; i++)
					cout << "ru";
			}
			else	cout << "tu+ru*" << (n_div + 1);
		}
	}
}
