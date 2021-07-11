#include <iostream>
using namespace std;

int arr[21] = {0,};
int dp(int n) {
	if (n == 0)
		return 0;
	if (n == 1 || n == 2)
		return 1;
	if (arr[n] > 0)
		return arr[n];
	arr[n] = dp(n - 1) + dp(n - 2);
	return arr[n];
}

int main() {
	int n; cin >> n;
	cout << dp(n);
}