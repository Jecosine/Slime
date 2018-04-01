# Slime
Game engine on linux console(impleted by python)

## Introduction

Slime now is a basic game structure which runs on linux terminal.It impletes some convenient methods and tools which may fit your bills when developing a game that runs on terminal(like snake).It is developed in python so that the origin code of the structure is opensource.Any suggestions and critises are welcome,and I will try my best to make optimations.
When it come to the principle of the structure, I use some function string which is built in linux(like `ESC[2J` etc.) to imitate the move of 'pixel'.Of course 'pixel' is not referred to the smallest renderer of screen, it is to say the char on screen.
The structure aimed at making development on commandline game less difficult, but as a student ,I am worried about quality of my codes and the effeciency of my program. So, I will appreciate it if you can point out somewhere to improve.

## Usage

The essenial of the structure is these three files:
<ul>
<li><b>GameObject.py</b>: It contain two class to implete the base element of game. The first one is <code>class Object</code>, it offer some behaviors to work ,and contain some basic attributes like <code>self.isEmpty</code>.The other one is <code>class pixel</code>.The different between the two is that:The Object is working with game logic,and usually participated in coordinate calculations directly wherear the pixels play a vital role in rendering.So, the logic is Object can contain pixels, and pixel links with a char on screen.When you want to create a unempty object, you should use <code>Object().add_pixel(...a list consisted of pixel()...)</code> to add pixels to the object.Don't forget to init pixels' position when initial them.</li>
 </ul>
