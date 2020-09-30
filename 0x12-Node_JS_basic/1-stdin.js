process.stdin.setEncoding('utf8');

process.stdout.write('Welcome to Holberton School, what is your name?\n');
// console.log('Welcome to Holberton School, what is your name?\n');


process.stdin.on('readable', () => {
    var chunk = process.stdin.read();
    process.stdout.write('Your name is: ' + chunk);
});

process.on('exit', () => {
    process.stdout.clearLine();
    process.stdout.write('This important software is now closing\n');
});
