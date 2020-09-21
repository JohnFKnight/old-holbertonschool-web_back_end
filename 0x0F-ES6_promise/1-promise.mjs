export default function getFullResponseFromAPI(success) {
  const promise = new Promise((resolve, reject) => {
    if (success) {
      resolve(
      {
        status: 200,
        body: 'Success',
      })
    } else {
      reject(Error('The fake API is not working currently'));
    }
  })
  return promise;;
}

console.log(getFullResponseFromAPI(true));
console.log(getFullResponseFromAPI(false));

// const askMom = function () {
//     getFullResponseFromAPI(true)
//         .then(function (fulfilled) {
//             // yay, you got a new phone
//             console.log(fulfilled);
//         })
//         .catch(function (error) {
//             // ops, mom don't buy it
//             console.log(error.message);
//         });
// }

// askMom();