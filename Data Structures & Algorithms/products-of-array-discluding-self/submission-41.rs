impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![1; n];

        // First pass: Calculate prefix products from left to right
        let mut prefix = 1;
        for i in 0..n {
            res[i] = prefix;
            prefix *= nums[i];
        }

        // Second pass: Multiply postfix products from right to left
        let mut postfix = 1;
        for i in (0..n).rev() {
            res[i] *= postfix;
            postfix *= nums[i];
        }

        res
    }
}