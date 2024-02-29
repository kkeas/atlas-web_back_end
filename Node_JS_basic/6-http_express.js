// Express application

const express = require('express');
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// 404 error handler for all other routes
app.use((req, res) => {
  res.status(404).send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Error</title>
    </head>
    <body>
    <pre>Cannot GET ${req.originalUrl}</pre>
    </body>
    </html>
  `);
});

// listen on port 1245
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

// Export the app
module.exports = app;
