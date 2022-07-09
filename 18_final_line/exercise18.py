"""
In this exercise, write a function (get_final_line) 
that takes a filename as an argument. 
The function should return that file’s final line on the screen.
"""


def get_final_line(filepath):
    last_line = ''
    with open(filepath) as f:
        for line in f:
            last_line = line
    return last_line


if __name__ == '__main__':
    print(get_final_line('/Users/jahedev/Desktop/test.txt'))
