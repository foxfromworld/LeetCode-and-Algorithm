/**
* Source : https://leetcode.com/problems/reverse-integer/
* Author : foxfromworld
* Date  : 27/09/2021
* First attempt
*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    ret = Math.abs(x).toString().split('').reverse().join('')
    if (ret > 2147483648) return 0
    return Math.sign(x) * ret 
};
