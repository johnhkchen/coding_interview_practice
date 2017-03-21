public class Solution {
    public void deleteNode(ListNode node) {
        // Copy value from next node, point to its next
        node.val = node.next.val;
        node.next = node.next.next;
    }
}