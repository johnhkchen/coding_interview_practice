var curry=require('lodash.curry');

var match = curry(function(what,str) {
  return str.match(what);
});

var replace = curry(function(what, replacement, str) {
  return str.replace(what, replacement);
});

var filter = curry(function(f, ary) {
  return ary.filter(f);
});

var map = curry(function(f, ary) {
  return ary.map(f);
});

console.log("Curry Done");

console.log("Match #1: ");
console.log(match(/\s+/g, 'hello world'));

var hasSpaces = match(/\s+/g);


console.log("Match #2: ");
console.log(hasSpaces('hello world'));

console.log("Match #3: ");
console.log(hasSpaces('hello'));

console.log("Match #3: ");
console.log(filter(hasSpaces, ['tori_spelling', 'tori amos']));

var findSpaces = filter(hasSpaces);

console.log("Match #4: ");
console.log(findSpaces(['llama drama', 'dramallama', 'odo meter']));

var noVowels = replace(/[aeiouy]/ig);

var censor = noVowels("_");

console.log(censor("Motherfucking dicknipples eating a cloud"));