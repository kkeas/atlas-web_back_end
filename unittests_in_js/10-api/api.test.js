// Test cases for the api.js file
const request = require('request');
const { expect } = require('chai');

// Add a test suite for the / endpoint
describe('Index page', function () {
    it('should return the correct status code and result', function (done) {
        request('http://localhost:3000', function (error, response, body) {
            if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});

// Add a test suite for the /cart/:id endpoint
describe('Cart page', function () {
    it('should return the correct status code and result', function (done) {
        request('http://localhost:3000/cart/12', function (error, response, body) {
            if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal(`Payment methods for cart 12`);
            done();
        });
    });

    it('should return 404 when :id is NOT a number', function (done) {
        request('http://localhost:3000/cart/hello', function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });

    // Add a test suite for the /login endpoint
describe('Users page', function () {
    it('should return the correct status code and result', function (done) {
        request.post({
            url: 'http://localhost:3000/login',
            json: { userName: 'Betty' }
        },
            function (error, response, body) {
            if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome Betty');
            done();
        });
    });

    // Add a test suite for the /available_payments endpoint
describe('Payment page', function () {
    it('should return the correct status code and result', function (done) {
        request('http://localhost:3000/available_payments', function (error, response, body) {
            if (error) return done(error);
            expect(response.statusCode).to.equal(200);
            expect(JSON.parse(body)).to.deep.equal({
                payment_methods: {
                    credit_cards: true,
                    paypal: false
                }
            });
            done();
            });
        });
    });
});
});
