export default function createIteratorObject(rpt) {
  const empList = [];
  for (const emp of Object.keys(rpt)) {
    empList.push(emp);
  }
  return empList;
}

const report = createReportObject({});
const reportWithIterator = createIteratorObject(report);
console.logt(reportWithIterator);
console.logt(typeof reportWithIterator[Symbol.iterator]);
