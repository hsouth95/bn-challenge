import spacy
from models import Member

class Extractor():

  def __init__(self):
    self.nlp = spacy.load("en_core_web_sm")

  def extract_member_info(self, member: Member) -> dict:
    return {
      "locations": self.extract_member_locations(member.bio),
      # job_roles is not currently used but returned in case of further work
      "job_roles": self.extract_member_job_roles(member.bio)
    }

  def extract_member_locations(self, bio: str) -> list[str]:
    doc = self.nlp(bio)

    # Check to see if this token has been categorised as a GeoPolitical Entity (GPE) and that the user wants to not avoid the location
    return [entity.text for entity in doc.ents if entity.label_ == 'GPE' and not self.is_outside_location(entity.text, bio)]

  def extract_member_job_roles(self, bio: str) -> list[str]:
    # I couldn't quite get this working as it returns more than just jobs (even if I were to remove known locations)
    # Leaving code here just to show one route I went with before just comparing words
    doc = self.nlp(bio)

    job_roles = []

    for noun_chunk in doc.noun_chunks:
      job_roles.append(noun_chunk)

    return job_roles


  def is_outside_location(self, location: str, bio: str) -> bool:
    """
    Determine if the location in the members bio is considered as where they want to work,
    or where they want to avoid e.g. Outside of London vs. In London
    """
    doc = self.nlp(bio)

    for token in doc:
      # Check keywords for outside location
      if token.text.lower() in ["outside", "away"]:
        # It's possible to have filler words
        if token.nbor(1).text.lower() in ["of", "from"]:
          # Finally we check the outside indicators are for this location e.g. outside of london
          if token.nbor(2).text.lower() == location.lower():
            return True

    return False