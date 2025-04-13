# **workEX: Your Personalized Workout Tracker and Fitness Companion**

## Overview

**workEX** is a comprehensive web app designed to help users track and manage their workout routines with ease. It features an interactive interface that allows users to log, track, and analyze their fitness progress. The app offers a variety of tools to ensure a personalized fitness journey, including workout tracking, progress monitoring, workout suggestions, and more.

## Features

- **User Authentication**: Secure login and logout functionality.
- **Workout Tracking**: Track your workouts with detailed information, including exercise type, sets, reps, and weight.
- **Progress Monitoring**: Visualize progress through graphs and statistics, allowing you to track improvements over time.
- **Workout Suggestions**: Get personalized workout suggestions based on your fitness level and goals.
- **Dark Mode**: Toggle between light and dark modes for a more comfortable user experience.
- **Responsive Design**: Optimized for desktop and mobile devices, ensuring a smooth experience across all platforms.
- **Privacy and Terms**: Access to the privacy policy and terms of service pages to ensure user data protection.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask framework)
- **Database**: JSON (workEX_workouts.json for storing workout data)
- **Styling**: CSS (workEX.css)
- **Interactivity**: JavaScript (workEX_progress.js, workEX_workout.js)

## Folder Structure

/WORKEX
├── /data
│   └── workEX_workouts.json
├── /static
│   ├── /CSS
│   │   └── workEX.css
│   ├── /images
│   │   └── workEX.jpg
│   └── /js
│       ├── workEX_progress.js
│       └── workEX_workout.js
├── /templates
│   ├── workEX_base.html
│   ├── workEX_contact.html
│   ├── workEX_darkmode.html
│   ├── workEX_index.html
│   ├── workEX_logout.html
│   ├── workEX_privacy.html
│   ├── workEX_progress.html
│   ├── workEX_settings.html
│   ├── workEX_terms.html
│   └── workEX_workout.html
├── workEX_README.md
├── workEX.env
├── .gitignore
└── workEX.py