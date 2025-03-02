# DAI-Assignment-23116045
Report for Iris Dataset

1. Introduction
In this report, I analyzed the Iris dataset, which contains measurements of iris flowers from three species: Setosa, Versicolor, and Virginica. The dataset includes four numerical features (sepal length, sepal width, petal length, and petal width) and one categorical feature (species). My goal was to clean the dataset, explore its structure, and uncover relationships between the variables.

2. Data Cleaning
2.1 Handling Missing Values
Function Used: isnull().sum()
Result: No missing values were found in the dataset.

2.2 Removing Duplicate Records
Function Used: drop_duplicates()
Result: 3 duplicate rows were removed, leaving 147 rows.

2.3 Treating Outliers
Function Used: IQR method (quantile(), any())
Result: Outliers were detected and removed, leaving 141 rows.

2.4 Standardizing Categorical Values
Function Used: str.lower(), replace()
Result: The species column was standardized to lowercase.

3. Exploratory Data Analysis (EDA)
3.1 Univariate Analysis
Functions Used: describe(), value_counts(), histplot(), boxplot()
Results:
a) Summary statistics were calculated for numerical columns.
b) Frequency distribution of the species column showed 50 flowers for each species.

Histogram of Sepal Length:
Histogram

Box Plot of Petal Width:
Box Plot

3.2 Bivariate Analysis
Functions Used: corr(), scatterplot(), barplot(), violinplot()
Results:
a) Correlation Matrix:Strong positive correlations were found between petal length & petal width (0.96) and sepal length & petal length (0.87).
Correlation Matrix

b) Scatter Plot: Sepal Length vs Sepal Width:Setosa flowers have smaller sepal lengths and larger sepal widths.
Scatter Plot

c) Bar Plot: Petal Length by Species:Virginica flowers have the longest petals.
Bar Plot

d) Violin Plot: Petal Width by Species:Setosa flowers have the smallest petal widths.
Violin Plot

3.3 Multivariate Analysis
Functions Used: pairplot(), heatmap(), groupby()
Results:

a) Pair Plot:Clear clusters for each species were observed.
Pair Plot

b) Heatmap:Confirmed strong correlations between petal length, petal width, and sepal length.
Heatmap

c) Grouped Comparison: Mean Petal Length by Species:Virginica flowers have the highest mean petal length (5.55 cm).
Grouped Bar Plot

4. Key Insights
a) Species Differentiation:
Setosa flowers are easily distinguishable from Versicolor and Virginica due to their smaller sepal lengths and larger sepal widths.
Virginica flowers have the largest petals, making them stand out from the other two species.

b) Strong Correlations:
Petal Length and Petal Width: These two features are highly correlated (0.96), indicating that as petal length increases, petal width also increases.
Sepal Length and Petal Length: These features also show a strong positive correlation (0.87), suggesting a relationship between sepal and petal sizes.

c) Outliers:
A few outliers were detected in the sepal width and petal width columns. These were removed to ensure the dataset’s integrity.

d) Visual Clusters:
The pair plot revealed clear clusters for each species, demonstrating that the features can effectively distinguish between Setosa, Versicolor, and Virginica.

e) Practical Implications:
The strong correlations and clear clusters suggest that these features can be used to build a machine learning model for species classification.
The dataset is well-suited for teaching and learning data analysis and machine learning concepts.

5. Conclusion:

a) Data Cleaning: The dataset was cleaned by removing duplicates, handling outliers, and standardizing categorical values. This ensured the dataset was ready for analysis.
b) Exploratory Data Analysis (EDA): Through univariate, bivariate, and multivariate analyses, I uncovered meaningful patterns and relationships in the data.
c) Key Findings:
Setosa flowers are distinct in terms of sepal width and petal size.
Virginica flowers have the largest petals, while Setosa flowers have the smallest.
Strong correlations exist between petal length, petal width, and sepal length.
d) Visualizations: Plots such as histograms, scatter plots, and heatmaps provided clear insights into the dataset’s structure and relationships.

Practical Applications:

a)The insights from this analysis can be used to build a machine learning model for classifying iris flowers based on their measurements.
b)The dataset is an excellent resource for teaching data analysis and visualization techniques.




