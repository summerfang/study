import { DataStore } from 'notarealdb';

const store = new DataStore('./data');

export const students = store.collection('students');
export const colleges = store.collection('colleges'); 
export default store