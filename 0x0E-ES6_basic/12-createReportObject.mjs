export default function createReportObject(employeesList) {
  const report = {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return report;
}
console.log(createReportObject("{ Software: [ 'Bob', 'Sylvie' ] }"));
// console.log(createReportObject("{ Software: [ 'Bob', 'Sylvie' ] }").getNumberofDepartments());
