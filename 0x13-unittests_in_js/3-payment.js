function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const calcnum = require('./utils.js');
    const pmt =  (calcnum.calculateNumber('SUM', a = totalAmount, b = totalShipping));
    console.log('The total is:', pmt);
}
module.exports = sendPaymentRequestToApi;
// sendPaymentRequestToApi(100, 50)
