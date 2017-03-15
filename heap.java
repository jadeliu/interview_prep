package dataStructure;

/**
 * Created by jadeliu on 3/15/17.
 */
import java.util.PriorityQueue;
import java.util.Comparator;

public class heap {

    static class MaxHeapComparator implements Comparator<Integer>{
        public int compare(Integer a, Integer b){
            return b-a;
        }
    }

    public static void main(String[] argv){
        PriorityQueue<Integer> minHeap=new PriorityQueue<Integer>();
        PriorityQueue<Integer> maxHeap=new PriorityQueue<Integer>(10, new MaxHeapComparator());

        for(int i=0; i<10; i++){
            minHeap.add(i);
            maxHeap.add(i);
            System.out.println("min heap peek value = "+minHeap.peek());
            System.out.println("max heap peek value = "+maxHeap.peek());

        }

    }
}
