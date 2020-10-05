const assert = require ("assert");
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('should work without rounding', function () {
    assert.strictEqual(calculateNumber(3, 4), 7);
  });
  it('should work with rounding', function () {
    assert.strictEqual(calculateNumber(3.4, 4.2), 7);
  });
  it('should work without rounding', function () {
    assert.strictEqual(calculateNumber(3.0, 4.0), 7);
  });
  it('should work without rounding', function () {
    assert.strictEqual(calculateNumber(-3, 4), 1);
  });
  it('should work without rounding', function () {
    assert.strictEqual(calculateNumber(3, - 4), -1);
  });
  it('should work with rounding', function () {
    assert.strictEqual(calculateNumber(-3.4, 4.5), 2);
  });
  it('should work with rounding', function () {
      assert.strictEqual(calculateNumber(-3.5, 2), -1);
  });
  it('should throw error if NaN passed', function () {
      assert.throws(function() {calculateNumber(NaN, 3), '[Function: TypeError]'});
  });
})
