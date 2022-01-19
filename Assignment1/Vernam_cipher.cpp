#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void print_vector(vector<int> v)
{
    for(int i=0;i<v.size()-1;i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<v[v.size()-1]<<endl;
}
void print_string(string v)
{
    for(int i=0;i<v.size()-1;i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<v[v.size()-1]<<endl;
}
vector<int> Text_to_Numbers(string x)
{
    int i;
    vector<int> t;
    for(i=0;i<x.size();i++)
    {
        if(x[i]>='A' && x[i]<='Z')
        t.push_back(x[i]-'A');
        else if(x[i]>='a' && x[i]<='z')
        t.push_back(x[i]-'a');
    }
    return t;
}
string Numbers_to_Text(vector<int> t,string x)
{
    int i;
    string s;
    for(i=0;i<t.size();i++)
    {
        if(x[i]>='A' && x[i]<='Z')
        s+=(char)(t[i]+'A');
        else if(x[i]>='a' && x[i]<='z')
        s+=(char)(t[i]+'a');
    }
    return s; 
}
string Encrypt(string pl,string key)
{
    int i,sum;
    vector<int> p,k,d;
    string s;
    p=Text_to_Numbers(pl);
    k=Text_to_Numbers(key);
    for(i=0;i<p.size();i++)
    {
        sum=p[i]+k[i];
        if(sum>=26)
        sum=sum-26;
        d.push_back(sum);
    }
    cout<<"Plain text after conversion:"<<endl;
    print_string(pl);
    print_vector(p);
    cout<<"Key after conversion:"<<endl;
    print_string(key);
    print_vector(k);
    cout<<"After converting to numbers and adding key plain text is: "<<endl;
    print_vector(d);
    s=Numbers_to_Text(d,pl);
    return s;
}
string Decrypt(string ct,string key)
{
    int i,diff;
    vector<int> c,k,s;
    string s1;
    c=Text_to_Numbers(ct);
    k=Text_to_Numbers(key);
    for(i=0;i<c.size();i++)
    {
        diff=c[i]-k[i];
        if(diff<0)
        diff=diff+26;
        s.push_back(diff);
    }
    cout<<"Cipher text after conversion:"<<endl;
    print_string(ct);
    print_vector(c);
    cout<<"Key after conversion:"<<endl;
    print_string(key);
    print_vector(k);
    cout<<"After converting to numbers and subtracting key cipher text is: "<<endl;
    print_vector(s);
    s1=Numbers_to_Text(s,ct);
    return s1;
}
int main()
{
    string p,k,c,x;
    cout<<"Enter Plain Text:"<<endl;
    cin>>p;
    cout<<"Enter Key:"<<endl;
    cin>>k;
    cout<<endl;
    if(p.size()!=k.size())
    {
        cout<<"The Size of Key and Plain text do not match try again..."<<endl;
    }
    else
    {
        c=Encrypt(p,k);
        cout<<"Encrypted/Cipher text is: "<<endl;
        print_string(c);
        cout<<endl;
        x=Decrypt(c,k);
        cout<<"Decrypted/Plain text is: "<<endl;
        print_string(x);
        cout<<endl;
    }
    return 0;
}