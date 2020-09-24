export default function getListStudentIds(arr) {
  if (Object.prototype.toString.call(arr) !== '[object Array]') {
    return [];
  }
    return arr.map((a) => a.id);
}
import getListStudents from './0-get_list_students.mjs';
console.log (getListStudentIds("hello"));
console.log (getListStudentIds(getListStudents()));
// console.log ((getListStudents()));
