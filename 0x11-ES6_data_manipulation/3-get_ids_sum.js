export default function getStudentIdsSum(arr) {
  return arr.reduce((tot, a) => tot + a.id, 0);
}

// import getListStudents from './0-get_list_students.js';
// console.log(getStudentIdsSum(getListStudents()));
