from  collections import defaultdict
import string 
import random


class UrlShortner: 
    urlDb= defaultdict() # two dictionaries, urldb to craete a lookup table for already hashed urls.
    HashedDb = defaultdict()
    
    def encodeUrl(self,longUrl, option):
        if not longUrl:
            return None

        if longUrl in self.urlDb:
            return self.urlDb[longUrl]

        if option == 1:
            # customize
            hash1= self.customizedInput() #added the customized option
            self.HashedDb[hash1]=longUrl
            self.urlDb[longUrl]=hash1 
            return hash1

        else: 
            #  print("going in")
            hash1=self.generateRandom(longUrl)
            #if hash is already present then generate random hash again
            while hash1 in self.HashedDb:
                hash1= self.generateRandom(longUrl)

            #indentation was incorrrect here it was inside the while loop and hence the None output
            self.HashedDb[hash1]=longUrl
            self.urlDb[longUrl]=hash1 
            return hash1

    def decodeUrl(self, shortUrl):
        if shortUrl in self.HashedDb:
            return self.HashedDb[shortUrl]
        return None

    def generateRandom(self, longUrl):
        letter = string.ascii_lowercase
        numbers= string.digits
        aplhabetchars= letter+numbers
        hashed_url_code= random.choice(aplhabetchars)
        return hashed_url_code

    def customizedInput(self):
        customized_word= input("Enter your shortened word u would like to use\n")
        return customized_word



b = UrlShortner()

encoded_url=b.encodeUrl("https://www.google1.com/", 0)
print("Enocded url is \n", encoded_url)
print(b.HashedDb)
print("After decoding \n", b.decodeUrl(encoded_url))

#customize option
encoded_url2=b.encodeUrl("https://www.google2.com/", 1)
print("Enocded url2 is \n", encoded_url2)
print(b.HashedDb)
print("After decoding \n", b.decodeUrl(encoded_url2))



