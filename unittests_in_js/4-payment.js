// Its just task 3 again

const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${sum}`);
    return sum;
}

module.exports = sendPaymentRequestToApi;