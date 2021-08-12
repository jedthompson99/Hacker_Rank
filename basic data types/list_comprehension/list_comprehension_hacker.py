
# if __name__ == '__main__':
xr = range(int(input())+1)
yr = range(int(input())+1)
zr = range(int(input())+1)
n = int(input())

sub_set = [[i, j, k] for i in xr for j in yr for k in zr if i+j+k != n]



print(sub_set)
      