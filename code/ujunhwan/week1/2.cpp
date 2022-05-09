#include <string>
#include <vector>
#include <iostream>

using namespace std;

int maxN;

int calc(vector<int> apeach, vector<int> lion) {
    int a = 0;
    int l = 0;
    
    for(int i = 0; i <= 10; i++) {
        if(apeach[i] == 0 && lion[i] == 0) continue;
        
        if(apeach[i] >= lion[i]) {
            a += 10-i;
        } else {
            l += 10-i;
        }
    }
    
    return l-a;
}

pair<int, vector<int> > bruteforce(int n, vector<int> apeach, vector<int> lion) {
    if(n < 0) return {-10000, vector<int>(11, 0)};
    
    if(n == 0) {
        return {calc(apeach, lion), lion};
    }
    
    pair<int, vector<int> > ret = {-100000, vector<int>(11, 0)};
    
    if(n == maxN) {
        for(int val = 1; val <= n; val++) {
            lion[10] += val;
            pair<int, vector<int> > cand = bruteforce(n-val, apeach, lion);
            lion[10] -= val;

            if(cand.first > ret.first) {
                ret = cand;
            } else if(cand.first == ret.first) {
                for(int k = 10; k >= 0; k--) {
                    if(cand.second[k] > ret.second[k]) {
                        ret = cand;
                        break;
                    } else if(cand.second[k] < ret.second[k]) {
                        break;
                    } else continue;
                }
            }
        }
    }
    
        
    for(int i = 0; i < 10; i++) {
        int toWin = apeach[i] - lion[i] + 1;
        if(toWin <= 0) continue;
        
        lion[i] += toWin;
        pair<int, vector<int> > cand = bruteforce(n-toWin, apeach, lion);
        lion[i] -= toWin; 
        
        if(cand.first > ret.first) {
            ret = cand;
        } else if(cand.first == ret.first) {
            for(int k = 10; k >= 0; k--) {
                if(cand.second[k] > ret.second[k]) {
                    ret = cand;
                    break;
                } else if(cand.second[k] < ret.second[k]) {
                    break;
                } else continue;
            }
        }
    }
    
    return ret;
}

vector<int> solution(int n, vector<int> info) {
    maxN = n;
    pair<int, vector<int> > answer = bruteforce(n, info, vector<int>(11, 0));
    if(answer.first > 0) {
        cout << answer.first << '\n';
        return answer.second;
    } else {
       	return vector<int>(1, -1);
    }
}