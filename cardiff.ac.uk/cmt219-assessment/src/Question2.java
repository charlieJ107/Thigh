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
    public static ArrayList<String> MergeSort(List<String> list, ICounter counter) {
        // If the ArrayList only contains one element, return the ArrayList.
        if (list.size() <= 1) {
            return new ArrayList<String>(list);
        }
        // Split the ArrayList into two ArrayLists.
        ArrayList<String> left = new ArrayList<String>();
        ArrayList<String> right = new ArrayList<String>();
        // Find the middle of the ArrayList.
        int middle = list.size() / 2;
        // Add the left half of the ArrayList into the new ArrayList.
        for (int i = 0; i < middle; i++) {
            left.add(list.get(i));
        }
        // Add the right half of the ArrayList into the new ArrayList.
        for (int i = middle; i < list.size(); i++) {
            right.add(list.get(i));
        }
        // Sort the left half of the ArrayList.
        left = MergeSort(left, counter);
        // Sort the right half of the ArrayList.
        right = MergeSort(right, counter);
        // Merge the left half of the ArrayList and the right half of the ArrayList.
        ArrayList<String> result = merge(left, right, counter);
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
    private static ArrayList<String> merge(List<String> left, List<String> right, ICounter counter) {
        // Create a new ArrayList to store the result.
        ArrayList<String> result = new ArrayList<String>();
        // Add the left half of the ArrayList into the new ArrayList.

        // Count the number of comparisons.
        counter.increment();
        while (left.size() > 0 || right.size() > 0) {
            // Compare the first element of the left ArrayList and the first element of the
            // right ArrayList.

            // Count the number of comparisons.
            counter.increment();
            if (left.size() > 0 && right.size() > 0) {
                // If the first element of the left ArrayList is smaller than the first element
                // of the right ArrayList, add the first element of the left ArrayList into the
                // new ArrayList.
                // Count the number of comparisons.
                counter.increment();
                if (left.get(0).compareTo(right.get(0)) <= 0) {
                    // Count the number of comparisons.
                    
                    // Add the first element of the left ArrayList into the new ArrayList.
                    result.add(left.get(0));
                    // Remove the first element of the left ArrayList.
                    left.remove(0);
                } else {

                    // Add the first element of the right ArrayList into the new ArrayList.
                    result.add(right.get(0));
                    // Remove the first element of the right ArrayList.
                    right.remove(0);
                }
                // If the left ArrayList is empty, add the first element of the right ArrayList
                // into the new ArrayList.
            
                // Count the number of comparisons.
                counter.increment();
            } else if (left.size() > 0) {
                // Add the first element of the left ArrayList into the new ArrayList.
                result.add(left.get(0));
                // Remove the first element of the left ArrayList.
                left.remove(0);
                
                // If the right ArrayList is empty, add the first element of the left ArrayList
                // into the new ArrayList.

                // Count the number of comparisons.
                counter.increment();
            } else if (right.size() > 0) {
                // Add the first element of the right ArrayList into the new ArrayList.
                result.add(right.get(0));
                // Remove the first element of the right ArrayList.
                right.remove(0);
            }
        }
        // Return the new ArrayList.
        return result;
    }
}
