# Source : https://leetcode.com/problems/read-n-characters-given-read4/
# Author : foxfromworld
# Date  : 30/12/2020
# First attempt 

class Solution:
  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """
    totalNum = 0
    lenBuf4 = 4
    pBuf = 0
    leftchar = n
    buf4 = [""]*4
    while lenBuf4 == 4 and leftchar > 0:
      lenBuf4 = min(read4(buf4),leftchar)
      totalNum += lenBuf4
      buf[pBuf:pBuf+lenBuf4] = buf4[:] 
      leftchar -= lenBuf4
      pBuf += lenBuf4
    return totalNum
