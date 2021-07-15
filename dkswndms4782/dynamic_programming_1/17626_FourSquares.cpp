#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int arr[50001] = { 0, };
	int n; cin >> n;
	for (int i = 1; i < 4; i++)
		arr[i] = i;
	for (int i = 4; i <= n; i++)
		arr[i] = 5;

	for (int i = 2; i*i <= n; i++) {
		arr[i*i] = 1;
		for (int j = i * i + 1; j < pow(i + 1, 2); j++) {
			for (int k = i; k > 1; k--) {
				arr[j] = min(arr[j], arr[k * k] + arr[j - k * k]);
			}
		}
	}
	cout << arr[n];
}