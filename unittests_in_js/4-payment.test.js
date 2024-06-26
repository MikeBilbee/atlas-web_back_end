// Tests for 4-payment

const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function() {
  let sinonStub;
  let consoleSpy;
  beforeEach(() => {
    sinonStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    sinonStub.restore();
    consoleSpy.restore();
  });

  it('two funcs should match', function() {
    sendPaymentRequestToApi(100, 20);
    expect(sinonStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });

  it('console logs correctly', function() {
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
  });
});