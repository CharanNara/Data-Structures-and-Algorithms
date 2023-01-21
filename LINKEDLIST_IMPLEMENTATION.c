#include<stdio.h>
#include<stdlib.h>

typedef struct node{
	int data;
	struct node *next;
} node;


node* link(int n){
	node *head = NULL;
	node *temp = NULL;
	node *p = NULL;
	int i;
	for(i=0;i<n;i++){
		temp = (node*)malloc(sizeof(node*));
		printf("Enter data %d",i+1);
		scanf("%d",&(temp->data));
		temp->next = NULL;
		if(head == NULL)
			head = temp;
		
		else{
			p = head;
			while(p->next != NULL){
				p = p->next;
				p->next = temp;
			}
		}
	}
	return head;
}

node* add_begin(){
	node* temp = NULL;
	temp = (node*)malloc(sizeof(node*));
	puts("Enter element to add at beginning");
	scanf("%d",&(temp->data));
	temp->next = head;
	head = temp;
}

node* add_end(node *head){
	node *temp = NULL;
	node *p = head;
	temp = (node *)malloc(sizeof(node*));
	puts("Enter node to add at end");
	scanf("%d",&(temp->data);
	while(p->next != NULL){
		p = p->next;
	}
	p->next = temp;
	temp->next = NULL;
	free(temp);
	return head;
}

node* del_begin(node* head){
	node* p = head;
	head = p->next;
	free(p);
	return head;
}

node* del_end(node* head){
	node* p = head;
	int i=1, counter = 0;
	while(p->next != NULL){
		p = p->next;
		counter++;
	}
	
	while(i<counter-1){
			p = p->next;
			i++;
		}
		p->next = NULL;
	}
	free(p);
	return head;
}

node* add_middle(node* head){
	int add_after;
	node* temp = NULL;
	node* store_node = NULL;
	node* p = head;
	temp = (node*)malloc(sizeof(node*));
	puts('Enter the element to add');
	scanf('%d',&temp->data);
	puts('Enter after which element to add');
	scanf('%d',&add_after);
	while(p->data != add_after){
		p = p->next;
	}
	store_node = p->next;
	p->next = temp;
	temp->next = store_node;
	free(p);
	return head;
}

int main()
{
	int n,ch;
	node *head = NULL;
	puts("Enter how many nodes");
	scanf("%d",&n);
	head = link(n);
	display(head)
	while(1){
		puts("Enter your choice");
		puts("1. Insert at begin\n2. Insert at end\n3. Delete at begin\n4. Delete at end\n5. Insert anywhere at middle\n6. Quit");
		scanf("%d",&ch);
		switch(ch){
			case 1: head = add_begin(head);
			display(head);
			break;
			
			case 2: head = add_end(head);
			display(head);
			break;
			
			case 3: head = del_begin(head);
			display(head);
			break;
			
			case 4: head = del_end(head);
			display(head);
			break;
			
			case 5: head = add_middle(head);
			display(head);
			break;
			
			case 6: exit(0);
			
			default: puts('Invalid input');
		}
	}
}