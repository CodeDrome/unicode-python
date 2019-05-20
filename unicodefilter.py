import unicodedata


def get_characters(character_name_like="", category_name_like=""):

    """
    Returns a list of dictionaries holding
    details of the Unicode characters
    which satisfy the search criteria
    given in the arguments.
    """

    character_name_like = character_name_like.lower()
    category_name_like = category_name_like.lower()

    category_names = _create_category_names()

    ucl = []

    for n in range(0, 137994):

        try:

            character = chr(n)
            name = unicodedata.name(character)
            category = unicodedata.category(character)
            category_name = category_names[category]

            if character_name_like in name.lower() \
            and category_name_like in category_name.lower():

                cd = {"codepoint_dec": n,
                      "codepoint_hex": format(n, "X"),
                      "character": character,
                      "name": name,
                      "category": category,
                      "category_name": category_name}

                ucl.append(cd)

        except ValueError as e:

            pass

    return ucl


def _create_category_names():

    category_names = {}

    # Letter
    category_names["Lu"] = "Letter, uppercase"
    category_names["Ll"] = "Letter, lowercase"
    category_names["Lt"] = "Letter, titlecase"
    category_names["Lm"] = "Letter, modifie"
    category_names["Lo"] = "Letter, other"

    # Mark
    category_names["Mn"] = "Mark, nonspacing"
    category_names["Mc"] = "Mark, spacing combining"
    category_names["Me"] = "Mark, enclosing"

    # Number
    category_names["Nd"] = "Number, decimal digit"
    category_names["Nl"] = "Number, letter"
    category_names["No"] = "Number, other"

    # Punctuation
    category_names["Pc"] = "Punctuation, connector"
    category_names["Pd"] = "Punctuation, dash"
    category_names["Ps"] = "Punctuation, open"
    category_names["Pe"] = "Punctuation, close"
    category_names["Pi"] = "Punctuation, initial quote"
    category_names["Pf"] = "Punctuation, final quote"
    category_names["Po"] = "Punctuation, other"

    # Symbol
    category_names["Sm"] = "Symbol, math"
    category_names["Sc"] = "Symbol, currency"
    category_names["Sk"] = "Symbol, modifier"
    category_names["So"] = "Symbol, other"

    # Separator
    category_names["Zs"] = "Separator, space"
    category_names["Zl"] = "Separator, line"
    category_names["Zp"] = "Separator, paragraph"

    # Other
    category_names["Cc"] = "Other, control"
    category_names["Cf"] = "Other, format"
    category_names["Cs"] = "Other, surrogate"
    category_names["Co"] = "Other, private use"
    category_names["Cn"] = "Other, not assigned"

    return category_names
