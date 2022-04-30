
//create XMLHttpRequest object
const xhr = new XMLHttpRequest()
//open a get request with the remote server URL
xhr.open("GET", "https://v1s1t0r999.herokuapp.com/make?src=https://leafstuios.com&name=testt")
//send the Http request
xhr.send()

//EVENT HANDLERS

//triggered when the response is completed
xhr.onload = function() {
  if (xhr.status === 200) {
    //parse JSON datax`x
    document.getElementById('jsonresp').innerHTML = x
      
