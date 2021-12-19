#include <iostream>
using namespace std;

int arr[1001];
int dp(int n) {
	if (arr[n] > 0) return arr[n];
	arr[n] = dp(n - 1) + dp(n - 2);
	arr[n] %= 10007;
	return arr[n];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	for (int i = 1; i < 3; i++)
		arr[i] = i;
	cout << dp(n);
}