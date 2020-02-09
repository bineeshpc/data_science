from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
# load results into a dataframe
filenames = ['experiment_timesteps_1.csv', 'experiment_timesteps_2.csv',
             'experiment_timesteps_3.csv', 'experiment_timesteps_4.csv', 'experiment_timesteps_5.csv']
results = DataFrame()
for name in filenames:
    results[name[11:-4]] = read_csv(name, header=0)
# describe all results
print(results.describe())
# box and whisker plot
results.boxplot()
pyplot.show()
