export default function getListStudentIds(arr) {
  return arr.map((a) => {a.id});
}
import getListStudents from './0-get_list_students.mjs';
console.log (getListStudentIds("hello"));
// console.log (getListStudentIds(getListStudentIds()));
// console.log ((getListStudents()));
