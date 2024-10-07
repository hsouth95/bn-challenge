import requests

from extractor import Extractor
from matcher import Matcher

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


if __name__ == "__main__":
  jobs, members = get_data()

  extractor = Extractor()

  for member in members:
    print(f"Looking for job matches for {member['name']}, who is searching: '{member['bio']}'")
    # append new fields to member object
    member = dict(extractor.extract_member_info(member), **member)
    for job in jobs:
      if Matcher.match_job(job, member):
        print(f"\tJob match found: {job['title']} in {job['location']}")
