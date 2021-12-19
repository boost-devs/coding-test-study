#include <iostream>
using namespace std;

int arr[12];
void dp() {
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;
	for (int i = 4; i < 12; i++) {
		arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
	}
}

int main() {
	int T,n; cin >> T;
	dp();
	while (T--) {
		cin >> n;
		cout << arr[n] << "\n";
	}
}