// test payment.js
const chai = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

const expect = chai.expect;

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with SUM type and log the result', function () {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    const consoleLogSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // make sure it was called correctly
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true;

    // make sure return was logged to the console
    expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;

    // Restore to prevent side effects
    calculateNumberSpy.restore();
    consoleLogSpy.restore();
  });
});
