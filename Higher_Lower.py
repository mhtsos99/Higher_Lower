import pandas as pd
import random

# Step 1: Load the CSV directly into a pandas DataFrame
url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
df = pd.read_csv(url)

# Step 2: Extract the most recent population data for each country
latest_population_data = df.loc[df.groupby('Country Name')['Year'].idxmax()]
countries_population = latest_population_data[['Country Name', 'Value']].values.tolist()

# Function to format population numbers with dots as thousands separators
def format_population(population):
    return "{:,}".format(population).replace(",", ".")

# Step 3: Game Logic
def play_higher_or_lower_game(countries_population):
    # Initial setup
    score = 0
    current_country, current_population = random.choice(countries_population)

    while True:
        formatted_population = format_population(current_population)
        print(f"\nCurrent country: {current_country} with population: {formatted_population}")

        # Select a new country
        new_country, new_population = random.choice(countries_population)

        # Ensure the new country is different from the current one
        while new_country == current_country:
            new_country, new_population = random.choice(countries_population)

        # Ask the user to guess
        guess = input(f"Is the population of {new_country} higher or lower than {current_country}? (h/l): ").strip().lower()

        # Compare populations
        if (guess == 'h' and new_population > current_population) or (guess == 'l' and new_population < current_population):
            print("\n" + "!" * 20 + " CORRECT " + "!" * 20 )
            score += 1
            # The new country becomes the current one
            current_country, current_population = new_country, new_population
        else:
            formatted_new_population = format_population(new_population)
            print(f"Wrong! {new_country} has a population of {formatted_new_population}. You found {score} correct answers.")
            break

# Start the game
play_higher_or_lower_game(countries_population)