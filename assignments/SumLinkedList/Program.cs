using System;

class LinkedList
{
	public static int sum = 0;

	// A Linked list node / 
	public class Node
	{
		public int data;
		public Node next;

		public Node() {

		}

		public Node(int i)
        {
			data =  i;
			next = null;
        }
	}

	// function to insert a node at the 
	// beginning of the linked list 
	static Node addNode(Node head_node, int new_data)
	{
		// allocate node / 
		Node new_node = new Node();

		// put in the data / 
		new_node.data = new_data;

		// link the old list to the new node / 
		new_node.next = (head_node);

		// move the head to point to the new node / 
		(head_node) = new_node;

		return head_node;
	}

	static void addToLast(Node head_node, int newData)
    {

		//Node new_node = new Node(newData);

		//Node currentNode = head_node;

        if (head_node.next == null)
        {
			head_node.next = new Node(newData);
        }
        else
        {
			addToLast(head_node.next, newData);
        }

  //      while (currentNode.next != null)
  //      {
		//	currentNode = currentNode.next;
  //      }
		//currentNode.next = new_node;
	}

	private Node Remove(Node headNode, int nodeValue)
	{
		Node currentNode = headNode;

		if (currentNode == null)
		{
			//throw new Exception("Node not found");
			return null;
		}
		else if (currentNode != null && currentNode.data == nodeValue)
		{
			currentNode = currentNode.next;
		}
		else
		{
			// Recursive call to the current function.
			currentNode.next = Remove(currentNode.next, nodeValue);
		}
		return currentNode;
	}

	// utility function to find the sum of nodes 
	static int sumOfNodesUtil(Node head)
	{
		sum = 0;

		// find the sum of nodes 
		//sumOfNodes(head);

		// if head = null 
		if (head == null)
			Console.WriteLine("Linked List cant be empty");

        while (head != null)
        {
			sum = sum + head.data;
			head = head.next;
        }

		// required sum 
		return sum;
	}

	// Driver program to test above 
	public static void Main(String[] args)
	{
		Node head = null;

		bool firstNode = true;

		// create linked list 7.6.8.4.1 
		head = addNode(head, 7);
		head = addNode(head, 6);
		head = addNode(head, 7);
		head = addNode(head, 4);
		head = addNode(head, 1);

		addToLast(head, 9);




		Console.WriteLine("Sum of nodes = " +
						sumOfNodesUtil(head));

		

		while (head!= null)
		{
			if (!firstNode)
			{
				Console.Write(" -> " + head.data);
				head = head.next;
			}
            else
            {
				
				Console.Write(head.data);
				firstNode = false;
				head = head.next;
			}

		}

       

		Console.ReadLine();
	}
}

