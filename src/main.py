import requests


JOBS_ENDPOINT = "https://bn-hiring-challenge.fly.dev/jobs.json"
MEMBERS_ENDPOINT = "https://bn-hiring-challenge.fly.dev/members.json"


def get_data() -> tuple[dict, dict]:
  try:
    jobs = requests.get(JOBS_ENDPOINT).json()
  except:
    print(f"Failed to get jobs from {JOBS_ENDPOINT}")
    raise

  try:
    members = requests.get(MEMBERS_ENDPOINT).json()
  except:
    print(f"Failed to get members from {MEMBERS_ENDPOINT}")
    raise

  return (jobs, members)


jobs, members = get_data()
print(jobs)
print(members)