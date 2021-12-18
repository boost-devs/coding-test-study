#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int n = numbers.size();
    
    for (int i = 0; i < (1 << (n)); i++) {
        int tmp = 0;
        for (int j = 0; j < n; j++)
            if (i & (1 << j)) tmp += numbers[j]; // 1
            else tmp -= numbers[j]; // 0
        if (tmp == target) answer++;
    }

    return answer;
}