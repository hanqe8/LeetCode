class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        replaceDict = {0: 1, 1: 0}
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                image[i][j] = replaceDict[image[i][j]]
        return image
