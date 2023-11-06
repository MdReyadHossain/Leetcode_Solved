/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let cnt = 0;
    for(let i = s.length-1; i >= 0; i--) {
        if(s[i] == 'I')
            cnt += 1;
        
        else if(s[i] == 'V') {
            cnt += 5;
            if(s[i - 1] == 'I')
                {cnt -= 1; i--;}
        }
        else if(s[i] == 'X') {
            cnt += 10;
            if(s[i - 1] == 'I')
                {cnt -= 1; i--;}
        }
        else if(s[i] == 'L') {
            cnt += 50;
            if(s[i - 1] == 'X')
                {cnt -= 10; i--;}
        }
        else if(s[i] == 'C') {
            cnt += 100;
            if(s[i - 1] == 'X')
                {cnt -= 10; i--;}
        }
        else if(s[i] == 'D') {
            cnt += 500;
            if(s[i - 1] == 'C')
                {cnt -= 100; i--;}
        }
        else if(s[i] == 'M') {
            cnt += 1000;
            if(s[i - 1] == 'C')
                {cnt -= 100; i--;}
        }
    }
    return cnt;
};

console.log(romanToInt('LVIII'));