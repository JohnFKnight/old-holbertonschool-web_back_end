export default fucntion handleResponseFromAPI(promise) {
  promise
    .then((response) => {
      {
        status: 200,
         body: 'Success',
      },
      console.log("Got a response from the API");
    })
    .catch((error) => {
	(Error());
    });
}
