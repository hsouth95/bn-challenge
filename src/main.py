import requests

from extractor import Extractor
from matcher import Matcher
from models import Member, Job

JOBS_ENDPOINT = "https://bn-hiring-challenge.fly.dev/jobs.json"
MEMBERS_ENDPOINT = "https://bn-hiring-challenge.fly.dev/members.json"


def get_data() -> tuple[dict, dict]:
  try:
    jobs_response = requests.get(JOBS_ENDPOINT).json()
    jobs = [Job(**job) for job in jobs_response]
  except:
    # TODO: Split this into requests and pydantic exceptions
    print(f"Failed to get jobs from {JOBS_ENDPOINT}")
    raise

  try:
    members_response = requests.get(MEMBERS_ENDPOINT).json()
    members = [Member(**member) for member in members_response]
  except:
    # TODO: Split this into requests and pydantic exceptions
    print(f"Failed to get members from {MEMBERS_ENDPOINT}")
    raise

  return (jobs, members)


if __name__ == "__main__":
  jobs, members = get_data()

  extractor = Extractor()

  for member in members:
    print(f"Looking for job matches for {member.name}, who is searching: '{member.bio}'")

    # Add extracted fields to member
    member.locations = extractor.extract_member_info(member)["locations"]
    for job in jobs:
      if Matcher.match_job(job, member):
        print(f"\tJob match found: {job.title} in {job.location}")
