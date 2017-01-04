class OddEven(object):
    
    def cal(self,a):
        
        for i in range(0,10):
            r = i % 2
            if(r == 0):
                print("{ %s : %d }")%(a[r],i)
            else:
                print("{ %s  : %d }")%(a[r],i)
obj=OddEven()
obj.a=["even","odd"]
obj.cal(obj.a)
