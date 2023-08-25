class Set:
    def _init_(self,set1):
        self.set1 = set1

    def ismember(self,element):
       if element in self.set1:
           return True
       else:
           False 

    def powerset(self):
        power_set = [[]]
        for i in self.set1:
            for j in power_set:
                power_set = power_set + [list(j)+ [i]]
            return power_set
        
    def subset(self,set2):
        for i in set2:
            if i not in self.set1:
                return False
            else:
                True

    def union(self,set2):
        return self.set1.union(set2)
    
    def intersection(self,set2):
        return self.set1.intersection(set2)
    
    def complement(self,universal_self):
        return universal_self.difference(self.set1)
    
    def difference(self,set2):
        return self.set1.difference(set2)
    
    def symmetric_difference(self,set2):
        return self.set1.symmetric_difference(set2)
    
    def cartesian_product(self,set2):
        cartesian_product = []
        for i in self.set1:
            for j in set2:
                cartesian_product.append((i,j))
            return cartesian_product
        
set1 = set(map(int,input("enter the elements of set1: ").split()))
s = input(Set(set1))
num = set([int(x) for x in input("enter the elements : ").split(" ")])
print("element exist in Set: ", s.ismember(num))
powerset = s.powerset
print("powerset of the set:",powerset)

set2 = set(map(int,input("enter the elements of set2:").split()))
print("set2 is subset of set1: ", s.subset(set2))

print("union of set1 and set2: ",s.union(set1))
print("intersection of set1 and set2: ",s.intersection(set2))

universal_set = set1 = set(map(int,input("enter elements of universal set: ").split()))
print("complement of set1: ", s.complement(universal_set))

print("difference between set1 and set2: ", s.difference(set2))
print("symmteric difference of set1 and set2 is: ",s.symmetric_difference(set2))

print("cartesian product of set1 and set2 is: ",s.cartesian_product(set2))