// my-reporter.js
var mocha = require('mocha');
module.exports = CMT120Reporter;

function CMT120Reporter(runner) {
    mocha.reporters.Base.call(this, runner);
    let passes = 0;
    let exercise = 0;
    let resultPasses = [];

    runner.on('suite end', function (test) {
        exercise++;
        if (exercise <= 10) {
            resultPasses.push(passes);
        }
        passes = 0;
    });

    runner.on('pass', function (test) {
        if (test.duration <= 3000) {
            passes++;
        }
        console.log(`pass: ${test.fullTitle()} (${test.duration}ms)`);
    });

    runner.on('fail', function (test, err) {
        console.log('fail: %s -- error: %s', test.fullTitle(), err.message);
    });

    runner.on('end', function() {
        console.error(process.env.npm_config_solutionfile, resultPasses.join(', '));
    });
}