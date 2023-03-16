import pandas as pd
import matplotlib.pyplot as plt

DQN_df = pd.read_csv('output_DQN_200episodes.csv')
ax = plt.gca()

DQN_df.plot(kind='scatter',
        x='Episode No',
        y='Steps',
        color='red', ax=ax, label='No of Steps')

DQN_df.plot(kind='scatter',
        x='Episode No',
        y='Score',
        color='green', ax=ax, label='Score')

# set the title
plt.title('Snake Agent - Performance with DQN')
plt.legend(loc='upper left')
# show the plot
plt.show()