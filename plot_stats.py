import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import sga

matplotlib.style.use('ggplot')

def plot_fitness_by_generation(fitnessArray):
    df = pd.DataFrame(fitnessArray, columns=["fitness"])
    df.fitness.plot()
    plt.ylim(df.fitness.min()*.9, df.fitness.max()*1.1)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.title('Fitness increase over generation')
    plt.show()

def plot_metrics(metrics, metricsNames,generalMetricName,
                 secondaryMetricName, save=False, figdir=None):
    df = pd.concat(map(lambda data: pd.Series(data), metrics), axis=1)
    df.columns = metricsNames
    df = df.fillna(1.0)
    df.plot(colormap=plt.cm.gnuplot)
    plt.xlabel(secondaryMetricName)
    plt.ylabel(generalMetricName)
    plt.ylim(df.min().min()*0.8, df.max().max()*1.2)
    plt.title(generalMetricName + " increase vs. " + secondaryMetricName)
    if not save:
        plt.show()
    elif save and figdir is not None:
        plt.savefig(figdir)

def main():
    n_pop = [10, 30, 50, 70, 100]
    general_metrics = ["max_fitness", "avg_fitness"]

    for general_metric_name in general_metrics:
        metrics = []
        metrics_names = []
        for population_size in n_pop:
            metrics.append(sga.SGA().sga(population_size, n_steps=10000)[general_metric_name + "_lst"])
            metrics_names.append("{0}={1}".format(general_metric_name, population_size))
        plot_metrics(metrics, metrics_names, general_metric_name, "generation")
