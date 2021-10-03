#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int _max = 0;
        int _min = INT_MAX;
        for (int i = 0; i < prices.size();i++){
            _max = max(_max, prices[i]-_min);
            _min = min(_min, prices[i]);
        }
        return _max;
    }
};