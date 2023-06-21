# Day 4 Notes

## Alternative Way of Breaking Down A Script

### Lets use Python!

New method:
* Get a movie script
    * This can be a movie script of any length
* Seperate it into scenes (this can be in the 1/8 method or just scene by scene)
    * Scenes in a movie script are usually identified by a new slugline, which includes the location and time of day. For example, "INT. COFFEE SHOP - DAY" would indicate a new scene taking place inside a coffee shop during the day.
* Use Python to seperate these scenes into string objects
    * Pseudo:
        * instantiate empty list # this will be used to hold 
        all the different scenes 
        * instantiate empty int # this will be used to hold the overall budget value
        * instantiate empty hashmap # this will hold the scenes and the budget value of each scene
        * while EOD of script hasn't been reached:
            * start string at beginning of "INT. COFFEE SHOP - DAY" and end string before "INT. COFFEE SHOP - NIGHT"
            * list.append(string)
        ### *Now you have all the scenes in a string object*
        * for scene in string:
            * ask chatGPT "what is the budget for ***$scene***" 
            * print(budget for scene)
            * hashmap.append(***scene***, ***budget***)
            * int += budget for scene

        * return int
* this function will than give you the budget for each scene by seperating the script scene by scene, than prompting chatGPT for each scene what the budget will be.

* Problems with this function: 
    * ChatGPT will not account for repeat objects that were already previously calculated in the last scene
        * Ex. a scene will mention an antique knife so chatGPT will put that in the budget for the scene. The antique knife comes up again in another scene. This will screw with the overall budget because the knife was already added to the budget in the previous scene
            * can be solved if chatGPT has some historical memory of objects its already accounted for
    * Sometimes theres information outside of the scenes in this case things could not be accounted for their.
        * maybe not though

Now for the rest of the budget thinks that can be added seperately. 
* Maybe lets have a form, once its filled in with information like for example, hourly rates for security, and more like salary info for people that would make this part be able to prompt chatGPT for calculations based on the given info.

---
### Adrien-Luxey/Da-Fonky-Movie-Script-Parser
https://github.com/Adrien-Luxey/Da-Fonky-Movie-Script-Parser/tree/master

* this repo parses movie scripts into scenes. It gets the movie from IDMB though




