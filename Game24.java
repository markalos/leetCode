import java.util.*;

public class Game24 {

	final double eps = 0.001;
	List<String> operator;
	private void swap(double [] data, int i, int j) {
		double tmp  = data[i];
		data[i] = data[j];
		data[j] = tmp;
	}
	private boolean judgePoint24(double [] nums, int pos, int end) {
		if (pos == end) {
			
			return Math.abs(nums[pos] - 24.0) < eps;
		}
		for (int i = pos; i <= end; ++i) {
			swap(nums, i, pos);
			double vpos = nums[pos]; // sets wrongly to nums[i] at first
			for (int j = pos + 1; j <= end; ++j) {
				//j == i is wrong!!!!
				double vj = nums[j];
				nums[j] = vpos - vj;
				
				if (judgePoint24(nums, pos + 1, end)) {
					return true;
				}
				
				if (Math.abs(vj) > eps) {
					nums[j] = vpos / vj;
					
					if (judgePoint24(nums, pos + 1, end)) {
						return true;
					}
					
				}
				nums[j] = vpos * vj;
				
				if (judgePoint24(nums, pos + 1, end)) {
					return true;
				}
				
				nums[j] = vpos + vj;
				
				if (judgePoint24(nums, pos + 1, end)) {
					return true;
				}
				
				nums[j] = vj;
			}
			swap(nums, i, pos);
		}
		return false;
	}
	public boolean judgePoint24(int[] nums) {
		double [] data = new double[nums.length];
		for (int i = 0; i < data.length; ++i) {
			data[i] = nums[i];
		}
        return judgePoint24(data, 0, nums.length - 1);
    }
}