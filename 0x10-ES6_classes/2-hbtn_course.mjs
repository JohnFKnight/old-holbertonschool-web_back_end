export default class HolbertonCourse {
  constructor(name, length, students) {
    if (Object.prototype.toString.call(name) === '[object String]') {
      this._name = name;
    } else {
      try {
        throw new TypeError('name must be a string');
      } catch (e) {
        console.log(e);
      }
    }
    if (Object.prototype.toString.call(length) === '[object Number]') {
      this._length = length;
    } else {
      try {
        throw new TypeError('length must be a Number');
      } catch (e) {
        console.log(e);
      }
    }
    if (Object.prototype.toString.call(students) === '[object Array]') {
      this._students = students;
    } else {
      try {
        throw new TypeError('students must be an Array');
      } catch (e) {
        console.log(e);
      }
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
      try {
        throw new TypeError('name must be a string');
      } catch (e) {
        console.log(e);
      }
    }
  }

  set length(length) {
    if (Object.prototype.toString.call(length) === '[object Number]') {
      this._length = length;
    } else {
      try {
        throw new TypeError('length must be a Number');
      } catch (e) {
        console.log(e);
      }
    }
  }

  set students(students) {
    if (Object.prototype.toString.call(students) === '[object Array]') {
      this._students = students;
    } else {
      try {
        throw new TypeError('students must be an Array');
      } catch (e) {
        console.log(e);
      }
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
// const c3 = new HolbertonCourse(13, '1', ['Bob', 'Jane']);
