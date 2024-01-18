## Seed Dataset Exploration and Clustering

This GitHub repository contains code for exploring and clustering the "Seed Dataset" using Python with the help of popular data manipulation (Pandas), visualization (Matplotlib, Seaborn), and machine learning (KMeans) libraries. The dataset is loaded from "seed.txt" and visualized through scatter plots for pairs of variables. Additionally, KMeans clustering is applied to two selected columns ("perimeter" and "asymmetry") to group similar data points into clusters.

### Table of Contents

1. [Dataset Information](#dataset-information)
2. [Code Overview](#code-overview)
3. [Data Visualization](#data-visualization)
4. [Clustering](#clustering)
5. [Getting Started](#getting-started)
6. [Dependencies](#dependencies)

### Dataset Information

The dataset used in this project, "seed.txt," consists of various attributes related to seed characteristics. The columns include "area," "perimeter," "compactness," "length," "width," "asymmetry," "groove," and "class." The "class" column categorizes each seed into one of the classes.

### Code Overview

The main script (`kmeans_seeds.py`) accomplishes the following tasks:

- Loads the dataset into a Pandas DataFrame.
- Visualizes all pairs of variables through scatter plots, with points colored by the "class" variable.
- Performs KMeans clustering on selected columns ("perimeter" and "asymmetry") and visualizes the results.

### Data Visualization

The scatter plots provide a visual representation of relationships between pairs of variables. Each point is colored according to its class, offering insights into the distribution and patterns within the dataset.

### Clustering

KMeans clustering is applied to group similar data points based on "perimeter" and "asymmetry." The assigned cluster labels are then compared with the original "class" values.

### Dependencies

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

Make sure to have these dependencies installed before running the code.

### Dataset Citation
If you use this dataset, please cite the original source:

Charytanowicz,Magorzata, Niewczas,Jerzy, Kulczycki,Piotr, Kowalski,Piotr, and Lukasik,Szymon. (2012). Seeds. UCI Machine Learning Repository. https://doi.org/10.24432/C5H30K.

Happy coding!
