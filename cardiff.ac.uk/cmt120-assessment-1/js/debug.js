const fs = require('fs');
/**
 * Check if char is in word. Acturally it can also be used to check if an element in an array
 * @param {char} char 
 * @param {string} word 
 * @returns true if char appeard in word
 */
const char_in_word = (char, word) => {
    for (let c_index = 0; c_index < word.length; c_index++) {
        const c = word[c_index];
        if (c === char) {
            return true;
        }
    }
    return false;
}
// Helper function for ex9 and ex10
/**
 * Check if a word satisfied the given wordle rules
 * @param {string} word word to check
 * @param {object} green green rule dictionary
 * @param {object} yellow yellow rule dictionary
 * @param {set} gray gray rule set
 * @returns 
 */
function satisfiedWordleRule(word, green, yellow, gray) {
    // yellow rule
    // 1. letter in y (keys) shoud appeared in word
    for (let y_index = 0; y_index < Object.keys(yellow).length; y_index++) {
        const y = Object.keys(yellow)[y_index]; // y should be a letter
        if (!char_in_word(y, word)) {
            return false;
        }
    }

    for (let char_index = 0; char_index < word.length; char_index++) {
        // yellow rule
        // 2.2 letter in y shoud not appear on y-value ( a set of positions) position. 
        if (char_in_word(word[char_index], Object.keys(yellow)) && yellow[word[char_index]].has(char_index)) {
            return false;
        }
        // gray rule
        // letter in word should not appeard in gray
        if (gray.has(word[char_index])) {
            return false;
        }
        // green rule
        // letter in word should appeared in green and in the green position
        if (char_in_word(char_index, Object.keys(green).map(val=>parseInt(val))) && word[char_index] != green[char_index]) {
            return false
        }
    }
    return true;
}

function wordleSet(green, yellow, gray) {
    let res = [];
    const wordle_text = fs.readFileSync("test_data/wordle.txt", {encoding: "utf-8"}).toString().split("\n");
    for (let word_index = 0; word_index < wordle_text.length; word_index++) {
        const word = wordle_text[word_index];
        if (satisfiedWordleRule(word, green, yellow, gray)) {
            res.push(word);
        }
    }

    return res;
}

const exercise10 = (green, yellow, gray) => {
    const words = wordleSet(green, yellow, gray);
    let score = {};
    for (let wrong_word_index = 0; wrong_word_index < words.length; wrong_word_index++) {
        const wrong_word = words[wrong_word_index];
        score[wrong_word] = 0;
        for (let correct_word_index = 0; correct_word_index < words.length; correct_word_index++) {
            if (correct_word_index === wrong_word_index) {
                // iterate all word except wrong word
                continue;
            }
            const correct_word = words[correct_word_index];
            // Rebuild new wordle rules
            green = {}
            yellow = {}
            gray = new Set();
            for (let word_char_index = 0; word_char_index < wrong_word.length; word_char_index++) {
                if (wrong_word[word_char_index] === correct_word[word_char_index]) {
                    green[word_char_index] = correct_word[word_char_index];
                } else {
                    if (char_in_word(wrong_word[word_char_index], correct_word)) {
                        if (yellow[wrong_word[word_char_index]] === undefined) {
                            yellow[wrong_word[word_char_index]] = new Set([word_char_index,]);

                        } else {
                            yellow[wrong_word[word_char_index]].add(word_char_index);
                        }
                    } else {
                        gray.add(wrong_word[word_char_index]);
                    }
                }
            }
            console.log(1)
            for (let word_index = 0; word_index < words.length; word_index++) {
                const word = words[word_index];
                if (satisfiedWordleRule(word, green, yellow, gray)) {
                    score[wrong_word] += 1;
                }
            }
        }
    }
    const sorted_score = Object.keys(score).sort((a, b) => score[a] - score[b]);
    let res = new Set();
    res.add(sorted_score[0]);
    sorted_score.forEach((value) => {
        if (score[value] === score[sorted_score[0]]) {
            res.add(value.replace("\r", ""));
        }
    })
    return res;
}
const green_1 = { 1: 'i', 3: 'c' }
const yellow_1 = { 'e': new Set([3]) }
const gray_1 = new Set(['r', 'a', 's', 'd', 'f'])

const green_2 = { 2: 'a' }
const yellow_2 = { 'a': new Set([3]), 'i': new Set([2]), 'l': new Set([3, 4]), 'r': new Set([1]) }
const gray_2 = new Set(['e', 't', 'u', 'o', 'p', 'g', 'h', 'c', 'm', 's'])

const green_3 = {}
const yellow_3 = { 'r': new Set([1]), 'i': new Set([2]), 'l': new Set([3]) }
const gray_3 = new Set(['g', 'o', 'u', 'p', 'c', 'h'])

const green_4 = { 4: 'r' }
const yellow_4 = { 'r': new Set([1]), 'i': new Set([1, 2]), 'l': new Set([0, 3]) }
const gray_4 = new Set(['g', 'o', 'u', 'p', 'c', 'h', 't', 'e'])
console.log(exercise10(green_1, yellow_1, gray_1))