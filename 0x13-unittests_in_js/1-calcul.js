module.exports = function calculateNumber(type, a, b) {
  if (isNaN(a) || isNaN(b)) {
      throw new TypeError();
  }
  if (type == SUM) {
    return Math.round(a) + Math.round(b);	
  } else if (type == SUBTRACT) {
    return Math.round(a) - Math.round(b);
  } else if (type == DIVIDE) {
    try {
      if (Math.round(b) == 0) throw 'Error';
      return Math.round(a) / Math.round(b);
    }
    catch(err) {
      return (err);
    }
  }
}
