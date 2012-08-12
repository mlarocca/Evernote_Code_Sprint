'''
Created on 11/ago/2012

@author: mlarocca
'''
from sys import stdin
import re


INTEGER_RE = "(\d+)"            #Regular expression: Matches any non negative integerS


def read_and_process_input(f = stdin):
  int_regex = re.compile(INTEGER_RE)  #Regular Expression for integers
  
  #INVARIANT: the input is assumed well formed and adherent to the specs
  line = f.readline()
  N  = int( int_regex.findall(line)[0] )
  start = end = 0
  el_nbr = 0
  _buffer = [0] * N


  while True:
#    print _buffer, start, end
    line = f.readline()

    if line[0] == 'L':
      #List all the elements in the buffer
      res = []
      if el_nbr == 0:
        #Empty buffer
        print
        continue
      elif start < end:
        for i in xrange(start, end):
          res.append(_buffer[i])       
      else: #INVARIANT: el_nbr!=0 => (start==end => el_nbr ==N)
        for i in xrange(start, N):
          res.append(_buffer[i])
        for i in xrange(0, end):
          res.append(_buffer[i])   
#      print(res)               
      print '\n'.join(res)
      
    elif line[0] == 'Q':
      #Quit
      break    
    
    elif line[0] == 'A':
      #Add n elements to the buffer
      n = int( int_regex.findall(line[2:])[0] )
      for i in xrange(n):
#        print _buffer, start, end
        val = f.readline().rstrip(' \t\n\r')

        _buffer[end] = val
        end += 1
        if end == N:
          end = 0
        if el_nbr == N:
          #Overwrites previous elements
          start = end
        else:
          el_nbr += 1        
         
    elif line[0] == 'R':
      #Removes n elements
      n = int( int_regex.findall(line[2:])[0] )
      el_nbr -= n
      
      if start < end:
        start += n
      else:
        start += n
        if start >= N:
          start -= N

read_and_process_input()