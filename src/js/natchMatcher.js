class NatchMatcher {
  constructor(query, tokenizationSplitPattern, tokenizationCleanupPattern) {
    this.tokenizationSplitPattern = tokenizationSplitPattern ?
        tokenizationSplitPattern : /[^0-9a-z ]/g;
    this.tokenizationCleanupPattern = tokenizationCleanupPattern ?
        tokenizationCleanupPattern : /[\']/g;
    this.tokenizedQuery = this.tokenize(query);
  }

  tokenize(text) {
    text = text.toLowerCase()
        .replace(this.tokenizationCleanupPattern, '')
        .replace(this.tokenizationSplitPattern, ' ')
        .split(' ');
    const tokens = text.filter(token => token);
    return tokens;
  }
  
  matches(subject, key) {
    // This assumes there will be fewer search tokens than subject tokens.
    // If that's not generally the case, this should be reversed.
    const subjectTokens = this.tokenize(key ? subject[key] : subject);
    for (let searchToken of this.tokenizedQuery) {
      let searchTokenInSubjectTokens = false;
      for (let subjectToken of subjectTokens) {
        if (subjectToken.startsWith(searchToken)) {
          searchTokenInSubjectTokens = true;
          break;
        }
      }
      if (!searchTokenInSubjectTokens) {
        return false;
      }
    }
    return true;
  }
  
  filter(subjects, key) {
    return subjects.filter(subject => this.matches(subject, key));
  }
}

export default NatchMatcher;
