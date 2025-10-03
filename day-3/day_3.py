class Solution:
    def CommonPrefix(self, strs: list[str]) -> str:  #-> it will returns string 
        if not strs:  # if it will not string then it returns empty
            return ""
        
        prefix = strs[0]   # given array string the 1 st one stored in the prefix 
        #it stores the prefix data 
        for i in strs[1:]:
            while not i.startswith(prefix):  # startswith is method used to find starting letters 
                prefix = prefix[:-1]
                if not prefix:     # if not egual it returns empty
                    return ""
        
        return prefix
    # if it matchs then the prefix will be return 
    
    # hear logic is if it is prefix then we can return the prefix matched letters otherwice we can return empty  
