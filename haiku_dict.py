import random

dict_of_mad_libs = {"Haikus are WORD#0, but sometimes they don't make WORD#1, WORD#2" :
            ["a one syllable adjective", "a one syllable noun", "a five syllable noun"],

            "Out of WORD#0, We wish to WORD#1 the whole WORD#2, But we never will." :
            ["a three syllable noun", "a one syllable verb", "a one syllable noun"],

            "Lightening WORD#0 -- what I thought were WORD#1, are plumes of pampas grass" :
            ["a one syllable verb", "a two syllable plural noun"]}


haiku = random.choice(dict_of_mad_libs.keys())
cues_for_reader = dict_of_mad_libs[haiku]

for index in range(len(cues_for_reader)):
    response = raw_input("Enter " + cues_for_reader[index] + ": ")
    haiku = haiku.replace("WORD#" + str(index), response.strip())

print haiku