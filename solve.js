let numArr = [20, 5, 1, 45, 4];

numArr.sort();

numArr.sort(
    function(x, y) {
        return x - y;
    }
);