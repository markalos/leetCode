public class ListNode {
	int val;
	ListNode next;
	ListNode(int x) {
		val = x;
	}
	public String toString() {
		return String.format("%d", val) + ((next != null) ? "," + next.toString() : "null");
	}
}