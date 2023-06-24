import pandas as pd
import os
def getData():
    files = os.listdir("dataset/")
    print(files)
    topics = {}
    i = 1
    weeks = []
    for file in files:
        if file == "prob_topicos.csv":
            continue
        df = pd.read_csv("dataset/"+file)
        weeks.append("Semana "+str(i))
        i += 1
        for index, row in df.iterrows(): 
            if row["topic"] in topics.keys():
                topics[row["topic"]].append(row["probability"])
            else:
                topics[row["topic"]] = [row["probability"]]
    return topics, weeks
#print(topics)

def getData2():
    df = pd.read_csv(r"C:\Users\Dell\OneDrive - Universidad de Sonora\desktop\Programming\pln\animated-octo-broccoli\dashboard\dataset\prob_topicos.csv")
    weeks = []
    probs = {}
    topics = []
    weeks = df["Week"].to_list()
    promedios = {}
    for col in df.columns:
        if col == "Week":
            continue
        else:
            probs[col] = df[col].to_list()
            promedios[col] = sum(df[col].to_list())/len(df[col].to_list())
            topics.append(col)
    #print(promedios)
    return probs, weeks, topics, promedios
    #print(weeks)
    #print(topics)
