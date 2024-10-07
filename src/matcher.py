class Matcher():

  @staticmethod
  def match_job(job: dict, member: dict) -> bool:
    return Matcher.match_location(job['location'], member['locations']) and Matcher.match_job_role(job['title'], member['bio'])

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