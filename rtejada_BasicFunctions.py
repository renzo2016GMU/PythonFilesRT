#Some basic functions in Python/ 
#Copyright: Renzo Tejada

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

#1
def fast_fib(n, results={}):
    if n in results:
        return results[n]
    else:
        results[n] = n if n < 2 else fast_fib(n-2) + fast_fib(n-1)
        return results[n]

#2
def reversed(xs):
    reverse_list = list(xs)
    reverse_list.reverse()
    return reverse_list

# 3
def is_prime(n):
    if n < 1:
        return False
    if n is 1:
        return False
    else:
        ctr = int(2)
        r = int(0)
        while ctr < n:
            r = n % ctr
            if 0 == r:
                return False
            ctr += 1
    if ctr == n:
        return True
    return False

# 4
def nub(xs):
    if not xs:
        return xs
    c_xs = []
    c_xs.append(xs[0])
   # print('length of xs is ', len(c_xs))
    duplicate = 0;
    for ctr in range(0, len(xs)):
        if xs[ctr] not in c_xs:
            c_xs.append(xs[ctr])
    return c_xs
#5
def zip_with(f, xs, ys):
    if len(xs) <= len(ys):
        size = len(xs)
    else:
        size = len(ys)

    new_list = []

    for i in range(0, size):
        new_list.append(f(xs[i], ys[i]))
    return new_list

# 6
def collatz(n):
    list = [n]

    if n < 1:
        return []

    while n > 1:
        is_Even = n % 2

        if is_Even == 0:
            n = n / 2

        else:
            n = (n * 3) + 1

        list.append(n)  # Added line
    return list

#7
def file_report(filename):
    with open(filename) as f:
        data_list = []
        for line in f:
            line = line.strip() # to deal with blank
            if line:            # lines (ie skip them)
                line_value = int(line)
                data_list.append(line_value)
    f.close()
    avg = float(sum(data_list))/len(data_list)
    data_list=sorted(data_list)
    
    #obtain mode
    number_counts = {}
    for number in data_list:
        number_counts[number] =number_counts.get(number, 0) + 1
    #print('num counts:', number_counts)
    #
    highest = max(number_counts.values())
    #print('worked?')
    #print ([k for k,v in number_counts.items() if v == highest])
    r=[k for k, v in number_counts.items() if v == highest]

    avg=round(avg,1)
    #(2.0, 2, [1, 2, 3])
    tup1 = (avg, median(data_list),r)
    #print ('tup', tup1)
    return tup1

#8
#The 4 methods are used for checking whether input grid meets the sudoku req's
def check_column(grid, column):
    sub_grid = []
    for row in grid:
        sub_grid.append(row[column])
    return check_no_duplicates(sub_grid) 

def check_row(grid, row):
    sub_grid = []
    for cell in grid[row]:
        sub_grid.append(cell)
    return check_no_duplicates(sub_grid)

def check_no_duplicates(sub_grid):  
    uniqueDigits = set()
    for num in sub_grid:
      if num != 0:
        if num  in uniqueDigits:
          return False
      uniqueDigits.add(num)
    return True

def check_subgrid(grid, row, column):
    sub_grid = []
    for i in range(row, row + 3):
        for j in range(column, column + 3):
            sub_grid.append(grid[i][j])
    return check_no_duplicates(sub_grid)

def check_sudoku(grid):
    for i in range(0, 7, 3):
      for j in range(0, 7, 3):
        if not check_subgrid(grid, i, j):
          return False
    for i in range(0, 9):
      if not check_column(grid, i):
          return False
      if not check_row(grid, i):
          return False
    
    return True
