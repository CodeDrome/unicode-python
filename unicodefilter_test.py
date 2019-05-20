import unicodedata

import unicodefilter


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Unicode       |")
    print("-----------------\n")

    print("Unicode version {}\n".format(unicodedata.unidata_version))

    ucl = unicodefilter.get_characters(character_name_like="coptic",
                                       category_name_like="number")

    for uc in ucl:

        print("| {:<6} | {:6} | {:4} | {:72} | {:2} | {:32} |"
              .format(uc["codepoint_dec"],
              uc["codepoint_hex"],
              uc["character"],
              uc["name"],
              uc["category"],
              uc["category_name"]))

    print("\n{} characters in filtered list\n".format(len(ucl)))


main()
