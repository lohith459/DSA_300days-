class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:  # it shows that it returns the int value 
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:    # if num is  less then 9 then it will be incremented by 1
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * n
    
''' # plus one sum 
                 if we have an array =[1,2,3,4] then the ==>  o/p=[1,2,3,5]
                
                last element in the array is incremented by the 1

            if array last value with 9 then ==> 9+1 = [ 1,0 ]     
            
             str=[1,2,3,4,9]
             
             o/p=[1,2,3,4,1,0]           
                
                
                '''



