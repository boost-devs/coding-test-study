#include <iostream>
#include<algorithm>
using namespace std;

int arr[5001] = { 0, };
int dp(int n) {
	arr[3] = 1; arr[5] = 1;
	for (int i = 6; i <= n; i++) {
		if (arr[i - 3]) arr[i] = arr[i - 3] + 1;
		if (arr[i - 5] && arr[i] != 0) arr[i] = min(arr[i], arr[i - 5] + 1);
		else if (arr[i - 5] && arr[i] == 0) arr[i] = arr[i - 5] + 1;
	}
	return arr[n];
}

int main() {
	int n; cin >> n;
	if (n <= 2 || n == 4)
		cout << "-1";
	else if (n == 3 || n == 5)
		cout << "1";
	else {
		dp(n);
		cout << ((arr[n] != 0) ? arr[n] : -1);
	}
}