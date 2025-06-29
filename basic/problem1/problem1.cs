using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
  static void Main()
  {
    int n = int.Parse(Console.ReadLine());
    List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
    int p = int.Parse(Console.ReadLine());

    List<int> result = new List<int>();

    if (p == 0)
    {
      result = numbers.Where(x => x % 2 == 0).ToList();
    }
    else
    {
      result = numbers.Where(x => x % 2 != 0).ToList();
    }

    Console.WriteLine(string.Join(" ", result));
  }
}
