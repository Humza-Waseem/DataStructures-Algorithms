class  LinkList{
    public:
       List(void) { head = NULL;
       next = NULL
       
       }  //constructor
       List(void);
       bool isEmpty(){
        
        return head == NULL;


       }
       Node* insertNode(int index , int x);  // insert at a given index
       
       Node* insertAtHead(int x){// to insert at start of list
          head.insert(x);

        }
       Node* insertAtEnd(int x){
        start = head
        while(start != NULL){

            if(start == x){
                start.insert(x)
                // return start
            } 
            else{
              start = start.next
            }
        }
        // head.insert(x)
        
          
       }// to insert at end of list
       bool findNode(int x){
        Node = LinkList.get(x)
        return Node
       }

       bool deleteNode(int x){
        
        Node = LinkList.get(x)
        return Node
       }
       bool deleteFromStart()
       {
          Node = LinkList.head()
          Node.remove()
       }
       bool deleteFromEnd(){
        while(Node != null)
        Node = Node.next
       }
       if(Node.next == null)
       {
            Node.remove()
       }

       void displayList(void);
       Node* reverseList();
       Node* sortList();
       Node* removeDuplicates(Node* list);
       Node* mergeLists(Node* list1,Node* list2);
       Node* interestLists(Node* list1, Node* list2);
    private:
    Node* head;

};