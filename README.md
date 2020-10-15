# CSS Property Alphabetizer

## Purpose
This script creates new a CSS file with alphabetically sorted properties. 
It does not sort selectors.
It works well with my personal styling preferences and is not bug-proof, use at your own risk.

## Usage
    py CSSPropertyAlphabetizer.py FILE.css
Will create alphabetized-FILE.css

## Example
### *style.css*

    input[type=text] {
        background-color: red;
        color: red;
        border-radius: 5px;
    }

    #someId {
        z-index: -1;
        position: relative;
        height: 50px;
    }

### *alphabetized-style.css*

    input[type=text] {
        background-color: red;
        border-radius: 5px;
        color: red;
    }

    #someId {
        height: 50px;
        position: relative;
        z-index: -1;
    }