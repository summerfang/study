import fetch from 'node-fetch';

async function fetchData(): Promise<any> {
  try {
    const res = await fetch('https://www.google.com');
    const data = await res.json();
    return data;
  } catch (error) {
    return "Error=" + error.message;
  }
}

(async () => {
  const msg = await fetchData();
  console.log(msg);
})();
