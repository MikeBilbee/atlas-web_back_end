// A small HTTP server using Express module

const express = require('express');

const app = express();

const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(port, () => {
  console.log(`Listening on port ${port}.`);
});

module.exports = app;
