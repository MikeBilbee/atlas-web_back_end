// A function that accepts two arguments, rounds them,
// and returns the sum, differnce, or quotient

function calculateNumber(type, a, b) {
  // Rounds two numbers and returns the sum, difference, or division
  if (type === 'SUM') {
    return Math.round(a) + Math.round(b);
  } else if (type === 'SUBTRACT') {
    return Math.round(a) - Math.round(b);
  } else if (type === 'DIVIDE') {
    if (Math.round(b) === 0) {
      return 'Error';
    }
    return Math.round(a) / Math.round(b);
  }
}

module.exports = calculateNumber;
