import java.util.ArrayList;
import java.util.List;

public class Question2 {

    /**
     * Question 2: Sort the words in the newWords ArrayList into alphabetical order.
     * 
     * @param list An ArrayList that contains all the words that are matching the
     *             words in file "google-10000-english.txt"
     * @return An ArrayList that contains all the words that are matching the words
     *         in file "google-10000-english.txt" in alphabetical order.
     */
    public static ArrayList<String> MergeSort(List<String> list, ICounter comparisonsCounter, ICounter movesCounter) {
        // If the ArrayList only contains one element, return the ArrayList.
        if (list.size() <= 1) {
            return new ArrayList<String>(list);
        }

        // Find the middle of the ArrayList.
        int middle = list.size() / 2;
        // Split the ArrayList into two ArrayLists.
        ArrayList<String> left = new ArrayList<String>(list.subList(0, middle));
        ArrayList<String> right = new ArrayList<String>(list.subList(middle, list.size()));
        // Sort the left half of the ArrayList.
        left = MergeSort(left, comparisonsCounter, movesCounter);
        // Sort the right half of the ArrayList.
        right = MergeSort(right, comparisonsCounter, movesCounter);
        // Merge the left half of the ArrayList and the right half of the ArrayList.
        ArrayList<String> result = merge(left, right, comparisonsCounter, movesCounter);
        // Return the new ArrayList.
        return result;
    }

    /**
     * Merge two ArrayLists into one ArrayList.
     * 
     * @param left  An ArrayList that contains the left half of the ArrayList.
     * @param right An ArrayList that contains the right half of the ArrayList.
     * @return An ArrayList that contains the left half of the ArrayList and the
     *         right half of the ArrayList.
     */
    private static ArrayList<String> merge(List<String> left, List<String> right, ICounter comparisonsCounter, ICounter movesCounter) {
        // Create a new ArrayList to store the result.
        ArrayList<String> result = new ArrayList<String>();
        
        // Initialise the index of the left ArrayList and the right ArrayList.
        int i = 0;
        int j = 0;
        
        while (i < left.size() && j < right.size()) {
            // Iterate through the left and right halves, respectively, of the input arrays. 
            // Count the number of comparisons.
            comparisonsCounter.increment();
            if (left.get(i).compareToIgnoreCase(right.get(j)) <= 0) { // Case insensitive comparison.
                // If the element in the left ArrayList is smaller than the element in the right ArrayList,
                result.add(left.get(i));
                i++;
            } else {
                result.add(right.get(j));
                j++;
            }
            comparisonsCounter.increment();
            movesCounter.increment();
        }
        while (i < left.size()) {
            result.add(left.get(i));
            i++;
            comparisonsCounter.increment();
            movesCounter.increment();
        }
        while (j < right.size()) {
            result.add(right.get(j));
            j++;
            comparisonsCounter.increment();
            movesCounter.increment();
        }
        // Return the new ArrayList.
        return result;
    }
}
