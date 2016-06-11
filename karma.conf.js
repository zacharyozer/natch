module.exports = function(config) {
  config.set({
    // I would love to make this work, but it just doesn't seem to be in the cards
    // browsers: ['PhantomJS'],
    basePath: '',

    frameworks: ['browserify', 'jasmine'],

    files: [
      'src/**/*.js',
      'test/**/*.js'
    ],

    exclude: [
    ],

    preprocessors: {
      'src/**/*.js': ['browserify'],
      'test/**/*.js': ['browserify']
    },

    browserify: {
      debug: true,
      transform: [['babelify', {'presets': ['es2015'], 'sourceMaps': true}]]
    }
  });
};
