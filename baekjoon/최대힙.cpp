#include<stdio.h>
#include<iostream>
#include<queue>

using namespace std;

int n;
priority_queue<int> pq;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    while (n--) { 
        int x; 
        cin >> x;
        if (x == 0) { 
            if (pq.empty()) cout << "0\n";
            else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else { 
            pq.push(x);
        }
    }
    return 0;
}

/*
#include <iostream>
#define HEAP_SIZE 100000

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
    if (heapCount == 0)return 0;

    int ret = heap[1];

    swap(&heap[1], &heap[heapCount]);
    heap[heapCount] = 0;
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

        if (j == 0) cout << pop();
        else push(j);
    }

    return 0;
} */
