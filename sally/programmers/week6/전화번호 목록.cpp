#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    int size_ = phone_book.size();
    sort(phone_book.begin(), phone_book.end());
    
    for (int i = 0; i < size_-1; i++) {
        int s = phone_book[i].size();
        if (phone_book[i].compare(phone_book[i+1].substr(0, s)) == 0) 
            return false;
    }

    return answer;
}