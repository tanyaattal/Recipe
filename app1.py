#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 19:56:01 2025

@author: tanyaattal
"""
import streamlit as st

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


recipe = st.selectbox (
      "What would you like to make today: ?",
      ["Pomodoro Pasta", "Spicy Peanut Noodles"]
)
st.write(f"you selected: {recipe}")
if recipe not in recipe_dict:
     st.write("Sorry, that recipe is not available. Please try again")
quantity = st.number_input("How many people will you be making this dish for? ")
    

def scaled_recipe():
    st.write("Here is your ingredients list for: ", recipe)
    servings_needed = recipe_dict[recipe]["servings"]
    scaled_amount = quantity / servings_needed
    for ingredient, amount in recipe_dict[recipe]["ingredients"].items():
            new_amount = amount * scaled_amount
            st.write("-" + ingredient + ": " + str(new_amount))

scaled_recipe()
