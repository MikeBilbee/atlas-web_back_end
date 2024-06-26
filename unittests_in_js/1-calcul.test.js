// Tests for 1-calcul.js

const calculateNumber = require('./1-calcul');
const assert = require('assert');


describe('calculateNumber', () => {
  describe('type=SUM', () => {
    it('should return rounded sum for SUM', function() {
      assert.strictEqual(calculateNumber('SUM', 6.2, 11.8), 18);
    });
  });
  describe('type=SUBTRACT', () => {
    it('should return rounded difference for SUBTRACT', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 15.8, 6.2), 10);
    });
  });
  describe('type=DIVIDE', () => {
    it('should return rounded division for DIVIDE', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 9.3, 2.7), 3);
    });
    it('should return Error for DIVIDE when b is 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 56.9, 0), 'Error');
    });
  });
});