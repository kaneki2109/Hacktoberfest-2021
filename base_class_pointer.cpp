#include<iostream>
using namespace std;
class Base 
{
    public:
    void fun1()
    {cout<<"fun1"<<endl;}
};
class Derived:public Base
{ 
public:
        void fun2()
        {cout<<"fun2"<<endl;}

    };
int main()
{
    //Derived *d;
    //d=new Derived();
    //d->fun1();
    //d->fun2();
    //Derived b;
    //Base*d=&b;
    //d->fun1();
    //d->fun2();
    Base b;
    //Derived *d=&b;
   // d->fun1();
    //d->fun2();
}
   

