class q {
    int front = -1;
    int rear = -1;
    int[] queue = {};
    int n = 5;

    void insert(int val) {
        if (front == -1 && rear == -1) {
            front++;
            rear++;
            queue[rear] = val;
        } else if (rear < n - 1) {
            rear++;
            queue[rear] = val;
        } else if (rear < n && rear % n < front - 1) {
            rear++;
            rear = rear % n;
            queue[rear] = val;
        } else {
            System.out.println("Queue Overflow");
        }
    }

    void pop() {
        if (front == -1) {
            System.out.println("Queue Underflow");
        } else if (front < rear) {
            front++;
        } else if (front > rear) {

        }
    }
}

public class Qu {
    public static void main(String[] args) {
        q queue = new q();
        queue.insert(5);
        queue.insert(10);
    }
}