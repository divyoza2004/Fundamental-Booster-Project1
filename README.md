# Fundamental Booster

## Objective:

"An Interactive Personal Data Collector built in Python to showcase fundamental programming concepts. The application dynamically captures and displays user metrics, utilizing core features like type casting, arithmetic operators, dynamic variables, and built-in functions like id() and type()."

## Requirements:

### 1. Use of print() and input() Functions 
- Ask the user to enter their name, age, height, and favourite number.
- Show clear messages to guide the user while entering information.
- Display the entered information in a neat and easy-to-read format.

### 2. Data Types, Variables & Operators
- Store the user's information in different variables.
- Use the correct data type for each value.
- Perform simple calculations using +,-,* and /
- For example, use age to calculate the birth year.
- Create user-friendly message using text formatting. 

### 3. Type Casting
- `Type casting` is the process of converting a value from one data type to another.
- **For example:**    
  - Convert age and favourite number into whole number.
  - Convert height into a decimal number.
  - Show that values can be changed from one data to another when needed. 

### 4. Using id() and type() Functions
- The `type()` function is used to identify and display the data type of a variable.
- The `id()` function is used to the unique memory address of a variable and stored in the computer's memory. 
- Show a summary containing:
   - Variable name
   - Stored value
   - Data type
   - Memory address 

## ▶ Demo Video

<a href="https://your-video-link.com/replace-with-real-link" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/%E2%96%B6-Watch%20Demo%20Video-e63946?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch demo video" />
</a>

## Output:
<img width="1093" height="713" alt="Screenshot 2026-06-24 200532" src="https://github.com/user-attachments/assets/bd710b13-6266-40d6-918f-e7b7e434e3ac" />

## How It Works: 
1. **Inputs:** The script prompts the user for information.
2. **Casting:** `age` and `fav` are cast to integers, `height` is cast to a float and `name` is cast to a str.
3. **Calculation:** It calculates the birth year: 
   $$\\text{Birth Year} = \\text{Current Year} - \\text{Age}$$
4. **Inspection:** It prints the collected values alongside their explicit Python data types and unique RAM memory addresses.
