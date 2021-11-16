import numpy as np
import csv
import json

def csv_to_dict(filename):
    relations = {}
    with open(f'{filename}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            if(row[0] not in relations):
                relations[row[0]] = [row[1]]
            else:
                relations[row[0]].append(row[1])
    return relations

def json_to_dict(filename):
    with open(f'{filename}.json') as json_file:
        data = json.load(json_file)
  
    return (data)

def get_relations_matrix(relations,keys):
    relations_matrix = []
    for key_a in keys:
        relation = []
        number_of_relations = len(relations[key_a])
        for key_b in keys:
            if (key_b in relations[key_a]):
                relation.append(1/number_of_relations)
            else:
                relation.append(0)   
        relations_matrix.append(relation)      
    relations_matrix_np = np.array(relations_matrix)
    relations_matrix_np_transposed = relations_matrix_np.T
    return relations_matrix_np_transposed

def page_rank(relations_matrix, number_of_nodes , iterations=85, alfa=0.85):
    one_matrix = np.ones((number_of_nodes,number_of_nodes))
    normalized_vector = np.empty(number_of_nodes)
    normalized_vector.fill(1/number_of_nodes)
    g_matrix = alfa*relations_matrix + ((1-alfa)/number_of_nodes)*one_matrix
    g_matrix_power = np.linalg.matrix_power(g_matrix,iterations)
    rank_vector = g_matrix_power.dot(normalized_vector)
    return rank_vector

def main():
    relations = json_to_dict('results2020')
    keys = list(relations.keys())
    number_of_nodes = len(keys)
    relations_matrix = get_relations_matrix(relations, keys)
    rank_vector = page_rank(relations_matrix,number_of_nodes,iterations=185)
    rank_vector_dict = dict(zip(keys,rank_vector))
    rank_vector_dict_sorted = dict(sorted(rank_vector_dict.items(), key=lambda item: item[1]))

    print(rank_vector_dict_sorted)
    

main()