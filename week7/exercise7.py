from week7.week7utils import read_file, score, MeaningRepresentation
from typing import Callable, List, Optional
import random

meaning_representations, references = read_file('week7/devset.csv')

def generate_trivial(mr: MeaningRepresentation) -> str:
    """Trivial NLG."""
    return "{} is a {} {}.".format(mr.name, mr.food, mr.eat_type)

def generate_2(mr: MeaningRepresentation) -> str:
    if mr.name and mr.food and mr.eat_type:
        return "{} is a {} {}.".format(mr.name, mr.food, mr.eat_type)
    elif mr.name and mr.food:
        return "{} offers {}.".format(mr.name, mr.food)
    elif mr.name and mr.eat_type:
        return "{} is a {}.".format(mr.name, mr.eat_type)
    else:
        return "unclear sorry"


def evaluate(
    generator: Callable[[MeaningRepresentation], str],
    meaning_representations: List[MeaningRepresentation],
    references: List[List[str]],
) -> None:
    for _ in range(10):
        print(generator(random.choice(meaning_representations)))
    print("\n")
    score(generator, meaning_representations, references)
    print("\n----\n")


evaluate(generate_trivial, meaning_representations, references)

evaluate(generate_2, meaning_representations, references)



########################################################################à
# EXERCISE 4

meaning_representations, references = read_file('week7/devset.csv')
tot = []
for mr, refs in zip(meaning_representations, references):
    out = refs.copy()
    print(refs)
    for key, value in mr.__dict__.items():
        if value is not None:
                out = [x.replace(value, "X-" + key.upper()) for x in out]
    tot.append(out)

import collections

c = collections.Counter([inner for outer in tot for inner in outer])
c
sorted(c.items(), key=lambda x:x[1], reverse=True)[:10]

#MOST POPULAR =
# ('X-NAME is a X-EAT_TYPE providing X-FOOD food in the X-PRICE_RANGE price range. It is located in the X-AREA. It is near X-NEAR. Its customer rating is X-CUSTOMER_RATING.', 38)
#38 INSTANCES
# 'X-NAME is a X-EAT_TYPE providing X-FOOD food in the X-PRICE_RANGE price range. IS A RECURRING PATTERN, other informations are jsut added.

def generate_3(mr: MeaningRepresentation) -> str:
    if mr.name and mr.eat_type and mr.food and mr.price_range and mr.area and mr.near and mr.customer_rating:
        return '{} is a {} providing {} food in the {} price range. It is located in the {}. It is near {}. Its customer rating is {}.'.format(
            mr.name, mr.eat_type, mr.food, mr.price_range, mr.area, mr.near, mr.customer_rating)
    elif mr.name and mr.eat_type and mr.food and mr.price_range and mr.near and mr.customer_rating:
        return '{} is a {} providing {} food in the {} price range. It is near {}. Its customer rating is {}.'.format(
            mr.name, mr.eat_type, mr.food, mr.price_range, mr.near, mr.customer_rating)
    elif mr.name and mr.eat_type and mr.food and mr.price_range and mr.area and mr.customer_rating:
        return '{} is a {} providing {} food in the {} price range. It is located in the {}. Its customer rating is {}.'.format(
            mr.name, mr.eat_type, mr.food, mr.price_range, mr.area, mr.customer_rating)
    elif mr.name and mr.eat_type and mr.food and mr.area and mr.near and mr.customer_rating:
        return '{} is a {} providing {} food It is located in the {}. It is near {}. Its customer rating is {}.'.format(
            mr.name, mr.eat_type, mr.food, mr.area, mr.near, mr.customer_rating)
    elif mr.name and mr.eat_type and mr.food and mr.area and mr.customer_rating:
        return '{} is a {} providing {} food It is located in the {}. Its customer rating is {}.'.format(mr.name,
                                                                                                         mr.eat_type,
                                                                                                         mr.food,
                                                                                                         mr.area,
                                                                                                         mr.customer_rating)
    elif mr.name and mr.eat_type and mr.food and mr.near and mr.customer_rating:
        return '{} is a {} providing {} food It is near {}. Its customer rating is {}.'.format(mr.name, mr.eat_type,
                                                                                               mr.food, mr.near,
                                                                                               mr.customer_rating)
    elif mr.name and mr.eat_type and mr.food and mr.price_range and mr.area and mr.near:
        return '{} is a {} providing {} food in the {} price range. It is located in the {}. It is near {}.'.format(
            mr.name, mr.eat_type, mr.food, mr.price_range, mr.area, mr.near)
    elif mr.name and mr.eat_type and mr.food and mr.price_range and mr.customer_rating:
        return '{} is a {} providing {} food in the {} price range. Its customer rating is {}.'.format(mr.name,
                                                                                                       mr.eat_type,
                                                                                                       mr.food,
                                                                                                       mr.price_range,
                                                                                                       mr.customer_rating)
    elif mr.name and mr.customer_rating and mr.near:
        return '{} has a {} customer rating and is located near {}.'.format(mr.name, mr.customer_rating, mr.near)
    elif mr.name and mr.eat_type and mr.food and mr.area and mr.near:
        return '{} is a {} providing {} food It is located in the {}. It is near {}.'.format(mr.name, mr.eat_type,
                                                                                             mr.food, mr.area, mr.near)
    else:
        return "unclear sorry"

    

evaluate(generate_3, meaning_representations, references)
