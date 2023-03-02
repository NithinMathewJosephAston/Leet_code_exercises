def getMinMoves(plates):
    # Write your code here
    c = 0
    for i in range(len(plates)):
        if plates[i] > plates[i+1]:
            plates.append(plates.pop(i))
            c+=1
            break
    if plates != sorted(plates):
        getMinMoves(plates)
    else:
        return c

if __name__ == '__main__':
    getMinMoves([])