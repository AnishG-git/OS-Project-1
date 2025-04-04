# Dev Log

## [03/09/2025] 2:40 PM

- Began looking at the project
- Ran cpu.py and understood the existing provided code
- Created a makefile to simplify running the project

## [03/17/2025] 8:26 PM

### Initial thoughts (forgot to add last time)

- I know that I need to create three separate programs (a logger, an encryption program, and a driver program)
- I plan to create three separate files (one for each program)

## [03/20/2025] 10:53 AM (session 1 start)

- My plan is to create the logger first. I want to do this part first because I have some experience writing to files in python so it's more of a low hanging fruit. I'll also start with the drivery but really only the bare minimum for the logger to work.

## [03/21/2025] 7:55 PM (session 1 end)

- I forgot to commit my changes from session 1 so that's why I'm committing the next day
- I was able to successfully create the logger and the MVP of the driver with regard to the logger
- A problem I ran into was that the output of the logger was not showing up in the logfile. However, I realized that the solution was that I needed to manually flush to the logfile

## [3/21/2025] 8:10 PM (session 2 start)

- For this session, I plan on finishing up the project by creating the encryption process and modifying the driver program to acknowledge all specified commands with proper functionality.

## [3/21/2025] 11:56 PM (session 2 end)

- I was able to successfully create the encryption program and modify the driver to acknowledge all commands
- I was trying to print to STDOUT from the encryption process, but nothing was printing to the console even after flushing. I realized that I needed to print the encryption process's STDOUT to the driver's STDOUT and that fixed it.

## [3/22/2025] 5:53 PM (session 3 start)

- I read the project requirements once more and I realized that for encryption and decryption, the user should be allowed to use words from their history so I plan to add that functionality this sesion.

## [3/22/2025] 9:29 PM (session 3 end)

- I was able to successfully modify the encryption program and driver to behave as expected with the history related options during encryption and decryption.

## [3/23/2025] 8:52 AM (session 4 start)

- I realized that the logger is not doing what it's supposed to do exactly so I'm modifying it in this session
- I anticipate that it will be a quick change since the modification will be at the level of the driver

## [3/23/2025] 9:54 AM (session 4 end)

- Over the duration of the session, I realized that I had to make modifications to all three files because I was not logging RESULT or ERROR in encryption.py in an expressive way
- In summary, I made logging more expressive and formatted printing to STDOUT
