class fibonacci:
    def fibo(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        if n<0:
            raise ValueError("n cannot be lower than 0")
        return self.fibo(n-1)+self.fibo(n-2)

