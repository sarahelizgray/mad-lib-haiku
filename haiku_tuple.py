import random

MAD_LIB_0 = ("Haikus are WORD#0, but sometimes they don't make WORD#1, WORD#2",
            ["a one syllable verb", "a one syllable noun", "a five syllable noun"])

MAD_LIB_1 = ("Out of WORD#0, We wish to WORD#1 the whole WORD#2, But we never will.",
            ["a three syllable noun", "a one syllable verb", "a one syllable noun"])

MAD_LIB_2 = ("Lightening WORD#0 -- what I thought were WORD#1, are plumes of pampas grass",
            ["a one syllable verb", "a two syllable plural noun"])

list_of_mad_libs = [MAD_LIB_0, MAD_LIB_1, MAD_LIB_2]

mad_lib = random.choice(list_of_mad_libs)

haiku = mad_lib[0]
cues_for_reader = mad_lib[1]

for index in range(len(cues_for_reader)):
    response = raw_input("Enter " + cues_for_reader[index] + ": ")
    haiku = haiku.replace("WORD#" + str(index), response.strip())

print haiku