//XMLHttpRequest helps get data without needed to refresha a page
var request = new XMLHttpRequest()

request.open('GET', 'https://www.balldontlie.io/api/v1/players', true)


// This is where the basketball player data will be accessed
request.onload = () => {

}

request.send