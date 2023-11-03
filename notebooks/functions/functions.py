def get_points(result:int) -> int:

    '''
    Info:
        This function recieve the match score and determine how many points correspond to the team. 
        3 - 1
        1 - 2
        0 - 0
    ------
    Input:
        result : result of the match [0,1,2] (type: str)
    ------
    Ouput:
        points : points according to the score (type: int)
    '''

    if result == 1:
        return 3
    elif result == 0:
        return 0
    else:
        return 1

def get_result(GF:int, GA:int) -> int:
    '''
    Info:
        This function recieve the amount of goals to determine the Result of the match. 
    ------
    Input:
        GF : Goals in favor (type: int)
        GA : Goals Against (type: int)
    ------
    Ouput:
        Result : [1,2,0] (type: int)
    '''

    if GF > GA:
        return 1
    elif GF < GA:
        return 0
    else:
        return 1