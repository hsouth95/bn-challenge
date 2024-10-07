import spacy
from models import Member

class Extractor():

  def __init__(self):
    self.nlp = spacy.load("en_core_web_sm")

  def extract_member_info(self, member: Member) -> dict:
    return {
      "locations": self.extract_member_locations(member.bio),
      # TODO: Update model to be able to extract job role (this would require training or much more complicated logic)
    }

  def extract_member_locations(self, bio: str) -> list[str]:
    doc = self.nlp(bio)

    # Check to see if this token has been categorised as a GeoPolitical Entity (GPE)
    return [entity.text for entity in doc.ents if entity.label_ == 'GPE']

  def extract_member_job_roles(self, bio: str) -> list[str]:
    # I couldn't quite get the logic working with spacy to extract the job roles but with further logic it may be possible
    raise NotImplementedError()
