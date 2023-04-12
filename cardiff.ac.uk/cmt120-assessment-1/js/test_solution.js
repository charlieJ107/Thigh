var expect = require('chai').expect;
var funcsToTest = require('./' + process.env.npm_config_solutionfile);


const EXERCISE1_TESTS = [
    { input: [1.5, 0.7, 2, 2.3], output: 'setosa' },
    { input: [1.9, 1.5, 2.7, 2.5], output: 'versicolor' },
];

describe("exercise1()", () => {
    EXERCISE1_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise1(...t.input)).to.be.eql(t.output);
        });
    });
});

const EXERCISE2_TESTS = [
    { input: ['Maltese', 9.5, 6.7, true], output: true },
    { input: ['Bulldog', 16, 44, false], output: false },
];

describe("exercise2()", () => {
    EXERCISE2_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise2(...t.input)).to.be.eql(t.output);
        });
    });
});

const EXERCISE3_TESTS = [
    { input: [[1, 2, 3, 4, 5]], output: [[1, 3, 3, 5], [1, 11, 9, 25]] },
    { input: [[7, 2, 4, 5]], output: [[2, 4.5, 4.5, 7], [4, 23.5, 20.5, 49]] }
]

describe("exercise3()", () => {
    EXERCISE3_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise3(...t.input)).to.have.deep.members(t.output);
        });
    });
});

const EXERCISE4_TESTS = [
    {
        input: [{"a/0": "a/1","a/1": "a/0"},
            'a',
            ['0', '0', '1', '1', '0', '0']
        ],
        output: ['1', '1', '0', '0', '1', '1']
    },
    {
        input: [
            {"a/0": "a/1","a/1": "b/0","b/0": "b/0","b/1": "a/1"},
            'a',
            ['0', '0', '1', '1', '0', '0']
        ],
        output: ['1', '1', '0', '1', '1', '1']
}
]

describe("exercise4()", () => {
    EXERCISE4_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise4(...t.input)).to.be.eql(t.output);
        });
    });
});


const EXERCISE5_TESTS = [
    { input: 'test_data/text1.txt', output: [128, 8, 10, 36, 3, 3]},
    { input: 'test_data/text2.txt', output: [84, 0, 3, 19, 1, 4] }
]

describe("exercise5()", () => {
    EXERCISE5_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise5(t.input)).to.have.deep.members(t.output);
        });
    });
});

const EXERCISE6_TESTS = [
    { input: [1, 2, 3], output: 1 },
    { input: [1, [2, []], [4, 5]], output: 3 }
]

describe("exercise6()", () => {
    EXERCISE6_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise6(t.input)).to.be.eql(t.output);
        });
    });
});

const EXERCISE7_TESTS = [
    { input: [3, 2], output: true },
    { input: [5, 2], output: false }
]

describe("exercise7()", () => {
    EXERCISE7_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise7(...t.input)).to.be.eql(t.output);
        });
    });
});

const EXERCISE8_TESTS = [
    { input: 'sehuoh', output: 1 },
    { input: 'caarto', output: 5 }
]

describe("exercise8()", () => {
    EXERCISE8_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise8(t.input)).to.be.eql(t.output);
        });
    });
});

const green_1 = { 1: 'i', 3: 'c' }
const yellow_1 = {'e': new Set([3])}
const gray_1 = new Set(['r', 'a', 's', 'd', 'f'])

const green_2 = {2:'a'}
const yellow_2 = {'a':new Set([3]),'i':new Set([2]),'l':new Set([3,4]),'r':new Set([1])}
const gray_2 = new Set(['e', 't', 'u', 'o', 'p', 'g', 'h', 'c', 'm', 's'])

const EXERCISE9_TESTS = [
    { input: [green_1, yellow_1, gray_1], output: 5},
    { input: [green_2, yellow_2, gray_2], output: 3}
]

describe("exercise9()", () => {
    EXERCISE9_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise9(...t.input)).to.be.eql(t.output);
        });
    });
});

const EXERCISE10_TESTS = [
    { input: [green_1, yellow_1, gray_1], output: new Set(['wince', 'yince', 'mince']) },
    { input: [green_2, yellow_2, gray_2], output: new Set(['laari', 'liard']) }
]

describe("exercise10()", () => {
    EXERCISE10_TESTS.forEach(t => {
        it(`should return "${t.output}" when given the input (${t.input})`, () => {
            expect(funcsToTest.exercise10(...t.input)).to.be.eql(t.output);
        });
    });
});
