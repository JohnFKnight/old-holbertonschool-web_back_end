export default class HolbertonCourse {
  constructor(name, length, students) {
    if (Object.prototype.toString.call(name) === '[object String]') {
      this._name = name;
    }
    if (Object.prototype.toString.call(length) === '[object Number]') {
      this._length = length;
    }
    if (Object.prototype.toString.call(students) === '[object Array]') {
      this._students = students;
    }
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

  set name(x) {
    this._name = x;
  }

  set length(x) {
    this._length = x;
  }

  set students(x) {
    this._students = x;
  }
}
