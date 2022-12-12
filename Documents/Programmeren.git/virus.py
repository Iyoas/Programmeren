import random
import string

def generate_virus(length: int) -> str:
    '''
    Returnt een virus.
    >>> random.seed(0)
    >>> generate_virus(4)
    'CCAT'
    >>> generate_virus(4)
    'CCTC'
    >>> generate_virus(3)
    'TGG'
    '''
    return ''.join([random.choice('AGTC') for i in range(length)])
    
def mutate(virus: str) -> str:
    '''
    Returnt een mutatie van een virus.
    >>> random.seed(0)
    >>> mutate('CCAT')
    'CCAC'
    >>> mutate('CCC')
    'ACC'
    >>> mutate('TATG')
    'TATC'
    '''
    element = random.choice('AGTC')
    replaced_element = random.choice(virus)
    element_replace = virus.replace(replaced_element, element, 1)
    while element_replace == virus:
        element = random.choice('AGTC')
        element_replace = virus.replace(replaced_element, element, 1)
    return element_replace 

def kill(viruses: list[str], mortality_prob: float)-> list[str]:
    '''
    Returnt een de virussen die het hebben overleefd.
    >>> random.seed(0)
    >>> kill(['ACTG', 'GACT', 'TTAC'], 0.5)
    ['ACTG', 'GACT']
    >>> kill(['ACTG', 'GTTT', 'TTAC'], 0.8)
    []
    >>> kill(['ACTG', 'GACT', 'TTAC', 'CCTA'], 0.3)
    ['ACTG', 'GACT', 'TTAC', 'CCTA']
    '''

    return [virus for virus in viruses if random.uniform(0, 1) > mortality_prob]

def reproduce(viruses: list[str], mutation_prob: float, reproduction_prob: float) -> list[str]:
    '''
    Returnt een kind van het virus.
    >>> random.seed(0)
    >>> reproduce(['ACTG'], 0.5, 0.5)
    ['ACTG']
    >>> reproduce(['ACTG'], 0.8, 0.9)
    ['ACTG', 'ACTG']
    >>> reproduce(['ACTG'], 0.3, 0.5)
    ['ACTG', 'ACTG']
    '''
    child = [virus for virus in viruses if random.uniform(0, 1) < reproduction_prob]
    for virus in child:
         if random.uniform(0, 1) < mutation_prob:
             mutate(virus)
    return viruses + child

def is_resistant(virus: str)-> bool:
    '''
    Retunt True als de virus resistent is anders False.
    >>> is_resistant('ACTG')
    False
    >>> is_resistant('AAAC')
    True
    >>> is_resistant('AGG')
    False
    '''
    if 'AAA' in virus:
        return True
    else: 
        return False

def reproduction_probability(viruses: list[str], max_reproduction_prob: float, max_population: int)-> float:
    return (1 - (len(viruses) / max_population)) * max_reproduction_prob if max_population > 0 else 0


if __name__ == '__main__':
    length = int(input('lengte: '))
    mortality_prob = float(input('overlevingkans: '))
    nucleotiden = ['A', 'G', 'C', 'T' ]
    reproduction_prob = float(input('Reproductiekans: '))
    mutation_prob = float(input('Mutatiekans: '))
    virus = generate_virus(length)
    mutation = mutate(virus)
    viruses = [mutate(virus)] + [mutate(virus)] + [mutate(virus)] + [mutate(virus)]
    child = [virus for virus in viruses if random.uniform(0, 1) < reproduction_prob]
    print(viruses)
    print(child)
    print(reproduce(viruses, mutation_prob, reproduction_prob))
    