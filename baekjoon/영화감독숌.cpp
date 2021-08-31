#include <iostream>
#include <string>

int main() {
	int N;

	int i = 666;
	int series_num = 0;
	std::string target;

	std::cin >> N;

	while (1) {
		target = std::to_string(i);
		for (int j = 0; j < target.length() - 2; j++) {
			if (target[j] == '6' && target[j + 1] == '6' && target[j + 2] == '6') {
				series_num++;
				if (series_num == N) {
					std::cout << i;
					return 0;
				}
				break;
			}
		}
		i++;
	}
}
