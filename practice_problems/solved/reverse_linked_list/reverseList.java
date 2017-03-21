/**
 * John's solution for reversing a linked list in Java
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode next;

        // Check if list is 0 or 1 long. If so, reversal is done already
        if(head == null || head.next == null) { return head; }

        // Remember the old "next", point the current node to the one before it, then jump to the old next node. Repeat
        while(head.next != null) {
            next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        
        // Final node - point it at the previous node
        head.next = prev;
        
        // return the final node, now the first in the reversed list
        return head;
    }
}