import unittest

from src.extractor import Extractor
from src.models import Member


class TestExtractor(unittest.TestCase):

  def test_extract_member_locations_single_location(self):
    extractor = Extractor()

    assert "London" in extractor.extract_member_locations("I want to work in London")

  def test_extract_member_locations_multiple_location(self):
    extractor = Extractor()

    self.assertListEqual(extractor.extract_member_locations("I want to work in London and Edinburgh"), ["London", "Edinburgh"])

  def test_extract_member_locations_no_locations(self):
    extractor = Extractor()

    self.assertListEqual(extractor.extract_member_locations("I want to work"), [])

  def test_extract_member_info_returns_single_location_dict(self):
    extractor = Extractor()

    member = Member(name="Test", bio="I want to work in Leeds")

    self.assertEqual(extractor.extract_member_info(member)["locations"], ["Leeds"])

  def test_extract_member_info_returns_multiple_location_dict(self):
    extractor = Extractor()

    member = Member(name="Test", bio="I want to work in Leeds and London")

    self.assertEqual(extractor.extract_member_info(member)["locations"], ["Leeds", "London"])

  def test_extract_member_info_returns_no_location_dict(self):
    extractor = Extractor()

    member = Member(name="Test", bio="I want to work")

    self.assertEqual(extractor.extract_member_info(member)["locations"], [])

  def test_is_outside_location_returns_true(self):
    extractor = Extractor()

    self.assertTrue(extractor.is_outside_location("London", "I want to work outside of London"))

  def test_is_outside_location_returns_false(self):
    extractor = Extractor()

    self.assertFalse(extractor.is_outside_location("London", "I want to work in London"))