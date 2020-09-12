export default function createEmployeesObject(departmentName, employees) {
  console.log(departmentName, employees);
  const iterable = {
    [Symbol.iterator]() {
      return {
        next() {
          return { value: departmentName.concat(...employees), done: true };
        },
      };
    },
  };
}
