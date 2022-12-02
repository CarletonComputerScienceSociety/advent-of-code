const fs = require('fs');

fs.readFile('input.txt', (err, data) => {
    if (err) return console.error(err);
    data.toString().split('\n').forEach((line, index) => {
        line = line.trim();
        console.log(index + ': ' + line);
    });
});
