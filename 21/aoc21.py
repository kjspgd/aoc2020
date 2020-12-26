#!/usr/local/bin/python3

ingredients = {}
allergyMap = {}
tempList = []
debug = 0
allergenCulprits = {}
inverseAllergenCulprits = {}
allCulprits = []
allIngredients = []

for line in open('input.txt'):
    tempList.append(line.rstrip())

for i in range(0,len(tempList)):
    ingredients.update({int(i):tempList[i].split("(")[0].split()})
    lineAllergens = []
    lineAllergens= (tempList[i].split("(")[1].replace(")","").replace("contains ","").split(", "))
    for allergen in lineAllergens:
        if debug: print("------------")
        if debug: print(str(i) + " " + str(allergen))
        updater=[]
        try:
            if debug: print(allergyMap[allergen])
            updater = allergyMap[allergen] + [int(i)]
            if debug: print("no exception")
        except:
            if debug: print("Exception on " + str(i) + " " + str(allergen))
            updater = [int(i)]
            if debug: print(updater)
            pass
        if debug: print(updater)
        allergyMap.update({allergen:updater})
        if debug: print(allergyMap)


for allergen in allergyMap.keys():
    if debug: print("-----------")
    if debug: print("Processing " + str(allergen))
    culprits = []
    recipeList = allergyMap[allergen]
    for i in range(0,len(recipeList)):
        if int(i) == 0: culprits = ingredients[recipeList[i]]
        for recipeNo in allergyMap[allergen]:
            culprits = list(set(culprits) & set(ingredients[int(recipeNo)]))
    if debug: print("Culprits for " + str(allergen) + " are " + str(culprits))

    allergenCulprits.update({allergen:culprits})

    for culpritItem in culprits:
        allCulprits.append(culpritItem)

for recipe in ingredients.values():
    for ingredient in recipe:
        allIngredients.append(ingredient)

safeIngredients = []
for ingredient in allIngredients:
    if ingredient not in allCulprits:
        safeIngredients.append(ingredient)

if debug: print(allergenCulprits)
if debug: print(allCulprits)
if debug: print(allIngredients)
if debug: print(safeIngredients)
if debug: print(len(safeIngredients))

#actualAllergens2 = []
#for item in allergenCulprits.values():
#    actualAllergens2 += item

actualAllergens = ['kjs']


while True:
    if len(set(actualAllergens))-1 == len(allergenCulprits.keys()):
        break
    else:
        for allergen in allergenCulprits.keys():
            if len(allergenCulprits[allergen]) != 1:
                for removeCandidate in allergenCulprits[allergen]:
                    if removeCandidate in actualAllergens:
                        #print("I can remove " + removeCandidate + " from " + allergen)
                        newAllergens = allergenCulprits[allergen]
                        newAllergens.remove(removeCandidate)
                        allergenCulprits.update({allergen:newAllergens})
            else:
                actualAllergens.append(allergenCulprits[allergen][0])
if debug: print(allergenCulprits)

print("Final ingredients sorted by allergen:")
string = ''
for item in sorted(allergenCulprits.keys()):
    string += str(allergenCulprits[item][0]) + ','

print(string[:-1])

