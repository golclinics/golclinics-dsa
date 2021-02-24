namespace csharpcompetitive
{
    class Program
    {
        static void Main(string[] args)
        {
            dosomeMath(3).PrintMyself();
        }

        static customStack<long> dosomeMath(long n)
        {
            var stack = new customStack<long>();
            while (n > 1)
            {
                if (!stack.isEmpty())
                {
                    n = stack.peek();
                }
                if (n % 2 == 0)
                {
                    stack.push(n / 2);
                }
                else
                {
                    stack.push((n * 3) + 1);
                }
                    n = stack.peek();
            }
            return stack;
        }


    }
}

