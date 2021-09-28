#include <iostream>
using namespace std;


int main(void) {
    string board;
    cin >> board;

    string ans = "";
    int i = 0;
    int cnt = 0;
    while (i < board.length()) {
        if (board[i] == '.') {
            i++;
            ans += '.';
        }
        for (int j = i; j < board.length() && board[j] == 'X'; j++) {
            cnt++;
        }
        if (cnt % 2 != 0) {
            cout << -1;
            return 0;
        }
        i += cnt;

        while (true) {
            if (cnt >= 4) {
                ans += "AAAA";
                cnt -= 4;
            }
            else if (cnt == 2) {
                ans += "BB";
                cnt -= 2;
            }
            else {
                break;
            }
        }
    }

    cout << ans;
}
