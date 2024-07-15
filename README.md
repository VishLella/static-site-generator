
# Static Site Generator

This project is a static site generator which takes in one or multiple markdown files (.md) and converts them into html files to be displayed staticly on a web browser. The project handles different features such as links, images, code blocks, titles, lists, text italics/bolding, and nested blocks. 

## Table of Contents

- [Features](#features)
- [Directory Structure](#directory-structure)
- [Setup and Usage](#setup)

## Features
- **Markdown to HTML Conversion**: Converts Markdown files into HTML documents using a customizable HTML template.
- **Static Asset Management**: Copies static files (such as CSS, images) to the deployment directory.
- **Recursive File Handling**: Processes files within directories recursively.

## Directory Structure

```
Project Root
├── content                    # Directory for markdown content files (Contains demo files)
│   ├── index.md
│   └── majesty
│       └── index.md
├── public                     # Output directory for generated HTML files
│   ├── images
│       └── rivendell.png
│   └── ...
├── README.md                  # README file
├── src                        # Source files for the project
│   ├── block_functions.py
│   ├── html_node.py
│   ├── leafnode.py
│   ├── main.py                # Main script
│   ├── markdown_functions.py
│   └── text_node.py
├── static                     # Directory to store static assets
│   ├── images
│       └── rivendell.png
│   └── index.css
├── test                       # Directory with test cases
│    ├── test_block_functions.py
│    └── ...
├── main.sh                    # Shell script to run the main.py
├── template.html              # HTML template file
└── test.sh                    # Shell script to run tests
```

## Setup and Usage
- Clone Repository
- Give permissions to run scripts
- Run testing script to make sure project is working smoothly
- Run main script to execute the program 
```
git clone <>
cd static_site_generator
chmod +x main.sh test.sh
./test.sh
./main.sh
```
