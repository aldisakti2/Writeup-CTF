names = ['name="f02b"/><!--', 'name="six"/><!--', 'name="fi"/><!--', 'name="f010"/><!--', 'name="f01b"/><!--', 'name="f014"/><!--', 'name="f01f"/><!--', 'name="eight"/><!--', 'name="f020"/><!--', 'name="f024"/><!--', 'name="finalkafsheva"/><!--', 'name="lamedholam"/><!--', 'name="f025"/><!--', 'name="f023"/><!--', 'name="afii10065"/><!--', 'name="uniF00C"/><!--', 'name="f015"/><!--', 'name="onesuperior"/><!--', 'name="uniF00D"/><!--', 'name="commaaccent"/><!--', 'name="f022"/><!--', 'name="f027"/><!--', 'name="f019"/><!--', 'name="f007"/><!--', 'name="f029"/><!--', 'name="f02e"/><!--', 'name="f013"/><!--', 'name="twosuperior"/><!--', 'name="f006"/><!--', 'name="f02c"/><!--', 'name="afii62881"/><!--', 'name="fl"/><!--', 'name="uniF00B"/><!--', 'name="zero"/><!--', 'name="undercommaaccent"/><!--', 'name="five"/><!--', 'name="uniF00E"/><!--', 'name="f028"/><!--', 'name="f02a"/><!--', 'name="threesuperior"/><!--', 'name="f026"/><!--', 'name="lamedholamdagesh"/><!--', 'name="seven"/><!--', 'name="uniF00A"/><!--', 'name="d"/><!--', 'name="f031"/><!--', 'name="f02f"/><!--', 'name="four"/><!--', 'name="afii10083"/><!--', 'name="vavshindot"/><!--', 'name="estimated"/><!--', 'name="afii10094"/><!--', 'name="f00f"/><!--', 'name="f"/><!--', 'name="f01d"/><!--', 'name="f017"/><!--', 'name="afii57391"/><!--', 'name="nine"/><!--', 'name="f009"/><!--', 'name="f018"/><!--', 'name="f01e"/><!--', 'name="f011"/><!--', 'name="f01a"/><!--', 'name="f016"/><!--', 'name="f02d"/><!--', 'name="f021"/><!--', 'name="f012"/><!--', 'name="f030"/><!--', 'name="f01c"/><!--', 'name="finalkafqamats"/><!--', 'name="f008"/><!--']

# Map of number names to their hex values
number_map = {
    "zero": 0x0,
    "one": 0x1,
    "two": 0x2,
    "three": 0x3,
    "four": 0x4,
    "five": 0x5,
    "six": 0x6,
    "seven": 0x7,
    "eight": 0x8,
    "nine": 0x9
}

# Extracting names from the list
extracted_names = [name.split('"')[1] for name in names]

# Creating the dictionary
map_odttf_file = {}
for name in extracted_names:
    if name in number_map:
        map_odttf_file[name] = hex(number_map[name])
    else:
        map_odttf_file[name] = "??"

print(map_odttf_file)
