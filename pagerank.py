import numpy as np
import csv

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

def get_relations_matrix(relations,keys):
    relations_matrix = []
    for user_a in keys:
        relation = []
        number_of_relations = len(relations[user_a])
        for user_b in keys:
            if (user_b in relations[user_a]):
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
    relations = csv_to_dict("teste")
    keys = list(relations.keys())
    number_of_nodes = len(keys)

    relations_matrix = get_relations_matrix(relations, keys)
    rank_vector = page_rank(relations_matrix,number_of_nodes,iterations=185)
    print(rank_vector)

main()