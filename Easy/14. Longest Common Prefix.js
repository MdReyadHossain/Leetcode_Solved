/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let str = "", s = [], isValid = true;

    strs.forEach((ele) => {
        s.push(ele.length);
    })
    let minStrs = Math.min(...s);

    for (let i = 0; i < minStrs; i++) {
        for (let j = 0; j < strs.length - 1; j++) {
            if (strs[j][i] !== strs[j + 1][i])
                return str;
        }
        str += strs[0][i];
    }

    return str;
};