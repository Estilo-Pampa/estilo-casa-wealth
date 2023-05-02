// Code for Node.js server
// Include necessary modules
const http = require('http');
const fs = require('fs');
const path = require('path');

// Define server port
const port = 3000;

// Create server object
const server = http.createServer((req, res) => {
  // Set response headers
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('Access-Control-Allow-Origin', '*');

  // Check if request is for root directory
  if (
