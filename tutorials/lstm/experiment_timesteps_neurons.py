
from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot
# load results into a dataframe
filenames = ['experiment_timesteps_1_neurons.csv', 'experiment_timesteps_2_neurons.csv',
             'experiment_timesteps_3_neurons.csv', 'experiment_timesteps_4_neurons.csv', 'experiment_timesteps_5_neurons.csv']
results = DataFrame()
for name in filenames:
    results[name[11:-12]] = read_csv(name, header=0)
# describe all results
print(results.describe())
# box and whisker plot
results.boxplot()
pyplot.show()
