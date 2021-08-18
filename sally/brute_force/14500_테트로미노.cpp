/*
# Brute force
# Problem: 14500
# Memory: 3000KB
# Time: 48ms
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

#define MAX 501

int N, M;
int result = 0;
int arr[MAX][MAX] = {0,};
int coords[19][4][2] = {{{0, 0}, {0, 1}, {0, 2}, {0, 3}},
						{{0, 0}, {1, 0}, {2, 0}, {3, 0}},
						{{0, 0}, {1, 0}, {0, 1}, {1, 1}},
						{{0, 0}, {0, 1}, {0, 2}, {1, 2}}, 
						{{0, 0}, {1, 0}, {2, 0}, {0, 1}}, 
						{{0, 0}, {1, 0}, {1, 1}, {1, 2}},
						{{2, 0}, {0, 1}, {1, 1}, {2, 1}}, 
						{{1, 0}, {1, 1}, {1, 2}, {0, 2}}, 
						{{0, 0}, {0, 1}, {1, 1}, {2, 1}}, 
						{{0, 0}, {1, 0}, {0, 1}, {0, 2}},
						{{0, 0}, {1, 0}, {2, 0}, {2, 1}}, 
						{{0, 0}, {1, 0}, {2, 0}, {1, 1}}, 
						{{1, 0}, {0, 1}, {1, 1}, {1, 2}}, 
						{{0, 1}, {1, 0}, {1, 1}, {2, 1}},
						{{0, 0}, {0, 1}, {0, 2}, {1, 1}}, 
						{{0, 0}, {0, 1}, {1, 1}, {1, 2}}, 
						{{0, 1}, {1, 1}, {1, 0}, {2, 0}}, 
						{{1, 0}, {1, 1}, {0, 1}, {0, 2}}, 
						{{0, 0}, {1, 0}, {1, 1}, {2, 1}}};

int main(void){
	cin.tie(NULL);
    ios::sync_with_stdio(false);

	cin >> N >> M;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++) cin >> arr[i][j];
	
	for(int k = 0; k < 19; k++){ // select block
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++){ // select start loc
				int tmp = 0;
				for(int t = 0; t < 4; t++){
					int x = i + coords[k][t][0];
					int y = j + coords[k][t][1];
					if(x < 0 || N <= x || y < 0 || M <= y) {
						tmp = 0;
						break;
					}
					tmp += arr[x][y];
				}
				result = max(result, tmp);
			}
	}

	cout << result << '\n';

	return 0;
}