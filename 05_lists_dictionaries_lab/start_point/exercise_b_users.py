users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
twit_Jonathan = users["Jonathan"]["twitter"]
print("Twitter handle", twit_Jonathan)

# 2. Get Erik's hometown
hometown_Erik = users["Erik"]["home_town"]
print("Home town: ", hometown_Erik)

# 3. Get the list of Erik's lottery numbers
lotto_numbers_Erik = users["Erik"]["lottery_numbers"]
print("Lottery numbers: ", lotto_numbers_Erik)

# 4. Get the species of Avril's pet Monty
pets_of_Avril = users["Avril"]["pets"]          #not very elegant solution! :(
print(pets_of_Avril)
print(type(pets_of_Avril))
pet_species = pets_of_Avril[0]["species"]
print(pet_species)

# 5. Get the smallest of Erik's lottery numbers
lotto_numbers_Erik = users["Erik"]["lottery_numbers"]
lotto_numbers_Erik.sort()
#print(lotto_numbers_Erik)
lowest_lotto_num = lotto_numbers_Erik[0]
print(lowest_lotto_num)

# 6. Return an list of Avril's lottery numbers that are even
lotto_numbers_Avril = users["Avril"]["lottery_numbers"]
#print(lotto_numbers_Avril)
even_numbers = []
for num in lotto_numbers_Avril:
    if num %2 ==0:
        even_numbers.append(num)

print(even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name":"fluffy", "species":"dog"})
print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Becky"]= {"twitter":"into_cakes",
                 "home_town": "Edinburgh",
                 "lottery_numbers":[],
                 "pets":[{"name":"Poppy",
                          "species":"dog"}]}

print(users)
