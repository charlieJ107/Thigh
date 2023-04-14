import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Question1 {

    /**
     * Question 1: Read the file "Input219.txt" and extract all words into an
     * @param newWords An ArrayList to store the words that are matching the words in file "google-10000-english.txt"
     * @return An ArrayList that contains all the words that are matching the words in file "google-10000-english.txt"
     * @details 
     * 1. Open the file "Input219.txt" and extract all words into an ArrayList.
     * 2. Open the file "google-10000-english.txt" and extract all words into an ArrayList.
     * 3. Check the word in the ArrayList and add the word into a new ArrayList if it is matching the words in file "google-10000-english.txt"
     *  3.1. Use the contains() method to check if the word is matching the words in file "google-10000-english.txt"
     *  3.2. If the word is matching, add the word into the new ArrayList.
     *  3.3. If the word is not matching, do nothing.
     *  3.4. Repeat step 3.1 to 3.3 until all the words in the ArrayList are checked.
     * 4. Return the new ArrayList.
     */
    public static ArrayList<String> ExtractWords() {
        ArrayList<String> newWords = new ArrayList<String>();
        try {
            // Open the file "Input219.txt" and extract all words into an ArrayList.
            File input = new File("./Input219.txt");
            Scanner scan;
            scan = new Scanner(input);
            ArrayList<String> words = new ArrayList<String>();
            while (scan.hasNext()) {
                words.add(scan.next());
            }
            scan.close();

            // Open the file "google-10000-english.txt" and extract all words into an
            // ArrayList.
            File google = new File("google-10000-english-no-swears.txt");
            scan = new Scanner(google);
            ArrayList<String> googleWords = new ArrayList<String>();
            while (scan.hasNext()) {
                googleWords.add(scan.next().toLowerCase());
            }
            scan.close();
            // Check the word in the ArrayList and add the word into a new ArrayList if it
            // is matching the
            // words in file "google-10000-english.txt"
            for (String word : words) {
                if (googleWords.contains(word.toLowerCase())) {
                    newWords.add(word);
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return newWords;
    }
}