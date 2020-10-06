const { expect } = require('chai');
// const assert = chai.assert;
// const expect = chai.expect;
// const should = chai.should();
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
    it('Sum function with rounding', function () {
	expect(calculateNumber('SUM', 3, 4)).to.equal(7);
	expect(calculateNumber('SUM', 3.4, 4.2)).to.equal(7);
	expect(calculateNumber('SUM', 3.0, 4.0)).to.equal(7);
	expect(calculateNumber('SUM', -3, 4)).to.equal(1);
	expect(calculateNumber('SUM', 3, - 4)).to.equal(-1);
	expect(calculateNumber('SUM', -3.4, 4.5)).to.equal(2);
	expect(calculateNumber('SUM', -3.5, 2)).to.equal(-1);
    });
    it('Subtract function with rounding', function () {
	expect(calculateNumber('SUBTRACT', 3, 4)).to.equal(-1);
	expect(calculateNumber('SUBTRACT', 3.4, 4.2)).to.equal(-1);
	expect(calculateNumber('SUBTRACT', 3.0, 4.0)).to.equal(-1);
	expect(calculateNumber('SUBTRACT', -3, 4)).to.equal(-7);
	expect(calculateNumber('SUBTRACT', 3, -4)).to.equal(7);
	expect(calculateNumber('SUBTRACT', -3.4, 4.5)).to.equal(-8);
	expect(calculateNumber('SUBTRACT', -3.5, 2)).to.equal(-5);
    });
    it('Divide function with rounding', function () {
	expect(calculateNumber('DIVIDE', 3, 4)).to.equal(0.75);
	expect(calculateNumber('DIVIDE', 3.4, 4.2)).to.equal(0.75);
	expect(calculateNumber('DIVIDE', 3.0, 4.0)).to.equal(0.75);
	expect(calculateNumber('DIVIDE', -3, 4)).to.equal(-0.75);
	expect(calculateNumber('DIVIDE', 3, -4)).to.equal(-0.75);
	expect(calculateNumber('DIVIDE', -3.4, 4.5)).to.equal(-0.6);
	expect(calculateNumber('DIVIDE', -3.5, 2)).to.equal(-1.5);
    });
    it('Divide by zero funtion. Return Error', function () {
	expect(calculateNumber('DIVIDE', -3.5, .4)).to.equal('Error');
    });
})
