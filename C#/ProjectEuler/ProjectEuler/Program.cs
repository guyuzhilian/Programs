using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            int sundays = 0;
            
            for (int year = 1901; year <= 2000; year++) {
                for (int month = 1; month <= 12; month++) {
                    if ((new DateTime(year, month, 1)).DayOfWeek == DayOfWeek.Sunday) {
                        sundays++;
                        Console.WriteLine("({0}, {1})", year, month);
                    }
                }
            }

            Console.WriteLine(sundays);
        }
    }
}
