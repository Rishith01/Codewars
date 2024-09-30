# Codewars

This repository contains the work done as part of the Codewars competition organized by the Web and Coding Club, IIT Bombay, in March 2023. The competition focused on developing strategies for an autonomous, real-time game involving resource management and island capture. My team consisted of Arijit, Deepan and Affaan.

Game Description
The game takes place in a 2D arena with a frame size of X×Y, where the objective is to capture one of the three islands located on the map. To win, a team must hold control of an island for 100 consecutive seconds while defending against rival teams and managing limited resources.

Objective:
Each team starts from opposite ends of the map and must capture an island by occupying it for 100 consecutive seconds.
The map contains 3 islands, each with a size of 3×3 tiles.
Pirates can be spawned to help defend the islands or attack opponents.
Resources:
Rum: This resource spawns only once during the game and is used to spawn pirates that fight on the team’s behalf. Pirates from the same team work together to defend islands or attack enemies.
Wood: Wood can be collected from the sea and is used to create temporary defenses around the islands. It replenishes over time, so players must manage its use wisely.
Gunpowder: Gunpowder is required to kill enemy agents. Like wood, gunpowder is collected from the sea and replenishes periodically. Teams need to balance their usage of gunpowder for both offense and defense.
Gameplay Mechanics:
Island Control: To take control of an island, a team must occupy it without being displaced by enemy players or pirates for 100 consecutive seconds.
Resource Gathering: Resources such as rum, wood, and gunpowder are scattered in the sea surrounding the islands. Teams must send agents to gather these resources while defending their islands from attacks.
Pirate Deployment: Pirates, once spawned using rum, help defend islands and attack enemy players. Pirates from the same team collaborate to increase the team's defensive and offensive capabilities.
Dynamic Resource Management: While rum spawns only once, wood and gunpowder replenish over time. Teams must constantly balance resource collection, defense, and attacks to succeed.
Starting Conditions:
Each team starts from opposite directions on the map and must quickly strategize how to gather resources, control islands, and deploy pirates to outmaneuver their opponents.
This repository contains:

Strategy Code: Defines the behavior of autonomous agents and pirates.
Simulation Logs: Provides game replay data for analysis.
Documentation: Detailed rules and strategies developed during the competition.



