// Async tests

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
    it('should return a resolved promise', function (done) {
        getPaymentTokenFromAPI(true)
            .then((data) => {
                expect(data).to.deep.equal({ data: 'Successful response from the API' });
                done();
            })
            .catch((error) => done(error));
    });
});
