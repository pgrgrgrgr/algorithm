#include <iostream>

int main() {
	int a;
	int chk = 0;
	int tmp = 1;

	std::cin >> a;

	while (a > chk) {
		chk += tmp;
		tmp++;
	}
	if (tmp % 2 == 0) {
		std::cout << (chk - a + 1) << "/" << tmp - (chk - a + 1);
	}
	else {
		std::cout << tmp - (chk - a + 1) << "/" << chk - a + 1;
	}
	
	return 0;
}
