def SearchHeightofDucks(self,node,StickHeight):
    countSame = 0   # count of ducks that are same height as the duck
    countGreater = 0  # count of ducks that are greater than the stick
    countLess = 0   # count of ducks that are less than the stick

    if(self.node == StickHeight):   # if duckHeight == stickheight the proceed to this if statement
        countSame+=1
        SearchHeightofDucks(SearchHeightofDucks(self.node.left))
        SearchHeightofDucks(SearchHeightofDucks(self.node.right))

    if(self.node > StickHeight):   # if duckHeight > stickheight the proceed to this if statement
        countGreater += 1
        SearchHeightofDucks(SearchHeightofDucks(self.node.left))

    if(self.node < StickHeight):   # if duckHeight < stickheight the proceed to this if statement
        countLess +=1
        SearchHeightofDucks(SearchHeightofDucks(self.node.right))
    return countGreater,countLess,countSame

           # the above Pseudo Code Implements a BST. The stickHeight will be compared to the nodes of the BST and based of the Equal,Greater,Less scenario, the individual counts will proceed.


# THis algo will take log n time as in a balanced BST the height is log n and the operations will be performed in log n time . 


    

