#include <iostream>
#include <algorithm>
using namespace std;

int arr[1000001] = { 0, };
int dp(int n) {
	if (n == 1) return 0;
	if (arr[n] > 0) return arr[n];
	int tmp = 10000;
	if (n % 3 == 0) tmp = min(tmp, dp(n / 3) + 1);
	if (n % 2 == 0) tmp = min(tmp, dp(n / 2) + 1);
	arr[n] = min(tmp, dp(n - 1) + 1);
	return arr[n];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	arr[2] = 1; arr[3] = 1;
	cout << dp(n);
}
