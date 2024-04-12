const url = 'https://www.google.com'
fetch(url)
    .then(response => {
        for(const pair of response.headers){
            console.log(`${pair[0]}: ${pair[1]}`); 
          }
        return response.text();
    }).then(data => {
        console.log(data);
    });