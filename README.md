# Minimax Search Animations with Manim

## General
* Animations using the python library [Manim](https://www.manim.community/), created for an educational capsule on minimax search.
* Explanations and examples heavily based on Chapter 6 of the book by Russel & Norvig: [Artificial intelligence: A Modern Approach](http://aima.cs.berkeley.edu/).

## Compilation

### Step 1: Prepare Your Python Animation File

First, you need to write your animations in a Python file. This script includes the code to create your animation. In our example, this file is `pseudocode_scene.py`. Replace it with the name of your Python file.

### Step 2: Understanding the Flags

The Manim command comes with several flags that help you customize the output video. In our example, we have used the `-qh` flag.

`-qh` sets the quality of the output video. It has options like `l` for low quality, `m` for medium quality, `h` for high quality, and `p` for production quality (the highest).

Make sure to replace these flags according to your requirement.

### Step 3: Name of the Output Video

Lastly, you need to name the output video. In our case, it's `PseudoCode`. Replace it with the name you want your output video file to have.

### Step 4: Executing the Command

After setting all the parameters, execute the command in your terminal:

```
manim -qh pseudocode_scene.py PseudoCode
```
