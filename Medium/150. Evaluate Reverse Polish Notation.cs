public class Solution
{
    public int EvalRPN(string[] tokens)
    {
        if (tokens.Length == 1)
        {
            return Convert.ToInt32(tokens[0]);
        }
        Stack stack = new Stack();
        int res = 0;
        foreach (string val in tokens)
        {
            int ascii = val.Length > 1 ? val[1] : val[0];
            if (ascii >= 42 && ascii <= 47)
            {
                int y = Convert.ToInt32(stack.Pop());
                int x = Convert.ToInt32(stack.Pop());
                if (val == "+") res = x + y;
                else if (val == "-") res = x - y;
                else if (val == "*") res = x * y;
                else if (val == "/") res = x / y;
                stack.Push(res);
                continue;
            }
            stack.Push(Convert.ToInt32(val));
        }
        return res;
    }
}