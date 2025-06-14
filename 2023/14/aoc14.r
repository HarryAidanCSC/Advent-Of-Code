
# Advent of Code 2023 - Day 14 --------------------------------------------
# Author: Harry Mancinelli
# Date: 29/12/2023

# Packages 
library(tidyverse)
library(memoise)

# Get Input
dirname(rstudioapi::getActiveDocumentContext()$path)
input <- readLines(paste0(dirname(rstudioapi::getActiveDocumentContext()$path), "/input.txt"))

# Turn into df

df <- data.frame(matrix(nrow = nchar(input[1]), 
                    ncol = length(input)))

for(i in 1:length(input)){
  df[i,] <- str_split_1(input[i], "")
}

# Initalise vector
summary <- 0

# Run for loop 
for(i in 1:ncol(df)){
 
col1 <- df[,i]
    
round <- which(col1 == "O") 
square <- which(col1 == "#") + 1
roll_possible <- unique(c(1,square))

# Roll destination 
blind_roll <- findInterval(round, roll_possible)

adjusted_roll <- roll_possible[pmax(1, blind_roll)] + 
  ave(seq_along(ave(seq_along(blind_roll))), blind_roll, FUN = function(x) seq_along(x) - 1)

value = sum(101 - adjusted_roll)
summary = summary + value

}

# Part 1 Answer
summary







# Part 2 ------------------------------------------------------------------
library(memoise)

# Define functions
rotate <- memoise(function(mat) t(apply(mat, 2, rev))) 
line_drop <- memoise(function(col1) {
  round <- which(col1 == "O") 
  square <- which(col1 == "#") + 1
  roll_possible <- unique(c(1, square))
  blind_roll <- findInterval(round, roll_possible)
  adjusted_roll <- roll_possible[pmax(1, blind_roll)] + ave(seq_along(blind_roll), blind_roll, FUN = function(x) seq_along(x) - 1)
  col2 <- gsub("O", ".", col1)
  col2[adjusted_roll] <- "O"
  return(col2)
})

drop_rocks <- memoise(function(mat) {
  for(i in 1:ncol(mat)) {
    mat[, i] <- line_drop(mat[, i])
  }
  return(mat)
})

# Run 
counter <- 0
mat <- as.matrix(data.frame(matrix(unlist(strsplit(input, "")), nrow = nchar(input), byrow = TRUE)))
mat_list <- list(mat)
flag <- TRUE

while (flag) {
  loop <- 0
  counter <- counter + 1
  
  while (loop < 4) {
    loop <- loop + 1
    mat <- drop_rocks(mat)
    mat <- rotate(mat)
  }
  
  for (i in 1:length(mat_list)) {
    maty <- mat_list[[i]]
    if (identical(maty, mat)) {
      start_loop = i
      end_loop = counter - 1
      flag <- FALSE  # Set flag to FALSE to exit the outer loop
    }
  }
  
  mat_list <- c(mat_list, list(mat))  # Update mat_list inside the loop
}

loop_length = end_loop  - start_loop + 2
table_index = (1000000000 - start_loop) %% loop_length + 1
mat = mat_list[[table_index + start_loop]]
summary <- 0

for(i in 1:ncol(mat)) {
  col1 <- mat[, i]
  square <- which(col1 == "O") 
  value <- sum(101 - square)
  summary <- summary + value
}

print(summary)


