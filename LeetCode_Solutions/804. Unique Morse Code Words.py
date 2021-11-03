# Source : https://leetcode.com/problems/unique-morse-code-words/
# Author : foxfromworld
# Date  : 03/11/2021
# First attempt

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        tf = []
        char = 'abcdefghijklmnopqrstuvwxyz'
        for word in words:
            temp = ""
            for ch in word:
                temp += code[char.find(ch)]
            if temp not in tf:
                tf.append(temp)
        return len(tf)
