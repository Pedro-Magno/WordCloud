import pandas

Removal_DF = pandas.read_csv("most-common-words-1k.csv")
Removal_DF = Removal_DF.drop(Removal_DF[Removal_DF["Main Type"] == "noun"].index)
Word_Collumn1 = Removal_DF.loc[:,"Word"]
List1 = Word_Collumn1.values.tolist()
List1_Upper = []
for i in List1:
    List1_Upper.append(i.upper())
To_Remove_DF = pandas.read_csv("../Dataframe.csv")
Word_Collumn2 = To_Remove_DF.loc[:,"Word"]
List2 = Word_Collumn2.values.tolist()

for i in List1_Upper:
        To_Remove_DF = To_Remove_DF.drop(To_Remove_DF[To_Remove_DF["Word"] == i].index)
#To_Remove_DF = To_Remove_DF.drop(To_Remove_DF.columns[0], axis = 1)
To_Remove_DF.to_csv("Semi_Formatted_Dataframe.csv")

print(To_Remove_DF)
print(List2)