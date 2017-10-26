import java.util.*;


class ReverseListInRange {


	public ListNode reverseBetween(ListNode head, int m, int n) {
        if (n == m) {
        	return head;
        }
        System.out.println(head);
        ListNode mpre = new ListNode(0);
        ListNode psudoHead = mpre;
        mpre.next = head;
        for (int i = 0; i < m - 1; ++i) {
        	mpre = mpre.next;
        }
        ListNode cur = mpre.next;
        ListNode next = null;
        mpre.next = null;
        for (int i = 0; i < n - m + 1; ++i) {
        	next = cur.next;
        	cur.next = mpre.next;
        	mpre.next = cur;
        	cur = next;
        }
        //foget to untie the circle formed in process of rearrange
        while(mpre.next != null) {
        	mpre = mpre.next;
        }
        mpre.next = next;
        return psudoHead.next;
    }

	public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(3);
		ReverseListInRange sol = new ReverseListInRange();
		System.out.println(sol.reverseBetween(head, 2, 3));
	}
}