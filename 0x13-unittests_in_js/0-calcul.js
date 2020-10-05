module.exports = function calculateNumber(a, b) {
  if (isNaN(a) || isNaN(b)) {
    throw TypeError;
  }
  return Math.round(a) + Math.round(b);
}
