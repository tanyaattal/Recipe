#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:56:01 2025

@author: tanyaattal
"""
import streamlit as st
from fractions import Fraction


recipe_dict = {
    "Pomodoro Pasta": {
        "servings": 6,
        "ingredients": {
            "Olive oil (cups)": 1/4,
            "Chopped yellow onion": 1,
            "Minced garlic cloves": 5,
            "Crushed red pepper flakes (tsp)": 1/4,
            "28- ounce can San Marzano whole peeled tomatoes": 1,
            "Kosher salt (tsp)": 1/2,
            "Chopped basil (cup)": 1/4,
            "Spaghetti (ounces)": 12,
            "Unsalted butter (tbs)": 2,
            "Finely grated parmensan cheese (cup)": 1/4,
            },
        },
        
    
    "Spicy Peanut Noodles": {
        "servings": 6,
        "ingredients": {
            "Salt (tsp)": 1,
            "Spaghetti (pounds)": 1,
            "No-stir creamy peanut butter(cups)": 1/3,
            "Thai chilli sauce (cups)": 1/4,
            "Soy sauce (tbs)": 2,
            "Boiling water (cups)": 1/4,
            "Green onions (tbs)": 2,
            },
        }       
    }

recipe_w_ing = {
      "Pomodoro Pasta": {
            "recipes": [
                "In a large skillet, heat the olive oil over medium heat.",
                "Add the onion and cook, stirring occasionally, for 10 minutes or until the onion is soft." ,
                "Add the garlic and red pepper flakes and cook for 3 minutes.",
                "Stir in the puréed tomatoes and season with salt.",
                "Cook the sauce until it starts to thicken, stirring occasionally. This will take about 20 minutes.", 
                "When the sauce has thickened, stir in the fresh basil.",
                "Bring a large pot of salted water to a boil.", 
                "Cook the pasta until al dente, according to package instructions.", 
                "**Reserve ½ cup of the pasta water and then drain the pasta.**",
                "Place the pasta back in the large pot, add the tomato sauce and hot pasta water. Stir until the sauce coats the pasta. Add butter and Parmesan cheese and toss until butter and cheese are melted. Plate the pasta and garnish with basil and Parmesan cheese, if desired"
                ],
                 
      },

      "Spicy Peanut Noodles": {
            "recipes": [
                "Cook the pasta:",
                "Bring a large pot of salted water to a boil over high heat.",
                "Cook the spaghetti or other noodles to al dente according to their package instructions.",
                "Drain the noodles in a colander and rinse with cool water until they’re no longer hot.",
                "Meanwhile, make the sauce:",
                "In a large mixing bowl, whisk together the peanut butter, chili sauce, soy sauce, and boiling water (from the pasta pot).",
                "Continue to whisk until the ingredients combine into a smooth sauce, about 1 minute.",
                "The sauce should be thick but still pourable.",
                "Taste the sauce and adjust the seasonings if you like, adding more soy sauce if you want it saltier, or more chili sauce for more sweetness.",
                "Toss noodles with sauce, and serve:",
                "Add the drained and cooled noodles to the bowl with the sauce.",
                "Use tongs to toss the noodles in the sauce until they’re evenly coated. Transfer the peanut butter noodles to serving dishes. Top with sliced green onions, cilantro, and/or sesame seeds, if you like, and serve right away."
                ],
                      }
}

recipe = st.selectbox (
      "What would you like to make today?",
      ["Pomodoro Pasta", "Spicy Peanut Noodles"]
)
st.write(f"you selected: {recipe}")
if recipe not in recipe_dict:
     st.write("Sorry, that recipe is not available. Please try again")
quantity = st.number_input("How many people will you be making this dish for? ")

def scaled_recipe():
    st.header("Here is your ingredients list: ")
    servings_needed = Fraction(recipe_dict[recipe]["servings"])
    scaled_amount = quantity / servings_needed
    for ingredient, amount in recipe_dict[recipe]["ingredients"].items():
            new_amount = amount * scaled_amount
            pretty_amount = Fraction(new_amount).limit_denominator(8)
            st.write("-" + ingredient + ": " + str(pretty_amount))
    st.write()
    st.write()

    st.header("Here is your recipe: ") 
    for recipes in recipe_w_ing[recipe]["recipes"]:
            st.write("-" + recipes)

scaled_recipe()


