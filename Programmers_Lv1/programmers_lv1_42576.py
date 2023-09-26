def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for parti, comp in zip(participant, completion): 
        if parti != comp:
            return parti
        
    return participant[-1]