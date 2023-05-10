import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Question1 {

    /**
     * Question 1: Read the file "Input219.txt" and extract all words into an
     * 
     * @param newWords An ArrayList to store the words that are matching the words
     *                 in file "google-10000-english.txt"
     * @return An ArrayList that contains all the words that are matching the words
     *         in file "google-10000-english.txt"
     */
    public static ArrayList<String> ExtractWords()
            throws Exception {
        String vocabularyFilename = "google-10000-english-no-swears.txt";
        String inputFilename = "Input219.txt";
        ArrayList<String> validWords = new ArrayList<>();
        ArrayList<String> vocabulary = new ArrayList<>();

        // Read the vocabulary file into an ArrayList
        try (BufferedReader br = new BufferedReader(new FileReader(vocabularyFilename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] words = line.split("[\\s]+");
                for (String word : words) {
                    String wordWithoutPunctuation = word.replaceAll("[^\\w\\s]", "");
                    if (wordWithoutPunctuation != null && !wordWithoutPunctuation.isEmpty()) {
                        vocabulary.add(wordWithoutPunctuation.toLowerCase());
                    }
                }
            }
        } catch (Exception e) {
            throw new Exception("Error reading vocabulary file: " + e.getMessage());
        }

        // Read the input file and extract valid words
        try (BufferedReader br = new BufferedReader(new FileReader(inputFilename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] words = line.split("[\\s]+");
                for (String word : words) {
                    String wordWithoutPunctuation = word.replaceAll("[^\\w\\s]", "");
                    if (wordWithoutPunctuation != null && vocabulary.contains(wordWithoutPunctuation.toLowerCase())) {
                        validWords.add(word);
                    }
                }
            }
        } catch (Exception e) {
            throw new Exception("Error reading input file: " + e.getMessage());
        }

        return validWords;
    }
}