import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                #p = joint_probability(people, {"Harry"}, {"James"}, {"James"})
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

def check_how_many_genes(person, one_gene, two_genes):
    """
    Determine the number of genes a person has based on sets.
    """
    if person in one_gene:
        return 1
    elif person in two_genes:
        return 2
    return 0


def probability_dont_have_parents(num_genes, trait):
    """
    Calculate probability without considering parents' genes.
    """
    return (PROBS["gene"][num_genes] * PROBS["trait"][num_genes][trait])


def probability_have_parents(people, person, one_gene, two_genes, num_genes):
    """
    Calculate probability considering parents' genes.
    """
    # If has mom and dad, get their genes
    # Get name of the mom
    mother = people[person]['mother']
    # Check how many genes she has
    mother_genes = check_how_many_genes(mother, one_gene, two_genes)
    # Get name of the dad
    father = people[person]['father']
    # Check how many genes she has
    father_genes = check_how_many_genes(father, one_gene, two_genes)


    # Probability of passing genes
    prob_father_pass_gene = father_genes/2
    prob_mother_pass_gene = mother_genes/2

        
    # Possible scenarios of parents passing genes
    p_father_pass_gene_and_dont_mutate = prob_father_pass_gene * (1 - PROBS["mutation"])
    p_father_pass_gene_and_do_mutate = prob_father_pass_gene * PROBS["mutation"]
    p_father_dont_pass_gene_and_dont_mutate = (1 - prob_father_pass_gene) * (1 - PROBS["mutation"])
    p_father_dont_pass_gene_and_do_mutate = (1 - prob_father_pass_gene) * PROBS["mutation"]
    p_mother_pass_gene_and_dont_mutate = prob_mother_pass_gene * (1 - PROBS["mutation"])
    p_mother_pass_gene_and_do_mutate = prob_mother_pass_gene * PROBS["mutation"]
    p_mother_dont_pass_gene_and_dont_mutate = (1 - prob_mother_pass_gene) * (1 - PROBS["mutation"])
    p_mother_dont_pass_gene_and_do_mutate = (1 - prob_mother_pass_gene) * PROBS["mutation"]

        
    # If num_genes = 0, we have 4 scenarios 
    if num_genes == 0:
        probability = (p_father_pass_gene_and_do_mutate * p_mother_dont_pass_gene_and_dont_mutate) + \
            (p_father_pass_gene_and_do_mutate * p_mother_pass_gene_and_do_mutate) + \
                (p_father_dont_pass_gene_and_dont_mutate * p_mother_pass_gene_and_do_mutate) + \
                    (p_father_dont_pass_gene_and_dont_mutate * p_mother_dont_pass_gene_and_dont_mutate)

    # If num_genes = 1, we have 8 scenarios 
    elif num_genes == 1:
        probability = (p_father_pass_gene_and_dont_mutate * p_mother_dont_pass_gene_and_dont_mutate) + \
            (p_father_pass_gene_and_dont_mutate * p_mother_pass_gene_and_do_mutate) + \
                (p_father_pass_gene_and_do_mutate * p_mother_dont_pass_gene_and_do_mutate) + \
                    (p_father_pass_gene_and_do_mutate * p_mother_pass_gene_and_dont_mutate) + \
                        (p_father_dont_pass_gene_and_do_mutate * p_mother_dont_pass_gene_and_dont_mutate) + \
                            (p_father_dont_pass_gene_and_do_mutate * p_mother_pass_gene_and_do_mutate) + \
                                (p_father_dont_pass_gene_and_dont_mutate * p_mother_pass_gene_and_dont_mutate) + \
                                    (p_father_dont_pass_gene_and_dont_mutate * p_mother_dont_pass_gene_and_do_mutate)

    # If num_genes = 2, we have 4 scenarios
    elif num_genes == 2:
        probability = (p_father_pass_gene_and_dont_mutate * p_mother_pass_gene_and_dont_mutate) + \
            (p_father_dont_pass_gene_and_do_mutate * p_mother_dont_pass_gene_and_do_mutate) + \
                (p_father_dont_pass_gene_and_do_mutate * p_mother_pass_gene_and_dont_mutate) + \
                    (p_father_pass_gene_and_dont_mutate * p_mother_dont_pass_gene_and_do_mutate)
    
    return probability


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    probability = 1
    for person in people:
        num_genes = check_how_many_genes(person, one_gene, two_genes)
        
        # By the definition of joint_probability, we know if the person has trait or not
        trait = person in have_trait

        # Check if has parents
        # If hasn't mom or dad, use the unconditional probability
        if not people[person]['mother'] or not people[person]['father']:
            probability *= probability_dont_have_parents(num_genes, trait)
        else:
            probability *= (probability_have_parents(people, person, one_gene, two_genes, num_genes) * PROBS["trait"][num_genes][trait])
        
    return probability 


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        num_genes = check_how_many_genes(person, one_gene, two_genes)

        # By the definition of update, we know if the person has trait or not
        trait = person in have_trait

        probabilities[person]["gene"][num_genes] += p
        probabilities[person]["trait"][trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # the values in the distribution sum to 1, and the relative values in the distribution are the same.
    for person in probabilities:
        sum_trait = sum(probabilities[person]["trait"].values())
        sum_gene = sum(probabilities[person]["gene"].values())

        # Working with genes
        for gene in probabilities[person]["gene"]:
            original_value = probabilities[person]["gene"][gene]
            normalized_value = original_value / sum_gene
            probabilities[person]["gene"][gene] = normalized_value

        #Working with traits
        for trait in probabilities[person]["trait"]:
            original_value_trait = probabilities[person]["trait"][trait]
            normalized_value_trait = original_value_trait / sum_trait
            probabilities[person]["trait"][trait] = normalized_value_trait

    return probabilities


if __name__ == "__main__":
    main()
