def findxidachhand(hand):
    max_limit = 28
    upper_limit = 21
    lower_limit = 16
    ranks = []
    possible_rank = []
    blackjack_ranking = {5: 'Magic Five', 4: 'Double Aces', 3: 'BlackJack', 2: 'Enough to check', 1: 'Not enough to check',0: 'Busted', -1: 'Outbursted'}
    
    for card in hand:
        if len(card) == 2:
            rank = card[0]
        elif len(card) == 3:
            rank = card[0:2]
        if rank == 'K' or rank == 'Q' or rank == 'J':
            rank = 10
        elif rank == 'A':
            rank = [1,10,11]

        ranks.append(rank)

        
    for i in range(len(ranks)):
        if type(ranks[i]) != str:
            continue
        if len(ranks[i]) <= 3:
            ranks[i] = int(ranks[i])
    
    #Double Aces
    if len(ranks) == 2:
        if ranks[0] == [1,10,11] and ranks[1] == [1,10,11]:
            possible_rank.append(4)
    #BlackJack
        elif (ranks[0] == [1,10,11] or ranks[1] == [1,10,11]) and (ranks[0] == 10 or ranks[1] == 10):
            possible_rank.append(3)

    total = 0
    if len(ranks) <= 5:
        if len(ranks) == 4 or len(ranks) == 5:
            for i in range(len(ranks)):
                if ranks[i] == [1,10,11]:
                    ranks[i] = 1 
                total += ranks[i]
                if total <= upper_limit and len(ranks) == 5:
                    possible_rank.append(5)
                elif upper_limit < total < max_limit:
                    possible_rank.append(0)
                elif total >= max_limit:
                    possible_rank.append(-1)
        
        elif len(ranks) < 4:
            for elem in ranks:
                if isinstance(elem, int):
                    total += elem
                elif isinstance(elem, list):
                    continue
                
            if [1,10,11] not in ranks:   
                if upper_limit >= total >= lower_limit:
                    possible_rank.append(2)
                
                elif total < lower_limit:
                    possible_rank.append(1)
                
                elif total >= max_limit:
                    possible_rank.append(-1)
                
                elif max_limit > total >= upper_limit:
                    possible_rank.append(0)
            
            elif ([1,10,11] in ranks) and (ranks.count([1,10,11]) < 2) and (ranks.count(10) == 0):
                for i in range(len(ranks)):
                    if ranks[i] == [1,10,11]:
                        if len(ranks) == 2:
                            if total >= 6:
                                ranks[i] = 11
                            elif total < 6:
                                ranks[i] = 1
                        elif len(ranks) == 3:
                            if total == 11:
                                ranks[i] = 10
                            elif 6 <= total <= 10:
                                ranks[i] = 11
                            elif total > 11 and total < 6:
                                ranks[i] = 1 
                total+=ranks[i]
        
                if total > upper_limit:
                    possible_rank.append(0)
                elif total > max_limit:
                    possible_rank.append(-1)
                elif total < lower_limit:
                    possible_rank.append(1)
                elif lower_limit <= total <= upper_limit:
                    possible_rank.append(2)
                    
    print(total) 
    ranks.sort(key=lambda x: x if isinstance(x, list) else [x])
    # print(ranks)  

    if not possible_rank:
        possible_rank.append(2)
    output1 = possible_rank
    output = blackjack_ranking[possible_rank[-1]]
    print(hand,output,output1)
    return output, total

if __name__ == '__main__':
    findxidachhand(['AS','3D','4C','5H','6S']) 
    findxidachhand(['AS','10D','KC','5H','6S']) 
    findxidachhand(['AS','5D','KC','5H','6S']) 
    findxidachhand(['AH','AD'])
    findxidachhand(['AD','KS']) 
    findxidachhand(['KS','AD']) 
    findxidachhand(['9H','10S']) 
    findxidachhand(['5H','8S','7C']) 
    findxidachhand(['KH','QS','8C']) 
    findxidachhand(['5D','10S']) 
    findxidachhand(['AD','5S']) 
    findxidachhand(['AD','5S', '6C']) 
    findxidachhand(['AD','5S', '5C']) 
    findxidachhand(['AD','5S', '5C','5S']) 
    findxidachhand(['KS','3H', 'AH','4D']) 
    findxidachhand(['KS','3H', 'AH','4D','2C'])
    findxidachhand(['KS','10D']) 
    findxidachhand(['10S','AD']) 
    findxidachhand(['AD','KS']) 
    findxidachhand(['KS','9H', 'AH','4D'])
    findxidachhand(['2S', '5D', '2H', '3S', '3H'])
    findxidachhand(['8S', 'AC'])
    
    
