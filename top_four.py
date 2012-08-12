'''
Created on 11/ago/2012

@author: mlarocca
'''
'''
Created on 11/ago/2012

@author: mlarocca
'''
from sys import stdin
from array import array

def read_and_process_input(f = stdin):

  #INVARIANT: the input is assumed well formed and adherent to the specs
  line = f.readline().rstrip(' \t\n\r')
  N  = int( line )

  if N < 4:
    #Special case: less then 4 elements
    res = []
    for i in xrange(N):
      line = f.readline().rstrip(' \t\n\r')
      res.append(int( line ))
      for j in xrange(i, 0, -1):
        if res[i-1] < res[i]:
          tmp = res[i-1]
          res[i-1] = res[i]
          res[i] = tmp
    for N in xrange(4):
      res.append('')
    print '\n'.join(map(str, res))
  else:
    #Statically dimensioned array
    res = array('l', [0]*4)
    #Insert the first 4 elements
    for i in xrange(4):
      line = f.readline().rstrip(' \t\n\r')
      res[i] = int( line ) 
      for j in xrange(i, 0, -1):
        if res[j-1] < res[j]:
          tmp = res[j-1]
          res[j-1] = res[j]
          res[j] = tmp    
    #Inserts the remaining elements
    for i in xrange(4, N):
      line = f.readline().rstrip(' \t\n\r')
      n = int( line )
      
      if n < res[3]:
        #The newly read element is smaller than the 4-th greatest one: can't be inserted in the results
        continue
      #Tests to see where to insert the new element
      j = 2
      while j >= 0:
        if res[j] < n:
          res[j+1] = res[j]
        else:
          break
        j -= 1
      res[j+1] = n
    
    #Prints the best results
    print '\n'.join(map(str, res)) 


read_and_process_input()