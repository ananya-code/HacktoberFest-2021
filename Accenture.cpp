#include <iostream>
#include <map>
#include <cstring>
#include <utility>
#include <set>
#include <vector>
#define ll long long
#define mod 1000000007
using namespace std;

int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        int m, n, sum=0;
        cout<<"Enter the value of m and n: "<<endl;
        cin>>m>>n;
        for(int i = m; i<=n; i++)
        {
            if((i%3==0)&&(i%5==0))
            {
                sum=sum+i;
            }
        }
        cout<<sum;
    }
    return 0;
}