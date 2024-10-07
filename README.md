# CaloriesBurntProgram
### Description
The Calories Burnt Program is a console-based fitness app designed to track calories burned during various exercises. It calculates energy expenditure based on the user's weight, type of exercise, and duration. The user can input their weight in pounds or kilograms, which the program will convert if necessary. The app also provides guidance on how to warm down after completing an activity and stores workout details in a history file.

### Features
• **Weight Conversion**: Allows the user to input their weight in either pounds or kilograms, automatically converting pounds to kilograms.<br>
• **Exercise Selection**: Offers a variety of exercises, such as running, swimming, and cycling, from which the user can select.<br>
• **Calories Burned Calculation**: Computes calories burned per minute based on the chosen exercise's MET value, the user's weight, and exercise duration.<br>
• **Warm-Down Guidance**: Offers recommendations on how to warm down after completing each activity.<br>
• **Workout History**: Saves workout details, including exercise type, MET values, duration, and total calories burned, to a text file for later review.<br>
• **Support for Multiple Exercises**: Allows users to combine multiple activities and calculates total calories burned for all exercises.<br>
• **User-Friendly Interface**: Includes input validation and guides the user through a clear and simple workout tracking process.<br>

### How to Run
1. Clone the repository:<br>
   ```git clone https://github.com/mthMay/CaloriesBurntProgram.git```
2. Navigate to the project directory:<br>
   ```cd CaloriesBurntProgram```
3. Run the application:<br>
   ```python3 main.py```
   
**NOTE: Ensure Python 3 is installed on your system before running the application.**

### How to Use
1. **Entering Weight**:<br>
• The program prompts you to enter your weight in either pounds or kilograms.
• If you enter your weight in pounds, the program will convert it to kilograms for accurate calculation.
2. **Choosing Exercise**:<br>
• The app presents a list of exercises to choose from. Simply type the name of the exercise, and the program will calculate the MET (Metabolic Equivalent of Task) value for that activity.
3. **Setting Duration**:<br>
• After selecting an exercise, the app will prompt you to input the duration of the activity in minutes.
4. **Viewing Results**:<br>
• The app will display the number of calories burned per minute and the total calories burned for the exercise duration.
5. **Adding More Exercises**:<br>
• You can combine multiple activities by choosing another exercise, and the app will keep a running total of your calorie expenditure.
6. **Warm-Down Guidance**:<br>
• After completing an activity, the program provides suggestions on how to warm down based on the selected exercise.
7. **Workout History**:<br>
• All workout data is stored in the "workout history.txt" file, which includes details like exercise type, MET value, and total calories burned. You can access this file to review your past workout sessions.
