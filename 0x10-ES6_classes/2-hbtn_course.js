export default class HolbertonCourse {
  constructor(name, length, students) {
    if (Object.prototype.toString.call(name) === '[object String]') {
      this._name = name;
    } else {
      throw TypeError('name must be a String');
    }
    if (Object.prototype.toString.call(length) === '[object Number]') {
      this._length = length;
    } else {
      throw TypeError('length must be a Number');
    }
    if ((Object.prototype.toString.call(students) === '[object Array]')
    && (students.every((s) => Object.prototype.toString.call(s) === '[object String]'))) {
      this._students = students;
    } else {
      throw TypeError('students must be an Array of String');
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

  set name(name) {
    if (Object.prototype.toString.call(name) === '[object String]') {
      this._name = name;
    } else {
      throw TypeError('name must be a String');
    }
  }

  set length(length) {
    if (Object.prototype.toString.call(length) === '[object Number]') {
      this._length = length;
    } else {
      throw TypeError('length must be a Number');
    }
  }

  set students(students) {
    if ((Object.prototype.toString.call(students) === '[object Array]')
    && (students.every((s) => Object.prototype.toString.call(s) === '[object String]'))) {
      this._students = students;
    } else {
      throw TypeError('students must be an Array of String');
    }
  }
}

// const c1 = new HolbertonCourse('ES6', 1, ['Bob', 'Jane']);
// console.log(c1.name);
// c1.name = 'Python 101';
// console.log(c1.name);
// console.log(c1);
// c1.name = 12;
// const c2 = new HolbertonCourse('ES6', '1', ['Bob', 'Jane']);
// const c3 = new HolbertonCourse('ES6', 1, [15, 'Jane']);
