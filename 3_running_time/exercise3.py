"""
System  administrators  often  use  Python  to  perform  a  variety  of  tasks,  including  pro-ducing reports from user inputs and files. It’s not unusual to report how often a par-ticular error message has occurred, or which IP addresses have accessed a server mostrecently,  or  which  usernames  are  most  likely  to  have  incorrect  passwords.  Learninghow to accumulate information over time and produce some basic reports (includingaverage  times)  is  thus  useful  and  important.  Moreover,  knowing  how  to  work  withfloating-point values, and the differences between them and integers, is important. For this exercise, then, we’ll assume that you run 10 km each day as part of yourexercise regime. You want to know how long, on average, that run takes.  Write  a  function  (run_timing) that asks how long it took for you to run 10 km.The function continues to ask how long (in minutes) it took for additional runs, untilthe user presses Enter. At that point, the function exits—but only after calculating anddisplaying the average time that the 10 km runs took. For example, here’s what the output would look like if the user entered three datapoints:
Enter10 km runtime:15
Enter10 km runtime:20
Enter10 km runtime:10
Enter10 km runtime:<enter>

Averageof 15.0,over 3 runs

Note  that  the  numeric  inputs  and  outputs  should  all  be  floating-point  values.  Thisexercise is meant to help you practice converting inputs into appropriate types, alongwith  tracking  information  over  time.  You’ll  probably  be  tracking  data  that’s  moresophisticated  than  running  times  and  distances,  but  the  idea  of  accumulating  dataover time is common in programs, and it’s important to see how to do this in Python.
"""
from decimal import Decimal
import sys

def runtime_calculator():
    total = Decimal(0)
    count = 0

    print('\nRuntime Calculator:\n')

    while user_input := input('Enter 10 km run time: '):
        if not is_float(user_input):
            print('Try again!')
            continue
        
        count += 1
        total += Decimal(user_input)

    if (total == 0):
        print('\nNo run times entered.')
        sys.exit();

    print('\nAverage of {:.2f}, over {} runs'.format(Decimal(total)/Decimal(count), count))

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    runtime_calculator()