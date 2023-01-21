// Implementing Stack using Arrays

#include<iostream>
using namespace std;

struct stack{
	int top;
	int capacity;
	int *elements;
}stack;

stack* create_stack(int capacity){
	stack* s;
	s = (stack*)malloc(sizeof(stack*));
	s->capacity = capacity;
	s->top = -1;
	s->elements = (int*)malloc(sizeof(int)*s->capacity);
	return s;
}

int isfull(stack* s){
	if(s->top == s->capacity - 1)
		return 1;
	else
		return 0;
}

int isempty(stack* s){
	if(s->top == -1)
		return 1;
	else
		return 0;
}

void push(stack* s, int item){
	if(!isfull(s)){
		s->top++;
		s->elements[s->top] = item;
	}
	else
		cout<<"Stack overflow"<<endl;
}

int pop(stack* s){
	int item;
	if(!isempty(s)){
		item = s->elements[s->top];
		s->top--;
		return item;
	}
	else
		return -1;
}

void display(stack* s){
	int i;
	for(i=0;i <= s->top;i++){
		cout<<s->elements[i]<<' ';
	}
	cout<<endl;
}

int main(){
	int n, ch, item;
	stack *s;
	cout<<'Enter how many elements'<<endl;
	cin>>n;
	s = create_stack(n);
	while(1){
		cout<<"Enter your choice"<<endl;
		cout<<"1. PUSH\n2. POP\n3. Display\n4. Quit"<<endl;
		cin>>ch;
		switch(ch){
			case 1: cout<<"Enter element value to push"<<endl;
			cin>>item;
			push(s,item);
			break;
			
			case 2: item = pop(s);
			if(item == -1)
				cout<<"Stack Underflow"<<endl;
			else
				cout<<item<<" is popped"<<endl;
			break;
			
			case 3: display(s);
			break;
			
			case 4: exit(0);
			
			default: cout<<"Invalid Input"<<endl;
		}
	}
}