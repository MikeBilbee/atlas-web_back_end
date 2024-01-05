export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(nCode) {
    if (typeof nCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = nCode;
  }

  set name(nName) {
    if (typeof nName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = nName
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}