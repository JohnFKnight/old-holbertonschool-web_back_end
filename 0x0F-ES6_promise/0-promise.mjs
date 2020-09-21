export default function getResponseFromAPI() {
  const promise = new Promise(() => {
  });
  return promise;
}

// import getResponseFromAPI from './0-promise.js'
const response = getResponseFromAPI();
console.log(response);
console.log(response instanceof Promise);
