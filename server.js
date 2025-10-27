const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Serve static files (e.g., HTML, CSS)
app.use(express.static('public'));

// Route to handle form submission
app.post('/submit_form', (req, res) => {
    const { name, email, message, honeypot } = req.body;

    // Honeypot field check
    if (honeypot) {
        return res.status(400).send('Bot submission detected.');
    }

    // Create a transporter
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'ryan.gallacher2@gmail.com', // Replace with your email
            pass: 'your-email-password'   // Replace with your email password
        }
    });

    // Email options
    const mailOptions = {
        from: email,
        to: 'ryan.gallacher2@gmail.com',
        subject: `Contact form submission from ${name}`,
        text: message
    };

    // Send email
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return res.status(500).send('Error sending email: ' + error.message);
        }
        res.status(200).send('Email sent: ' + info.response);
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});