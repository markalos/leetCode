
import java.util.*;

class UnionFind {
	int [] parents;
	UnionFind(int n) {
		parents = new int[n];
		for (int i = 0; i < n; ++i) {
			parents[i] = i;
		}
	}

	//from a to b
	boolean union(int root, int child) {
		parents[child] = find(root);
		return  (find(child) != child);
	}

	int find(int child) {
		if (parents[child] == child) {
			return child;
		}
		parents[child] = find(parents[child]);
		return parents[child];
	}
}