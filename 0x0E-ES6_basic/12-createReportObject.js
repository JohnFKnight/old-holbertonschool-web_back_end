export default function createReportObject(employeesList) {
  const report = {
    allEmployees: {
      [Object.keys(employeesList)]: [Object.values(employeesList)],
    },
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return report;
}
