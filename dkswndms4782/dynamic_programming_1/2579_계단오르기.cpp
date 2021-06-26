#include <iostream>
#include <algorithm>
using namespace std;

//현재 한칸이면 [n][1], 현재 두칸째이면 [n][2]
int score[301][3] = { (0,0,0), };

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int N; cin >> N;
	for (int i = 1; i <= N; i++)
		cin >> score[i][0];
	score[1][1] = score[1][0];
	score[2][1] = score[2][0];  score[2][2] = score[1][1] + score[2][0];
	for (int i = 3; i <= N; i++) {
		score[i][2] = score[i - 1][1] + score[i][0];
		score[i][1] = max(score[i - 2][1], score[i - 2][2]) + score[i][0];
	}
	cout << max(score[N][1], score[N][2]);
}