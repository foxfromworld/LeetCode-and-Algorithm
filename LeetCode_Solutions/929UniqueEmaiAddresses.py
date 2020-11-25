# Source : https://leetcode.com/problems/high-five/
# Author : foxfromworld
# Date  : 25/11/2020
# Third attempt 

class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    setL = set()
    for email in emails:
      localName, domainName = email.split('@')
      ret = localName.find('+')
      localName = localName[:ret] if ret > 0 else localName
      setL.add(localName.replace('.', '')+'@'+domainName)
    return len(setL)

# Date  : 25/11/2020
# Second attempt 

import re
class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    setL = set()
    for email in emails:
      for i in range(len(email)-1,0,-1):
        if email[i] == "@":
          domainName = email[i:len(email)]
          break
      for i in range(len(email)):
        if email[i] == "+":
          localName = email[0:i]
          break
        elif email[i] == "@":
          localName = email[0:i]
          break
      setL.add(localName.replace('.', '')+domainName)
    return len(setL)


# Date  : 25/11/2020
# First attempt 

import re
class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    returnL = []
    for email in emails:
      for i in range(len(email)-1,0,-1):
        if email[i] == "@": # get the domain name
          domainName = email[i:len(email)]
          break
      for i in range(len(email)): # get the local name
        if email[i] == "+":
          localName = email[0:i]
          break
        elif email[i] == "@":
          localName = email[0:i]
          break
      returnL.append(localName.replace('.', '')+domainName)
    return len(set(returnL))
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]        
emails = ["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]
newClass = Solution()
print(newClass.numUniqueEmails(emails))   
