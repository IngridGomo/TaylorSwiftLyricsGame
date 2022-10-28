# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:28:04 2022

@author: elisr
"""

#lyrics_game_vol2
#by using dictionaries?

#godta tegnsetting


import random
import re

def get_songs(filename):
    
    with open(filename) as f:
        data = f.read()  
    
    okay = data.split('#')
                
    song_titles = okay[::2]
    song_lyrics = okay[1::2]
    
    return song_titles, song_lyrics

def add_album(shelf, albumname, artist):
    filename = str(albumname)+ '_lyrics.txt'
    song_titles, song_lyrics = get_songs(filename)
    shelf[albumname] = {'artist': artist, 'song titles': song_titles, 'song lyrics' : song_lyrics }
    

def make_album_collection():
    '''
    more albums can be added, but make sure to save it like song title#song#song title#song osv
    the name of the file should be albumname_lyrics.txt
    save it in same folder
    '''
    shelf = {}
    add_album(shelf, 'folklore', 'Taylor Swift')
    add_album(shelf, 'evermore', 'Taylor Swift')
    #add_album(shelf, 'lover', 'Taylor Swift')
    add_album(shelf, '1989', 'Taylor Swift')
    add_album(shelf, 'red', 'Taylor Swift')
    
    return shelf

def pick_song(shelf):
    
    random_album = random.choice(list(shelf))
    album = shelf[random_album]
    
    song_titles = album['song titles']
    song_lyrics = album['song lyrics']
    artist = album['artist']
    
    N = len(song_titles)
    random_number = random.choice(range(0,N))
    ran_song = song_titles[random_number]
    ran_lyrics = song_lyrics[random_number]
    
    return ran_song, ran_lyrics, artist, random_album              

def scramble_song(song_lyrics, k, b):
    '''
    song_lyrics: long string
    k, b: int
    '''
    word_list = re.split(' |\n', song_lyrics)
    song_lenght = len(word_list)
    if song_lenght < k+1:
        k = song_lenght
        songpart = word_list
    else:
        start = random.choice(range(0, song_lenght - k))
        stop = start + k
        songpart = word_list[start:stop]
    
    original_songpart = songpart.copy()
    int_list = random.sample(range(0,k-1), b)
    int_list.sort()
    
    removed_words = []
    for i in int_list:
        removed_words.append(songpart[i])
        songpart[i] = ' --- '
    
    return original_songpart, songpart, removed_words

def clean_list(x):
    #x is a list with strings
    for i in range(len(x)):
        word = x[i]
        word = word.lower()
        word = ''.join(ch for ch in word if ch.isalnum())
        x[i] = word
    return x

def compare_words(word_guess, removed_words):
    points = 0
    word_guess_list = word_guess.split(" ")
    
    word_guess_list = clean_list(word_guess_list)
    removed_words = clean_list(removed_words)
    
    for word in word_guess_list:
        if word in removed_words:
            removed_words.remove(word)
            points += 1
    
    return points

def game_intro():
    print('Welcome to the Taylor Swift lyrics game!')
    print('...'*15)
    print('....'*3, 'Rules of the game', '...'*3)
    print('...'*15)
    print('You will get a random part of a song with random words deleted')
    print('Guess the missing words and the song')
    print('1 point for each right word, does not have to be in the right order')
    print('4 points for guessing the song before full lyrics is printed')
    print('2 points for guessing the song after revealed lyrics')
    print('...'*15)
    
   
    
def the_game():
    #a point system might be added later :)
    #adjust to right degree of difficulity
    k = 20 # max number of words to be used
    b = 12 # number of blank spaces

    shelf = make_album_collection()
    game_intro()
    
    points = 0
    rounds = 0
    while True:
        rounds += 1
        
        ran_song, ran_lyrics, artist, random_album = pick_song(shelf)
        original_songpart, songpart, removed_words = scramble_song(ran_lyrics, k, b)
        print()
        print('***'*5, 'ROUND ', rounds, '***'*5)
        print()
        print(' '.join(songpart))
        print()
        word_guess = str(input('Which words are missing? Write them down with a space between, then press enter. '))
        word_points = compare_words(word_guess, removed_words)
        points += word_points
        print()
        print('*******************'*2)
        print()
        guessed_song = str(input('What is the song title? '))
        print()
        if guessed_song.lower() == ran_song.lower():
            points += 4
            print('Correct!')
            guess_again = False

        else:
            guess_again = True
            print('False (or you wrote it wrong), try again with more words')

        
        print()
        print('...'*10)
        print(' '.join(original_songpart))
        print('...'*10)
        #print('\n', ' '.join(removed_words))
        print()
        print('\n You got ', word_points, ' words correct')
        if guess_again == True:
            guessed_song = str(input(' \n what is the song title?'))
            if guessed_song == ran_song:
                points += 2
                print()
                print('Correct!')
            else:
                print()
                print('False, the song was  ', ran_song)
            
        print()
        print('*******************'*2)
        print()
        new_round = input('new song? (yes or no)')
        print()
        if new_round == 'no':
            print('Well done! You got ', points, ' points in ', rounds, ' rounds.')
            print('Average: ', str(round(points/rounds, 2)))
            break


the_game()







