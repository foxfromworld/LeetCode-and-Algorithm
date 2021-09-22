# Source : https://leetcode.com/problems/two-sum/
# Author : foxfromworld
# Date  : 21/09/2021
# First attempt

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var visited =  {}
    for (let i = 0; i < nums.length; i++){
        remain = target - nums[i]
        if (remain in visited) {
            return [i, visited[remain]]
        }else{
            visited[nums[i]] = i
        }
    }
};
