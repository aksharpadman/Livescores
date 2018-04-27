#code to acquire live IPL scores and generate applaud for fours and sixes
#!/usr/bin/env python
from pycricbuzz import Cricbuzz
import os 
import subprocess 
import json
#the pycricbuzz library is used to acquire the live scores
c = Cricbuzz()
matches = c.matches()
for match in matches:   
    diction = c.livescore(match['id'])
    if (diction['matchinfo']['id'] == '1'):#this line checks for the specific match using the appropriate id 
        #sum of sixes scored by the batsmen at the crease
        prev =  int(diction['batting']['batsman'][0]['six']) + int(diction['batting']['batsman'][1]['six'])
        #sum of fours scored by the batsman at the crease
        prev4_0 = int(diction['batting']['batsman'][0]['fours']) + int(diction['batting']['batsman'][1]['fours'])
        #the while loop executes until the match is over 
        while (diction['matchinfo']['mchstate'] == 'inprogress'):
            try:
                #the sum of the sixes scored by  the batsmen at the crease is calculated and if the sum increases by 1 ,sound is generated
                if (int(diction['batting']['batsman'][0]['six']) + int(diction['batting']['batsman'][1]['six']) == prev + 1 ):
                    {  
                        #print ("Sixer")
                        subprocess.Popen(['mpg123','-q', '/home/alarm/livescore/cheer.mp3'])

                    }
                #Sum of the fours scored by the batsmen at the crease and checked for increase by 1   
                elif (int(diction['batting']['batsman'][0]['fours']) + int(diction['batting']['batsman'][1]['fours']) == prev4_0 + 1 ):
                    
                    {    
                        #print('four')
                        subprocess.Popen(['mpg123', '-q', '/home/alarm/livescore/crowdapplause.mp3'])
                    }
                #update the sum of sixes
                prev = int(diction['batting']['batsman'][0]['six']) + int(diction['batting']['batsman'][1]['six'])
                #update the sum of fours
                prev4_0 = int(diction['batting']['batsman'][1]['fours']) + int(diction['batting']['batsman'][0]['fours'])
                print (prev ,prev4_0)
                diction = c.livescore(match['id'])   

            except IndexError:
                pass

