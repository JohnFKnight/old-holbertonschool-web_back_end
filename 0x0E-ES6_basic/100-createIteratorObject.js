export default function createIteratorObject(rpt) {
  const empList = [];
  for (const emp of Object.keys(rpt)) {
    empList.push(emp);
  }
  return empList;
}
