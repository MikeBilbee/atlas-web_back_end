// A function that takes an argument called success (boolean)
// When success is true, it should return a resolved promise
// with the object {data: 'Successful response from the API' }

function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  } else {
    return Promise.resolve();
  }
}

module.exports = getPaymentTokenFromAPI;