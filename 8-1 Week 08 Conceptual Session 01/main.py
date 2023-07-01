import pandas as pd
import numpy as np

data = {
  "Outlook": ["Rainy", "Rainy", "Overcast","Sunny","Sunny","Sunny","Overcast","Rainy","Rainy","Sunny","Rainy","Overcast","Overcast","Sunny"],
  "Temp": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
  "Humidity": ["High", "High", "High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
  "Windy":['no','yes','no','no','no','yes','yes','no','no','no','yes','yes','no','yes'],
  "Play":["no","no","yes","yes","yes","no","yes","no","yes","yes","yes","yes","yes","no"]
}

df = pd.DataFrame(data)

#data precessing
x = df.drop(df.columns[-1], axis= 1)
y = df[df.columns[-1]]

dic = {}
# model testing
for item in x.columns:
    uniqueValue = np.unique(df[item])
    for feature in uniqueValue:
        count = 0
        countYes = 0    
        for index in range(len(df[item])):
            if feature == df[item][index] and y[index] == 'yes':
                countYes += 1

            if feature == df[item][index]:
                count += 1
        dic[feature] = {'yes': countYes, 'no': count - countYes, 'total': count}


print(dic)