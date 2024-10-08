from models import Member, Job

class Matcher:

  @staticmethod
  def match_job(job: Job, member: Member) -> bool:
    # Check to see if we can match any locations, otherwise we'll say all locations match
    # If the member has specified locations, we check to see if they match where the job is located
    is_location_match = len(member.locations) == 0 or Matcher.match_location(job.location, member.locations)

    is_job_match = Matcher.match_job_role(job.title, member.bio)

    return is_location_match and is_job_match

  @staticmethod
  def match_location(job_location: str, member_locations: list[str]) -> bool:
    for location in member_locations:
      if job_location.upper() == location.upper():
        return True
    return False

  @staticmethod
  def match_job_role(job_role: str, member_bio: str) -> bool:
    # Split job role to make matching simpler e.g. Marketing Internship should match Marketing
    job_roles_split = job_role.split(" ")

    for word in member_bio.split(" "):
      for job_roles_word in job_roles_split:
        if job_roles_word.upper() == word.upper():
          return True
    return False