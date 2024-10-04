#Homogenous List

integers ={1, 2, 3, 8, 33}

animals ={"dog", "cat", "goat", "Quebec"}

names= {"John", "Emiliano", "Gael"}

floats= {2.2, 3.3, 4.4, 5.5}

#Heterogenus List

numbers_animals_names= {2, "cat", 34.33, "Kanye"}

list_lists= [[1,2,3],["cat", "dog", "spider"]]

#How to access an element in a list

words = ["apple", "balloon", "cat", "dream", "elephant", "flower", "guitar", "honey", "island",
    "jelly", "kite", "lamp", "mountain", "notebook", "ocean", "pancake", "quokka", "rainbow",
    "starfish", "turtle", "umbrella", "violin", "window", "xylophone", "yogurt", "zebra",
    "avocado", "bicycle", "cookie", "dinosaur", "echo", "flamingo", "galaxy", "hammock",
    "iguana", "jigsaw", "koala", "lemonade", "mango", "nest", "octopus", "parrot", "quilt",
    "robot", "sunbeam", "teapot", "unicorn", "volcano", "walrus", "x-ray", "anchor", "beach",
    "castle", "daisy", "energy", "fountain", "garden", "helmet", "ice cream", "jellyfish",
    "lollipop", "mermaid", "nebula", "olive", "penguin", "quasar", "raccoon", "spaghetti",
    "telescope", "ukulele", "velvet", "windmill", "yarn", "zeppelin", "almond", "broccoli",
    "cloud", "dragon", "emerald", "falcon", "grape", "horizon", "ink", "jasmine", "key",
    "lavender", "mushroom", "nutmeg", "orange", "pumpkin", "quiche", "raspberry", "sunflower",
    "tangerine", "universe", "whisper", "xerus", "azimuth", "bumblebee", "cinnamon", "daffodil",
    "feather", "harp", "iceberg", "javelin", "kiwi", "lantern", "mist", "nectar", "opal",
    "pineapple", "quartz", "seashell", "tambourine", "unity", "vortex", "willow", "xylophonist",
    "yawn", "zest", "acorn", "bat", "cloudberry", "daisy", "eggplant", "fern", "globe",
    "honeydew", "igloo", "jackfruit", "kaleidoscope", "moonlight", "nightingale", "owl",
    "quilt", "racquet", "snowflake", "treasure", "vanilla", "windchime", "yarrow", "zenith",
    "antelope", "beachcomber", "butterfly", "cherry", "dainty", "flamingo", "gardenia",
    "hologram", "iceland", "juniper", "lavender", "mint", "nutmeg", "olive", "peach",
    "quinoa", "sapling", "thistle", "underwater", "violet", "wispy", "xenon", "yacht",
    "zucchini", "artichoke", "basil", "cactus", "dolphin", "eucalyptus", "fuchsia", "ginger",
    "hibiscus", "indigo", "jalapeno", "kiwifruit", "lime", "mushroom", "nectar", "orange",
    "papaya", "quokka", "radish", "saffron", "tulip", "urchin", "vanilla", "wasabi", "xanadu",
    "yellow", "zinnia"]

print(words [-1])

#List slicing

List= [3, 22, 30, 5, 3, 20]

print (list[:])

print(list[1:3])

#Update a list

science=["art", "chemistry", "math"]

science[1]= "geology"

print(science)

integers = [2,5,9,20,27]

integers.remove (27)

print(integers)

integers.pop()

print(integers)

list_fruits=["Sandia", "Limon", "naranja"]

#pop remove del

del list_fruits[1]

print(list_fruits)

list_names=["Anahi", "Pamela", "Quebec"]

list_names.append("Dania")

print(list_names)

list_of_squares= []
for int in range (1,10):
    square= int**2
    list_of_squares.append(square)
    
print(list_of_squares)

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
#[expression for int in list if condition]
squared2 = [int**2 for int in range(1, 10)]
print(squared2)

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9,]
for numbers in numbers:
    print(numbers**3)
    
cubic = [num**3]
print

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9,]

#1 doubling the values of each element

#2 filtering the list to include and double only the even numbers

#3 combining list comprehensions with condition.


double_numbers = [num*2 for num in numbers if num%2 == 0]

print (double_numbers)