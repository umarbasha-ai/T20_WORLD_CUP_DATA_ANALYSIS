import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:/MY_AI_AND_ML_PROJECTS/T20_WORLD_CUP_DATA_ANALYSIS/DATASET/WC DATA.csv")
print(df.head())
print(df.info())

# Venue Analysis
Venuestadium = df['Venuestadium'].value_counts()
colors = sns.color_palette("bright")
plt.figure(figsize=(10,7))
plt.barh(Venuestadium.index,Venuestadium.values,color=colors)
plt.title("MATCHES VENUES")
plt.xlabel("Matches Played")
plt.ylabel("Stadium")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(True)
plt.savefig("D:/MY_AI_AND_ML_PROJECTS/T20_WORLD_CUP_DATA_ANALYSIS/VISUALS/venue_distribution.png")
plt.show()

# Toss Decision Analysis
Tossdecision = df['Tossdecision'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=Tossdecision.index,y=Tossdecision.values,hue=Tossdecision.index,palette='Set1',legend=False)
plt.title("toss decision distribution")
plt.xlabel("decision")
plt.ylabel("count")
plt.grid(True)
plt.tight_layout()
plt.savefig("D:/MY_AI_AND_ML_PROJECTS/T20_WORLD_CUP_DATA_ANALYSIS/VISUALS/toss_decision.png")
plt.show()

#  Toss Winner vs Match Winner
df['Toss_Winner_Won'] = df['Tosswinner'] == df['Winningteam']
print(df['Toss_Winner_Won'].head(10))
toss_winner_rate = df['Toss_Winner_Won'].value_counts(normalize=True)*100
colors = sns.color_palette("dark")
plt.figure(figsize=(10,6))
plt.bar(['win after toss','loss after toss'],toss_winner_rate.values,color=colors)
plt.title("Impact of toss on match")
plt.ylabel("percentage")
plt.xlabel("Match Result")
plt.tight_layout()
plt.grid(True)
plt.savefig("D:/MY_AI_AND_ML_PROJECTS/T20_WORLD_CUP_DATA_ANALYSIS/VISUALS/toss_impact.png")
plt.show()

#  Man of the Match Frequency
colors = sns.color_palette("deep6")
mom_counts = df['Manofmatch'].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(mom_counts.index,mom_counts.values,color=colors)
plt.title("top 10 man of match winners")
plt.xlabel("Player")
plt.xticks(rotation=90)
plt.ylabel("Man of match count")
plt.tight_layout()
plt.savefig("D:/MY_AI_AND_ML_PROJECTS/T20_WORLD_CUP_DATA_ANALYSIS/VISUALS/Man_of_the_Match_Frequency.png")
plt.show()

# Win Type Distribution
print(df[['Winbyruns','Winbywickets']].head(10))
df['Win_type'] = df[['Winbyruns','Winbywickets']].apply(lambda x : 'Runs' if x['Winbyruns']>0 else('Wickets' if x['Winbywickets']>0 else 'Other'),axis=1)
print(df['Win_type'].head(10))
win_type_count = df['Win_type'].value_counts()
print(win_type_count)
colors = sns.color_palette("muted6")
plt.figure(figsize=(10,6))
plt.bar(win_type_count.index,win_type_count.values,color=colors)
plt.xlabel("Win Type")
plt.ylabel("count")
plt.title("Win type distribution")
plt.tight_layout()
plt.savefig("D:/MY_AI_AND_ML_PROJECTS/T20_WORLD_CUP_DATA_ANALYSIS/VISUALS/win_type_distribution.png")
plt.show()