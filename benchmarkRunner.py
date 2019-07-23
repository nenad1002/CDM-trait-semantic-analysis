import json

def extract_example_data(file):
    example_dict = {}

    with open(file) as json_file:
        data = json.load(json_file)
        for trait in data["data"]:
            attribute_name = trait.get('attribute')
            trait_set = set(trait.get('traits'))
            example_dict[attribute_name] = trait_set

    return example_dict


def measure_similarity(original_dict, example_dict):
    diff1 = 0
    diff2 = 0
    total1 = 0
    total2 = 0

    for output_att in original_dict:
        if output_att in example_dict:
            original_set = original_dict[output_att]
            example_set = example_dict[output_att]
            diff1 += len(original_set.difference(example_set))
            diff2 += len(example_set.difference(original_set))
            total1 += len(original_set)
            total2 += len(example_set)

    overlap_index = (total1 + total2 - (diff1 + diff2)) / (2 * (min(total1, total2)))

    return overlap_index