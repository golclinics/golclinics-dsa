#include <bits/stdc++.h>

using namespace std;

// The rotation helper can rotate both left and right, all we have to do is 
// state the direction of rotation
vector<int> rotateHelper(const vector<int> &a, int &d, const bool isRightRotation = false){
    // If we are doing a right rotation flip the way we are calculating
    // the index
    d = isRightRotation ? -d : d;
    
    // If the number of rotations is equal to array size
    // then the rotation will not do anything therefore
    // we return the original array
    if(d % a.size() == 0){
        return a;
    }
    
     // Get the array_size
    int array_size = a.size();
      
    // Create a temporary vector for swapping
    // in O(n)
    vector<int> temp(array_size);
    
    // Loop over each element in the original array
    for(int i = 0; i < array_size; ++i){
        int calculated_index = (array_size + (i + d)) % array_size;
        
        temp[i] = a[calculated_index];
    }
    
    return temp;
}

// Complete the rotLeft function below.
vector<int> rotLeft(vector<int> a, int d) {
    return rotateHelper(a, d);
}
