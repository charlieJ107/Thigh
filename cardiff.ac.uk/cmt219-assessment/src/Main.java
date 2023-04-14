import java.util.ArrayList;

public class Main {
    // Create a main method.
    public static void main(String[] args) {
        /////////////////////////////////////////////////////////
        //////////////////// Question 1 /////////////////////////
        /////////////////////////////////////////////////////////
        // Create a new ArrayList to store the words that are matching the words in file "google-10000-english.txt"
        ArrayList<String> newWords = Question1.ExtractWords();
        // Print the words in the ArrayList.
        for (String word : newWords) {
            System.out.println(word);
        }
        System.out.println("There are " + newWords.size() + " words in the new list.");

        // End of Question 1

        /////////////////////////////////////////////////////////
        //////////////////// Question 2 /////////////////////////
        /////////////////////////////////////////////////////////
        // Create a counter to count the number of comparisons.
        Counter counter = new Counter();
        // Sort the words in the newWords ArrayList into alphabetical order.
        ArrayList<String> sorted_full = Question2.MergeSort(newWords, counter);
        // Print the words in the ArrayList.
        System.out.println("The words in the newWords ArrayList are:");
        for (String word : sorted_full) {
            System.out.println(word);
        }        

        // Reset the counter.
        counter.reset();
        // Set a timer to count the time.
        long startTime = System.nanoTime();
        // Sort the first 100 words in the newWords ArrayList into alphabetical order.
        ArrayList<String> sorted_100 = Question2.MergeSort(newWords.subList(0, 100), counter);
        // Stop the timer.
        long endTime = System.nanoTime();
        // Print the time it takes to sort the first 100 words in the newWords ArrayList into alphabetical order.
        System.out.println("It takes " + (endTime - startTime) + " nanoseconds to sort the first 100 words in the newWords ArrayList into alphabetical order.");
        // Print the number of comparisons.
        System.out.println("There are " + counter.getCount() + " comparisons.");
        // Print the words in the ArrayList.
        System.out.println("The first 100 words in the newWords ArrayList are:");
        for (String word : sorted_100) {
            System.out.println(word);
        }

        // Reset the counter.
        counter.reset();

        // Set a timer to count the time.
        startTime = System.nanoTime();
        // Sort the first 200 words in the newWords ArrayList into alphabetical order.
        ArrayList<String> sorted_200 = Question2.MergeSort(newWords.subList(0, 200), counter);
        // Stop the timer.
        endTime = System.nanoTime();
        // Print the time it takes to sort the first 200 words in the newWords ArrayList into alphabetical order.
        System.out.println("It takes " + (endTime - startTime) + " nanoseconds to sort the first 200 words in the newWords ArrayList into alphabetical order.");
        // Print the number of comparisons.
        System.out.println("There are " + counter.getCount() + " comparisons.");
        // Print the words in the ArrayList.
        System.out.println("The first 200 words in the newWords ArrayList are:");
        for (String word : sorted_200) {
            System.out.println(word);
        }

        // Reset the counter.
        counter.reset();

        // Set a timer to count the time.
        startTime = System.nanoTime();
        // Sort the first 300 words in the newWords ArrayList into alphabetical order.
        ArrayList<String> sorted_300 = Question2.MergeSort(newWords.subList(0, 300), counter);
        // Stop the timer.
        endTime = System.nanoTime();
        // Print the time it takes to sort the first 300 words in the newWords ArrayList into alphabetical order.
        System.out.println("It takes " + (endTime - startTime) + " nanoseconds to sort the first 300 words in the newWords ArrayList into alphabetical order.");
        // Print the number of comparisons.
        System.out.println("There are " + counter.getCount() + " comparisons.");   
        // Print the words in the ArrayList.
        System.out.println("The first 300 words in the newWords ArrayList are:");
        for (String word : sorted_300) {
            System.out.println(word);
        }
        // End of Question 2
    }

}
