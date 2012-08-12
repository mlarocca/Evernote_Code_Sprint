Evernote_Code_Sprint
====================
https://evernote.interviewstreet.com/

Evernote Code Sprint, 11/August/2012


- Circular buffer	(Python - Completely solved)
	
	Since the size of the buffer is known, the buffer is allocated once and two indexes, pointing to head and tail of the queue, are used.
	An extra parameter keeping track of the number of elements in the buffer is kept in order to distinguish among the various edge cases, like empty and full buffer.

- Top Four (Python - Completely solved)

	We only need to keep a 4-elements statically allocated ordered array to save the biggest 4 elements encountered ever since.
	The first 4 element from the input can be directly inserted into this array, the remaining ones are first compared to the smallest of the four found so far, so that only the bigger ones are saved in the results 4-elements array, using insertion sort.
	Since the results array has a constant number of elements, insertion in this array is constant, so that the whole function is linear in time and space.
	To improve performance, the results array is implemented through a static dimensional long array (using array.array).

- Frequent Terms (Python - Completely solved)
	A dict is used to count the occurrences of every word encountered in the text.
	After all the input has been read and accounted for, the number of occurrences of the k-th most frequent word is computed using a k-elements fixed size min-heap.
	The elements in the dictionary are then filtered according to this value and the sorted: after that the k-th best elements can be returned and printed.

- MultiplyExceptSelf 	(Java - Completely solved)
	To achieve space-efficiency the cumulative prodcut of all elements is computed while the input elements are read; if the input array is A, then the resulting array R's elements will be R[i] = mul / A[i].
	Special care is due if any of the input integers is zero. If exactly one input array is zero, let's say A[i], then every R[j], j!=i will be zero while R[i] will be the product of all the remaining A[j], j!=i. If more than one input integer is equal to zero, i.e. A[i] == A[k] == 0, i!=k, then R[j]==0 for every value of j.