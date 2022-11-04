# Tasks:
- check links on TOC
- find credits to add
- add mine and flag images to features

# MINESWEEPER GAME

# Table Of Contents
- [Minesweeper Project Overview](#minesweeper-project-overview)
   - [Live Project](#live-project-link-to-live-project)
   - [Project Introduction](#project-introduction)
- [Responsive Review](#responsive-review)
   - [Am I Responsive?](#am-i-responsive-link-to-responsive-review-website)
   - [Development Note on Responsive Design](#development-note-on-responsive-design)
- [User Experience (UX)](#user-experience-ux)
   - [Website Objectives](#website-objectives)
   - [Website Design](#website-design)
   - [Structure Non-Linear Plane](#structure-non-linear-plane)
   - [Wireframes](#wireframes)
   - [Features](#features)
- [Further Development](#further-development)
- [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)
- [Testing](#testing)
   - [HTML Validator Results](#html-validator-results)
   - [CSS Validator Results](#css-validator-results)
   - [JS Validator Results](#js-validator-results)
   - [Console Log Warning](#console-log-warning)
   - [Lighthouse Accessibility Results](#lighthouse-accessibility-results)
   - [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
   - [Further Testing](#further-testing)
   - [Development Bugs](#development-bugs)
   - [Key Learn](#key-learn)
- [Deployment](#deployment)
   - [Set Up Local GitHub Repository](#set-up-local-github-repository)
   - [Repository Framework](#repository-framework)
   - [Update Repository](#update-repository)
   - [GitHub Pages](#github-pages)
- [Credits](#credits)
   - [Development Resources](#development-resources)
   - [Media Resources](#media-resources)
   - [Acknowledgements](#acknowledgements)

<br>

# Minesweeper Project Overview
   ## Live Project [*(link to live project)*](https://minesweeper-python-project.herokuapp.com/)

   ## Project Introduction
   (**Note:** The aim of this project will be to develop the classic game 'Minesweeper'. This game will be devloped using Python and will be deployed using mock terminal on the Heroku platform.

   Minesweeper is a challanging single player logic game where the user must select tiles on a grid without hitting a mine. If the user successfully selects a tile without hitting a mine then the tile will provide information as to whether a mine or multiple mines are hidden within its neighbouring tiles. This is presented in the form of numbers, a tile with 3 mines in neighbouring tiles will present the user with the number 3.

   If the user selects all tiles on the grid without mines they win the game, however if they land on a tile hiding a mine the game is lost.

   If you would like to learn more about Minsweeper you can find more information here: https://en.wikipedia.org/wiki/Minesweeper_(video_game)

   <br>

# Responsive Review

   ## Am I Responsive? [*(link to responsive review website)*](https://ui.dev/amiresponsive?url=https://minesweeper-python-project.herokuapp.com/)
   ![Responsive Review](readme_assets/responsive_design/responsive-screenshot.png)

   ## Development Note on Responsive Design
   The objective of this project was to develop a Python command-line application and was not focused on developing a responsive website.<br>
   As this was not in the scope of the project it was not given consideration.
   
   <br>

# User Experience (UX)

   ## Project Objectives

   <details>
      <summary style="font-weight:bold">Developer Goals</summary>

   As the developer I want to create a simple and engaging game that is easy to use and will result in users returning to the site. 
   * Easy to use functionality.
   * Addictive gameplay to encourage return users and drive positive word of mouth to encourage new users.
   * Provide clear instruction as to the rules of the game.
   * Set a range of difficulties to allow user progression and continued engagment.
   * Record winning scores based on difficulty and completion time to promote re-vistiation and competition between users.
   * Build in flag functionality to allow users to mark cells they believe to have mines.
   * Build a appealing user interface whilst observing the limitations of the project scope(command-line application).
   
   ---
   </details>

   <details>
      <summary style="font-weight:bold">Developer Future Goals</summary>
   
   Points to consider for future development:
   * Potential to implement a more userfriendly interface such as tkinter or pygame (excluded as not in scope for this project).
   * Build to be responsive (excluded as not in scope for this project).
   * If responsive design is set-up then a customised difficulty could be implemented to allow the user to generate a board with a their desired size and number of mines. This was not feasible in this project as it may have exceeded the console size available.

   ---
   </details>

   <details>
      <summary style="font-weight:bold">First-Time User Goals</summary>

   * Understand the purpose of the site.
   * Immediately engaged by easy to use yet challanging gameplay.
   * Invoke nosatalgia.
   * Simple intuitive menu navigation.
   * Rules easliy located and understood.

   ---
   </details>

   <details>
      <summary style="font-weight:bold">Returning User Goals</summary>
   
   * Use the scoreboard to improve their scores and compete with other users.
   * Tailor the difficulty to their experience with the game.

   ---
   </details>


   ## HTML/CSS Design
   The focus of this project was to develop a command-line application. HTML and CSS development was not in scope for this project.

   However, I did tailor the course provided HTML and CSS files slightly to produse a more engaging user experience.

  <details>
      <summary style="font-weight:bold">Background</summary>
   Utilised a SVG file from https://freesvg.org:<br>
    <img src="readme_assets/ux/backgound_img.svg" alt="explossion drawing" width="450px"/>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Position of terminal</summary>

   Centred the terminal console on the page and increaed it's size to cols: 80, rows: 50 to accommodate the game layout.<br>
   <img src="readme_assets/ux/terminal-centred.png" alt="terminal poitioning on the page" width="450px"/>

   ---

   </details>


   <details>
      <summary style="font-weight:bold">Run program button</summary>
   Button also centred and colours changed to be inkeeping with the game theme and backgroung colour scheme.<br>
   <img src="readme_assets/ux/button.png" alt="image of run program button" width="450px"/>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Flavicon</summary>
   Flavicon updated for better user experience.<br>
   <img src="readme_assets/ux/flavicon.png" alt="image of the flavicon on the web tab" width="450px"/>

   ---

   </details>


   ## Wireframes

   Only a skeleton plane has been developed for this project due to it being a command-line application and therefore having pre-set formating.

   - [Skeleton Plane](https://www.figma.com/file/M0wxItI1Bx3Nh4LRIBNp1e/Untitled?node-id=0%3A1)

   **Note:** The structure and wireframes are only to act as a concept and are subject to change as the game development evolves.


   ## Features

   ### **Features planning**

   <details>
      <summary style="font-weight:bold">Mind-Map</summary>
   <br>
   The below image provides an initial mind-map into what features might be appropriate for the game based on the set objectives.

   ![Mind Map](readme_assets/features/mind-map.png)
   If you have a LucidChart account you can also view this Mind-Map [here](https://lucid.app/lucidspark/e0824881-e88c-4530-937e-03f8b923e9b2/edit?viewport_loc=-953%2C-1%2C3247%2C1693%2C0_0&invitationId=inv_d875bc30-8e51-4375-b0f2-c2a63991877b)
   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Priority Matrix</summary>
   <br>
   The below maps out the feaibility of the features considered against the user value they provide to help establish the priortiy they have as part of the build.

   ![Priority Matrix](readme_assets/features/priority-matrix.png)
   If you have a LucidChart account you can also view this priority matrix [here](https://lucid.app/lucidspark/4b1e28c9-055d-4535-87d6-0f258286fe20/edit?viewport_loc=-2982%2C2311%2C4151%2C2041%2C0_0&invitationId=inv_67402cc9-c065-4b2a-ac9d-b9c360a0b967)
   <br>

   Following this review the build order of the features will be broken down into phases:

   #### Phase 1:
   - Gameplay
   - Validations
   - Rules
   - Difficulty

   #### Phase 2:
   - Clear screen
   - Titles

   #### Phase 3:
   - Scoreboard
   - Username (useless without scoreboard)

   #### Phase 4 (Future enhancements - currently out of scope):
   - User interface (e.g. tkinter, pygame)

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Process Flow</summary>
   <br>
   The below details the process flow for the game from beginning to end.

   ![Process Flow](readme_assets/features/process-flow.png)<br>
   If you have a LucidChart account you can also view this process flow [here](https://lucid.app/lucidchart/6f4a551a-5f6e-43eb-9645-1834994d4e27/edit?viewport_loc=-136%2C-64%2C3656%2C1771%2CI~k5YlUlNz8V&invitationId=inv_4642de00-28f1-4eff-8cd1-fe81b08e943d)
   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Functions Flow</summary>
   <br>
   The below demonstrates the key game functions and how they interact with each other. It also details the inclusion of the Gameplay class.

   ![Functions Flow](readme_assets/features/function-flow.png)<br>
   If you have a LucidChart account you can also view this functions flow [here](https://lucid.app/lucidchart/6f4a551a-5f6e-43eb-9645-1834994d4e27/edit?viewport_loc=-391%2C-96%2C4221%2C2189%2CMrp4u2cXQ7zq&invitationId=inv_4642de00-28f1-4eff-8cd1-fe81b08e943d)
   <br>

   ---
   
   </details>

   <details>
      <summary style="font-weight:bold">Class Requirements</summary>
   <br>
   The below breaks down the Gameplay class detailing it's purpose, class variables and methods.

   ![Class Requirements](readme_assets/features/class-breakdown.png)<br>
   If you have a LucidChart account you can also view this class requirements [here](https://lucid.app/lucidchart/6f4a551a-5f6e-43eb-9645-1834994d4e27/edit?viewport_loc=-1010%2C-180%2C3889%2C2017%2CVWq4R58lY_hn&invitationId=inv_4642de00-28f1-4eff-8cd1-fe81b08e943d)
   <br>

   ---
   
   </details>


   ### **Features breakdown**

   Each section below will detail their specific function.
   

   <details>
      <summary style="font-weight:bold">HTML/CSS</summary>
   <br>

   The HTML and CSS development was not in scope for this project. However, small ammendments were made to the template provided by the course to align better with the game aesthetics and accomodate the termainal size requirements.

   ---

   #### Console size and position
   Console was centred for a cleaner look.
   It was also increased from '80 columns by 24 rows' to '80 columns by 50 rows' to allow for additional info to be provided without the user needing to scroll on the page. This was especially inportant for higher difficulty games as the grid took up a substancial amount of the space available.

   ![Console Position](readme_assets/features/demo-features/console-position.png)
   <br>

   ---

   #### SVG img
   An SVG image was used in the background.
   Due to the build I was not able to implement a png background and instread imput the SVG coordinates directly into the layout.html file.

   ![Background Img](readme_assets/ux/backgound_img.svg)
   <br>

   ---

   #### Flavicon
   Flavicon updated for better user experience. 
   This could not be achieved through the normal process of storing a flavicon icon in the root directory and instead had to link to an external web image.

   ![Flavicon Img](readme_assets/ux/flavicon.png)
   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Titles</summary>
   <br>

   To enhance the asthetics of the game without using a interface library such as pygame or tkinter I used pyfiglet to make more engaging titles and to help the user seperate and navigate the various pages/functions.

   ---

   #### Import required
      import pyfiglet
      from pyfiglet import figlet_format 
   <br>

   ---
   #### Home page
   For the Intro and home page I wanted to generate a more impactful title. This would make users instantly aware of what they are playing and invoke a positive emotional response.

   ![Intro Title](readme_assets/features/demo-features/intro-title.png)
   <br>

   ---

   #### Other pages
   For each of the other pages I also used pyfiglet to make an impactful title.<br>
   See an example of a title (rules) below.<br><br>
   This was applied to:
   - Rules
   - Scoreboard Selection
   - Scoreboard
   - Gameplay
   - Win
   - Gameover

   ![Other titles](readme_assets/features/demo-features/rules-title.png)
   <br>

   </details>

   <details>
      <summary style="font-weight:bold">Clear Board</summary>
   <br>

   To ensure that the terminal does not get too cluttered and the user is not provided more information than they need to play the game I utilised a clear function which I obtained from stack overflow:<br>
   https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console

   This function was stored on another py sheet (format.py) to avoid clutter on the main run.py file.

   ---

   #### Import required
      import os
   <br>

   ---

   #### Function code
      def cls(): 
         os.system('cls' if os.name=='nt' else 'clear')
   <br>

   </details>

   <details>
      <summary style="font-weight:bold">Username</summary>
   <br>

   Set a requirement for the user to enter a username. This username is passed through the functions and used in the scorebaord update if the user wins a game. 

   Upon playing a new game following a win or loss the user will not be required to re-enter their username.

   ---

   #### Username format
   To appear consistantly on the scoreboard each username was set to be 10 characters long.<br>
   This was achieved by running a while loop that added a space to the end of the word until it's length equalled 10.

      while len(user_name) < 10:
         user_name = user_name + " "
   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Rules</summary>
   <br>

   Rules has little complexity and is simply a breakdown of the instructions required to play the game.

   This was spit into 2 pages for readability and also to eliminate a bug identified in manual testing. This bug is detailed in the [Development Bugs](#development-bugs) section of this readme file.

   ---

   #### Imports required
   To format the title the pyfiglet is required.<br>

      import pyfiglet
      from pyfiglet import figlet_format
   <br>

   ---

   #### Page 1
   This page provides a link to an instruction video on youtube and the game objectives.
   It has a input field which will take any user-input entered to move onto the next page of the rules breaking down the instructions.

   ![Page 1](readme_assets/features/demo-features/rules-page-one.png)
   <br>

   ---

   #### Page 2
   This details the instruction required to play the game.
   It also has a input field which will take any user-input entered to move back to the home navigation page.

   ![Page 2](readme_assets/features/demo-features/rules-page-two.png)
   <br>

   ---

   </details>


   <details>
      <summary style="font-weight:bold">Scoreboard</summary>
   <br>

   The scoreboard utilises the username which has been entered at the commencement of the game as well as the time the gameplay begins and ends if the user wins. It then updates a specific google sheet dependant on the difficulty the user played and presents the top 5 scores back to the scoreboard screen.

   ---

   #### Imports required
   This scoreboard requies an API link with google sheets.<br>

      import gspread
      from google.oauth2.service_account import Credentials

   To format the title the pyfiglet is required.<br>
   
      import pyfiglet
      from pyfiglet import figlet_format
   <br>

   ---

   #### Define constants
   Using the tutorial provided as part of the 'love-sandwiches' course project, I defined the constants I would require to read and update the google sheet utilising the imports above.<br>
   (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/?child=first)<br>

      SCOPE = [
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"
         ]

      CREDS = Credentials.from_service_account_file("creds.json")
      SCOPED_CREDS = CREDS.with_scopes(SCOPE)
      GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
      SHEET = GSPREAD_CLIENT.open("Minesweeper_scoreboard")
   <br>

   ---
   
   #### Page 1
   This page allows the user to select the appropriate scoreboard. Each difficulty level has it's own scoreboard( easy, medium, hard).

   ![Page 1](readme_assets/features/demo-features/scoredboard-navigation.png)
   <br>

   ---

   #### Page 2
   Once the game is won, the game duration is calculated and recorded alongside the difficulty and username. This is then imported to the google sheets.<br>
   When the scoreboard page is called it presents back the top 5 scores on the specified google sheet whilst eliminating any unessesary data (difficulty - because this is on the title, time in secs - shown in proper format)

   ![Top 5](readme_assets/features/demo-features/scoreboard-top-five.png)

   ---

   ![Google Sheets](readme_assets/features/demo-features/google-sheets-scores.png)
   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Difficulty</summary>
   <br>

   The difficulty page allows the user to select a level that is appropriate to their skill and experience with the game.

   ---

   #### Imports required
   To format the title the pyfiglet is required.<br>

      import pyfiglet
      from pyfiglet import figlet_format
   <br>

   ---

   #### Difficulty selection
   The difficutly options that the user selects will affect the size of the board and the number of mines hidden.

   ![Difficulty](readme_assets/features/demo-features/difficulty.png)
   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Gameplay</summary>
   <br>

   The gameplay works by first using a class to generate a board with all the mines and values placed. It then generates a second board which is presented to the user without the mines and value information. Once a user makes a coordinate guess the cell the user guesses on the user board is updated to equal that of the values board.

   If the user selects a cell with a mine they lose, if they select all cells without a mine they win.

   ---

   #### Imports required
   Class is assigned to board in gameplay to set the board relative to the board size and mines passed. This then sets the mine postions utilising import random and the values in realtion to those mines. The class is called to  update the userboard with guesses and return a visual userboard to the console.<br>

      import game_layout
      import random (called in class GameLayout)

   To format the title the pyfiglet is required.<br>

      import pyfiglet
      from pyfiglet import figlet_format

   To take the start time of the game which will later be used to calculate the game duration in the win function.<br>

      import time

   <br>

   ---

   #### Starting board
   The board board size and number of mines depends on the difficulty selected by the user.
   Each round a board is presented to the user showing the values from their prevous guesses.

   ![Starting Board](readme_assets/features/demo-features/gameplay/starting-board.png)
   <br>

   ---

   #### Enter coordinates
   The user will then enter coordinates in the following format (row coloumn).
   They will then be offered the opportunity to place a flag. If the user enter 'n' the space will be revealed.

   ![First Guess](readme_assets/features/demo-features/gameplay/starting-board-with%20guesses.png)
   <br>

   ---

   #### Selected number value
   If the user selects a cell which is next to a mine it will present a number. The number will reference how many mines are in it's neighbouring cells.

   ![Select Number](readme_assets/features/demo-features/gameplay/select-number.png)

   ![Present Number](readme_assets/features/demo-features/gameplay/opened-number.png)
   <br>

   ---

   #### Flags
   Flags are placed by the user on cells they deduce have mines to ensure they do not forget and select them by accident.
 
   Each time a user makes a guess they will be asked if they would like to place a flag at these coordinates. If they select yes then the board will show a 'F' in this cell on the next round.

   ![Place Flag](readme_assets/features/demo-features/gameplay/place-flag.png)

   ![Show Flag](readme_assets/features/demo-features/gameplay/show-flag.png)

   ---

   If a user selects a cell that has a flag on it, they will be informed that a flag exites at this position and asked if they would like to dig anyway.

   ![Dig Flag](readme_assets/features/demo-features/gameplay/dig-flag.png)

   ---

   Consideration was made for using an image instead of a 'F' on the board.
   To do this considered using the following Unicode Character ("\U0001F6A9") 🚩

   However, the unicode character took up 2 spaces on the board which did not look right as the rest was set up to deal with single characters. I considered changing the cell size on the board to accomodate this but this would have meant that either the 1 character numbers or the flag would have been slightly off center.

   In the end I opted to keep the 'F' as I felt this was inkeeping with the games old school asthetic being a console game.

   <br>

   ---

   #### Selected cell not next to mine
   If the user selects a cell that is not neighbouring a mine then the board will update this cell to show a 0. It then uses a recursion loop to check each of it's neibouring cells as a new guess, which then in turn does the same for their neighbouring cells, and so on. This will continue to take place until it reaches values higher than 0 wiich will break the loop.

   This results in the 0's spreading until they reach cells neighbouring mines which will show the appropriate values.

   ![Select Zero](readme_assets/features/demo-features/gameplay/selecting-zero.png)

   ![Show Zero](readme_assets/features/demo-features/gameplay/opened-zero.png)


   <br>

   ---

   #### Selected mine
   If a user selects a cell hiding a mine then they lose the game.
   The user will be given the game over screen, shown the full revealed board and given an input field to hit 'Enter' to start a new game.

   ![Select Mine](readme_assets/features/demo-features/gameplay/select-mine.png)

   ![Show Mine](readme_assets/features/demo-features/gameplay/show-mine.png)

   ---

   Consideration was made for using an image instead of a '*' on the board.
   To do this considered using the following Unicode Character ("\U0001F4A5") 💥

   However, as with the flag the unicode character took up 2 spaces on the board which did not look right as the rest was set up to deal with single characters. I considered changing the cell size on the board to accomodate this but this would have meant that either the 1 character numbers or the mine would have been slightly off center.

   In the end I opted to keep the '*' as I felt this was inkeeping with the games old school asthetic being a console game.


   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Win Game</summary>
   <br>

   Once the number of available spaces minus the number of mines is equal to the number of cells on the board the game will take a stop time,present the user with congratulations and update the google sheet with the users name, diffulty played and time.

   ___

   #### Imports required
   This win function requies an API link with google sheets to update the data recoreded with new winners.<br>

      import gspread
      from google.oauth2.service_account import Credentials

   The time is used to take a end time which is used in conjunction with the passed start time to calculate the came duration.
   Math import is used to round down seconds with math.floor. (The standard round function could round up to 60 which may result in a 0min 60secs time).<br>

      import time
      import math

   To format the title the pyfiglet is required.<br>
   
      import pyfiglet
      from pyfiglet import figlet_format

   ___

   #### Evaluating win status
   The win activities are triggered when the number of available spaces equalls the number of mines.

      if len(board.guesses) == (board.board_size ** 2) - board.no_mines:

   <br>

   ---

   #### Win layout
   The win page will inform the user of their time and let them know that the scoreboard has been updated.

   ![Win](readme_assets/features/demo-features/gameplay/win.png)

   ---
   

   <br>

   ---

   #### Update scoreboard
   The win game will call the upate scoreboard function.

      def update_scoreboard(data, level):
         print("\n................................................................................\n")
         print("\nUpdating scoreboard...\n")
         scoreboard_colate_data = SHEET.worksheet(level)
         scoreboard_colate_data.append_row(data)
         print("Scoreboard updated successfully\n")
         print("\n................................................................................\n")

   <br>

   ---

   </details>

   <details>
      <summary style="font-weight:bold">Validations</summary>
   <br>

   Validations have been added to the majority of the input fields to ensure that the game does not break and that the user is advised as to what error they have made when inputing data.

   All input fields use the .lower() function to allow the ability to check input regardless on case.

   Any input fields without restrictions (i.e hit 'Enter' to continue) do not have validations as the user can enter anything they wish and it will still work as required when they hit enter.

   ---

   #### Import required
   Validations use the colorama import to highlight the statements in bright red to stand out to the user.<br>
   I used the following tutorial to understand the use of colorama:<br>
   https://www.youtube.com/watch?v=u51Zjlnui4Y

   Note the colorama.init(autoset=True) automatically returns the text to it's default format after the colorama is applied to a string.

      import colorama #colorama tuorial
      from colorama import Fore, Style
      colorama.init(autoreset=True) 

   <br>

   ---

   #### Username validations
   The user name input must be at least one character long and not exceed 10 characters.
   The .strip() function has been applied to stop users from entering spaces as their only characters.

   ![No Entry](readme_assets/features/demo-features/validations/val-username-none.png)

   ---

   ![To Long](readme_assets/features/demo-features/validations/val-username-to-long.png)

   <br>

   ---

   #### Homepage validations
   If any input other than 'p', 'r' or 's' is entered the user will be informed that this is not a valid entry and provided feedback on what they entered.

   ![Not Valid](readme_assets/features/demo-features/validations/val-home-page.png)

   <br>

   ---

   #### Scoreboard Selection & Difficulty validations
   If any input other than 'e', 'm' or 'h' is entered the user will be informed that this is not a valid entry and provided feedback on what they entered.

   ![Not Valid](readme_assets/features/demo-features/validations/val-difficulty.png)

   <br>

   ---

   #### Gameplay validations
   When asked for coordinates, if the user enters letters, special characters or more/less than the 2 required coordinates the following error will show.

   ![Non Coordinates](readme_assets/features/demo-features/validations/val-coordinates-non-values.png)

   ---

   If the user enters coordinates outside the range of the board it will highlight this to them.

   ![Out Range](readme_assets/features/demo-features/validations/val-xy-out-range.png)

   ---

   ![Out Range](readme_assets/features/demo-features/validations/val-x-out-range.png)

   ---

   ![Out Range](readme_assets/features/demo-features/validations/val-y-out-range.png)

   ---

   If the user trys to select a cell that has already been revealed the following error message will appear.

   ![Already Dug](readme_assets/features/demo-features/validations/val-already-dug.png)

   ---

   If the user enters and invalid entry when asked if they wish to place a flag on the seleced cell the following message will show.

   ![Non Coordinates](readme_assets/features/demo-features/validations/val-flag.png)

   ---

   If the user enters and invalid entry when asked if they wish to dig on a flag cell the following message will show.

   ![Non Coordinates](readme_assets/features/demo-features/validations/val-dig-flag.png)

   <br>

   ---

   </details>
   
   <br>

# Further Development
   * Transfer to a more user friendly interface.
   * Interface allowing responsive design would allow custom difficulty where the user can specify the board size and number on mines they desire.
   * Potential to add other games and create a home page forgame selection.
   
   <br>

# Technologies Used

   ## Languages Used

   - HTML (not in scope but used to a minor extent)
   - CSS (not in scope but used to a minor extent)
   - Python


   ## Frameworks, Libraries and Programs Used

   1. Git:
      - Used for version control and to Push to GitHub.
   2. GitHub:
      - Used to store and share the code.
   3. Heroku:
      - Used as a platform to store and play the game.
   4. Figma:
      - Used to plan out website format.
   5. Web Developer:
      - Used to analyse HTML, CSS output and correct where required.
   6. Lucidchart:
      - Used to develop
         - mind map
         - process flow
         - function flow
         - class breakdown
         - priority matrix
   7. Google Sheets:
      - Set up API to update with user scores and feedback to the game.
   8. os module:
      - Used to clear console screen
   9. time module:
      - Used to time game
   10. math module:
         - Round down seconds
   11. random module:
         - Used to randomly place mines
   12. pyfiglet module:
         - Used to build aesthetically pleasing titles
   13. colorama module:
         - Used to color validations
   14. gspread:
         - Used to read and update google sheets
   15. google.oauth2.service_account:
         - Allow API link to google sheets using credentials

   See requirements.txt for versions of modules used.

   <br>

# Testing
   ## HTML Validation: 
   - HTML not in scope for this project.

   
   ## CSS Validator Results
   - CSS not in scope for this project.

  
   ## JS Validator Results
   - JS not in scope for this project.


   ## JS PEP8 Validation Results
   TO BE ADDED


   ## Testing User Stories From User Experience (UX) Section

   <details>
      <summary style="font-weight:bold">Developer Goals</summary>

   As the developer I want to create a simple and engaging game that is easy to use and will result in users returning to the site. 
   * Easy to use functionality.
      - **REVIEW - Simple intuitive inputs and eady to interpret content on the screen. Built without overcomplicating and game requirements.**
   * Addictive gameplay to encourage return users and drive positive word of mouth to encourage new users.
      - **REVIEW - Used feedback from testers to build a game which has been well received with testers re-using for their own enjoyment.**
   * Provide clear instruction as to the rules of the game.
      - **REVIEW - Specific section of the game dedicated to detailing the rules which is easy to navigate to. Aslo has an external video link providing further instruction if required.**
   * Set a range of difficulties to allow user progression and continued engagment.
      - **REVIEW - 3 game difficulties available to the user. Each difficulty has a diffent size of board and number of mines.**
   * Record winning scores based on difficulty and completion time to promote re-vistiation and competition between users.
      - **REVIEW - User name, game completion time and diffulctly recorded with the top 5 scores per difficulty fed back to the user in the form of the scoreboard.**
   * Build in flag functionality to allow users to mark cells they believe to have mines.
      - **REVIEW - This functionality has been built into the game. Each time a user makes a guess they are asked if they wish to place a flag. Flags will appear as a 'F'.**
   * Build a appealing user interface whilst observing the limitations of the project scope(command-line application).
      - **REVIEW - ASCII art, use of pyfiglet, a clear function using os and colorama to colour and brighted validations were used to make tha console game more appealing to the user. Selection options where spread over one line to give the impression of a games interface page.**
      **I also increased the console size to better accomodate the minesweeper board size.**
   ---
   </details>

   <details>
      <summary style="font-weight:bold">First-Time Visitor Goals</summary>
      <summary style="font-weight:bold">First-Time User Goals</summary>

   * Understand the purpose of the site.
      - **REVIEW - Very clear game purpose and easy to locate and read rules where required.**
   * Immediately engaged by easy to use yet challanging gameplay.
      - **REVIEW - Engaging gameplay and visuals developed based on user feedback to ensure an immediate and continued interest in the game.**
   * Invoke nosatalgia.
      - **REVIEW - The use of an old school console based interface works well with the retro gameplay of this classic.**
   * Simple intuitive menu navigation.
      - **REVIEW - Clear navigational instructions provided throughout the game with validation errors to aide the user if they enter invalid info.**
   * Rules easliy located and understood.
      - **REVIEW - Rules located in their own section with clear menu navigation leading to them.**

   ---
   </details>

   <details>
      <summary style="font-weight:bold">Returning User Goals</summary>
   
   * Use the scoreboard to improve their scores and compete with other users.
      - **REVIEW - Scoreboard set up using an API with google sheets to record the winning times by the user and present back the top 5 for each difficulty setting.**
   * Tailor the difficulty to their experience with the game.
      - **REVIEW - 3 difficulty settings created with varyious board sizes and number of mines.**

   </details>


   ## Further Testing
   * Tested across Google Chrome, Safari, Microsoft Edge, Fire Fox browsers on both Mac and Windows.
   * Gameplay and validations tested by developer and friends to ensure functionality worked as expected.
   * Issued to Slack community to review and provide feedback on.


   ## Development Bugs

   <details>
      <summary style="font-weight:bold">Add Value Function</summary>
   
   **Add Value Function Initial Issue:**<br>

   ![Add Value One](readme_assets/bugs/add-val/bug-add-val-one.png)

   When calling the cell check via a list call the min/max function duplicated checks when the cells were on the perimeter of the grid.

   If it was checking a -1 it would check as a 0 and then it would check the 0 again on the next loop.

   ___

   **Created a for loop to run through neighbouring cells:**<br>
   
   ![Add Value Two](readme_assets/bugs/add-val/bug-add-val-two.png)

   The issue with this fix was that it was searching for cells outside of the grid e.g. -1, -1. This resulted in it identifying mines at the end of the previous column.
   
   To resolve this, I looked to implement the min max function I used when searching list items in the previous code. This should work as it is setting a range not looking for specific items and therefore duplicating.

   ___

   **Marked up solution:**<br>

   ![Add Value Three](readme_assets/bugs/add-val/bug-add-val-three.png)

   Implemented the min max to the range to keep the review of neighbouring cells to within the grid coordinates. Needed to add +2 to the top limit as this would not be included (range goes up to top limit e.g. 1,10 goes 0-9.
   
   Used comments to check the progress of the code for each loop to easily identify issues and understand where to place the board update.

   ___

   **Working solution:**<br>

   ![Add Value Four](readme_assets/bugs/add-val/bug-add-val-four.png)

   Solution works as required.

   ___

   </details>

   <details>
      <summary style="font-weight:bold">Failure To Update requirements.txt File</summary>
   
   **Error experienced:**<br>

   ![Requirements.txt](readme_assets/bugs/requirements/requirements.png)
   
   I failed to update the requiements.txt file with the module i neede to run my code. As a result when it was uploaded and run through Heroku it gave the above error.

   Following a conversation with a Code Institute Tutor I realised my mistake and he showed me how to update this file automatically using the following comand:<br>
   pip freeze > requirements.txt

   ![pip3 freeze](readme_assets/bugs/requirements/pip3-freeze.png)
  
   <br>

   ___

   </details>

   <details>
      <summary style="font-weight:bold">Rules Title</summary>
   
   xxx

   ![xxx]()
  
   <br>

   ___

   </details>

   <details>
      <summary style="font-weight:bold">Username Accepted Space</summary>
   
   xxx

   ![xxx]()
  
   <br>

   ___

   </details>

   <details>
      <summary style="font-weight:bold">Scoreboard Presentation Issue</summary>
   
   xxx
  
   <br>

   **Code blocks detailing issue:**

   Python code:

      if len(user_name) > 0 and len(user_name) <= 10:
                while len(user_name) < 10:
                    user_name = user_name + " "

   </details>
   

   ## Key Learn
   The main key learn I took from this project was to build the readme file in conjunction with the website development.

   I was not sure if the design and functionality were feasible for the development of this project given my limited experience in CSS and JS. Therefore, I spent a lot of time building it in a test environment before deciding I could accomplish the desired result.

   By the time I had realised it was feasible I had completed a lot of the work. As a result of this I had to retrospectively complete sections of the readme file which would have been better suited to completing at the scoping, researching and initial build stages.

   Despite this I feel that I did a good job recording my progress through easy-to-understand concise commits which made it easier to revisit certain elements of the project where necessary.

   <br>


# Deployment
   ## Set Up Local GitHub Repository
   1. Go to https://github.com/Code-Institute-Org/gitpod-full-template.
   2. Select use this template.
   3. Add repository name within my GitHub. (This will generate a repository in my Git Hub with the appropriate files.)


   ## Repository Framework
   1. Select the repository on GitHub and open with GitPod (green button).
   2. Create required html page.
   3. Create assets folder.
   4. Within assets folder create CSS folder, images folder, JS folder & readme-assets folder.
   5. Add required files to folders including style.css, images, script.js, etc.


   ## Update Repository
   1. When adding a new feature create a separate branch to work in safely typing into the terminal "git branch 'name of required feature/update'".
   2. Checkout the branch with "git checkout 'name of required feature/update'".
   3. Make updates and test using "python -m http.server".
   4. Once testing is complete add to Git staging area using "git add ."
   5. Commit the changes and add a useful explanation of what action was done to track the history in GitHub using "git commit -m 'explanation of update'".
   6. Once the feature is complete, fully tested, and ready to be added to the main branch first go to the main branch using "git checkout main".
   7. Merge the feature branch into the main using "git merge 'name of required feature/update'".
   8. Confirm merge was successful and then if it is not going to be re-used delete the feature branch using "git branch -d 'name of required feature/update'". (If deleting a branch with commits not merged to main delete with -D instead of -d)
   9. Use "git push" to push the commits to GitHub. These will then appear in the live website if it has been set up in GitHub Pages.


   ## GitHub Pages
   Deploy in GitHub Pages:
   1. Log in to my GitHub and go to my appropriate repository.
   2. Access settings.
   3. Under 'Code and Automation' go to pages.
   4. Leave the source as Deploy from Branch.
   5. Set Branch to Main.
   6. Save.
   7. Give GitHub a few minutes and the live URL is provided at the top of the GutHub Pages section of settings.
   8. Any Git Pushes from the terminal whilst working on the repository using GitPod will now update in this live site.

   <br>


# Credits
   ## Development Resources
   The following sources acted as guidance for understanding. No code was taken directly for use in this project.


   * Learning how to use linear gradients. This was used to develop the look of a notepad with re-occurring lines. (https://www.w3schools.com/css/css3_gradients.asp), (https://codepen.io/ceg9498/post/creating-lined-paper)
   * FlexBox guidance/re-fresh. (https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
   * Intro to canvas in JS to create the hangman image. (https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
   * Canvas responsive. (https://stackoverflow.com/questions/34772957/how-to-make-canvas-responsive)
   * Clearing the canvas. (https://stackoverflow.com/questions/2142535/how-to-clear-the-canvas-for-redrawing)
   * Understanding event listeners. (https://www.w3schools.com/js/js_htmldom_eventlistener.asp)
   * Change mouse pointer on hover for menu list items (https://www.w3schools.com/cssref/pr_class_cursor.asp)
   * Understand the toggle class method to utilise in menu activation. (https://www.w3schools.com/howto/howto_js_toggle_class.asp)
   * Set JS rules dependent on-screen size. (https://www.w3schools.com/jsrEF/met_win_matchmedia.asp)
   * Wrap entire game in an initialise function to eliminate global variables. (https://www.youtube.com/watch?v=_4V4yUxGng8)
   * Stack Overflow used for generalised queries during development.


   ## Media Resources
   * All images were obtained from Unsplash.
      - Image for the background wood effect (jon-moore-5fIoyoKlz7A-unsplash.jpg).
      - Image of the mountain doodle which shows on large screen viewings (nicolas-pinilla-GcDr6ZIzbIw-unsplash.jpg).
   * Audio was taken form YouTube videos
      - Sound on correct answer. (https://www.youtube.com/watch?v=403gX7TnhTQ)
      - Sound on incorrect answer. (https://www.youtube.com/watch?v=RZEsfS1rGyY) - modified using Audacity
      - Sound on getting word correct. (https://www.youtube.com/watch?v=ytjxf9YNJ-0) - modified using Audacity
      - Sound on getting word incorrect. (https://www.youtube.com/watch?v=na-a3lLB13Q&t=16s) - modified using Audacity


   ## Acknowledgements
   * Thank to my Mentor (Spencer Barriball) for his feedback and guidance.
   * The Code Institute Slack community for helping with any and all queries.