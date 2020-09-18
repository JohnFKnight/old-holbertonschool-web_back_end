export default function createIteratorObject(rpt) {
  const allEmps = {
    getAllEmps(rpt) {
      const empList = [];
      for (const emp of Object.keys(rpt)) {
        empList.push(emp);
      }
      return empList;
    },
  };
  return allEmps;
}

const report = createReportObject({});
const reportWithIterator = createIteratorObject(report);
console.log(reportWithIterator);