questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen"
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {capital}.\n")