// Import the required Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import {
  getAuth,
  createUserWithEmailAndPassword,
  onAuthStateChanged,
  signOut,
} from "https://www.gstatic.com/firebasejs/11.0.2/firebase-auth.js";
import {
  getDatabase,
  ref,
  set,
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
  const loggedInContent = document.getElementById("loggedInContent");
  const loggedOutContent = document.getElementById("loggedOutContent");
  const youAreLoggedIn = document.getElementById("youAreLoggedIn");
  const logoutButton = document.getElementById("logoutButton");

  // Function to handle user registration
  function register(event) {
    event.preventDefault();
    var email = document.getElementById("emailInput").value;
    var password = document.getElementById("passwordInput").value;
    var businessName = document.getElementById("businessNameInput").value;
    var businessType = document.getElementById("businessTypeInput").value;
    var location = document.getElementById("location").value;
    var owner = document.getElementById("owner").value;


    createUserWithEmailAndPassword(auth, email, password)
      .then(function (userCredential) {
        const user = userCredential.user;
        const userRef = ref(database, "users/" + user.uid);
        const user_data = {
          id: user.uid,
          email: email,
          businessName: businessName,
          lastLogin: Date.now(),
          businessType: businessType,
          location: location,
          owner: owner,

        };
        set(userRef, user_data)
          .then(() => {
            alert("User " + email + " signed up successfully!");
            window.location.href = "/public/index.html";
          })
          .catch((error) => {
            console.error("Error saving user data:", error.message);
          });
      })
      .catch(function (error) {
        alert("Error: " + error.message);
      });
  }

  // Function to handle user logout
  function logout() {
    signOut(auth)
      .then(() => {
        alert("You have been logged out.");
      })
      .catch((error) => {
        console.error("Error logging out:", error.message);
      });
  }

  // Check if a user is logged in and show content accordingly
  onAuthStateChanged(auth, function (user) {
    if (user) {
      // User is logged in, show logged-in content and hide logged-out content
      loggedInContent.style.display = "flex";
      loggedOutContent.style.display = "none";
      youAreLoggedIn.innerHTML = "You are logged in as " + user.email;
    } else {
      // No user is logged in, show logged-out content and hide logged-in content
      loggedInContent.style.display = "none";
      loggedOutContent.style.display = "flex";
    }
  });

  // Attach the register function to the button click event
  const registerButton = document.getElementById("registerButton");
  registerButton.addEventListener("click", register);
  logoutButton.addEventListener("click", logout);
});
