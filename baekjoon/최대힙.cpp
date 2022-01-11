#include <iostream>
#define HEAP_SIZE 256
#define ARRAY_SIZE 10

using namespace std;
int heap[HEAP_SIZE];
int heapCount = 0;

void swap(int* a, int* b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void push(int x) {
    heap[++heapCount] = x;

    int child = heapCount;
    int parent = child / 2;

    while (child > 1 && heap[child] > heap[parent]) {
        swap(&heap[child], &heap[parent]);
        child = parent;
        parent = child / 2;
    }

}

int pop() {
    int ret = heap[1];

    swap(&heap[1], &heap[heapCount]);
    heapCount = heapCount - 1;
    

    int parent = 1;
    int child = parent * 2;

    if (child + 1 <= heapCount) {
        child = (heap[child] > heap[child + 1]) ? child : child + 1;
    }

    while (child <= heapCount && heap[child] > heap[parent]) {
        swap(&heap[child], &heap[parent]);
        parent = child;
        child = parent * 2;

        if (child + 1 <= heapCount) {
            child = (heap[child] > heap[child + 1]) ? child : child + 1;
        }
    }

    return ret;
}


int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int j;
        cin >> j;
        if (j == 0) {
            if (heap[1] == 0)cout << 0;
            else cout << pop();

        }
        else {
            push(j);
        }
    }
    return 0;
}
