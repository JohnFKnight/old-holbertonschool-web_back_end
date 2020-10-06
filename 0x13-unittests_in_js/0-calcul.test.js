const assert = require("assert");
const calcnum = require('./0-calcul.js');

describe('Round', function () {
  it('should work without rounding', function () {
    assert.equal(calcnum(3, 4), 7);
  });
  it('should work with rounding', function () {
    assert.equal(calcnum(3.4, 4.2), 7);
  });
  it('should work without rounding', function () {
    assert.equal(calcnum(3.0, 4.0), 7);
  });
  it('should work without rounding', function () {
    assert.equal(calcnum(-3, 4), 1);
  });
  it('should work without rounding', function () {
    assert.equal(calcnum(3, - 4), -1);
  });
  it('should work with rounding', function () {
    assert.equal(calcnum(-3.4, 4.5), 2);
  });
  it('should work with rounding', function () {
      assert.equal(calcnum(-3.5, 2), -1);
  });
  it('should throw error if NaN passed', function () {
      assert.throws(function() {calcnum(NaN, 3), '[Function: TypeError]'});
  });
})
