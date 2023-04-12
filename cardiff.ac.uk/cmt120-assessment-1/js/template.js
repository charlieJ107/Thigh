const fs = require('fs');

/**
 * Check if char is in word. Acturally it can also be used to check if an element in an array
 * it's alternative to "if ... in .." of python
 * @param {char} char 
 * @param {string} word 
 * @returns true if char appeard in word
 */
const charInWord = (char, word) => {
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
        if (!charInWord(y, word)) {
            return false;
        }
    }

    for (let char_index = 0; char_index < word.length; char_index++) {
        // yellow rule
        // 2.2 letter in y shoud not appear on y-value ( a set of positions) position. 
        if (charInWord(word[char_index], Object.keys(yellow)) && yellow[word[char_index]].has(char_index)) {
            return false;
        }
        // gray rule
        // letter in word should not appeard in gray
        if (gray.has(word[char_index])) {
            return false;
        }
        // green rule
        // letter in word should appeared in green and in the green position
        if (charInWord(char_index, Object.keys(green).map(val=>parseInt(val))) && word[char_index] != green[char_index]) {
            return false
        }
    }
    return true;
}
/**
 * Create a set of wordle words satisfied given wordle rules
 * @param {object} green dictionary of green rules
 * @param {object} yellow dictionary of yellow rules
 * @param {Set} gray gray ruls set
 * @returns words set
 */
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

module.exports = {

    // Exercise 1 - Iris Species Classifier
    exercise1: (SepalLen, SepalWid, PetalLen, PetalWid) => {
        let setosa = "setosa";
        let versicol = "versicolor";
        let virginic = "virginica";
        if (PetalLen < 2.5) {
            return setosa;
        } else if (PetalWid < 1.8) {
            if (PetalLen < 5) {
                if (PetalWid < 1.7) {
                    return versicol;
                }
                else {
                    return virginic;
                }
            } else {
                if (PetalWid >= 1.6) {
                    if (PetalLen < 7) {
                        return versicol;
                    } else {
                        return virginic;
                    }
                } else {
                    return virginic;
                }
            }
        } else {
            if (PetalLen < 4.9) {
                if (SepalLen < 6) {
                    return versicol;
                } else {
                    return virginic;
                }
            } else {
                return virginic;
            }
        }
    },

    // Exercise 2 - Dog Breeds Standards
    exercise2: (breed, height, weight, male) => {
        let gender = male ? "male" : "female";
        breedMap = {
            "Bulldog": {
                "male": {
                    height: 15,
                    weight: 50
                },
                "female": {
                    height: 14,
                    weight: 40
                }
            },
            "Dalmatian": {
                "male": {
                    height: 24,
                    weight: 70
                },
                "female": {
                    height: 19,
                    weight: 45
                }
            },
            "Maltese": {
                "male": {
                    height: 9,
                    weight: 7
                },
                "female": {
                    height: 7,
                    weight: 6
                }
            }
        }
        let minHeight = breedMap[breed][gender].height * 0.9;
        let maxHeight = breedMap[breed][gender].height * 1.1;
        let minWeight = breedMap[breed][gender].weight * 0.9;
        let maxWeight = breedMap[breed][gender].weight * 1.1;
        return minHeight <= height && height <= maxHeight &&
            minWeight <= weight && weight <= maxWeight;
    },

    // Exercise 3 - Basic Statistics
    exercise3: (list) => {
        const sorted_origin = list.sort((a, b) => a - b);
        let sum_origin = 0;
        let sum_squared = 0
        let squared = [];
        sorted_origin.forEach(element => {
            sum_origin += element;
            let sq = element * element;
            squared.push(sq);
            sum_squared += sq;
        });
        const sorted_squared = squared.sort((a, b) => a - b);
        let mid_origin = 0;
        let mid_squared = 0;
        if (sorted_origin.length % 2 === 0) {
            mid_origin = (sorted_origin[sorted_origin.length / 2 - 1] + sorted_origin[sorted_origin.length / 2]) / 2;
            mid_squared = (sorted_squared[sorted_squared.length / 2 - 1] + sorted_squared[sorted_squared.length / 2]) / 2;
        } else {
            mid_origin = sorted_origin[Math.floor(sorted_origin.length / 2)];
            mid_squared = sorted_squared[Math.floor(sorted_squared.length / 2)];
        }
        const st_origin = [
            sorted_origin[0], // min of origin
            sum_origin / sorted_origin.length, // ave of origin
            mid_origin, // mid of origin
            sorted_origin[sorted_origin.length - 1] // max of origin
        ];
        const st_squared = [
            sorted_squared[0], // min of squared
            sum_squared / sorted_squared.length, // ave of squared
            mid_squared,  // mid of squared
            sorted_squared[sorted_squared.length - 1] // max of squred
        ];

        return [st_origin, st_squared];

    },

    // Exercise 4 - Finite-State Machine Simulator
    exercise4: (trans, init_state, input_list) => {
        let state_machine = {}
        Object.keys(trans).forEach(element => {
            const input_and_state = element.split('/');
            const output_and_state = trans[element].split('/');
            const input_state = input_and_state[0];
            const input = input_and_state[1];
            if (state_machine[input_state] === undefined) {
                state_machine[input_state] = {};
            }
            state_machine[input_state][input] = output_and_state;
        });
        let res = [];
        input_list.forEach(element => {
            res.push(state_machine[init_state][element][1])
            init_state = state_machine[init_state][element][0]
        });
        return res
    },

    // Exercise 5 - Document Stats
    exercise5: (filename) => {
        const reg_arr = [
            /[a-zA-Z]/g, // letters
            /\d/g, // numbers
            /[^a-zA-Z0-9\s]/g, // symbol
            /[a-zA-Z0-9]+/g, // words
            /[^.?!]+[.!?]/g, // sentences
            /\S[\n][\n]/g // paragraph
        ];
        let res = [];
        
        // remove "\r" to handle line breaks difference between unix style and windows
        const text = fs.readFileSync(filename, {encoding: "utf-8"}).toString().replace(/\r/g, ""); 
        for (let i = 0; i < reg_arr.length; i++) {
            const reg = reg_arr[i];
            const match_arr = text.match(reg);
            if (match_arr === null) {
                // Nothing matched 
                res.push(0);
            } else {
                res.push(match_arr.length);
            }
        }
        // Handle final paragraph without another empty line
        res[5] = res[5] + 1;
        return res;

    },

    // Exercise 6 - List Depth
    exercise6: (l) => {
        let max_depth = 1;
        let entered_recursive = false;
        for (let i = 0; i < l.length; i++) {
            let e = l[i];
            if (typeof e == typeof []) {
                entered_recursive = true;
                let depth = module.exports.exercise6(e);
                if (depth > max_depth) {
                    max_depth = depth;
                }
            }
        }
        if (entered_recursive === false) {
            return 1;
        } else {
            return max_depth + 1;
        }
    },

    // Exercise 7 - Change, please
    exercise7: (amount, coins) => {
        let possible_cois = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01];
        if (amount === 0 && coins === 0) {
            return true;
        } else if (amount === 0 || coins === 0) {
            return false;
        }
        for (let i = 0; i < possible_cois.length; i++) {
            let coin_value = possible_cois[i];
            if (amount < coin_value) {
                continue;
            } else {
                // Use Math.round to fix decimal calcualtion error
                if (module.exports.exercise7(Math.round((amount - coin_value) * 100) / 100, coins - 1)) {
                    return true;
                }
            }
        }
        return false
    },

    // Exercise 8 - Five Letter Unscramble
    exercise8: (s) => {
        let count = 0;
        const origin = s; // Deep copy to a constant to backup value
        const wordle_list = fs.readFileSync("test_data/wordle.txt", {encoding: "utf-8"}).toString().split("\n");
        for (let i = 0; i < wordle_list.length; i++) {
            word_in_wordle = wordle_list[i].replace("\r", ""); // remove "\r" to handle line breaks difference between unix style and windows
            let word_to_check = origin; // restore from backup
            let all_char_in_wordle_in_s = true;
            for (let char_index = 0; char_index < word_in_wordle.length; char_index++) {
                const char = word_in_wordle[char_index];
                if (charInWord(char, word_to_check)) {
                    word_to_check = word_to_check.replace(char, "");
                } else {
                    all_char_in_wordle_in_s = false;
                    break;
                }
            }
            if (all_char_in_wordle_in_s) {
                count++;
            }
        }
        return count;
    },

    // Exercise 9 - Wordle Set
    exercise9: (green, yellow, gray) => {
        return wordleSet(green, yellow, gray).length;
    },

    // Exercise 10 - One Step of Wordle
    exercise10: (green, yellow, gray) => {
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
                        if (charInWord(wrong_word[word_char_index], correct_word)) {
                            if (yellow[wrong_word[word_char_index]] === undefined) {
                                yellow[wrong_word[word_char_index]] = new Set([word_char_index,]);
    
                            } else {
                                yellow[wrong_word[word_char_index]].add(word_char_index);
                            }
                        } else {
                            // Letter not exist
                            gray.add(wrong_word[word_char_index]);
                        }
                    }
                }
                // Calculating wrong_word score
                for (let word_index = 0; word_index < words.length; word_index++) {
                    const word = words[word_index];
                    if (satisfiedWordleRule(word, green, yellow, gray)) {
                        score[wrong_word] += 1;
                    }
                }
            }
        }
        // sort by score to get the best words
        const sorted_score = Object.keys(score).sort((a, b) => score[a] - score[b]);
        let res = new Set();
        res.add(sorted_score[0].replace("\r", "")); // remove "\r" to handle line breaks difference between unix style and windows
        sorted_score.forEach((value) => {
            if (score[value] === score[sorted_score[0]]) {
                res.add(value.replace("\r", "")); // remove "\r" to handle line breaks difference between unix style and windows
            }
        })
        return res;
    },
}

