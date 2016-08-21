var gulp = require('gulp');

gulp.task('hello', function () {
    console.log('Hello');
});

gulp.task('world', ['hello'], function () {
    console.log('Gulp!');
});

gulp.task('default', ['world']);
