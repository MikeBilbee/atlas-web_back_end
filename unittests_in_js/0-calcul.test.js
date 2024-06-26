// Test for calcul.js

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should round and sum positive numbers', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round and sum negative numbers', () => {
    assert.strictEqual(calculateNumber(-2.8, -1.3), -4);
  });

  it('should round and sum positive and negative numbers', () => {
    assert.strictEqual(calculateNumber(3.5, -2.1), 1);
  });

  it('should round and sum numbers with decimals near .5', () => {
    assert.strictEqual(calculateNumber(2.49, 2.51), 5);
    assert.strictEqual(calculateNumber(2.5, 2.5), 5);
  });

  it('should handle integer inputs', () => {
    assert.strictEqual(calculateNumber(2, 3), 5);
  });
});
