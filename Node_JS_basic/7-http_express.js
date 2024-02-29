// Express server

const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  try {
    const { totalStudents, studentsByField } = await countStudents(process.argv[2]);
    res.write(`Number of students: ${totalStudents}\n`);
    for (const field in studentsByField) {
      if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
        const list = studentsByField[field];
        const count = list.length;
        const names = list.join(', ');
        res.write(`Number of students in ${field}: ${count}. List: ${names}\n`);
      }
    }
  } catch (error) {
    res.write(error.message);
  }
  res.end();
});

app.listen(1245, () => {
  console.log('Listening on port 1245');
});

module.exports = app;
