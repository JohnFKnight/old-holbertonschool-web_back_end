const sinon = require("sinon");

const chai = require('chai');
const assert = chai.assert;
// const assert = sinon.assert;
const expect = chai.expect;
const should = chai.should();
const sendpmt = require('./4-payment.js');
const calcNum = require('./utils.js');


describe('sendPayment', function () {
    it('should pass using sendpmt function', function () {
	// const callback = sinon.spy(calcNum.calculateNumber);
	// const callback = sinon.spy(sendpmt);

	// const pmt = sinon.stub(calcNum, 'calculateNumber').returns(10);
	const pmt = sinon.stub(sendpmt, 'sendPaymentRequestToApi').returns(10);

	const consoleSpy = sinon.spy(console, 'log');

	// callback(100, 20);
	// pmt(type = 'Sum', a = 100, b = 20);
	pmt(100, 20);

	// expect(console.log.calledWith('The total is: 10')).to.be.false;
	// console.log(console.log.calledWith());
	// expect(consoleSpy.getCall(0).returnValue, 'The total is: 10');

	// assert.equal(pmt.getCall(0).returnValue, 10);

	console.log(pmt.getCalls());
	// console.log(pmt.getCall(0).returnValue);

	// console.log(consoleSpy.getCalls());
	// console.log(consoleSpy.getCall(0).returnValue);


	// console.log(callback('SUM', 50, 37));
	// console.log(callback.called);
	// console.log(callback.getCalls());
	// console.log(callback.getCall(0));
	// console.log(callback.getCall(0).args);
	// console.log(callback.getCall(0).returnValue);

	// assert(callback.called, "callback called");
	// assert.equal(callback.getCall(0).returnValue, 120);
       
    });

    // it('should not use Utils.calculateNumber function', function () {
    // 	const spy = sinon.spy(sendpmt);
    // 	calcNum.calculateNumber('SUM', 100, 20), spy;
	
    // 	expect(callback.called);
       
    // });
});
