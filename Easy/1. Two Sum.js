/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let temp = [...nums];
    nums.sort(function(a, b){return a-b;});
    
    let l = 0, r = nums.length - 1; 
    for(let i = 0; i < nums.length; i++) {
        if(nums[l] + nums[r] == target){
            l = nums[l];
            r = nums[r];
            break;
        }
        else if(nums[l] + nums[r] > target) 
            r--;
        else
            l++;
    }

    let res = [];
    for(let i = 0; i < temp.length; i++) {
        if(temp[i] == l || temp[i] == r)
            res.push(i);
    }
    return res;
};

console.log(twoSum([25,5,11,4], 9));
