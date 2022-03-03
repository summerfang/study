# Clear objects of environment first.
rm(list = ls())

# Install the package in an elegant way.
required_packages <- c("tidyverse")
packages_needed <- required_packages[!(required_packages %in% installed.packages()[,"Package"])]
if(length(packages_needed))
  install.packages(packages_needed)

library(tidyverse)
