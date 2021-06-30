#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int N; cin >> N;
	int num[1001];
	int length[1001] = {0,};
	for (int i = 0; i < N; i++) cin >> num[i];
	int max = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < i; j++) {
			if (num[j] < num[i] && length[j] >= length[i]) length[i] = length[j] + 1;
		}
		if (length[i] == 0) length[i] = 1;
		if (max < length[i]) max = length[i];
	}
	cout << max;
}