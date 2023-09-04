System Commands (notes)
System commands are usually used to automate tasks or to access system information.

In Python, we can use the os module to interface with the operating system.

The os module has a function called system which allows us to run system commands.

Let's take a look at an example.



We'll start by importing the os module.

import os
Next, we'll use the system function to run the ls command.

Please note this command only exists on Linux and Mac OS X. For Windows use the dir command. Because we use system commands, the commands you can run will depend on your Operating System.



This will list all the files in the current directory.

os.system('ls')
Windows version:

os.system('dir')
We can also store the output of the command in a variable.

output = os.system('ls')
Now, if we print the output variable, we'll see the exit code of the command.

An exit code of 0 means the command was successful.

print(output)
In this example, we've just run a simple ls command.

But we can run any system command we want.

For example, we could run the date command to print the current date and time.

os.system('date')
We could also use the system function to run multiple commands at once.

To do this, we just need to use the ; character to separate the commands.

os.system('date;ls')
As you can see, the date and ls commands are both executed.

And that's how you can run system commands in Python.