import pandas as pd
import numpy as np
covid_19_confirm_cases_dataset = pd.read_csv('Covid-19 Case Study/covid_19_confirmed_v1_lyst1747728690432.csv')
print(covid_19_confirm_cases_dataset)

covid_19_deaths_dataset = pd.read_csv('Covid-19 Case Study/covid_19_deaths_v1_lyst1747728711771.csv')
print(covid_19_deaths_dataset)

covid_19_recovered_people_dataset= pd.read_csv('Covid-19 Case Study/covid_19_recovered_v1_lyst1747728719904.csv')
print(covid_19_recovered_people_dataset)