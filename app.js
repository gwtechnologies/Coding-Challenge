var express = require('express');
var app = express();
var path = require('path');

app.use(express.static(path.join(__dirname, '.')));

// viewed at http://localhost:8080

app.listen(8080);