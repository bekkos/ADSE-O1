import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'data.csv'
data = pd.read_csv(csv_file)

Fatalities = data['Fatalities']
Date = data['Date']

x=[]
y=[]

x=list(Date)
y=list(Fatalities)


# plt.bar(x,y)
# plt.xlabel('Date')
# plt.ylabel('Fatalities')
# plt.title('Data')
# plt.show()


print(y)