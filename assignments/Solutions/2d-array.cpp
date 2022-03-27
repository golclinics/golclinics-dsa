#include <bits/stdc++.h>
#include <stddef.h>
#include <cstdio>
using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    int highest_sum = -INT_MAX;
    
    for(size_t i = 0; i < arr.size() - 2; ++i){
        for(size_t j = 0; j < arr[0].size() - 2; ++j){
           // First row
           int first_row_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2];
           
           // Second row
           int second_row_value = arr[i + 1][j + 1];
           
           // Third row
           int third_row_sum = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
           
           // Get the total sum
           int total_sum = first_row_sum + second_row_value + third_row_sum;
            
           // Highest sum
           highest_sum = total_sum > highest_sum ? total_sum: highest_sum;
        }
    }  
    
    return highest_sum; 
}