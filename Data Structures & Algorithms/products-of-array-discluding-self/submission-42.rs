impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = vec![1; n];

        let mut prefix = 1;
        for i in 0..n {
            unsafe { *res.get_unchecked_mut(i) = prefix; }
            prefix *= unsafe { *nums.get_unchecked(i) };
        }

        let mut postfix = 1;
        for i in (0..n).rev() {
            unsafe { *res.get_unchecked_mut(i) *= postfix; }
            postfix *= unsafe { *nums.get_unchecked(i) };
        }

        res
    }
}