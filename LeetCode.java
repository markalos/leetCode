import java.util.*;



class Solution {
	public ListNode reverseBetween(ListNode head, int m, int n) {
        if (n == m) {
        	return head;
        }
        ListNode mpre = head, npre = head;
        for (int i = 0; i < m - 1; ++i) {
        	mpre = mpre.next;
        }
        for (int i = 0; i < n - 1; ++i) {
        	npre = npre.next;
        }
        int tmp = mpre.val;
        mpre.val = npre.val;
        npre.val = tmp;
        return head;
    }
}

public class LeetCode {


	public static void main(String[] args) {
		Solution sol = new Solution();
		ListNode head = new ListNode(2);
		head.next = new ListNode(1);
		System.out.println(head);
		System.out.println(sol.reverseBetween(head, 1, 2));
	}
}
