export default function getListStudentIds(arr) {
  if (Object.prototype.toString.call(arr) !== '[object Array]') {
    return [];
  }
  return arr.map((a) => a.id);
}
