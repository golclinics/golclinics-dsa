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

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr)
    {
        var top = 1;
        var left = 1;
        //length of each row
        var right = arr[0].Length - 1;
        var bottom = arr.Length - 1;

        //initialize to a certain min value
        var max = Int32.MinValue;

        for (int i = left; i < right; i++)
        {
            for (int n = top; n < bottom; n++)
            {
                var t = arr[i][n];
                t += arr[i - 1][n - 1];
                t += arr[i - 1][n];
                t += arr[i - 1][n + 1];

                t += arr[i + 1][n - 1];
                t += arr[i + 1][n];
                t += arr[i + 1][n + 1];

                if (t > max)
                {
                    max = t;
                }
            }
        }
        return max;

    }

    static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int[][] arr = new int[6][];

        for (int i = 0; i < 6; i++)
        {
            arr[i] = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
        }

        int result = hourglassSum(arr);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}