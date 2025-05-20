url = "https://jobicy.com/api/v2/remote-jobs"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
data = response.json()
print("Total number of received vacancies:", len(data.get("jobs", [])))

import json
print(json.dumps(data, indent=2)[:1500])  # imprime o JSON formatado, cortado


print(f"Total of open vacancies: {len(data["jobs"])}")

jobs_2 = []
for job in data.get("jobs", []):
    jobs_2.append({
        "Title": job.get("jobTitle"),
        "Company": job.get("companyName"),
        "Location": job.get("jobGeo"),
        "Tags": ", ".join(job.get("jobType", []) + job.get("jobIndustry", [])),
        "Description": None,  
        "URL": job.get("url")
    })

jobicy_df = pd.DataFrame(jobs_2)
jobicy_df.to_csv("jobicy_jobs.csv", index=False)
print("Saved vacancies in jobicy_jobs.csv")