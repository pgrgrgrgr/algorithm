#include <iostream>
using namespace std;

int main() {
	int A, B;
	cin >> A >> B;

	int* nums = new int[B];

	int index = 0;
	int num = 1;
	while (!(B==index)) {
		for (int i = 0; i < num; i++) {
			nums[index] = num;
			index++;
			if (index == B)break;
		}
		num++;
	}

	int sum = 0;
	for (int i = A-1; i < B; i++) {
		sum += nums[i];
	}
	cout << sum;
	return 0;
}
