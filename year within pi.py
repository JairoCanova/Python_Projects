//you need the pack "mpmath" to run this code, type < pip install mpmath > at a terminal to download

from mpmath import mp

def find_birth_year_in_pi(birth_year):
    mp.dps = 10000
    pi_digits = str(mp.pi)[2:]
    birth_year_str = str(birth_year)
    position = pi_digits.find(birth_year_str)
     return position

if __name__ == "__main__":
    birth_year = input("Enter your birth year (YYYY): ")
    
    try:
        birth_year = int(birth_year)
        position = find_birth_year_in_pi(birth_year)
        
        if position != -1:
            print(f"The sequence {birth_year} appears in the decimal expansion of pi at position {position}.")
        else:
            print(f"The sequence {birth_year} does not appear in the decimal expansion of pi.")
    except ValueError:
        print("Please enter a valid year.")
