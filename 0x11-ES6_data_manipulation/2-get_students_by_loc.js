export default function getStudentsByLocation(arr, city) {
  return arr.filter((a) => a.location === city);
}

// import getListStudents from './0-get_list_students.js';
// console.log(getStudentsByLocation(getListStudents(), "Paris"));
// console.log(getStudentsByLocation(getListStudents(), "San Francisco"));
