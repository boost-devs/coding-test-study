#include <iostream>
using namespace std;

int arr[1001];
int dp(int n) {
	if (n == 1) return 1;
	if (n == 2) return 3;
	if (arr[n] > 0) return arr[n];
	arr[n] = dp(n - 1) + dp(n - 2)*2;
	arr[n] %= 10007;
	return arr[n];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	cout << dp(n);
}