# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3q7mV8tCuv5RC22qgDxUO2eyUa0HDrb
"""

!pip install -q streamlit

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle
import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    # Input for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Find the largest number
    result = find_largest_number(num1, num2, num3)

    # Display the result
    st.write(f"The largest number is: {result}")

if __name__ == "__main__":
    main()

