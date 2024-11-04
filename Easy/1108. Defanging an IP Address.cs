public class Solution
{
    public string DefangIPaddr(string address)
    {
        for (int i = 0; i < address.Length; i++)
        {
            if (address[i] == '.')
            {
                string post = address[..i];
                string pre = address[(i + 1)..];
                address = post + "[.]" + pre;
                i++;
            }
        }

        return address;
    }
}