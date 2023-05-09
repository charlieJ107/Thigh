# CMT219 Coursework Report
By [Your Name Here] (Your Student Number Here)

## Question 1
1. The program works by reading the contents of the "Input219.txt" file and creating a list of all the words in the file, including duplicates and attached punctuation. Then it reads the contents of the "google-10000-english-no-swears.txt" file and creates a HashSet of all the valid words in the vocabulary. The program then iterates through the list of words from the input file and checks if each word is present in the vocabulary HashSet. If a word is valid, it is added to the result ArrayList. Finally, the program sorts the result ArrayList using the merge sort algorithm and prints the sorted list to the console.

2. The use of ArrayLists affects the time complexity of the program by adding a constant factor to the time complexity of each operation that involves adding or removing elements. In the case of this program, the time complexity of adding elements to the result ArrayList is O(1) on average, as long as the underlying array has enough space to accommodate the new element. The time complexity of removing elements is O(n), as all the remaining elements after the removed one need to be shifted one position to the left. The overall time complexity of the program is dominated by the time complexity of iterating through the list of words from the input file and checking if each word is valid, which is O(n), where n is the number of words in the input file.

3. The efficiency of the program could be improved in several ways. For example, instead of using an ArrayList to store the result, we could use a HashSet to avoid adding duplicate elements. This would reduce the time complexity of adding elements to O(1) on average, and would also eliminate the need for sorting the result. Another way to improve efficiency would be to use a more efficient data structure to store the valid words from the vocabulary, such as a Trie or a Bloom filter. This would reduce the time complexity of checking if a word is valid to O(k), where k is the length of the word, and would also reduce the memory requirements of the program. Finally, we could also parallelize the program by using multiple threads to process different parts of the input file simultaneously, which would take advantage of multi-core CPUs and reduce the overall processing time.

## Question 2
1. Here is the output of the program when run with the input file "Input219.txt":

```
It takes 229000 nanoseconds to sort the first 100 words in the newWords ArrayList into alphabetical order.
There are 1214 comparisons.
The first 100 words in the newWords ArrayList are:
It takes 425600 nanoseconds to sort the first 200 words in the newWords ArrayList into alphabetical order.
There are 2830 comparisons.
The first 200 words in the newWords ArrayList are:
It takes 534100 nanoseconds to sort the first 300 words in the newWords ArrayList into alphabetical order.
There are 4589 comparisons.
```

The merge sort program works by recursively dividing the input list into smaller sub-lists until each sub-list contains only one element, and then merging the sub-lists together in a sorted order. The merge operation compares the first element of each sub-list and selects the smallest one, adds it to the output list, and then moves to the next element of the sub-list that contained the smallest element. This process continues until all the elements of both sub-lists have been merged into the output list.