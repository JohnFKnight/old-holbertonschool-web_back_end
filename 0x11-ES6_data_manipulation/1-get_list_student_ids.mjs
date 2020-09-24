export default function getListStudentIds(arr) {
  return arr.map(() => {return arr.id;});
}
import getListStudents from './0-get_list_students.mjs';
console.log (getListStudentIds("hello"));
// console.log (getListStudentIds(getListStudentIds()));
