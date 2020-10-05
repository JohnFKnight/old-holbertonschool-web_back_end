const assert = require ("assert");
const calcNum = require('./0-calcul.js');

describe('calcNum', function () {
  it('Add 2 integers', function () {
    assert.strictEqual(calcNum(3, 4), 7);
  });
  it('Add 2 floats', function () {
    assert.strictEqual(calcNum(3.4, 4.2), 7);
  });
  it('Add 2 floats .0', function () {
    assert.strictEqual(calcNum(3.0, 4.0), 7);
  });
  it('Add neg and pos ints; pos result', function () {
    assert.strictEqual(calcNum(-3, 4), 1);
  });
  it('Add neg and pos ints; neg result', function () {
    assert.strictEqual(calcNum(3, - 4), -1);
  });
  it('Add neg and pos flosts; pos result', function () {
    assert.strictEqual(calcNum(-3.4, 4.5), 2);
  });
  it('Add neg and pos floats; neg result', function () {
      assert.strictEqual(calcNum(-3.5, 2), -1);
  });
});
