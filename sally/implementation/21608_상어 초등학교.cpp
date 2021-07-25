/*
# Implementation
# Problem: 21608
# Memory: 2028KB
# Time: 4ms
*/
#include <iostream>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;

#define MAX 20

int N, target;
int arr[MAX][MAX] = {0,};
int xy[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
int cand[MAX * MAX + 1][4] = {0,};
int score[5] = {0, 1, 10, 100, 1000};

void select_dir(){
	int result_x = N-1, result_y = N-1;
	int friend_cell = 0;
	int empty_cell = 0;
	for(int i = N-1; i >= 0; i--){
		for(int j = N-1; j >= 0; j--){
			if (arr[i][j] == 0){
				int empty_tmp = 0;
				int friend_tmp = 0;
				for (int k = 0; k < 4; k++){
					int x = i + xy[k][0];
					int y = j + xy[k][1];
					if(0 <= x && x < N && 0 <= y && y < N){
						if(arr[x][y] == 0) empty_tmp++;
						for(int t = 0; t < 4; t++)
							if(arr[x][y] == cand[target][t]) friend_tmp++;
					}
				}
				if (friend_cell < friend_tmp || (friend_cell == friend_tmp && empty_cell <= empty_tmp)) {
					result_x = i;
					result_y = j;
					friend_cell = friend_tmp;
					empty_cell = empty_tmp;
				}
			}
		}
	}
	arr[result_x][result_y] = target;
}

int get_score(){
	int result = 0;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++){
			int cnt = 0;
			for (int k = 0; k < 4; k++){
				int x = i + xy[k][0];
				int y = j + xy[k][1];
				if(0 <= x && x < N && 0 <= y && y < N){
					for(int t = 0; t < 4; t++)
						if(arr[x][y] == cand[arr[i][j]][t]) cnt++;
				}
			}
			result += score[cnt];
		}

	return result;
}

int main(void) {
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N;
	for(int i = 0; i < N*N; i++){
		cin >> target;
		cin >> cand[target][0] >> cand[target][1] >> cand[target][2] >> cand[target][3];

		if (i == 0) arr[1][1] = target;
		else select_dir();
	}
		
	int result = get_score();
	cout << result << '\n';

	return 0;
}
