def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerbed_size = len(flowerbed)
        count = 0

        for i in range(0, flowerbed_size):
            if flowerbed[i] == 1:
                continue
            elif flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                flowerbed[0] = 1
            elif flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                count += 1
                flowerbed[i] = 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
            elif flowerbed[-1] == 0 and flowerbed [-1 - 1] == 0:
                count += 1
            else:
                continue


        if count >= n:
            return True
        

        return False
        
print(canPlaceFlowers([1,0,0,0,1], 1))