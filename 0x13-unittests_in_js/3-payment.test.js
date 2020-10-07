const sinon = require("sinon");

const chai = require('chai');
const assert = chai.assert;
const expect = chai.expect;
const should = chai.should();
const sendpmt = require('./3-payment.js');
const calcNum = require('./utils.js');

describe('sendPayment', function () {
    it('should pass using sendpmt function', function () {
	const callback = sinon.spy();
	sendpmt(100, 20), callback;
	expect(callback.called);
       
    });
    it('should not use Utils.calculateNumber function', function () {
	const callback = sinon.spy();
	calcNum.calculateNumber('SUM', 100, 20), callback;
	expect(callback.called);
       
    });
});
