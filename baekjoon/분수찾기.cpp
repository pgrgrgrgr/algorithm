#include <iostream>

int main() {
	int a;
	int chk = 1;
	int tmp = 1;
	
	std::cin >> a;

	while (a > chk) {
		chk += tmp;
		tmp++;
	}
	std::cout << chk - a / tmp - (chk - a);

	return chk - a / tmp - (chk - a);

}
