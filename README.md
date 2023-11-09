# Python-ML-Snippets

## Overview

This project is part of my portfolio, focusing on practical applications of machine learning (ML) and artificial intelligence (AI) concepts. The chosen dataset is based on FIFA players, motivated by my familiarity with the game and passion for football, making it easier to understand and work with the data.

## Data Collection

I utilized a Java-based web scraper, leveraging HtmlUnit and Apache Commons CSV libraries, to extract player data from the SoFIFA website. The web scraping project can be found [here](https://github.com/RenanFR/sofifa-web-scraping).

### FIFA Players Position Classification

#### Preprocessing Steps

##### 1. Dimensionality Reduction
- Aggregated specific skill ratings into columns representing different aspects of the game (Attack, Skill, Movement, Power, Mentality, Defending, Goalkeeping) by taking the mean of relevant attributes.

##### 2. Feature Engineering
- Removed irrelevant attributes such as ID.
- Transformed player's birthdate into a numerical age column.
- Converted financial attributes (salary, market value, release clause) from string to numeric values.
- Applied one-hot encoding for the dominant foot (left or right).

##### Challenges and Identified Issues

- Discrepancies in player attributes between the CSV and the SoFIFA website, possibly due to version differences.
- A need for further refinement and optimization of both preprocessing and decision tree parameters to improve model accuracy.

## Files

### 1. FIFA_players_Age_MarketValue_Correlation.ipynb
- Explores the correlation between player age and market value.
- Provides insights into age-related trends in player market values.

### 2. classify_player_position_with_decision_tree.ipynb
- Preprocesses player data and trains a decision tree model to classify player positions.
- Highlights challenges faced and discusses steps for improvement.

### 3. preprocessed_players_data.csv
- CSV file containing the preprocessed player data for further analysis and refinement.

## Next Steps

- Investigate and resolve discrepancies in player attributes between the CSV and SoFIFA website.
- Refine preprocessing steps to improve model accuracy.
- Optimize decision tree parameters for better performance.

Feel free to explore the notebooks for a detailed understanding of the project's process, challenges, and future steps. Contributions and suggestions for improvement are welcomed.
