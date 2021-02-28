# motion_detector
motion_detector for dark environments

This repo is just a basic motion detector...

It works this way:
- It selects Red channel (the closes one to the Near InfraRed, so the best for dark/night picts.).  
- Then it makes the difference of pixel values between 2 frames.  
- Finally, it calculates the mean of the values of the pixel differences.  
- If mean of the difference is bigger than 3.5 (chenge this threshold if necessary),  
we can assume that there is some kind of motion.


