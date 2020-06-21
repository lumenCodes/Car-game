def fibbonaccisequence (n):
    numberOfTerms = int(n)#input('Please, write the number of terms '))
    firstTerm, secondTerm = 5,6  #first two terms of the sequence
    count = 1

    if numberOfTerms <= 0:     #Checking if the number of terms is valid
        print('Please enter a positive integer ')
    elif numberOfTerms == 1:
        print('Fibbonacci sequence up to {}'.format(numberOfTerms))
        print(firstTerm)
    else:
        print('Fibbonacci Sequence: ')
        while count < numberOfTerms:
            print(firstTerm)
            nthTerm = firstTerm + secondTerm
            firstTerm = secondTerm     #update values
            secondTerm = nthTerm
            count += 1


fibbonaccisequence(8)