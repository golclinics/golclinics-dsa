using System;
using System.Collections.Generic;
namespace csharpcompetitive
{
    public class customStack<T>
    {
        private List<T> list;
        public customStack()
        {
            list = new List<T>();
        }

        //push
        public void push(T element) {
            list.Add(element);
        }

        //pop
        public T pop() {
            var lastindex = list[size() - 1];
            list.Remove(lastindex);
            return lastindex;
        }
        //peek
        public T peek() {
            return list[size() - 1];
        }
        //isEmpty
        public bool isEmpty() {
            return size() == 0;
        }
        //size
        public int size() {
            return list.Count;
        }

        // printmyselfout
        public void PrintMyself() {
            foreach (var item in list) {
                Console.Write($"{item},"); // print them on the same line
            }

        }

    }
}
