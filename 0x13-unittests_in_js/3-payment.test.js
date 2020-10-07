const sinon = require("sinon");

const chai = require('chai');
const assert = chai.assert;
const expect = chai.expect;
const should = chai.should();
const sendpmt = require('./3-payment.js');

describe('sendPayment', function () {
    it('should calc payment', function () {
	const callback = sinon.spy();
	sendpmt(100, 20), callback;
	expect(callback.called);
       
    });
});
