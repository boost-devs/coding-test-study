#include <iostream>
#include <cmath>
using namespace std;

unsigned long long factorial[31] = { 1, };
void make_factoral() {
	factorial[1] = 1;
	for (int i = 2; i <= 15; i++) {
		factorial[i] = factorial[i - 1] * i;
	}
	return;
}

unsigned long long num(int m,int n) {
	unsigned long long tmp = m;
	for (int i = m - 1; i > m - n; i--)
		tmp *= i;
	return tmp;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int T, n, m; cin >> T;
	make_factoral();
	while (T--) {
		cin >> n >> m;
		if (n == m) {
			cout << "1\n";
			continue;
		}
		if (n > (m-n))
			n = m - n;
		cout << num(m,n) / factorial[n] << "\n";
	}
}