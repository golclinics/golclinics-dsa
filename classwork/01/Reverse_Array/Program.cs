using System;


namespace Reverse_Array
{
    
    class Program
    {
        static int[] reverse_a(int[] array1)
        {
            return array1;
        }
        static void Main(string[] args)
        {
            int[] array1 = Array.ConvertAll(Console.ReadLine().Split(' '), aTemp =>Convert.ToInt32(aTemp));

            int[] result = reverse_a(array1);

            Console.WriteLine(result);

        }
    }
}
