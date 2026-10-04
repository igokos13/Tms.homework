class SuperStr(str):
    def is_repeatance(self, s):
        if len(s)==0:
            return False
        
        if len(self)%len(s) != 0:
            return False
        
        return self ==s*(len(self)//len(s))
    
    def is_palindrom(self):
        clean_str=self.lower().replace('','')
        
        return clean_str==clean_str[::-1]
    
s = SuperStr('abcabcabc')
print(s.is_repeatance('abc'))
print(s.is_repeatance('ab'))
print(s.is_repeatance(''))
            
    