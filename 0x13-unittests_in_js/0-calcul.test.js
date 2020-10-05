const assert = require ("assert");
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('Add 2 integers', function () {
    assert.strictEqual(calculateNumber(3, 4), 7);
  });
  it('Add 2 floats', function () {
    assert.strictEqual(calculateNumber(3.4, 4.2), 7);
  });
  it('Add 2 floats .0', function () {
    assert.strictEqual(calculateNumber(3.0, 4.0), 7);
  });
  it('Add neg and pos ints; pos result', function () {
    assert.strictEqual(calculateNumber(-3, 4), 1);
  });
  it('Add neg and pos ints; neg result', function () {
    assert.strictEqual(calculateNumber(3, - 4), -1);
  });
  it('Add neg and pos flosts; pos result', function () {
    assert.strictEqual(calculateNumber(-3.4, 4.5), 2);
  });
  it('Add neg and pos floats; neg result', function () {
      assert.strictEqual(calculateNumber(-3.5, 2), -1);
  });
  it('should throw error if NaN passed', function () {
      assert.throws(function () {calculateNumber(NaN, 3), '[Function: TypeError]'});
  });
});
