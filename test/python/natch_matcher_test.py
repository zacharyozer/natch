# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Zachary Ozer
"""
import unittest

import natch_matcher

_SUBJECTS = [
  'Alps/Alpine Electronics',
  'Apple, Inc.',
  'Johnson & Johnson Services, Inc.',
  'Reverend Martin Luther King, Jr.',
  'Sandra Day O\'Connor',
  'Sears, Roebuck & Company',
  'Viola Davis'
]

_TESTS = [
  {
    'message': 'Should check equality',
    'query': 'Sears, Roebuck & Company',
    'expectedResult': ['Sears, Roebuck & Company']
  },
  {
    'message': 'Should search by prefix',
    'query': 'Viola',
    'expectedResult': ['Viola Davis']
  },
  {
    'message': 'Should search by suffix',
    'query': 'Davis',
    'expectedResult': ['Viola Davis']
  },
  {
    'message': 'Should ignore capitalization',
    'query': 'davis',
    'expectedResult': ['Viola Davis']
  },
  {
    'message': 'Should match multiple subjects',
    'query': 'Inc.',
    'expectedResult': ['Apple, Inc.', 'Johnson & Johnson Services, Inc.']
  },
  {
    'message': 'Should match multiple prefixes',
    'query': 'da',
    'expectedResult': ['Sandra Day O\'Connor', 'Viola Davis']
  },
  {
    'message': 'Should match subjects with single quotes when the quote is  provided',
    'query': 'O\'Connor',
    'expectedResult': ['Sandra Day O\'Connor']
  },
  {
    'message': 'Should match subjects with single quotes when the quote is not provided',
    'query': 'oconnor',
    'expectedResult': ['Sandra Day O\'Connor']
  },
  {
    'message': 'Should ignore ampersands',
    'query': 'Company',
    'expectedResult': ['Sears, Roebuck & Company']
  },
  {
    'message': 'Should ignore commas and periods',
    'query': 'jr',
    'expectedResult': ['Reverend Martin Luther King, Jr.']
  },
  {
    'message': 'Should match the term before a separator',
    'query': 'alps',
    'expectedResult': ['Alps/Alpine Electronics']
  },
  {
    'message': 'Should match the term after a separator',
    'query': 'Alpine',
    'expectedResult': ['Alps/Alpine Electronics']
  }
]

class TestNatchMatcher(unittest.TestCase):
  
  def test(self):
    for test in _TESTS:
      message = test['message']
      query = test['query']
      expected_result = test['expectedResult']
      matcher = natch_matcher.NatchMatcher(query)
      self.assertEquals(expected_result, matcher.filter(_SUBJECTS), message)

if __name__ == '__main__':
  unittest.main()
