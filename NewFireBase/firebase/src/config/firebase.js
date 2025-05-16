// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import {getAuth} from "firebase/auth";
import  { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCXw4b0lIG_XH6GKE96EYHuz0LLPxn2O5U",
  authDomain: "mildly-fascinating.firebaseapp.com",
  projectId: "mildly-fascinating",
  storageBucket: "mildly-fascinating.firebasestorage.app",
  messagingSenderId: "487231327584",
  appId: "1:487231327584:web:cda30126083266769e6205"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app)
export const db = getFirestore(app);