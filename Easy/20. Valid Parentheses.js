/**
 * @param {string} s
 * @return {boolean}
 */

var isValid = function (s) {
    let str = [], x;
    for (let i = 0; i < s.length; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            str.push(s[i]);

        else {
            x = str.pop()
            if (s[i] == ')' && x != '(')
                return false;

            else if (s[i] == '}' && x != '{')
                return false;

            else if (s[i] == ']' && x != '[')
                return false;
        }
    }
    if (str.length == 0)
        return true;

    else
        return false;
};