#include<iostream>
using namespace std;
#define OVERFLOW 1
#define UNDERFLOW 2
class Stack
{
    private:
        int capacity;
        int top;
        int* ptr;
    public:
        Stack(int);
        void Push(int);
        int Peek();
        int Pop();
        ~Stack();
        bool IsFull();
        bool IsEmpty();
        int GetSize();
        int GetCapacity();
        void Display();
};
void Reverse(Stack &stk);
Stack::Stack(int cap)
{
    capacity=cap;
    top=-1;
    ptr=new int[capacity];
}
void Stack::Push(int data)
{
    if(IsFull())
    {
        throw OVERFLOW;
    }
    top++;
    ptr[top]=data;
}
int Stack::Peek()
{
    if(top==-1)
    {
        throw UNDERFLOW;
    }
    return ptr[top];
}
int Stack::Pop()
{
    if(top==-1)
    {
        throw UNDERFLOW;
    }
    int temp=ptr[top];
    top--;
    return temp;
}
Stack::~Stack()
{
    while(ptr!=nullptr)
    {
        delete []ptr;
    }
}
bool Stack::IsFull()
{
    return top==capacity-1;
}
bool Stack::IsEmpty()
{
    return top==-1;
}
int Stack::GetSize()
{
    return top+1;
}
int Stack::GetCapacity()
{
    return capacity;
}
void Stack::Display()
{
    int i;
    for(i=0;i<=top;i++)
    {
        cout<<ptr[i]<<" ";
    }
}
void Reverse(Stack &stk)
{
    int v;
    Stack stk1(stk.GetCapacity());
    int size = stk.GetSize(); 
    for(int i = 0; i < size; i++)
    {
        v = stk.Pop();
        stk1.Push(v);
    }
    stk = stk1;
}
void Minimum_Value(Stack &stk)
{
    Stack stk1(stk.GetCapacity());
    int size=stk.GetSize();
    int min=ptr[0];
    for(int i=0;i<size;i++)
    {
        if()
    }
}
int main()
{
    Stack s1(5);
    s1.Push(2);
    s1.Push(88);
    Reverse(s1);
    s1.Display();
    //s1.Pop();
    //s1.Peek();
    cout<<endl;
    return 0;
}