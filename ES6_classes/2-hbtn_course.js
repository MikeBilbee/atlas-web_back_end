export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;

  }
  get students() {
    return this._students;
  }

  set name(newN) {
    if (typeof newN !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newN;
  }

  set length(newL) {
    if (typeof newL !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = newL;
  }

  set students(newS) {
    if (!Array.isArray(newS) || !newS.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = newS;
  }
}
