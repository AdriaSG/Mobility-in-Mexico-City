# Mobility Analysis Tool (Mexico-City)
### General 
This application is the demo por a geospatial analysis tool applied to data from Mexico City. The website allows user to interact with 3 main maps: 1) Public transport: user can see subway, bus and bicycle stations as well as bicycle lanes, 2) Traffic during the day: showing aggregated data from Uber Q1 2020 to visualize traffic density in the city along the day and 3) Mobility Paths: where user visulizes most traveled paths across clutered districs in the city. All maps are interactive but with static data. 

If I would get Edlich's investment, the application would grow an duser will be able to create their on maps adding different layers, filters and slicers to be complete visualization tool for urban data. 
### Prerequisites
Pandas
Shapely 
Kepler gl


## 2 Unified Model Language
For the UML digramas I chose to present the following:
1. [Use Case diagram.](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/Use%20case%20diagram%20-%20Urban%20Technology%20app.png) Extending the cases to the functionalities that I would include later in the web-tool.
2. [Activity diagram.](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/Activity%20diagram%20-%20Urban%20Mobility%20app.png) Walks through the main activities that could be done in the complete idea of the tool.
3. [Sequence diagram.](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/Sequence%20diagram%20-%20Urban%20Mobility%20app.png) Shows interactions (calls and responses) between main components and the user. 

## 3 DDD 
For the [Domain Driven Design diagram](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/DDD%20-%20Urban%20Mobility%20app.png), I had sketched what would be the complete problem space for the application as starting point while drafting the general goal of the application. There could be found several different subdomains, components and features that either had been implemented or would be implemented in the future to deliver promised value to the end-user. The DDD diagramp is also mapping the up and downstream relations as well as key partnetships for the application to work properly. Furthermore I had created an small [glossary](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/Glossary.md) containing ubiquitous language for each domain, this would allow a better understanding of the architecture and code.

## 4 Metrics
For metrics, I chose Sonarqube online version because it's much easier to integrate with your repository that running a local server. In general the code looks good, there were found lot of duplications because the html maps contains fixed data inside that might be counted as duplicates, to avoid this warning false positives rule could be set up. Please fin screenshot [here](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/Sonarcloud_screenshot.png)

## 5 Clean Code Development

## 6 Build Management
For build management I had used pybuilder, which is a powerful tool when using python. You can fin 3 files created for this purpose:
- [build.py](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/src/build.py)
- [setup.py](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/src/setup.py)
- [pyproject.tolm](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/src/pyproject.toml)

After configured the files, if I run pyb from cmd the [build start running](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/Buildpy_screenshot_screenshot.png)

## 7 Unit-Tests

## 8 Continuous Delivery
I used Git Actions to create the continious delivery pipeline (file found [here](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/.github/workflows/python-app.yml) and screenshot of sucessful integration [here](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/CDransuccessfully_screenshot.png) by default the workflow builds the following tasks:

- set up ubuntu environment
- set up Python with Version 3.8
- installs or upgrades pip
- installs or upgrades flake8
- installs (if provided) the requirements.txt
- checks if there are syntax errors in python
- run unit tests

I also tried to use TravisCI to explore the tool, however I got the error "We are unable to start your build at this time. You exceeded the number of users allowed for your plan. Please review your plan details and follow the steps to resolution." which I was unable to resolve yet. 

## 9 IDE
I had used [PyCharm 2021.3.2 (Community Edition)](https://github.com/AdriaSG/Mobility-in-Mexico-City/blob/main/tasks/PyCharm_asIDE.png) using Anaconda Python 3.8 as interpreter. I find very useful to use it this way for an easier environment and package management even if I deside to use other tools like Jupyter Notebook or Google collab, Anaconda as interpreter will save time not having to install save packages everywhere. The integration with Git using this IDE was straight forward and I was able to commit, pull and push updates without facing an issue, would be interesting to start trying it with multiple branches for more complex project.

Another feature I like very much about this IDE, is the new package manager for PyCharm that allows you to install and update packages within few click, no pip is needed. My most used shortcuts are:
1. Ctrl + K to show commit window 
2. Ctrl + Shift + C to cpy document path 
3. Alt + Shift + F9 to run selected 

Out of curiosity, full short-cut list could be found [here](https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf)

## 10 DSL

## 11 Functional Programming
