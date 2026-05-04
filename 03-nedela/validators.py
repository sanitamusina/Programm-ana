def is_email(text):
    """
    Pasaka True vai False - vai ievadītais teksts izskatās pēc e-pasta adreses

    Args:
        text: teksts, kas jāpārbauda
                
    Returns:
       True: ja ievadītais teksts izskatās pēc e-pasta adreses (satur @ un .)
       False: ja ievadītais teksts nav e-pasta adrese

    Raises:
        ValueError: ja nav ievadīts teksts

    Example:
        >>> is_email("sanita@inbox.lv")
        True
        >>> is_email("sanita.inbox.lv")
        False
    """
    if (text) == ([]):
        raise ValueError("ievadi tekstu")

    if "@" in text and "." in text:
        return True
    else:
        return False
    
def is_phone_number(text):
    """
    Pasaka True vai False - vai ievadītais teksts izskatās pēc Latvijas telefona numura

    Args:
        text: ievadītie simboli, kas jāpārbauda
                
    Returns:
        True: ja ievadītais teksts izskatās pēc Latvijas telefona numura (sastāv no +371 koda, tukšuma un 8 cipariem)
        False: ja ievadītais teksts nav Latvijas telefona numurs

    Raises:
        ValueError: ja nav ievadīti cipari

    Example:
        >>> is_phone_number("+371 12345678")
        True
        >>> is_phone_number("123-456-7890")
        False
        >>> is_phone_number("1234567890")
        False
        >>> is_phone_number("123 456 7890")
        False
        >>> is_phone_number("123.456.7890")
        False
    """
    if (text) == ([]):
        raise ValueError("ievadi tālruņa numuru")

    if not text.startswith("+371 "):
        return False
    atļautie_simboli = "0123456789+ "
    for simbols in text:
        if simbols not in atļautie_simboli:
            return False
        if not len(text) == 13:
            return False
    return True

def is_valid_age(age):    
    """
    Pasaka True vai False - vai ievadītais skaitlis izskatās pēc derīga vecuma

    Args:
        age: skaitlis, kas jāpārbauda
                
    Returns:
        True: ja ievadītais skaitlis izskatās pēc derīga vecuma (ir vesels skaitlis un ir lielāks par 0 un mazāks par 150)
        False: ja ievadītais skaitlis nav derīgs vecums

    Raises:
        ValueError: ja nav ievadīts vesels skaitlis

    Example:
        >>> is_valid_age(25)
        True
        >>> is_valid_age(-5)
        False
        >>> is_valid_age(150)
        True
        >>> is_valid_age(0)
        True
    """
    if not isinstance(age, int):
        raise ValueError("ievadi veselu skaitli")

    if age > 0 and age < 150:
        return True
    else:
        return False
    
def is_strong_password(text):
    """
    Pasaka True vai False - vai ievadītais teksts ir droša parole

    Args:
        text: parole, kas jāpārbauda
                
    Returns:
        True: ja ievadītais teksts ir droša parole (ir vismaz 8 simboli, satur burtus un ciparus)
        False: ja ievadītais teksts nav droša parole

    Raises:
        ValueError: ja nav ievadīts teksts

    Example:
        >>> is_strong_password("P@ssw0rd")
        True
        >>> is_strong_password("password")
        False
        >>> is_strong_password("P@ssw0r")
        False
    """
    if (text) == ([]):
        raise ValueError("ievadi paroli")

    if len(text) < 8:
        return False
    if not any(char.isdigit() for char in text):
        return False
    if not any(char.isalpha() for char in text):
        return False
    return True

def is_valid_date(text):
    """
    Pasaka True vai False - vai ievadītais teksts ir datums formātā YYYY-MM-DD

    Args:
        text: ievadītais datums, kas jāpārbauda
                
    Returns:
        True: ja ievadītais teksts ir datums formātā YYYY-MM-DDtums)
        False: ja ievadītais teksts nav datums formātā YYYY-MM-DD

    Raises:
        ValueError: ja nav ievadīts nekas vai ievadīti burti

    Example:
        >>> is_valid_date("31/12/2020")
        False
        >>> is_valid_date("31/02/2020")
        False
        >>> is_valid_date("2020-12-20")
        True
    """
    if (text) == ([]):
        raise ValueError("ievadi datumu")

    import datetime
    try:
        datetime.datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False






if __name__ == "__main__":
    print(is_email("janis@saulelv"))
    print(is_phone_number("+271 11122233"))
    print(is_valid_age(125))
    print(is_strong_password("123sanita"))
    print(is_valid_date("18.12.2025"))
