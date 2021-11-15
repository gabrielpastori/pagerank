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

def export_to_json(file_name):
    json_object = json.dumps(matchs_relations, indent=4, ensure_ascii=False)
    with open(f"{file_name}.json", "w", encoding="utf-8") as outfile:
        outfile.write(json_object)

def main():
    with open('campeonato-brasileiro.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        get_teams_by_date('2020-08-08','2021-02-25',csv_reader)
    export_to_json("results2020")
main()    
    
