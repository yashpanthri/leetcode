#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        int j = i;
        while(j>0 && arr[j-1]> arr[j]){
            int temp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j]= temp;
            j--;
        }
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    insertionSort(arr);

    for (int x : arr)
        cout << x << " ";
    return 0;
}