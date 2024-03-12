const express = require('express');
const path = require('path');
const app = express();

// Serve static files from the "frontend/public" directory
app.use(express.static(path.join(__dirname, '../frontend/public')));

// Route to serve the index.html page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend/public', 'index.html'));
});

// Start the server
const PORT = process.env.PORT || 1002;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});