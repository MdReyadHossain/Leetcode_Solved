/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let res = 0, n, y = x;

    while(y > 0) { 
        n = parseInt(y / 10);
        res = (res * 10) + (y % 10);
        y = n;
        console.log(res);
    }

    if (res == x && x >= 0) 
        return true;
    else
        return false;
}

console.log(isPalindrome(123));