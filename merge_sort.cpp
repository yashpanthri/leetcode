#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& arr, int low, int mid,int high);
void mergeSort(vector<int>& arr, int low, int high) {
    if(low>= high){
        return;
    }
    int mid =(int) ((low+high)/2);
    mergeSort(arr, low,mid);
    mergeSort(arr, mid+1,high);
    merge(arr,low,mid, high);
}
void merge(vector<int>& arr, int low, int mid,int high){
    vector<int> temp;
    int left = low;
    int right=mid+1;
    while(left<=mid && right<=high){
        if(arr[left]<=arr[right]){
            temp.push_back(arr[left]);
            left++;
        }
        else{
            temp.push_back(arr[right]);
            right++;
        }
    }
        while(left<=mid){
            temp.push_back(arr[left]);
            left++;
        }
        while(right<=high){
            temp.push_back(arr[right]);
            right++;
        }

    for(int i = low; i<=high;++i){
        arr[i] = temp[i-low];
    }
}


int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    mergeSort(arr, 0, arr.size() - 1);

    for (int x : arr)
        cout << x << " ";
    return 0;
}