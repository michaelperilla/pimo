from sys import stdin

def valid(sp,k):
   return sp.count('c') < k
       
def Bk(n,k,sp,cs,fac):
   suma = 0
   if fac < n:
      for j in cs:
         sp1 = sp
         sp1[fac] = j
         if valid(sp1,k):
            if fac < n-1:
               suma += Bk(n,k,sp1,cs,fac+1)
            else:
               suma += 1
   return suma        

def main():
   n,k = [int(x) for x in stdin.readline().split()]
   sp = ['' for i in range(n)]
   CS = ['c','s']
   print(Bk(n,k,sp,CS,0))
       
main()
