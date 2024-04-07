import Car3 from "./Car3";

export default function Garage(props) {
    const api_call = () => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts');
        // xhr.responseType = 'json';
        xhr.onreadystatechange = () => {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const data = JSON.parse(xhr.responseText)
                    console.log(data);
                } else {
                    console.log('Error' + xhr.statusText);
                }

            }
        }
        xhr.send();
    }

    const featchData = () => {
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.log('Error' + error));  
    }

    return (
        <div>
            <h1>Who lives in my garage?</h1>
            <Car3 brand="Telsa 3" make="Tesla" year="2023" color="red"/>
            <button onClick={api_call}>Get Data</button>
            <button onClick={() => featchData()}>Fetch Data</button>
        </div>  
        );
}