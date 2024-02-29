// asynchronously read from a db

const fs = require('fs').promises;
const path = require('path');

module.exports = async function countStudents(filePath) {
    const absolutePath = path.resolve(filePath);

    let data;
    try {
        data = await fs.readFile(absolutePath, 'utf8');
    } catch (error) {
        throw new Error('Cannot load the database');
    }

    // Split the file by lines and remove the header
    const listy = data.split('\n').filter((line) => line !== '').slice(1);

    console.log(`Number of students: ${listy.length}`);

    // Parse students and count by field
    const fields = {};
    for (const student of listy) {
        const row = student.split(',');
        const field = row[3];
        const firstname = row[0];
        if (!fields[field]) {
            fields[field] = [];
        }
        fields[field].push(firstname);
    }

    for (const field in fields) {
        if (field) {
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
    }
};
