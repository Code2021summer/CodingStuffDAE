// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import {
    getAuth,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    onAuthStateChanged,
    signOut
} from "https://www.gstatic.com/firebasejs/11.6.0/firebase-auth.js";
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
const auth = getAuth(app);

//chat
// Sign up function
window.signUp = function () {
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;
  
    createUserWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        alert("Sign-up successful!");
        console.log("Signed up:", userCredential.user);
      })
      .catch((error) => {
        alert("Sign-up error: " + error.message);
      });
  };
  
  //Sign in function
  window.logIn = function () {
    const email = document.getElementById("signin-email").value;
    const password = document.getElementById("signin-password").value;
  
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        alert("Sign-in successful!");
        console.log("Signed in:", userCredential.user);
      })
      .catch((error) => {
        alert("Sign-in error: " + error.message);
      });
  };
  
  // Log out function
  window.logOut = function () {
    signOut(auth)
      .then(() => {
        alert("Logged out!");
      })
      .catch((error) => {
        alert("Logout error: " + error.message);
      });
  };
  
  // Watch auth state
  onAuthStateChanged(auth, (user) => {
    const userInfo = document.getElementById("user-info");
    if (user) {
      userInfo.textContent = `Logged in as: ${user.email}`;
    } else {
      userInfo.textContent = "You're not signed in :(";
    }
  });