#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
survey = pd.read_csv("class_survey.csv")
# print(len(survey))
# gamers = survey[survey["minutes_gaming"] > 60 ]
# print(len(gamers))
# print(len(survey))

#%%
#Columns
survey["pet"] #Pulls a single column -> Pandas refers to a single column as a Series
survey[["pet", "hours_sleep"]] #Pulls multiple columns -> do not forget the two brackets
#Rows
survey["minutes_gaming"] > 60 #Boolean table: true or false for each student
gamers = survey[survey["minutes_gaming"] > 60] #Keeps only the True rows from survey and stores them in a new table gamers
survey[survey["pet"] == "dog"] #Filter based on text, always need "" around text/strings. = stores/assigns, while == compares
survey[survey["pet"].isin(["dog", "cat"])] #isin([]) keeps rows matching any value in the list

#%%
#Students who game over 60 minutes and sleep under 8 hours
gamers[gamers["hours_sleep"] < 8.0]
survey[(survey["minutes_gaming"] > 60) & (survey["hours_sleep"] < 8)] # and -> &, or -> |


# %%
survey["hours_gaming"] = survey["minutes_gaming"] / 60
survey.head()