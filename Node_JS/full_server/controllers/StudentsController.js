// A class named StudentsController

import { readDatabase } from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    try {
      const data = readDatabase();
      response.status(200).send(`This is the list of our students\n${data}`);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }

  static getAllStudentsByMajor(request, response) {
    try {
      const data = readDatabase();
      response.status(200).send(`This is the list of our students\n${data}`);
    } catch (error) {
      response.status(500).send('Cannot load the database');
    }
  }
}
