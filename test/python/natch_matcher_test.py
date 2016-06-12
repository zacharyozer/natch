# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Zachary Ozer
"""
import json
import os
import unittest

import natch_matcher


class TestNatchMatcher(unittest.TestCase):

  def test(self):
    f = open(os.path.join(os.path.dirname(__file__), '../fixtures/tests.json'))
    json_data = json.loads(f.read())
    subjects = json_data.get('subjects')
    tests = json_data.get('tests')
    for test in tests:
      message = test['message']
      query = test['query']
      expected_result = test['expectedResult']
      matcher = natch_matcher.NatchMatcher(query)
      self.assertEquals(expected_result, matcher.filter(subjects), message)

if __name__ == '__main__':
  unittest.main()
