var _ = require('ramda');

var compose = function(f, g) {
  return function(x) {
    return f(g(x))
  }
}

var toLower = function(x){
  return x.toLowerCase();
}
var mutter = function(x) {
  return x + '...';
};

var mumble = compose(mutter, toLower);

console.log(mumble("WHERE ARE YOU"));