function createEmployeesObject(departmentName, employees) {
    const iterable = {
	[Symbol.iterator]() {
	    // let step = 0;
	    const iterator = {
		new () {
		    return {
			value: departmentName.concat(...employees).toString(), done: true
		    };
		}
	    };
	    return iterator;
	}
    };
}

console.log(createEmployeesObject("Software", [ "Bob", "Sylvie" ]));
