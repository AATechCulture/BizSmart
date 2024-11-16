// Import the required Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-auth.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-database.js";

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
  function register(event) {
    event.preventDefault(); // Prevent form submission
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;
    var businessName = document.getElementById("businessNameInput").value;

    console.log(email);
    console.log(password);
    console.log(businessName);

    auth
      .createUserWithEmailAndPassword(email, password)
      .then(function (userCredential) {
        const user = userCredential.user;
        const userRef = database.ref("users").child(user.uid);
        const user_data = {
          email: email,
          businessName: businessName,
          lastLogin: Date.now(),
        };
        userRef
          .set(user_data)
          .then(() => {
            alert("User " + email + " signed up successfully!");
          })
          .catch((error) => {
            console.error("Error saving user data:", error.message);
          });
      })
      .catch(function (error) {
        alert("Error: " + error.message);
      });
  }

  // Attach the register function to the button click event
  const registerButton = document.getElementById("registerButton");
  registerButton.addEventListener("click", register);
});
