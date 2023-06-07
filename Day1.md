# Day 1 Notes

## Training ChatGPT on your own data set
---

### Train ChatGPT On Your Data (Easy Method) 
https://youtu.be/y9Gi3UgNA3E

* CustomGPT.ai
* He makes a chatbot on all the info created on his website
* With custom GPT you can submit a sitemap and the bot will grab the content from the site and now it can answer questions about the site
* The bot can choose whether to work from your data or from chatGPT + your data
* Once its done reading your website it can answer any question about your site
* You can upload your own files to the website, PDF/DOC/ZIPS
* You can delete data after processing
* Can integrate within site with API key

---
### Use Open AI (ChatGPT) On Your Own Large Data -Part 1
https://youtu.be/eNKu307k59g

* Convert document to a word embedding
* Use Azure open AI studio
* word embedding - convert words to numerical values
    * uses cosine similarity and dot products to find similarity between phrases
* Azure OpenAI Embeddings Repo on GitHub
    * https://github.com/ruoccofabrizio/azure-open-ai-embeddings-qna
* Azure form recognizer is a service that can recognize text from PDF.
* Azure open-ai service creates word embeddings
* RediSearch used to cache data embeddings
* find out the closest word embedding to what the user has asked
* what is text for chosen word embedding? figure that out, and than let chatGPT or other openAI models to answer
* Answer can be provided from relevant information from word embeddings
* You can run on Azure
    * Or you can run locally on Docker
* you must have openAI on Azure
* you need form recognizer on Azure
* add translator for documents that are not in english
---
### Open AI+ Azure = Revolutionize the Way You Do Business
https://youtu.be/JXvSbu12VY4
* Watch this if you need some background on Azure and openAI
---
### Use ChatGPT On Your Own Large Data - Part 2
https://youtu.be/RcdqdWEYw2A
* this video shows you how to use Azure Cognitive search to index data, and use chatGPT to answer the question with the relevant information from your dataset
* Chat with your data essentially
* https://github.com/Azure-Samples/azure-search-openai-demo
    * this is repository for this application
* can answer questions with citation
* In this video, the presenter demonstrates how to use Azure Cognitive search to index and retrieve relevant information from your own structured or unstructured data. This allows for sophisticated questions to be asked using ChatGPT without token limit issues, using both images and tables. The video includes step-by-step instructions on how to create a web app and connect it to your data.
---
### Filmustage leverages AI to break down film scripts, create shooting schedules and more

https://techcrunch.com/2023/03/20/filmustage-leverages-ai-to-breakdown-film-scripts-create-shooting-schedules-and-more/

* this article explains how filmustage breaks down scripts and basically does a lot of line producer work.
---
### FILMUSTAGE
https://filmustage.com/

* this site is the site that breaks down scripts and gives you a scheduling service.
* It basically does what this tool is supposed to be doing
* It can't do budget estimation yet
---
Our only goal is to do budget estimation at the moment. To me it makes sense to first have the AI breakdown the script into props and such. and than breakdown scheduling for each scene. And only than can it be able to estimate a budget based on research!

Questions:
* is it possible for us to skip all this script breakdown stuff and get right to estimation?
* What is the proper way in which this tool should do this?
* Our biggest competitor is Filmustage, however while they are appealling to all movies we are appealing to independent developers
    * How can we use ScreenCrib to tailor specifically to independent developers to outdo the competition?
    * What do these developers need?
    * What do they not need?

