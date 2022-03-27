using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution
{
    static void Main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int num = Convert.ToInt32(Console.ReadLine());
        //create list which is easier than an array to hold initial brackets string
        List<string> valList = new List<string>();
        for (int u = 0; u < num; u++)
        {
            valList.Add(Console.ReadLine());
        }
        List<string> resultList = new List<string>();

        //loop through each element in valList
        foreach (string str in valList)
        {
            List<char> lst = new List<char>();
            bool error = false;
            foreach (char s in str)
            {
                if (!error)
                {
                    if (s == '{' || s == '(' || s == '[')
                    {
                        lst.Add(s);
                    }
                    else if (s == '}')
                    {
                        if (lst.Count() > 0)
                        {
                            if (lst[lst.Count() - 1] == '{')
                            {
                                lst.RemoveAt(lst.Count() - 1);
                            }
                            else
                            {
                                error = true;
                            }
                        }
                        else
                        {
                            error = true;
                        }
                    }
                    else if (s == ')')
                    {
                        if (lst.Count() > 0)
                        {
                            if (lst[lst.Count() - 1] == '(')
                            {
                                lst.RemoveAt(lst.Count() - 1);
                            }
                            else
                            {
                                error = true;
                            }
                        }
                        else
                        {
                            error = true;
                        }
                    }
                    else if (s == ']')
                    {
                        if (lst.Count() > 0)
                        {
                            if (lst[lst.Count() - 1] == '[')
                            {
                                lst.RemoveAt(lst.Count() - 1);
                            }
                            else
                            {
                                error = true;
                            }
                        }
                        else
                        {
                            error = true;
                        }
                    }
                }


            }
            if ((!error || string.IsNullOrEmpty(str)) && lst.Count() == 0)
            {
                Console.WriteLine("YES");
            }
            else
            {
                Console.WriteLine("NO");
            }

        }
        Console.ReadLine();

    }
}
