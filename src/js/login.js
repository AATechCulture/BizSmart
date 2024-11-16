// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCYQyzjwjBm6I067ISbizMwujJxS1C7dw4",
  authDomain: "bizsmart-login.firebaseapp.com",
  projectId: "bizsmart-login",
  storageBucket: "bizsmart-login.firebasestorage.app",
  messagingSenderId: "649837784329",
  appId: "1:649837784329:web:560ddb948a1e0f563577d8",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = app.auth();
const db = app.database();
