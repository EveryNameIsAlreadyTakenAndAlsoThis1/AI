Trieda DataHandler vyžaduje názov súboru ako parameter konštruktoru.  
Po vytvorení inštancie si pred začatím každej hry zavoláme funkciu startGame()  
V cykle hry je potrebné volať funkciu add(action,reward)  
Po skončení hry zavolať funkciu endGame(epsilon,learningRate)  
Po skončení tréningu/animácie zavolať funkciu saveToFile()  
V konštruktore triedy sa nachádza atribút writeCount ktorý určuje po koľkých hrách sa bude ukladať do súboru.  
Príklad použitia triedy je v súbore priklad.txt  
