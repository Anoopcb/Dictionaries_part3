
user_info3 = {
    "name": "Anoop",
    "last_name": "Singh",
    "age": 37,
    "fav_movies": ["coco", "kimi no na wa"],
    "fav_tunes": ["awakening", "fairy tale"]
}

more_info = {"state": "Haryana", "hobbies": ["coding", "dancing", ], "name": "Anoop Singh"}

user_info3.update(more_info)
print(user_info3)
## fromkeys() method

d = dict.fromkeys(["name", "age", "height"], "unknown")
print(d)


## get() method


print(user_info3.get("name"))
print(user_info3.get("names"))

if user_info3.get("name"):
    print("There in the dictionary")
else:

    print( "Not there")



if user_info3.get("names"):
    print("There in the dictionary")
else:

    print( "Not there")
## clear() method will clear the dictionary and you will get empty dictionary
d.clear()
print(d)


## copy() mehtod


user_info4 = user_info3.copy()
print(user_info4)
user_info3.clear()
print(user_info3)
print(user_info4)

## more about get() methods



print(user_info4.get("name", "not found"))

## cube finder function
def cube_finder(num):
    cubes ={}

    for i in range(1, num+1):
        cubes[i] = i**3

    return cubes
print(cube_finder(10))


# how to make funciton for counting character to create dictionary 
def word_counter(s):
    count = {}
    for char in s:

        count[char] = s.count(char)
    return count

print(word_counter("AnoopSheroan"))





























