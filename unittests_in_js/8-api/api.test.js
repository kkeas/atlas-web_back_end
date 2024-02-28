// Test cases for api.js
const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
    it('should return correct status code', function (done) {
        request('http://localhost:7865', function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return correct result', function (done) {
        request('http://localhost:7865', function (error, response, body) {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});
