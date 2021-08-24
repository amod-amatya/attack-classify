import spacy

# Create the nlp object
nlp = spacy.load("en_core_web_sm") # en_core_web_sm pretrained model package that supports all core capabilities trained on web text

# Process a text
attack = nlp("Unsafe activation of different Audi vehicle functions by sending Device Control messages to different ECUs via CAN in Europe.")

# Print the document text
print(attack.text)

for token in attack:
    print(token.text, token.pos_) #print part of speech

for ent in attack.ents:
    print(ent.text, ent.label_)

print(spacy.explain("PRODUCT"))

attack_type = attack[0:2]

print(attack_type.text)


