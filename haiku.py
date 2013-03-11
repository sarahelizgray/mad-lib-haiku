# author Sarah Gray

import random

mad_lib_0 = ("Haikus are %0, but sometimes they don't make %1, %2",
            ["a one syllable adjective", "a one syllable noun", "a five syllable noun"])

mad_lib_1 = ("Out of %0, We wish to %1 the whole %2, But we never will.",
            ["a three syllable noun", "a one syllable verb", "a one syllable noun"])

mad_lib_2 = ("Lightening %0 -- what I thought were %1, are plumes of %2",
            ["a one syllable adjective", "a two syllable plural noun", "a three syllable noun"])

list_of_mad_libs = [mad_lib_0, mad_lib_1, mad_lib_2]

mad_lib = random.choice(list_of_mad_libs)

haiku = mad_lib[0]
cues_for_reader = mad_lib[1]

for i in range(len(cues_for_reader)):
    response = raw_input("Enter " + cues_for_reader[i] + ": ")
    haiku = haiku.replace("%" + str(i), response)

print haiku




