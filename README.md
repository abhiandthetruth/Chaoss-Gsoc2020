# Chaoss-Gsoc2020
Gsoc2020 microtasks for Chaoss-grimoire lab

# Idea
[Implement the Social Currency Metrics System in GrimoireLabs](https://github.com/chaoss/grimoirelab/issues/288)

# Summary
Following is a precise definition I have tried to form for Social currency based on my knowledge followed by a description of terms used in the definition.

“Social currency of a social entity is the tuple of the values of the different parameters defined in a codex assigned to that particular entity by an established assignment function.”

* The codex must be accepted as a standard by the people using the system. 
* The values to the parameters may be assigned manually or automatically i.e., the assignment function(mapping) may be performed by learning mechanisms such as humans or machine learning models.
* Social entity in the definition refers to any unit data which is capable of being assigned the values in terms of the defined parameters, mathematically speaking, the data lies in the domain of the assignment function. Here entity may represent a comment or review. 
* Parameters can be Transparency, Utility, Consistency, Merit, Trust, Reputation etc.
* In a binary valued system the range of the assignment function for a given parameter is {0, 1}. 0 denoting not present and 1 denoting present. This is the system used in the examples. This may be called ‘tagging’, if the tag is present it is equivalent to value 1 else 0.

Thus we can calculate the net social currency associated with a product, a system or a decision based on the data as the tuple of the sum of the values of individual parameters of all the social entities associated with the object in consideration. The mapping of social entities to different objects is also done by people or models i.e a function is required.

The project is about adding the following functionalities into GrimoireLab for establishing a social currency metric system for an organization:
* A mechanism to collect relevant data from various sources.
* A mechanism to allow value assignment or tagging the data collected.
* A mechanism to view the results of tagging and see the trends.
 
#### Goals: 
The net social currency may be used as a metric input to make future decisions in the organisation. The goal is to achieve full utilization of the data that is available to us by milking out the social currency metrics from it and using it to make better decisions and develop better understanding. 

# About Me
I am a 2nd yr undergrad studying in IIITA. I love to learn new things. I am kind of lazy if I have not committed to things but If I have I tend to complete them fast and without fail. I am a Gold medalist in acads, so you may gauge my understanding capabilities from it. I am quick to learn and understand things without external intervention. Creativity is also one of the weapons in my arsenal. To be honest I am not that experienced in python, having experienced it for a year or so. But I think I am well over the skill requirement for the project with my level of experience and capability of quick learning. Please visit my github profile to explore my projects in python. During the last year I have done web scraping, data manipulations, game development, website development, and touched a little bit of ml enough to set up the basic pipeline for a classifier. I have worked extensively with various API’s as a web developer, even the Google and Twinword text analysis api. I was a mentor for OpenCode2020, a mini GSoC organized by my College. I am currently the head of web development department in the technical society of my college. Here is the link to my microtasks repository and Microtask-10 which contains the list of my contributions to CHAOSS. My plans after GSoC is to search for a proper internship and continue open source on the side. So I will contribute to CHAOSS even after GSoC. To be honest I selected CHAOSS on a whim, but stayed here due to the wonderful community and interesting projects. If I commit, I will finish it. The timeline will keep me on track. The genuine interest in this project will only enhance my focus by many folds. I believe we will finish the project goals before time and start working on stretch goals. The estimated time I can devote the project is 40 hrs/week. I may have my college during GSoC due to a probable shift in schedule due to the pandemic. But I will be able to squeeze more than enough time for the project. I hope we have a good coding period ahead.

Thank You

