export async function getToken4email(email : string) {
    const response = await fetch(`http://localhost:5000/token/${email}`);
    const data = await response.json();
    return data;
}