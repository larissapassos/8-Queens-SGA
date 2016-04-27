import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

matplotlib.style.use('ggplot')

def plot_fitness_by_generation(fitnessArray):
    df = pd.DataFrame(fitnessArray, columns=["fitness"])
    df.fitness.plot()
    plt.ylim(df.fitness.min()*.9, df.fitness.max()*1.1)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.title('Fitness increase over generation')
    plt.show()

def plot_metrics(firstMetric, firstMetricName,
                 secondMetric, secondMetricName,
                 generalMetricName, save=False, figdir=None):
    assert(len(firstMetric) == len(secondMetric))
    df = pd.concat(
        map(lambda data: pd.Series(data), [firstMetric, secondMetric]),
        axis=1,
        names=[firstMetricName, secondMetricName]
        )
    df.plot()
    plt.title(
        "{0} vs. {1} evaluation" \
        .format(firstMetricName, secondMetricName)
        )
    plt.xlabel(generalMetricName)
    if not save:
        plt.show()
    elif save and figdir is not None:
        plt.savefig(figdir)
