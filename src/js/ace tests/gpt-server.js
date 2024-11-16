const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

// Import routes
const chatgptRoutes = require("./chatgptRoutes");
const authRoutes = require("./authRoutes");

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Use routes
app.use("/api/auth", authRoutes);
app.use("/api/chat", chatgptRoutes);

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});