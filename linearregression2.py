import pandas as pd 
import csv
import plotly.express as px
reading=pd.read_csv('d212.csv')
toefl=reading["TOEFL Score"].tolist()
chanceofadmit=reading["ChanceofAdmit"].tolist()
fig=px.scatter(x=toefl,y=chanceofadmit)
fig.show()
m=0.95
b=-93
y=[]
for x in toefl:
    yvalue=m*x+b
    y.append(yvalue)
fig=px.scatter(x=toefl,y=chanceofadmit)
fig.update_layout(shapes=[dict(type='line',y0=min(y),y1=max(y),x0=min(height),x1=max(height))])
fig.show()
x=250
y=m*x+b
print(f"chance of admit of a person with toefl score{x}is{y}")
toefl=np.array(height)
chanceofadmit=np.array(weight)
m,b=np.polyfit(toefl,chanceofadmit,1)
y=[]
for x in height:
    yvalue=m*x+b
    y.append(yvalue)
fig=px.scatter(x=toefl,y=chanceofadmit)
fig.update_layout(shapes=[dict(type='line',y0=min(y),y1=max(y),x0=min(height),x1=max(height))])
fig.show()
x=250
y=m*x+b
print(f"chance of admit of a person with toefl score{x}is{y}")
