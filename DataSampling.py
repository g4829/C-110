import pandas as pd 
import plotly.figure_factory as ff 
import statistics
import random
import csv

df=pd.read_csv("medium_data.csv")
data=df["id"].tolist()
population_mean=statistics.mean(data)
print("THE POPULATION MEAN IS:- {}".format(population_mean))
fig=ff.create_distplot([data],["id"],show_hist=False)
fig.show()

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for  i in range(0,100):
        set_of_means=random_set_of_means(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

#def show_fig(mean_list):
    #sample_mean=mean_list
    #fig=ff.create_distplot([sample_mean],["id"],show_hist=False)
    #fig.show()