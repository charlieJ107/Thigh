import java.util.ArrayList;

public class ProductRecommender {

	public static void main(String args[]) {

		ArrayList<Product> products = new ArrayList<Product>();
		products.add(new Product("DeLorean DMC-12", 100000, 2));
		products.add(new Product("Skoda Octavia", 20000, 5));
		products.add(new Product("Vauxhall Nova", 8000, 2));

		System.out.println("Best product according to LeastExpensiveStrategy:");
		System.out.println(getBestProduct(new LeastExpensiveStrategy(), products).name);

		System.out.println("Best product according to MostPracticalStrategy:");
		System.out.println(getBestProduct(new MostPracticalStrategy(), products).name);
	}

	private static Product getBestProduct(ScoringStrategy scoringStrategy, ArrayList<Product> products) {
		int best_index = 0;
		Product first_product = products.get(0);

		// Complete the line below to retrieve the score of first_product according to
		// scoringStrategy
		int best_score = scoringStrategy.getScore(first_product);

		// Loop through products keeping track of which has the best score
		for (int i = 1; i < products.size(); i++) {
			Product current_product = products.get(i);
			// Complete the line below to retrieve the score of current_product according to
			// scoringStrategy
			int current_score = scoringStrategy.getScore(current_product);
			if (current_score > best_score) {
				best_score = current_score;
				best_index = i;
			}
		}
		return products.get(best_index);
	}

}
