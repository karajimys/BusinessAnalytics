# Import pandas
import pandas as pd
# Import matplotlib and seaborn (modules for Vizualization)
import matplotlib.pyplot as plt
import seaborn as sns

# To ignore warnings, use the following code to make the display more attractive.
import warnings
warnings.filterwarnings("ignore")



# import pandas & read data. Here the data is in folder named "data" and is near our working file
df = pd.read_csv("data/iris.csv")

# see first rows 
df.sample(5)

# columns
list(df.columns)

# Plots Using Matplotlib
# a simple scatterplot using matplotlib 
plt.scatter(df['sepal_length'], y=df['petal_length'])
plt.show()


# Plots Using Seaborn
# scatter plot
sns.lmplot(x="sepal_length", y="petal_length", data=df, fit_reg=False)
plt.show()


# scatter plot with classes
sns.lmplot(x="sepal_length", y="petal_length", data=df, fit_reg=False, hue="class")
plt.show()


# barplot
sns.barplot(data=df, x="class", y="sepal_length")
plt.show()

# barplot with the same color
sns.barplot(data=df, x="class", y="sepal_length", color='b')
plt.show()

# horizontal barplot
sns.barplot(data=df, x="sepal_length", y="class")
plt.show()

# To plot the species data using a box plot:
sns.boxplot(x="class", y="sepal_length", data=df).set(title='Boxplot of petal lenght per class')
plt.show()

# A violin plot shows the density of the data, simularly to a scatter plot,
# and presents categorical data like a box plot.
# Denser regions of the data are fatter.
sns.violinplot(x="class", y="sepal_length", data=df).set(title='Violin plot of petal lenght per class')
plt.show()

# Density plot of distributions with a title
# A density plot is a representation of the distribution of a numeric variable
sns.kdeplot(data=df["petal_length"]).set(title='Distribution of petal lenght')
plt.show()

# Density plot of distributions
# ploting two distributions
sns.kdeplot(data=df["petal_length"])
sns.kdeplot(data=df["sepal_length"])
plt.show()

# We can see the joint distribution and the marginal distributions together
figure1 = sns.jointplot(x="sepal_length", y="petal_length", data=df, kind='kde')
plt.show()

#save Figure
figure1.savefig("output.png")