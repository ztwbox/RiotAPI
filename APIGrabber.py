#This tutorial was built by me, Farzain! You can ask me questions or troll me on Twitter (@farzatv)

#First we need to import requests. Installing this is a bit tricky. I included a step by step process on how to get requests in readme.txt which is included in the file along with this program.
import requests

def requestSummonerData(region, summonerName, APIKey):

    #Here is how I make my URL.  There are many ways to create these.
    
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    print (URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    #Here I return the JSON we just got.
    return response.json()

def requestRankedData(region, accountID, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/match/v3/matchlists/by-account/" + accountID + "/recent?api_key=" + APIKey
    print (URL)
    response = requests.get(URL)
    return response.json()
    

def main():
    print ("\nWhat up homie. Enter your region to get started")
    print ("Type in one of the following regions or else the program wont work correctly:\n")
    print ("NA or EUW (Note: You can add more regions by just changing up the URL!\n")

    #I first ask the user for three things, their region, summoner name, and API Key.
    #These are the only three things I need from them in order to get create my URL and grab their ID.

    region = 'na1'
    summonerName = 'ZTWbox'
    APIKey = 'RGAPI-8362cf43-ad7e-40f1-b0e2-e10365878e54'

    #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    responseJSON  = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON['accountId']
    accountID = str(ID)
    print (ID)
    responseJSON2 = requestRankedData(region, accountID, APIKey)
    print (responseJSON2)


#This starts my program!
if __name__ == "__main__":
    main()

