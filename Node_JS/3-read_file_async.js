// A function named countStudents that returns a promise

const fs = require('fs');

function countStudents(pathArg) {
  return new Promise((resolve, reject) => {
    try {
      const data = fs.readFileSync(pathArg, 'utf8');
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      console.log(`Number of students: ${lines.slice(1).length}`);

      const csStudents = [];
      const sweStudents = [];
      for (let i = 1; i < lines.length; i += 1) {
        const row = lines[i].split(',');
        if (row[3] === 'CS') {
          csStudents.push(row[0]);
        }
        if (row[3] === 'SWE') {
          sweStudents.push(row[0]);
        }
      }

      console.log(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}`);
      console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);
      resolve();
    } catch (error) {
      reject(Error('Cannot load the database'));
    }
  });
}

module.exports = countStudents;
