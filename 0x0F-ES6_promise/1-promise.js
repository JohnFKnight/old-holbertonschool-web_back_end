export default function getFullResponseFromAPI(success) {
  const promise = new Promise((resolve, reject) => {
    if (success) {
      const obj = {
        status: 200,
        body: 'Success',
      };
      resolve(obj);
    } else {
      const reason = new Error('The fake API is not working currently');
      reject(reason);
    }
    return promise;
  });
}
