using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution
{

    // Complete the minimumBribes function below.
    static void minimumBribes(int[] arrayIn)
    {
        int bribes = 0;
        for (int i = arrayIn.Count() - 1; i >= 0; i--)
        {
            if (arrayIn[i] - (i + 1) > 2)
            {
                Console.WriteLine("Too chaotic");
                return;
            }


            for (int j = arrayIn[i] - 2 > 0 ? arrayIn[i] - 2 : 0; j < i; j++)
            {
                if (arrayIn[j] > arrayIn[i])
                    bribes++;
            }
        }


        Console.WriteLine(bribes);


    }

    static void Main(string[] args)
    {
        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++)
        {
            int n = Convert.ToInt32(Console.ReadLine());

            int[] q = Array.ConvertAll(Console.ReadLine().Split(' '), qTemp => Convert.ToInt32(qTemp))
            ;
            minimumBribes(q);
        }
    }
}
