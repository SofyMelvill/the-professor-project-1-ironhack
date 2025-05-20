import requests
import pandas as pd
import os
from dotenv import load_dotenv

print("Existent directory:", os.getcwd())

print("\nFiles in this folder:")
print(os.listdir())

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

#APP_ID = os.getenv("ADZUNA_APP_ID")
# APP_KEY = os.getenv("ADZUNA_APP_KEY")

APP_ID = "25f3af84"
APP_KEY = "ad67b007b7380aa78a5c5fd452bd94cf"

print("\nAPP_ID:", repr(APP_ID))
print("APP_KEY:", repr(APP_KEY))


url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 20,
    "what": "data analyst",
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)
print("Texto da resposta:", response.text[:500])

try:
    data = response.json()
    print("JSON recebido:")
    print(data)
except Exception as e:
    print("Erro ao converter para JSON:", e)
    data = {}


jobs = []

if "results" not in data or not data["results"]:
    print("⚠️ Nenhum resultado encontrado ou estrutura inesperada.")
else:
    for job in data["results"]:
        jobs.append({
            "Title": job.get("title"),
            "Company": job.get("company", {}).get("display_name"),
            "Location": job.get("location", {}).get("display_name"),
            "Salary_Min": job.get("salary_min"),
            "Salary_Max": job.get("salary_max"),
            "Salary_Avg": job.get("salary_max") or job.get("salary_min"),
            "Salary_Is_Predicted": job.get("salary_is_predicted"),
            "Category": job.get("category", {}).get("label"),
            "Description": job.get("description"),
            "URL": job.get("redirect_url")
        })


adzuna_df = pd.DataFrame(jobs)
adzuna_df.to_csv("adzuna_jobs.csv", index=False)
print(adzuna_df.head())