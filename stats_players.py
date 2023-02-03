import pandas as pd
pd.set_option('display.max_columns', None)

df_players_stats = pd.read_csv('players_stats.csv')

df_players_stats = df_players_stats.drop(["Unnamed: 0",
                                          "ID",
                                          "Unnamed: 25",
                                          "Url"],
                                   axis = 1)

df_players_stats = df_players_stats.rename(columns={"T/R" : "Tit. ou Rempl.",
                                             "E" : "Essais",
                                             "T" : "Transfo.",
                                             "P": "Pénalités",
                                             "D" : "Drops",
                                             "J" : "Cart. Jau.",
                                             "R" : "Cart. Rou."})
                                             
                                             
def stats_player(name_player):
    df_stats_player = df_players_stats[df_players_stats["Nom"] == name_player]
    print("Prénom :",df_stats_player["Prénom"].unique())
    print("Nom :", df_stats_player["Nom"].unique())
    print("Nombre de matchs joués par compétition", df_stats_player[["Compétition","Matchs"]].groupby("Compétition").sum())
    print("Nombre de matchs joués total :", df_stats_player["Matchs"].sum())
    print("Minutes jouées par compétition :", df_stats_player[["Compétition","Temps"]].groupby("Compétition").sum())
    print("Minutes totales :", df_stats_player["Temps"].sum())
    print("Âge :", df_stats_player["Âge"].unique())
    print("Poids :", df_stats_player["Poids"].unique())
    print("Taille :", df_stats_player["Taille"].unique())
