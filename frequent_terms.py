'''
Created on 11/ago/2012

@author: mlarocca
'''
'''
Created on 11/ago/2012

@author: mlarocca
'''
from sys import stdin


def read_and_process_input(f = stdin):
  #INVARIANT: the input is assumed well formed and adherent to the specs above
  line = f.readline().rstrip(' \t\n\r')
  N  = int( line )

  hash_table = {}

  #Insert all the words in a dictionary to count occurrences
  for i in xrange(N):
#        print _buffer, start, end
    term = f.readline().rstrip(' \t\n\r')
    if term in hash_table:
      hash_table[term] += 1
    else:
      hash_table[term] = 1
    
#  print hash_table.items()
  line = f.readline().rstrip(' \t\n\r')
  k = int( line )
  
  #To find the number of occurrences of the k-th term, uses a min-heap with a bounded number of elements: at most k.
  #INVARIANT: heap[0] is the smallest of the top k occurrences count at any moment
  heap = [(0, '')] * k
  heap_size = 0
  
  for count in hash_table.values():
  
    if heap_size == k:
        if count < heap[0]:
            #The heap is full: if the new value is smaller than the k-th element,
            #then it can't be one of the k most frequently used  terms                      
            continue
              
        pos = 0
        # Bubble up the smaller child until hitting a leaf.
        child_pos = 2 * pos + 1    # leftmost child position
        while child_pos < heap_size:
            # Set childpos to index of smaller child.
            right_pos = child_pos + 1
            if right_pos < heap_size and heap[child_pos] > heap[right_pos]:
                child_pos = right_pos
            # Move the smaller child up.
            if heap[child_pos] >= count:
                break
            heap[pos] = heap[child_pos]
            pos = child_pos
            child_pos = 2*pos + 1
        heap[pos] = count           
    else:
               
        heap[heap_size] = count
        pos = heap_size
        heap_size += 1
        # Follow the path to the root, moving parents down until finding a place
        # that fits the new element.
        while pos > 0:
            parent_pos = (pos - 1) >> 1
            parent = heap[parent_pos]
            if count < parent:
                heap[pos] = parent
                pos = parent_pos
            else:
                break
        heap[pos] = count       

    
#  print res
  #Filter out the words that occurs less frequently than the k-th most frequent one
  #then sorts the remaining ones according to frequency and lexicographic order
  #and takes the k best elements
  valid_results = sorted([(1./count, term) for (term, count) in hash_table.items() if count >= heap[0]])[:k]
  for (count, term) in valid_results:
    print term

read_and_process_input()