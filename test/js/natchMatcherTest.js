import NatchMatcher from '../../src/js/natchMatcher';

const assert = require('assert');
const fs = require('fs');
const path = require('path');

/* eslint-env mocha */
describe('Natural Language Typeahead Matcher', () => {
  const fixturesDir = path.join(__dirname, '../fixtures');
  const testData = JSON.parse(fs.readFileSync(path.join(fixturesDir, 'tests.json')).toString());
  const subjects = testData.subjects;
  const tests = testData.tests;

  for (let test of tests) {
    it(test.message, () => {
      const matcher = new NatchMatcher(test.query);

      assert.deepEqual(test.expectedResult, matcher.filter(subjects));
    });
  }
});
