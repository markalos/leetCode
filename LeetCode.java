import java.util.*;



class Solution {

	public int lengthOfLongestSubstring(String s) {
        char [] data = s.toCharArray();
        if (data.length < 2) {
        	return data.length;
        }
        int [] position = new int[256];
        Arrays.fill(position, -1);
        int tmp = 0;
        int ans = 1;
        for (int i = 0; i < data.length; ++i) {
        	tmp = Math.min(tmp + 1, i - position[data[i]]);
        	position[data[i]] = i;
        	if (tmp > ans) {
        		ans = tmp;
        	}
        }
        return ans;
    }

	public int[] findRedundantDirectedConnection(int[][] edges) {
        int hasInEdge [] = new int [edges.length + 1];
        UnionFind uf = new UnionFind(edges.length + 1);
        int ans [] = new int[2];
        for (int [] edge : edges) {
        	if(hasInEdge[edge[0]] > 0) {
        		ans[0] = hasInEdge[edge[0]];
        		ans[1] = edge[1];
        		continue;
        	}
        	hasInEdge[edge[0]] = edge[1];
        	// graph.get(edge[0]).add(edge[1]);
        }
        for (int [] edge : edges) {
        	if (!uf.union(edge[0], edge[1])) {
        		System.out.println("union failed " + Arrays.toString(edge));
        		if (ans[0] != 0) {
        			ans[1] = hasInEdge[ans[0]];
        		}
        		return edge;
        	}
        }
        //  = new int[2];
        // dfs(graph, new boolean[edges.length + 1], ans, 1);
        return ans;
    }
}

public class LeetCode {


	public static void main(String[] args) {
		Solution sol = new Solution();
		ListNode head = new ListNode(2);
		head.next = new ListNode(1);
		System.out.println(head);
		int data [] = {9, 9, 4, 7};
		int edges[][] = {{2, 1}, {3, 1}, {4, 2}, {1, 4}, {1, 5}};
		System.out.println(sol.lengthOfLongestSubstring("qgq"));

	}
}

