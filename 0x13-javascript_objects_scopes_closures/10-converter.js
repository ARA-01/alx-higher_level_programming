#!usr/bin/node
exports.converter = function (base) {
  Number.prototype.toBase = function (base) {
    return parseInt(this, 10).toString(base);
  };

  return function (number) {
    return number.toBase(base);
  };
};
