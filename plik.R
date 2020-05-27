library(withr, lib.loc='D:/licencjat/bachelors_thesis_movie_clustering_codes/R_directories')
library(tidyverse, lib.loc='D:/licencjat/bachelors_thesis_movie_clustering_codes/R_directories')

boxoffice <- read.csv(file = 'preprocessed_data/first_month_boxoffice_gross_inflation_adjusted.csv', row.names=1, check.names=FALSE)

.libPaths()
myPaths <- .libPaths()
myPaths <- c(myPaths, 'D:/licencjat/bachelors_thesis_movie_clustering_codes/R_directories')
.libPaths(myPaths)
.libPaths()