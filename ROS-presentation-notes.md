# Presentation on ROS

## Potential Topics to cover:

```

    What is ROS?
    History of ROS
    Learning ROS (It's BIG)
    Gazebo simulation
    RVIZ visualization
    Ready to use algorithms for
        SLAM
        Localization
        Mapping
        Path planning
        Sensor fusion
    Interprocess Communication
        Processes (Nodes) exchange Messages by publishing and subscribing to Topics
        Actions
        Services
    Interface to the physical hardware
        sensors
        actuators
    Using pigpio
        Interrupt speed on all GPIO pins
        Precise PWM
    Installation on Ubuntu 20.04 LTS
        Full Desktop installation
        Core install (headless)
    Packages & Workspaces
    Building the actual robot
    Programming the nodes (mostly in Python)
    Resources
```

### Background
* I've always enjoyed building things, (with an Erector set as a kid)
* Computers are new. When I was in college, I used a slide rule. The HP35 came out for $350.
* I deemed at the time that computers were **toys**.
* At some point, computers became useful to me:
    * 3D CAD made it possible to "buiild machines" virtually.
    * At Kodak we used UG, but in the RL, we had a policy of eencouraging a wk or two of training / yr
    * so I sent myself to training in HPUX, networking, HP CAD
* linux happened
* learned PYthon

### In retirement, I still enjoy building things.
* Build something new & useful that uses what I already know but extends my knowledge incrementally.
* have built a few wheeled robots, each time building from scratch, but extending my technical knowledge.
* I found myself building the lidar from scratch and inventing algorithms to navigate through the envrionment.
* I had heard of SLAM but didn't know how to incorporate it
* I had heard of ROS but didn't know exactly what it was or whether I needed it.
* Learning ROS turns out to be a "chicken or egg" dilema... For me, at least. It can be kind of dry learning about how it works without being able to see stuff happening on a robot. But in order to see stuff happening on your own real robot, you have to already know ROS pretty well.



* According to [Wikipedia](https://en.wikipedia.org/wiki/Robot_Operating_System), ROS is an open-source robotics middleware suite.

* ROS is not an operating system. It is an open-source software framework that allows all the sensors, motors and actuators on your robot to talk to each other through any number of computers. Oh and by the way, ROS implements a large collection of algorithms and tools so you don't have to write them from scratch.

* My goal in this talk is to give you a feel for what ROS is and what it does. My approach is to share with you my own path of discovery. [Here](my-relationship-with-computers.md) I reminisce a bit as I describe my relationship with computers early in my career.

But if we fast-forward, it might be enough to know that I moved to Florida in 2017, bringing with me a background knowledge in:
* Mechanical Design / Engineering
* Linux OS
* Python
* Raspberry Pi

In 2019, on a summer trip back North, I found myself with some spare time and learned Git.
(It seems to be a pattern with me that I undertake big projects when I am away from home and without my usual routines.

* Here is an incomplete list of some of the things that ROS provides:
    * Coordination of multiple processes (nodes) running on multiple computers
    * message-passing between nodes
    * command-line tools
    * services & actions
    * simulation 
    * hardware abstraction 
    * low-level device control
    * Implementation of commonly used algorithms such as:
        * Sensor Fusion
        * SLAM (Simultaneous Localization And Mapping)
        * Navigation and Path Planning
    * visualization tools
    * package management

* As a hands-on (retired) mechanical engineer, the description given above didn't bring me to a point where I could say "Oh, I see! It's all quite clear now."

Instead, I had to follow a step-by-step process, gradually coming up the learning curve.

1. Learn the basics of ROS
2. Learn the basics of Robot Navigation
3. Install ROS on my computer (In my case: a Raspberry Pi)
4. Build the simplest possible ROS autonomous mobile robot
5. Get the robot working in teleop mode
6. Get the robot working under control of ROS navigation 

# Outline of Presentation

## Intro

* Introduce myself
* Explain what will be covered in today's presentation

Today, I will take you along my learning path and hopefully, as you follow along, you will end up with a pretty good idea of what ROS is.

## Overview of Some Simple Robots I have built

* Tele-Operation (manually coontrolled)
* Line following
    * Tape on the floor
    * Dots on floor
    * Grout lines on the tile floor
* Wall following
    * Distance sensor to navigate around the Kitchen Island
* GPS following
    * drive to GPS waypoints on the driveway
* Map Following (using Lidar)
    * Drive a path through the house

## What is ROS? And why would you want to use it on your robot?

* ROS is more of a **middleware** than an OS. It currently runs best on Ubuntu Linux.
* Open Source
* Has become a defacto standard within the robotics community
* ROS is a s/w framework that handles communication between s/w components called **Nodes**.
* Nodes can be stopped and started on the fly, allowing you to make changes or substitutions while the rest of the robot is still running
* Nodes can run on more than one computer, allowing for
    * distribution of the processing load
    * collaboration between robots.
* The way it works is that **roscore** node is started first, then
    * new nodes register themselves with roscore, specifying **topics** on which they will broadcast or publish messages
   * Roscore provides a kind of directory, referring nodes wishing to subscribe to a particular topic to the publisher.
* In addition, roscore serves as a master clock, parameter server, and package manager
* [Package management](http://wiki.ros.org/Packages) in ROS
    * Software in ROS is organized in packages.
    * A package might contain
        * ROS nodes,
        * a ROS-independent library,
        * a dataset,
        * configuration files,
        * a third-party piece of software,
        * or anything else that logically constitutes a useful module.
    * The goal of these packages is to provide this useful functionality in an easy-to-consume manner so that software can be easily reused.
    * In general, ROS packages follow a "Goldilocks" principle: enough functionality to be useful, but not too much that the package is heavyweight and difficult to use from other software.

    * Packages are easy to create by hand or with tools like `catkin_create_pkg`.
    * A ROS package is simply a directory descended from ROS_PACKAGE_PATH (see ROS Environment Variables) that has a package.xml file in it.
    * Packages are the most atomic unit of build and the unit of release.
* ROS provides lots of command line tools
* ROS provides many pre-built packages incorporating sophisticated algorithms. No need to code them from scratch.
    * Sensor Fusion
    * Co-ordinate frame transformations
    * Mapping [mapping video](http://wiki.ros.org/rplidar)
    * Localization
    * Autonomous Navigation / Path Planning
* ROS also comes with tools for
    * Graphing system configuration
    * Plotting message values
    * Visualization of entities in 3D space
    * Troubleshooting
    * Simulation
        * You don't even need to have a real robot!

## My ROS Learning Path
* I started without a real robot.
    * I actually started without even having ROS installed on my computer.
    * I was visiting friends & family up North last summer and signed up for online ROS training course: **ROS in 5 Days**
        * It actually took me more like 5 weeks to get through it
    * Next I took the online course: ROS Navigation in 5 Days
* I then decided it was time to wean myself from the online environment and install ROS locally
    * I hoped to be able to install on a Raspberry Pi 4 (8 GB ram)
    * Overview of how **ROS versions** are linked with **Ubuntu LTS** versions
        * [ROS Releases linked 1:1 with Ubuntu LTS releases](http://wiki.ros.org/Distributions#Release_Schedule)
        * [List of ROS distributions](http://wiki.ros.org/Distributions#List_of_Distributions)
        * [Ubuntu LTS distributions](https://ubuntu.com/blog/what-is-an-ubuntu-lts-release)
* Spun up on some ROS tutorials
* Decided to make my own robot
    * Details of this process....

    
## Learning resources:
* Book: Practical Robotics in C++ by Lloyd Bromabach, published: 2019
* Check out [A Gentle Introduction to ROS article on Medium](https://medium.com/swlh/a-gentle-introduction-to-using-ros-on-your-robots-329aa5e261d1).
* [Automatic Addison]()
* [Robot Ignite Academy]()
