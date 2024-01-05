export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._loaction = location;
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._loaction;
  }
}