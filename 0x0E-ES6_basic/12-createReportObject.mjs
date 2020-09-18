export default function createReportObject(employeesList) {
    employeesList = createEmployeesObject();
     [Symbol.iterator]() {
    // Get all the dept's in an employee list
	 const depts = Object.values(this.employeesList);

	 // Store the current dept and emp'ee index
	 let currentDeptIdx = 0;
	 let currentEmpeeIdx = 0;

	 return {
	     // Implementation of next()
	     next() {
		 const empees = depts[currentDeptIdx];

		 // doNotHaveMoreEmpees is true when the depts array is exhausted.
		 // That is, all items are consumed.
		 const noMoreEmpees = !(currentDeptIdx < depts.length);
		 if (noMoreEmpees) {
		     // i.e done is true
		     return {
			 value: undefined,
			 done: true
		     };
		 }

		 // if everything is correct, return the employee from the 
		 // current dept and incerement the currentEmpeeindex
		 // so next time, the next employee can be returned.
		 return {
		     value: depts[currentDeptIdx][currentEmpeeIdx++],
		     done: false
		 }
	     }
	 };
     }
};

for (const empee of employeesList) {
    console.log(empee);
}
