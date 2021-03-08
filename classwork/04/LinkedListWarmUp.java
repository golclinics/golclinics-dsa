class LinkedListWarmUp {

    public static void main(String args[]) {
        // Efficient way to create
        MyLinkedListManager linkedList = new MyLinkedListManager();

        // then use the access methods
        linkedList.addLast(linkedList, 3);
        linkedList.addLast(linkedList,10 );
        linkedList.addLast(linkedList, 5);
        linkedList.addLast(linkedList, 1);
        linkedList.addLast(linkedList, 6);

        printList(linkedList);
        System.out.println(listSum(linkedList));
    }


    static void printList(MyLinkedListManager linkedList){
        MyNode currentNode = linkedList.head;
        while(currentNode !=null){
            System.out.print(currentNode.data+ "\n");

            currentNode = currentNode.next;
        }
    }

    static int listSum(MyLinkedListManager linkedList){
        int sum = 0;
        MyNode currentNode = linkedList.head;
        while(currentNode!=null){
            sum+= currentNode.data;
            currentNode = currentNode.next;
        }
        return sum;
    }

    //node
    static class MyNode {
        int data;
        MyNode next;

        public MyNode(int data) {
            this.data = data;
            next = null;
        }
    }

    static class MyLinkedListManager {
        MyNode head; // start
        MyNode tail; // end

        public void addLast(MyLinkedListManager list, int data) {

            MyNode new_node = new MyNode(data);
            new_node.next = null;

            //check for null ( defensive programming )
            if (new_node == null)
                return;

            //if head is null start by creating head
            if(list.head == null){
                list.head = new_node;
            }else{
                //traverse till last node and insert node there
                MyNode currentNode = list.head;
                while(currentNode.next!=null){
                    currentNode = currentNode.next;
                }

                // insert at last
                currentNode.next = new_node;
            }

        }

    }
}
