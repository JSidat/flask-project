# QAC Fundamental Project


## Table of contents

* [Introduction](#Introduction)
* [Project Scope](#Project-Scope)
* [Technology constraints](#Technology-constraints)
* [Entity Relationship Diagrams](#Entity-Relationship-Diagrams)
* [Risk Assessment](#Risk-Assessment)
* [Deployment](#Deployment)
* [Testing](#Testing)







## Introduction

The purpose of this project was to create a 'CRUD' application whilst utilising the tools tools, methodologies and technologies that were taught in the modules in this Enable DevOps course.


## Project Scope

The scope of the project outlines the minimum requirements to successfully complete the project and assesses our development against SFIA.
The minimum requirements for the project are outlined as follows:

* Project Tracking via a kanban style board such as trello that identifies the user story, use cases and progression of the project over a period of time.

* A relational database containing a minumum of two tables with some sort of relationship to store data generated in the application. 

* Documentation showing the structure of the project and as well as a risk assessment.

* A functional CRUD application developed in python following best practices.

* Fully comprehensive test suite with high test coverage of the back end with reports and evidence of testing results. Also needs to include automated validation testing for the application.
  
* A functioning front-end website that has full CRUD functionality.

* Use of github as the version control system using the feauture-branch model to fully integrate the code for the application.

## Technology constraints

The technology required to build the application were discussed during the training for this project and following technologies were to
be utilized to complete the project:

* Kanban style board(Trello board)
* GCP SQL database
* Programming language: Python
* Unit testing: Pytest
* Front-end: Flask(HTML)
* Version control: Git
* CI server: Jenkins
* Cloud server: GCP

## Project Management
 In this section I will be outlining the tools and methodologies used to keep on track with the project and cater for any changes that had to be made as the project progressed. Proper planning is imperative to make sure any unexpected occurences can be dealt with appropriately without negatively affecting the quality of the product.

### Agile methodologies
The agile methodology promotes thorough and constant communication ad breaking the project into several stages which arent dependant on each other in a linear fashion. This allows for flexibility when it comes to sudden changes to the project specification. The cycle of planning, executiing and evaluating that agile is based on, allows for top quality work to be produced in a timely manner.

Being a solo project some of the principles and methodologies had to be adapted to cater for the independent nature of the project:

* Individuals and interactions over processes and tool: this didnt apply to me as the project was a solo project. However we still conducted morning briefs and daily stand-ups to gain a good understanding of whatwas required on a daily basis.

* Working software over comprehensvie documentation: The purpose of the SFIA1 project is to test our porgramming skills and we were ultiamtely being tested on how well our applications worked and if they met the requirements set out in the project scope.

* Customer collaboration over contract negotiations: This part was not really applicable but I made the project with an intended end user in my mind, as shown through user stories.

* Responding to change over follwoing the plan: The direction my project went in was a slightly different to what I intended at the start but careful planning allowed me make these changes without affecting my overall performance.

### Kanban Board

A kanban style board was used to plan the project and layout my user stories and tasks. At the academy, we were introduced to the Trello board as a tool to plan the project, so this was the project planning tool that was used throughout the project.  

User stories are defined on the board. A product backlog based on these user stories is created from which tasks are created and completed with an ultimate objective of meeting the requirements set out in the user stories by adding all the relevant functionality and features. The board allows you to slide tasks form left to right as you start, progress and complete it and gives you a visual representation of your tasks and progress.

My definition of 'done' was the correct implementation of a feature or function where the feature ran without any bugs or issues and added the fucntionality that it was intended for.

#### Initial Kanban Board

For the intial Kanban board, a list was created that outlined the user stories for the project and the purpose for the productoin of the applcation. MoSCoW prioritisation was also used on the board. Anything marked with a red label was high priority and directly related to producing the minimum viable product, which in the grand scheme of things was the most important milestone to reach through the whole project. Marking these tasks allowed me focus on them and complete the minimum requirements for the project before moving onto other features and tasks.

![Initial Kanban Board](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-21.png)


#### Final Kanban Board

As the final Kanban board shows, the high priority jobs were completed which in turn meant the minimum requirements for the project were completed. The application had complete CRUD funtionality with a relational database to effectively store the relevant data from the application.

![Final Kanban Board](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-24.png)


### Entity Relationship Diagrams

Entity relationship diagrams were used to plna and set out the databases for the project and show the type of relationships between the tables in the database. 

#### Initial ERD

My initial plan was to make an app that that had more than stored data of users, lists of exercises and their properties, list of workouts and their properties and all the set data from each exercise logged(number of sets, reps in a set, weight of each set.)

![Initial ERD](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-24%20(3).png) 

#### Final ERD

As the project progressed, my idea evolved from being a bodybuilding app to a powerlifting app where the main difference was that each workout only has one exercise. As a result, my database did not require tables for sets and reps as powerlfiters are only interested in a 1 rep set of the maximum amount of weight they can lift. My final ER diagram contained a table to log workouts and a pre-populated table of exercises that the user can choose from via a drop down menu on the add workout page. 

![Final ERD](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-24%20(2).png)

### Risk Assessment

The risk assessement allows for planning of possible events that could occur that negatively impact the project and stop someone from completing any part of a job. It outlines event or risks that could potentially occur whilst working on a project. It also briefly explains what the consequence of the risk would be. The deductions section of the risk assessment puts forward possible actions that can be taken to counter the risk and neutralise any issues the risk might cause. The outcome section is a follow up on deductions and tells us what we expect to happen if we carry put the correct precautionary measures to stop the risk from occurring. Each risk was plotted on a matrix where two factors were taken into account, the severity of the risk, and the likelihood of the risk occuring. Any risk that had a high possibility of occurence coupled with high severity would be plotted in the red area of the colour coded matrix. Any risk placed in the green is likely to be something that is tolerable and won't have huge negative impact on the project. 

![Risk Assessment](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-25.png)

### Unit testing

Due to time constraints, only unit testing was carried out in the project. Pytest was used for unit testing. Tests were written to see if each page was accessible and tests were also written for each part of the CRUD functionality. The final coverage report showed that 89% coverage was achieved, with around 8 lines in the routes file unaccounted for. 

![Unit testing](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-25%20(1).png)

### Deployment

A webhook was created on github that triggered the CI server Jenkins whenever anything was pushed up to github. Jenkins would then be able to deploy the app as a service. There was a slight issue with jenkins where the build would hang, but the app would still run. Whenever the build was successful, it would show an error message suggesting the secret key had not been exported even though the command to export the secret key was in the command shell on jenkins, so this is an issue that needs further investigation.

#### CI pipeline

![CI pipeline](https://github.com/JSidat/flask-project/blob/master/Screenshots/2020-05-25%20(2).png)

### Areas for improvement

Having had no previous experience in IT I wanted to focus all my attention on the modules that have been tsught over the last 5 weeks. As a result the front-end design was neglected, so this is an area of improvement. As my skills improve I would like to add some additional functionality to the website and look forward to working on it and developing it further. Further testing is necessary and integration testing could be carried out to see how all the different parts of the app work together as a whole. A few issues on the deployment side of things and jenkins need addressing as well. A user/login functionality would also work well on an app like this as it would me the app more personal and possibly customizable. 

### Conclusion

The project was thoroughly enjoyable and over the last 5 weeks, has given me a well-rounded perspective and understanding of how this sort of web application works and the importance of each component of the project. It has also showed me the tools required and how these tools work in synergy. The project management modules gave me a good understanding of the agile methodology and why it is beneficial in a DevOps environment, and where applicable, helped me to plan and deliver my project. The project as a whole was very enjoyable and challenging and gave me a small taste of the kind of mindset and work ethic required in this profession and I look forward to building on this foundation and continuing to challenge myself.

### Acknowlegements

I'd like to thank all the trainers who have taught me over the last 5 weeks for working tirelessly and being so receptive and patient with us and given us all the tools and information for us to complete the project.










