# -*- coding: utf-8 -*-
"""
A simple natural language typeahead matcher for English.

:copyright: (c) 2016 by Zachary Ozer
"""
import re

_DEFAULT_TOKENIZATION_SPLIT_PATTERN = re.compile('[^0-9a-z ]')
_DEFAULT_TOKENIZATION_CLEANUP_PATTERN = re.compile('[\']')

class NatchMatcher():
  def __init__(self, query, tokenization_split_pattern=None, tokenization_cleanup_pattern=None):
    self.tokenization_split_pattern = (tokenization_split_pattern if tokenization_split_pattern
                                       else _DEFAULT_TOKENIZATION_SPLIT_PATTERN)
    self.tokenization_cleanup_pattern = (tokenization_cleanup_pattern
                                         if tokenization_cleanup_pattern
                                         else _DEFAULT_TOKENIZATION_CLEANUP_PATTERN)
    self.tokenized_query = self.tokenize(query)

  def tokenize(self, text):
    text = _DEFAULT_TOKENIZATION_CLEANUP_PATTERN.sub('', text.lower())
    text = _DEFAULT_TOKENIZATION_SPLIT_PATTERN.sub(' ', text)
    return filter(None, text.split(' '))

  def _search_token_in_subject_tokens(self, search_token, subject_tokens):
    return next(
      (True for subject_token in subject_tokens if subject_token.startswith(search_token)), False
    )

  def matches(self, subject, key=None):
    # This assumes there will be fewer search tokens than subject tokens.
    # If that's not generally the case, this should be reversed.
    subject_tokens = self.tokenize(subject[key] if key else subject)
    return all(
      self._search_token_in_subject_tokens(search_token, subject_tokens)
      for search_token in self.tokenized_query
    )

  def filter(self, subjects, key=None):
    return [subject for subject in subjects if self.matches(subject, key)]
