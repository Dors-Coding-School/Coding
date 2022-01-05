import csv
from sys import argv


def main():

    # check for correct number of arguments
    # if correct, we assume we have .csv file in second argument and .txt file in third argument
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # open files
    database_file = open("./"+ argv[1])
    dna_file = open("./" + argv[2])

    # obtain STRs from header of database
    database_reader = csv.DictReader(database_file)
    strs = database_reader.fieldnames[1:]



    # copy contents of dna_file into string dna and close file
    dna = dna_file.read()
    dna_file.close()

    # count number of occurences of each STR in sequence.txt and store value in dict dna_fingerprint
    dna_fingerprint = {}
    for str in strs:
        dna_fingerprint[str] = consec_repeats(str, dna)
        


    # search through csv file to find match
    for row in database_reader:

        # if there is match, print name, close files, and end program
        if match(strs, dna_fingerprint, row):
            print(f"{row['name']}")
            database_file.close()
            return

    # if no match was found, print No match and close files.
    print("No match")
    database_file.close()


# repeats determines the maximum number of consecutive repeats of str in dna
def consec_repeats(str, dna):
    i = 0
    while str*(i+1) in dna:
        i += 1
    return i




# match determines whether dna_fingerprint matches row from database
def match(strs, dna_fingerprint, row):
    for str in strs:
        if dna_fingerprint[str] != int(row[str]):
            return False
    return True


main()