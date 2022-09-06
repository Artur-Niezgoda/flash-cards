# Flash Cards App

An application with GUI to help you learn words in foreign language. 
If you run the app for the first time, it loads a data from a csv file.
It should contain two columns: column_1 with words in the language
you want to learn, column_2 with words in your language with the language. 
The first row must contain names of the languages.

# 
When the app starts it displays randomly chosen word in the foreign language.
<p align="center" width="100%">
    <img width="33%" src="images/README/flash_card_front.png">
</p>
In order to see the translation you can click "Turn Over" button:

<p align="center" width="100%">
    <img width="33%" src="images/README/flash_card_back.png">
</p>

If you know this word, click green (tick symbol) button, otherwise click red 
(cross symbol) one. Whenever green button is clicked, the word removed from
the list of words to learn. When all the words have been displayed, the message is displayed and
the list containing words to learn is saved to a new file to_learn.csv. 

<p align="center" width="100%">
    <img width="33%" src="images/README/flash_card_end.png">
</p>

The next time the program is started
it will search for the file "to_learn.csv" to continue the learning process. If the file
cannot be found or it is empty, it will load the full database.
