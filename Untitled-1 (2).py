import random
adjectives = ["Tall", "Short", "Lazy", "Fancy", "Brawny", "Rude", "Ugly", "Scary", "Pretty", "Tiny", "Skinny", "Chubby", "Small", "Big", "Cool"]
nouns = ["Dog", "Cat", "bunny", "Fish", "Horse", "Toad", "Lizard", "Snake","Hamster", "Rat", "Gerbil", "Turtle", "Parrot", "Spider", "Donkey"]
verbs = ["Eat", "Pay", "Feel", "Jump", "Learn", "Clean", "Stretch", "Seek", "Hide", "Lay", "Spin", "Dance", "Run", "Play", "Sleep"]
verbs_pasts = ["Eaten", "Payed", "Feeled", "Jumped", "Learned", "CLeaned", "Stretched", "Seeked", "Hidden", "Layed", "Spinned", "Danced", "Runned", "Played", "Sleeped"]
places = ["Shoe Carnival", "Walmart", "Sam's Club", "McDonalds", "Pizza Hut", "Perrie Gardens", "Rural King", "Subway", "Burger King", "Five Guys", "Pandra", "Dairy Queen", "Casey's", "Olive Graden", "Barnes & Noble"]
emotions = ["Happy", "Sad", "Angry", "Scared", "Surprise", "Shame", "Excitement", "Regret", "Relief", "Pity", "Guilt", "Envy", "Joyful", "Grumpy", "Disgust"]
numbers = ["100", "1", "23", "86", "47", "7", "18", "69", "95", "43", "234", "156", "1000", "73", "32"]

print("Jen was looking to buy a pet " + random.choice(nouns) + ".")
print("Jen was looking for a pet that can " + random.choice(verbs) + ".")
print("Jen wouldn't stand a pet that was " + random.choice(adjectives) + ".")
print("In order to find the pet Jen went to " + random.choice(places) + ", where instead of finding " + random.choice(nouns) + " they found " + random.choice(nouns) + ".")
print("After a hour of shopping, Jen picked a " + random.choice(nouns) + ".")
print("But Jen didn't just get one, they got " + random.choice(numbers) + ", but she really wanted to get " + random.choice(numbers) + ".")
print("When they went home Jen's house. the new pets choose to " + random.choice(verbs) + " all over the house.")
print("After about " + random.choice(numbers) + " hours spent at home, Jen had to leave.")
print("The new pets watched as it's new owner " + random.choice(verbs) + " out the door, leaveing the new pets to " + random.choice(verbs) + " at home.")
print("So when Jen got home, she saw that her new pet had " + random.choice(verbs_pasts) + " all througout the house.")
print("This made Jen so " + random.choice(emotions) + ".")
print("Jen " + random.choice(verbs_pasts) + " before heading to bed with all her new pets.")
print("Jen felt " + random.choice(emotions) + " as she drifted off to sleep, today was a good day.")