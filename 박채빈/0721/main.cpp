#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n,tmp;
    vector<int> arr;
    
    cin>>n;

    for(int i=0;i<n;i++){
        cin>>tmp;
        arr.insert(arr.begin()+n-tmp-1,i+1);
    }

    for(int i=0;i<n;i++)
        cout<<arr[i];


    return 0;
}