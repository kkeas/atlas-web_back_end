// take input from command line

console.log('Welcome to Holberton School, what is your name?');

// user input event listener
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name !== null) {
    process.stdout.write(`Your name is: ${name}`);
  }
});

// exit event listener
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
