import csv
import json
matchs_relations = {}

def add_match_relation(team_winner,team_loser):
    if(team_loser not in matchs_relations):
        matchs_relations[team_loser] = [team_winner]
    else:
        matchs_relations[team_loser].append(team_winner)


def get_loser(team_A,team_B,team_winner):
    if(team_A==team_winner):
        return team_B
    if(team_B==team_winner):
        return team_A
    return "-"

def get_teams_by_date(min_date,max_date,csv_reader):
    count=0
    for row in csv_reader:
        date = row[2]
        if(date>=min_date and date<=max_date):
            count+=1
            team_A = row[5]
            team_B = row[6]
            team_winner = row[7]
            team_loser = get_loser(team_A,team_B,team_winner)

            if(team_winner=="-"):
                add_match_relation(team_A,team_B)
                add_match_relation(team_B,team_A)
            else:
                add_match_relation(team_winner,team_loser)
    json_object = json.dumps(matchs_relations, indent=4, ensure_ascii=False)
    with open("sample.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_object)
    print(count)

def merge_results():
    new_dict = {}
    dict = matchs_relations
    teams = list(matchs_relations.keys())
    for current_index in range(0, len(teams) - 1):
        current = teams[current_index]
        for next_index in range(current_index + 1, len(teams)):
            next = teams[next_index]
            next_in_current  = dict[current].count(next)
            current_in_next = dict[next].count(current)
            if next_in_current < current_in_next:
                if next not in new_dict.keys():
                    new_dict[next] = [current]
                else:
                    new_dict[next].append(current)
            elif next_in_current > current_in_next:
                if current not in new_dict.keys():
                    new_dict[current] = [next]
                else:
                    new_dict[current].append(next)
            else:
                if current not in new_dict.keys():
                    new_dict[current] = [next]
                else:
                    new_dict[current].append(next)
                if next not in new_dict.keys():
                    new_dict[next] = [current]
                else:
                    new_dict[next].append(current)
    
    return new_dict

    
def export_to_json(file_name,dict):
    json_object = json.dumps(dict, indent=4, ensure_ascii=False)
    with open(f"{file_name}.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_object)

def main():
    start_date = '2020-08-02'
    end_date = '2021-02-28'
    with open('campeonato-brasileiro.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        get_teams_by_date(start_date,end_date,csv_reader)
    
    fixed_data = merge_results()
    print(fixed_data)
    #export_to_json("results2020",fixed_data)
main()    
    
