import copy


set1 = {1,2}
set2 = {2,1}

set3 = copy.deepcopy(set1)

print(set1==set3)

set3.add(6)

print(set1==set3)
print(set1)

# #if count == 0 then there are no any mines
        # if count == 0:
        #     for neigbhor in neigbhors:
        #         if neigbhor not in self.moves_made:
        #             self.mark_safe(neigbhor)
                    
        # else:
        #     visitedAmoungNeigbhors = set()
        #     for neigbhor in neigbhors:
        #         if neigbhor in self.moves_made and neigbhor in self.safes:
        #             visitedAmoungNeigbhors.add(neigbhor)       

        #     nonVisitedAmoungNeigbhors = neigbhors - visitedAmoungNeigbhors

        #     #if count == cells then all cells are mines
        #     if count==len(nonVisitedAmoungNeigbhors):
        #         for nonVisitedAmoungNeigbhor in nonVisitedAmoungNeigbhors:
        #             self.mark_mine(nonVisitedAmoungNeigbhors)
        #     else:
        #         newSentence = Sentence(nonVisitedAmoungNeigbhors,count)
        #         self.knowledge.append(newSentence)

        #4) mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        