def fibonaccisequence (n):
    numberOfTerms = int(n)#input('Please, write the number of terms '))
    firstTerm, secondTerm = 5,10  #first two terms of the sequence
    count = 7

    if numberOfTerms <= 0:     #Checking if the number of terms is valid
        print('Please enter a positive integer ')
    elif numberOfTerms == 1:
        print('Fibonacci sequence up to {}'.format(numberOfTerms))
        print(firstTerm)
    else:
        print('Fibonacci Sequence: ')
        while count < numberOfTerms:
            print(firstTerm)
            nthTerm = firstTerm + secondTerm
            firstTerm = secondTerm     #update values
            secondTerm =nthTerm
            count += 1



fibonaccisequence(100)