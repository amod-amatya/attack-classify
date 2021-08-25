import spacy

from spacy.matcher import Matcher

# Create the nlp object
nlp = spacy.load("en_core_web_sm") # en_core_web_sm pretrained model package that supports all core capabilities trained on web text

# Process a text
attack = nlp("Unsafe activation of different Audi vehicle functions by sending DeviceControl messages to different ECUs via CAN in Europe. 9 vehicles attacked in last month")
# Print the document text
print("Attack = {} \n".format(attack.text))

print("Token with Part of Speech POS:")
for token in attack[0:5]:
    print(token.text, token.pos_) #print part of speech

print("\nDefault Entity Recognition with label:")
for ent in attack.ents:
    print(ent.text, ent.label_)

print("\nProduct means: {}".format(spacy.explain("PRODUCT")))

# attack_type = attack[0:2]

# print(attack_type.text)

matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "DeviceControl"}, {"TEXT": "messages"}]

matcher.add("MESSAGE_PATTERN", [pattern])

# Use the matcher on the doc
matches = matcher(attack)
print("\nMatch 1:", [attack[start:end].text for match_id, start, end in matches])

matcher2 = Matcher(nlp.vocab)

pattern2 = [{"IS_DIGIT": True}, {"TEXT": "vehicles"}]

# Add the pattern to the matcher and apply the matcher to the doc
matcher2.add("Vehicle_Count", [pattern2])
vehicleCount_match = matcher2(attack)

print("\nTotal matches found for vehicle count:", len(vehicleCount_match))

#Iterate over the matches and print the span text
for match_id, start, end in vehicleCount_match:
    print("Match found:", attack[start:end].text)