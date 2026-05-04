def capitalize(text):
    """
    Pārvērš teksta pirmo burtu par lielo burtu un pārējos par maziem burtiem

    Args:
        text (str): teksts, kuru pārvērst

    Returns:
        str: teksts ar pirmo lielo burtu un pārējiem maziem burtiem

    Raises:
        ValueError: ja ievadīti cipari nevis teksts

    Example:
        >>> capitalize("sanita")
        'Sanita'
        >>> capitalize("sANITA")
        'Sanita'
    """

    if not isinstance(text, str):
        raise ValueError("Ievadi tekstu!")

    if len(text) == 0:
        return ""

    return text[0].upper() + text[1:].lower()


def truncate(text, max_len=20):
    """
    Saīsina tekstu līdz norādītajam maksimālajam garumam
    un, ja teksts ir saīsināts, pievieno "...".

    Args:
        text (str): teksts, kuru saīsināt
        max_len (int): maksimālais teksta garums simbolos (noklusējums 20)

    Returns:
        str: pilnais vai saīsinātais teksts

    Raises:
        ValueError: ja max_len ir mazāks vai vienāds ar 0

    Example:
        >>> truncate("Sveika, pasaule!", 6)
        'Sveika...'
        >>> truncate("Sveika", 20)
        'Sveika'
    """
 
    if max_len <= 0:
        raise ValueError("max_len jābūt lielākam par 0")

    if len(text) > max_len:
        return text[:max_len] + "..."

    return text

def count_words(text):
    """
    Saskaita vārdus ievadītajā tekstā

    Args:
        text (str): teksts, kurā tiks skaitīti vārdi
        
    Returns:
        (int): vārdu skaits

    Raises:
        ValueError: ja (text) = (int) vai (float)

    Example:
        >>> count_words("Sveika, pasaule!")
        2
        >>> count_words("Mani sauc Sanita")
        3
    """
    
    if not isinstance(text, str):
        raise ValueError("Ievadi tekstu nevis skaitļus!")
   
    return len(text.split())

def clamp(num, low, high):
    """
    Ierobežo skaitli intervālā no līdz

    Args:
        num: skaitlis, ko ievada
        low: apakšējā skaitļu virknes robeža, par kuru ievadītais skaitlis nedrīkst būt mazāks
        high: augšējā skaitļu virknes robeža, par kuru ievadītais skaitlis nedrīkst būt lielāks
        
    Returns:
       num: ievadīto skaitli, vai zemāko robežskaitli, ja ievadītais ir par to mazāks vai arī augstāko robežskaitli, ja ievadītais skaitlis ir lielāks

    Raises:
        ValueError: ja (num) = (str)

    Example:
        >>> clamp(2, 1, 10)
        2
        >>> clamp(-5, 1, 10)
        1
        >>> clamp(12, 1, 10)
        10
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Ievadi skaitļus, nevis tekstu!")

    if num < low:
        return low
    if num > high:
        return high
    return num

def is_prime(num):
    """
    Pasaka True vai False - vai ievadītais skaitlis ir pirmskaitlis

    Args:
        num: skaitlis, ko ievada
                
    Returns:
       True: ja ievadītais skaitlis ir pirmskaitlis (dalas tikai ar sevi un 1)
       False: ja ievadītais skaitlis nav pirmskaitlis

    Raises:
        ValueError: ja (num) <= 1 vai (str)

    Example:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """

    if not isinstance(num, int):
        raise ValueError ("ievadi skaitli, kas ir lielāks par 1")
    
    if num <= 1:
        raise ValueError("Skaitlim jābūt lielākam par 1")

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def factorial(n):
    """
    aprēķina ievadītā skaitļa (n) faktoriāli n!

    Args:
        n: skaitlis, kura faktoriāli jāaprēķina
                
    Returns:
       factorial(n) - ievadītā skaitļa n faktoriāli n!

    Raises:
        ValueError: ja n ir negatīvs vai nav vesels skaitlis

    Example:
        >>> factorial(3)
        6
        >>> factorial(4)
        24
    """
    if n < 0:
        raise ValueError("Ievadi skaitli, kas ir lielāks vai vienāds ar 0")
    if not isinstance(n, int):
        raise ValueError("Skaitlim jābūt veselam un lielākam par 0")

    if n == 0:
        return 1
     
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def total(numbers):
    """
    aprēķina ievadīto skaitļu kopsummu

    Args:
        numbers: skaitļu virkne, kurai jāaprēķina kopsumma
                
    Returns:
       total(numbers) - ievadīto skaitļu kopsumma

    Raises:
        ValueError: ja (numbers) nav skaitļu virkne vai skaitļu vietā ir teksts

    Example:
        >>> total(1, 2, 3)
        6
        >>> total(4, 2, 5)
        11
    """    
    if not isinstance(numbers, list):
        raise ValueError("ievadi skaitļu virkni")
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError("ievadi skaitļu virkni")
    summa = 0
    for i in numbers:
        summa = summa + i
    return summa


def average(numbers):
    """
    aprēķina vidējo vērtību no ievadītajiem skaitļiem

    Args: 
        numbers: skaitļu virkne, kurai jāaprēķina vidējā vērtība
    
    Returns:
        average(numbers): vidējā ievadīto skaitļu vērtība

    Raises:
        ValueError: ja numbers nav skaitļu virkne vai saraksts ir tukšs

    Example:
        >>> average(1, 2, 3)
        2
        >>> average(2, 4, 6, 8)
        5

    """
    if not isinstance(numbers, list):
        raise ValueError("ievadi skaitļu virkni")
    for n in numbers:
        if not isinstance(n, (int, float)):
            raise ValueError("ievadi skaitļu virkni")
    if len(numbers) == 0:
        raise ValueError("saraksts nedrīkst būt tukšs")

    summa = 0
    skaits = 0
    for i in numbers:
        summa = summa + i
        skaits = skaits +1
    return summa / skaits
    
if __name__ == "__main__":
    print("rĪGA".capitalize())
    print("truncate(šis teksts ir jāsaīsina līdz maksimums divdesmit simboliem, max_len=20)")
    print(truncate("šis teksts ir jāsaīsina līdz maksimums divdesmit simboliem", max_len=20))
    print(count_words("Saskaiti vārdus šajā garajā teikumā"))
    print(count_words("Jānis Toms Klāvs Viktors Sanita Ruta Inese Modris Artūrs"))
    print(clamp(6, 0, 100))
    print(clamp(-2, 0, 100))
    print(clamp(103, 0, 100))
    print(is_prime(10))
    print(is_prime(13))
    print(factorial(4))
    print(factorial(5))
    numbers = [4, 5, 2, 5, 7, 8, 32]   
    print(total(numbers))
    numbers = [1, 2, 3, 4, 5]
    print(average(numbers))