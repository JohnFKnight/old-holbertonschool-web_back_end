export default class HolbertonCourse {
  constructor(name, length, students) {
  String this._name = name;
  int this._length = length;
  Array this._students = students;
  }
  get name() {
    return this._name;
  }
  get length() {
    return this._length;
  }
  get students() {
    return this._students
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
