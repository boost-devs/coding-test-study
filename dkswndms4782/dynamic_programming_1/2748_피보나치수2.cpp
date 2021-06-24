#include <iostream>
using namespace std;

long long int arr[91] = {0,};
long long int dp(int n) {
	if (n < 2)
		return n;
	if (arr[n] > 0)
		return arr[n];
	arr[n] = dp(n - 1) + dp(n - 2);
	return arr[n];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	cout << dp(n);
}
