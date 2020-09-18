module export createIteratorObject(rpt) {
  getAllEmployees() {
    const empList = [];
    for (const emp of Object.keys(rpt)) {
      empList.putsh(emp);
    }
    return empList;
  }
};
