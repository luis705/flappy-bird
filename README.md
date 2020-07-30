<h1 align='center'>Flappy Bird</h1>

---

<p align="center">
  A flappy bird clone made both for playing and for training a NEAT neural network
</p>

<p align="center">
	
  <a href="https://github.com/luis705">
    <img alt="Made by Luis Otávio" src="https://img.shields.io/badge/made%20by-Luís%20Otávio%20Amorim-brightgreen">
  </a>

  <img alt="Last Commit" src="https://img.shields.io/badge/last%20commit-july%202020-yellowgreen">

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">
</p>

---


# Table of Contents
<ul>
	<li><a href="#-getting-started">Getting Started</a></li>
	<li><a href="#-features">Features</a></li>
  	<li><a href="#-controls">Controls</a></li>
</ul>

---

# 🚀 Getting Started</h1>
<h2> Prerequisites </h2>

<h3>Clone</h3>
<ul>
	<li>Clone this repo using in the terminal:
</ul>

```
git clone git@github.com:luis705/flappy-bird.git
```
<h3>Install python</h3>
<ul>
	<li>Windows
		<p>Go to <a href="http://python.org/download">python.org</a>, download the installer and run it.</p>
	</li>
	<li>Linux
		<p>Type on terminal:</p>
	</li>
</ul>

```
sudo apt-get install python3
```

<h3>Install required packages</h3>
<p>Open the terminal and run</p>

```
pip install pygame neat-python
```


<h2>Using</h2>
<p>To play the game just open the terminal inside the game folder and run main.py with</p>

```
python3 main.py
```
<p>To see the training of the neural network run the ai.py filey</p>

```
pythohn3 ai.py
```

---

# 📋 Features</h1>

- [X] Flappy bird game
- [X] Neural netowrk using NEAT

<h2> Built with</h2>
<ul>
	<li>Core
    		<p>
			<a href="python.org">Python</a> - a easy to learn, but powerfull programming language
		</p>
  	</li>
  <li>Graphics
    <p>
      <a href="https://pygame.org">Pygame</a> -  
      a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library.
    </p>
  </li>
  <li>Neural Network
    <p>
    <a href='https://neat-python.readthedocs.io/en/latest/'>Neat-pythohn</a> - 
      a pure Python implementation of NEAT, with no dependencies other than the Python standard library.
    </p>
</li>
</ul>
	
--- 

# 🎮 Controls</h1>
<h3>Playing</h3>
<ul>
  <li>Spacebar: jump</li>
  <li>R: restart after death</li>
</ul>

<h3>Neural network</h3>
<ul>
  <li>After 100 generations their data will be saved on scores.json</li>
</ul>

<h3>


---

# 📝 License </h1>

<img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">

This project is licensed under the MIT license - see the <a href="https://github.com/luis705/flappy-bird/blob/master/LICENSE">LICENSE</a> file for details
