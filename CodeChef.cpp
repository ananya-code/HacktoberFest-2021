//MEX element
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
    while (t--)
    {
        ll n, m, a, b=0;
        cin>>n>>m;
        vector<ll>ve;
        map<ll,ll>mp;
        for(ll i=0; i<n; i++)
        {
            cin>>a;
            if(a!=m)
            {
                ve.push_back(a);
                mp[a] = 1;
                b++;
            }
        }
        a=1;
        while(mp[a]==1)
            ++a;
        if(a!=m)
            b=-1;
        cout<<b<<endl;
    }
    return 0;
}
