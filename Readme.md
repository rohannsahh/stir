## Assignment completion for Stir internship  
   project demonstartion video: https://drive.google.com/file/d/1WEm1aJntFoTnCyJ0HxsOJaJuM8poATur/view?usp=sharing    
       
# Task to scrape twitter trends from twitter home page using selenium and proxymesh  
  
# steps to run project locally  
1. ```bash  
      git clone https://github.com/rohannsahh/stir.git  
      cd stir  
  
2.  Prerequisites-  
    Python,  Chrome, ChromeDriver, MongoDB(local or atlas), pip  
    Configure proxymesh account and update proxy in edit proxies section from dashboard  
    ```bash   
       python proxy.py  # it creates zip file for chrome extension for setting up proxy in selenium   
        
3. create a virtual environment  
   ```bash  
      python -m venv venv  
      source venv/bin/activate  # For Linux/Mac  
      venv\Scripts\activate        
  
3. ```bash  
      pip install -r requirements.txt  

4. create .env file refer .env.example   
  
5. update chrome driver path  
    ```bash  
       service = Service("path/to/chromedriver")  

6.  use this command to run trends.py file  
    ```bash  
       python trends.py  

7. use this command to access webpage in browser  
   using flask at http://127.0.0.1:5000/  
   ```bash  
      python app.py   

# About me   
My name is Rohan kumar . I am final year Btech IT undergrad at Bhartividyapeeth college of engineering. This is my submission for sde intern task .It scrapes the top 5 trending topics from twitter's home web page ,properly login's , scrapes and save the data in mongodb database. It is built exactly as mentioned in the task uses selenium for scraping , proxymesh for rotating ip address and mongodb as database.    
  
Prior experience:    
  
frontend intern @Jm tech pvt ltd. https://github.com/rohannsahh/frontendui     
worked on travelled based startup serving people travelling to europe for visa services . Built the whole frontend for the product from scratch to payment intergration. Proper error handling , state management to make product robust.      
full stack intern @Digital guruji www.ai4chat.co worked on a Ai startup working on automating workflow integration with zapier and other ai tools.    
Apart from that i worked as a freelancer for various dev projects including some beautiful frontend focussed websites    
  
Front-End: React, Redux, Next.js    
Back-End: Node.js, Express.js, Prisma, Django, flask    
Databases: MongoDB, PostgreSQL, MySQL, Redis    
Others: WebRTC, socket.io, AWS, Docker, ML algorithms      
Resume: https://drive.google.com/file/d/1C8wU22R9C7Ib9gLkQNle-B-uSb06gmKf/view?usp=sharing
Availability - Immediately available to join from 1jan /onsite/hybrid/remote  
rohannsahh@gmail.com  
  
  