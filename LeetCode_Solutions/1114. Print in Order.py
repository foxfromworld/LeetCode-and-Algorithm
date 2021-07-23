# Source : https://leetcode.com/problems/print-in-order/
# Author : foxfromworld
# Date  : 23/07/2021
# First attempt

from threading import Lock, current_thread
class Foo(object):
  def __init__(self):
    self.firstjob = Lock()
    self.secondjob = Lock()
    self.firstjob.acquire()
    self.secondjob.acquire()
  def first(self, printFirst):
    """
    :type printFirst: method
    :rtype: void
    """        
    # printFirst() outputs "first". Do not change or remove this line.
    printFirst()
    print(current_thread().name)
    self.firstjob.release()
  def second(self, printSecond):
    """
    :type printSecond: method
    :rtype: void
    """
    # printSecond() outputs "second". Do not change or remove this line.
    with self.firstjob:
      printSecond()
      self.secondjob.release()
  def third(self, printThird):
    """
    :type printThird: method
    :rtype: void
    """
    # printThird() outputs "third". Do not change or remove this line.
    with self.secondjob:
      printThird()
