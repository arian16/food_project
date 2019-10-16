# food_project
# App name: food-safe, link: https://food-safe-app.herokuapp.com/
# Tag: Prediction of health code violations in restaurants

According to the CDC, about 3 million people are affected by foodborne illnesses every year. The goal of the current project is to predict inspection grade of restaurants in order to help the city to identify high health-risk restaurants and priortize inspection. 

This project is important specifically when there is a foodborne illness outbreak since the number of inspection officers are less than the number of restaurants.

I looked at the inspection grade for restaurants for Las Vegas in 2017. About 89% of the restaurants received an inspection grade of A, which is less than 10 violations and I grouped them as good restaurants. And I categorized restaurants with more than 10 violations as bad ones. 

For predictor variables, I relied on Yelp dataset that included features like star rating, review counts, etc. For each tip, I counted the number of health violation related terms based on a glossary of food safety terms. Additionally, I used aggregate inspection grade from 2013-2016. Price and review count were slightly higher for the good restaurants, whereas aggregate grade prior to 2017 was minimally higher for the bad restaurants.

For model development, I implemented logistic regression which is a suitable choice for binary classification and my performance metric was model accuracy. I used Random Forests as an alternative method. I oversampled my outcome variable since it was imbalanced. 
The model accuracy was about 75% with review count, and number of tips, as the most important features. The baseline accuracy with dummy classifier was between 40-60%.

This domain is very important in order to identify high health-risk restaurants during foodborne illness outbreaks. I accomplished this project and made it available by developing a web app using flask and deploying it on Heroku. For instance, inspection officer could type in the aggregate inspection grade and other features from looking at the Yelp review of a restaurant and determine wheter the restaurant is categorized as good ( < 10 violations) or bad ( > 10 violations) restaurant.
