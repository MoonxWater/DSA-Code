class Node {
    int data;
    Node next;

    Node(int data, Node next) {
        this.data = data;
        this.next = next;
    }

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedListPrac {
    private static Node convert_arr_to_LL(int[] arr) {
        Node head = new Node(arr[0]);
        Node mover = head;

        for (int i = 1; i < arr.length; i++) {
            Node temp = new Node(arr[i]);
            mover.next = temp;
            mover = temp;
        }
        return head;
    }

    public static void print(Node head) {
        Node temp = head;

        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }

    public static Node deleteHead(Node head) {
        head = head.next;
        return head;        
    }

    public static Node deleteTail(Node head) {
        Node temp = head;

        while (temp.next.next != null){
            temp = temp.next;
        }
        temp.next = null;
        return head;
    }

    public static Node insertHead(Node head, int val) {
        return new Node(val, head); 
    }

    public static void insertTail(Node head, int val) {
        while (head.next != null) {
            head = head.next;
        }

        head.next = new Node(val);
    }

    public static void main(String[] args) {
        int[] x = {12, 4, 6, 8};
        Node head = convert_arr_to_LL(x);

        head = deleteTail(head);
        
        head = insertHead(head, 50);
        insertTail(head, 99);
        
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }

    }
}