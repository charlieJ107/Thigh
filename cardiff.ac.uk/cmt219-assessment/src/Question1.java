import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

// Create a class called Question1 that has a main method.
class Question1 {
    public static void main(String[] args) {

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
                googleWords.add(scan.next());
            }
            scan.close();
            // Check the word in the ArrayList and add the word into a new ArrayList if it is matching the
            // words in file "google-10000-english.txt"
            ArrayList<String> newWords = new ArrayList<String>();
            for (String word : words) {
                if (googleWords.contains(word)) {
                    newWords.add(word);
                }
            }

            // Print the words in the ArrayList.
            for (String word : newWords) {
                System.out.println(word);
            }
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
}