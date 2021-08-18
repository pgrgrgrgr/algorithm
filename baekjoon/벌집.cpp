#include <iostream>

int main() {
	int cnt = 1;
	int room_num = 1;
	int a;

	std::cin >> a;

	while (a > 1) {
		a -= 6 * cnt;
		room_num += 1;
		cnt += 1;
	}

	std::cout << room_num;

}
