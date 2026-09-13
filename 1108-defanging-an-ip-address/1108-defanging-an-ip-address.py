class Solution(object):
    def defangIPaddr(self, address):
        ans = ""
        index = 0
        
        while index < len(address):
            if address[index] == '.':
                ans += "[.]"
            else:
                ans += address[index]
            index += 1
            
        return ans