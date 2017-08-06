import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.*;

class WordNode{
    String word;
    int numSteps;
    WordNode pre;
 
    public WordNode(String word, int numSteps, WordNode pre){
        this.word = word;
        this.numSteps = numSteps;
        this.pre = pre;
    }
}
 
public class maxPointsInLine {

	public static void main(String[] args) {
		String [] dict = {
			"hug", "hit",
			"pig", "bud",
			"pit", "bag",
			"put", "gag",
			"hat", "gay",
			"bat", "god",
			"bad", "git",
			"dad", ""
		};
	}

    public List<List<String>> findLadders(String start, String end, Set<String> dict) {
        List<List<String>> result = new ArrayList<List<String>>();
 
        LinkedList<WordNode> queue = new LinkedList<WordNode>();
        queue.add(new WordNode(start, 1, null));
 
        dict.add(end);
 
        int minStep = 0;
 
        HashSet<String> visited = new HashSet<String>();  
        HashSet<String> unvisited = new HashSet<String>();  
        unvisited.addAll(dict);
 
        int preNumSteps = 0;
 
        while(!queue.isEmpty()){
            WordNode top = queue.remove();
            String word = top.word;
            int currNumSteps = top.numSteps;
 
            if(word.equals(end)){
                if(minStep == 0){
                    minStep = top.numSteps;
                }
 
                if(top.numSteps == minStep && minStep !=0){
                    //nothing
                    ArrayList<String> t = new ArrayList<String>();
                    t.add(top.word);
                    while(top.pre !=null){
                        t.add(0, top.pre.word);
                        top = top.pre;
                    }
                    result.add(t);
                    continue;
                }
 
            }
 
            if(preNumSteps < currNumSteps){
                unvisited.removeAll(visited);
            }
 
            preNumSteps = currNumSteps;
 
            char[] arr = word.toCharArray();
            for(int i=0; i<arr.length; i++){
                for(char c='a'; c<='z'; c++){
                    char temp = arr[i];
                    if(arr[i]!=c){
                        arr[i]=c;
                    }
 
                    String newWord = new String(arr);
                    if(unvisited.contains(newWord)){
                        queue.add(new WordNode(newWord, top.numSteps+1, top));
                        visited.add(newWord);
                    }
 
                    arr[i]=temp;
                }
            }
 
 
        }
 
        return result;
    }
}

// class Solution {
// public:
//     vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
//         vector<vector<string>> res;
//         unordered_set<string> dict(wordList.begin(), wordList.end());
//         vector<string> p{beginWord};
//         queue<vector<string>> paths;
//         paths.push(p);
//         int level = 1, minLevel = INT_MAX;
//         unordered_set<string> words;
//         while (!paths.empty()) {
//             auto t = paths.front(); paths.pop();
//             if (t.size() > level) {
//                 for (string w : words) dict.erase(w);
//                 words.clear();
//                 level = t.size();
//                 if (level > minLevel) break;
//             }
//             string last = t.back();
//             for (int i = 0; i < last.size(); ++i) {
//                 string newLast = last;
//                 for (char ch = 'a'; ch <= 'z'; ++ch) {
//                     newLast[i] = ch;
//                     if (!dict.count(newLast)) continue;
//                     words.insert(newLast);
//                     vector<string> nextPath = t;
//                     nextPath.push_back(newLast);
//                     if (newLast == endWord) {
//                         res.push_back(nextPath);
//                         minLevel = level;
//                     } else paths.push(nextPath);
//                 }
//             }
//         }
//         return res;
//     }
// };

// class Point {
// 	public int x, y;
// 	public Point(int x, int y) {
// 		this.x = x;
// 		this.y = y;
// 	}
// }

// class Solution{
// 	public int maxPoints(Point[] points) {
// 		if (points==null) return 0;
// 		if (points.length<=2) return points.length;
		
// 		Map<Integer,Map<Integer,Integer>> map = new HashMap<Integer,Map<Integer,Integer>>();
// 		int result=0;
// 		for (int i=0;i<points.length;i++){ 
// 			map.clear();
// 			int overlap=0,max=0;
// 			for (int j=i+1;j<points.length;j++){
// 				int x=points[j].x-points[i].x;
// 				int y=points[j].y-points[i].y;
// 				if (x==0&&y==0){
// 					overlap++;
// 					continue;
// 				}
// 				int gcd=generateGCD(x,y);
// 				if (gcd!=0){
// 					x/=gcd;
// 					y/=gcd;
// 				}
				
// 				if (map.containsKey(x)){
// 					if (map.get(x).containsKey(y)){
// 						map.get(x).put(y, map.get(x).get(y)+1);
// 					}else{
// 						map.get(x).put(y, 1);
// 					}   					
// 				}else{
// 					Map<Integer,Integer> m = new HashMap<Integer,Integer>();
// 					m.put(y, 1);
// 					map.put(x, m);

// 				}
// 				System.out.println("max.x.y = " + y);
// 				max=Math.max(max, map.get(x).get(y));

// 			}
// 			result=Math.max(result, max + overlap + 1);
// 			System.out.println("result = " + result);

// 		}
// 		return result;
		
		
// 	}
// 	private int generateGCD(int a,int b){

// 		if (b==0) return a;
// 		else return generateGCD(b,a%b);
		
// 	}
// }

// public class maxPointsInLine {
// 	public static void main(String[] args) {
// 		Point [] points = new Point[10];
// 		for (int i = 0; i < points.length; ++i) {
// 			points[i] = new Point(0, i * i);
// 		}
// 		Solution sol = new Solution();
// 		int res = sol.maxPoints(points);
// 		System.out.println(res);
// 	}
// }