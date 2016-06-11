import NatchMatcher from '../../src/js/natchMatcher';

describe('Natural Language Typeahead Matcher', function () {
  const subjects = [
    'Alps/Alpine Electronics',
    'Apple, Inc.',
    'Johnson & Johnson Services, Inc.',
    'Reverend Martin Luther King, Jr.',
    'Sandra Day O\'Connor',
    'Sears, Roebuck & Company',
    'Viola Davis'
  ];

  const tests = [
    {
      message: 'should check equality',
      query: 'Sears, Roebuck & Company',
      expectedResult: ['Sears, Roebuck & Company']
    },
    {
      message: 'should search by prefix',
      query: 'Viola',
      expectedResult: ['Viola Davis']
    },
    {
      message: 'should search by suffix',
      query: 'Davis',
      expectedResult: ['Viola Davis']
    },
    {
      message: 'should ignore capitalization',
      query: 'davis',
      expectedResult: ['Viola Davis']
    },
    {
      message: 'should match multiple subjects',
      query: 'Inc.',
      expectedResult: ['Apple, Inc.', 'Johnson & Johnson Services, Inc.']
    },
    {
      message: 'should match multiple prefixes',
      query: 'da',
      expectedResult: ['Sandra Day O\'Connor', 'Viola Davis']
    },
    {
      message: 'should match subjects with single quotes when the quote is  provided',
      query: 'O\'Connor',
      expectedResult: ['Sandra Day O\'Connor']
    },
    {
      message: 'should match subjects with single quotes when the quote is not provided',
      query: 'oconnor',
      expectedResult: ['Sandra Day O\'Connor']
    },
    {
      message: 'should ignore ampersands',
      query: 'Company',
      expectedResult: ['Sears, Roebuck & Company']
    },
    {
      message: 'should ignore commas and periods',
      query: 'jr',
      expectedResult: ['Reverend Martin Luther King, Jr.']
    },
    {
      message: 'should match the term before a separator',
      query: 'alps',
      expectedResult: ['Alps/Alpine Electronics']
    },
    {
      message: 'should match the term after a separator',
      query: 'Alpine',
      expectedResult: ['Alps/Alpine Electronics']
    }
  ];

  for (let test of tests) {
    it(test.message, () => {
      const matcher = new NatchMatcher(test.query);
      expect(matcher.filter(subjects)).toEqual(test.expectedResult);
    });
  }
});
