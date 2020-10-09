const sinon = require("sinon");

const chai = require('chai');
const assert = chai.assert;
const expect = chai.expect;
const should = chai.should();
const sendpmt = require('./3-payment.js');
const calcNum = require('./utils.js');

describe('sendPayment', function () {
    it('should pass using sendpmt function', function () {
	// const callback = sinon.spy(calcNum.calculateNumber);
	const callback = sinon.spy(sendpmt);
	callback(100, 20);
	// console.log(callback('SUM', 50, 37));
	// console.log(callback.called);
	// console.log(callback.getCall(0));
	// console.log(callback.getCall(0).args);
	// console.log(callback.getCall(0).returnValue);
	assert(callback.called, "callback called");
	// assert.equal(callback.getCall(0).returnValue, 120);
       
    });

    // it('should not use Utils.calculateNumber function', function () {
    // 	const spy = sinon.spy(sendpmt);
    // 	calcNum.calculateNumber('SUM', 100, 20), spy;
	
    // 	expect(callback.called);
       
    // });
});
