// Import the required Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  onAuthStateChanged,
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
  let userId = null;
  onAuthStateChanged(auth, (user) => {
    if (!user) {
      alert("You are not logged in. Please log in to access this page.");
      // redirect to the login page
      window.location.href = "index.html";
    } else {
      userId = user.uid;
    }
  });
  const form = document.getElementById("contact-form");

  form.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const formData = new FormData(form);
    const jsonData = {
      expenses: formData.get("expenses"),
      amount: parseFloat(formData.get("amount")),
      date: formData.get("date"),
      category: formData.get("category"),
    };

    const uuid = userId;

    console.log("Data to be saved:", jsonData);
    console.log("UUID:", uuid);

    try {
      const response = await fetch(`/${uuid}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(jsonData),
      });

      if (response.ok) {
        const result = await response.json();
        alert("Expense saved successfully: " + JSON.stringify(result));
      } else {
        alert("Failed to save expense. Status: " + response.status);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  });
});
