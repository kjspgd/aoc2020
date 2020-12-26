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

#print(ingredients)
#print(allergyMap)

for allergen in allergyMap.keys():
    print("-----------")
    print("Processing " + str(allergen))
    culprits = []
    recipeList = allergyMap[allergen]
    #print(recipeList)
    for i in range(0,len(recipeList)):
        #culprits=[]
        #print(recipeList[i])
        #recipe = ingredients[i]
        #print(int(i))
        #print("*-(")
        if int(i) == 0: culprits = ingredients[recipeList[i]]
        for recipeNo in allergyMap[allergen]:
            #print("Recipe No")
            #print(recipeNo)
            #print("Ingredients")
            #print(ingredients[int(recipeNo)])
            #print(set(culprits))
            #print("Vs")
            #print(ingredients[int(recipeNo)])
            culprits = list(set(culprits) & set(ingredients[int(recipeNo)]))
    print("Culprits for " + str(allergen) + " are " + str(culprits))

    allergenCulprits.update({allergen:culprits})
    ##ADD INVERSE CULPRITS FOR LINE HERE?

    for culpritItem in culprits:
        allCulprits.append(culpritItem)

for recipe in ingredients.values():
    for ingredient in recipe:
        allIngredients.append(ingredient)

safeIngredients = []
for ingredient in allIngredients:
    if ingredient not in allCulprits:
        safeIngredients.append(ingredient)

print(allergenCulprits)
print(allCulprits)
print(allIngredients)
print(safeIngredients)
print(len(safeIngredients))
