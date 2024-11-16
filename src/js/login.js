// Import the required Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-auth.js";
import {
  getDatabase,
  ref,
  update,
} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";

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
const auth = getAuth(app);
const database = getDatabase(app);

// Wait for the DOM to be fully loaded before defining the register function
document.addEventListener("DOMContentLoaded", function () {
  // Function to handle user registration
  function login(event) {
    event.preventDefault();
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;
    signInWithEmailAndPassword(auth, email, password)
      .then(function (userCredential) {
        const user = userCredential.user;
        const userRef = ref(database, "users/" + user.uid);
        const user_data = {
          lastLogin: Date.now(),
        };
        update(userRef, user_data)
          .then(() => {
            alert("User " + email + " logged in successfully!");
            window.location.href = "/public/index.html";
          })
          .catch((error) => {
            console.error("Error logging in user:", error.message);
          });
      })
      // redirect to the home page

      .catch(function (error) {
        alert("Error: " + error.message);
      });
  }

  // Attach the register function to the button click event
  const loginButton = document.getElementById("loginButton");
  loginButton.addEventListener("click", login);
});
