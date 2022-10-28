# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:27:16 2022

@author: elisr
"""

import random

def get_songs(filename):
    
    with open(filename) as f:
        data = f.read()  
    
    okay = data.split('#')
                
    song_titles = okay[::2]
    song_lyrics = okay[1::2]
    
    return song_titles, song_lyrics

def scramble(song_titles, song_lyrics, k, b):
    '''
    song_titles, song_lyrics: list
    k, b: int
    '''
    #pick random song
    N = len(song_titles)
    random_number = random.choice(range(0,N))
    ran_song = song_titles[random_number]
    ran_lyrics = song_lyrics[random_number]
    #pick random part of song
    word_list = ran_lyrics.split(" ")
    song_lenght = len(word_list)
    if song_lenght < k+1:
        k = song_lenght
        song_part = word_list
    else:
        start = random.choice(range(0, song_lenght - k))
        stop = start + k
        song_part = word_list[start:stop]
    
    song_part_copy = song_part.copy()
    #replace b random words with blank spaces
    b_list = random.choices(range(0,k), k = b)

    for b in b_list:
        song_part[b] = ' --- '
        
    return song_part, song_part_copy, ran_song



'''
what i have: 2 lists

want:
1 list of the removed words
1 list with words removed

need random numbers in range(0,k), non-repeating
'''
 
    
def the_game():
    #a point system might be added later :)
    #adjust to right degree of difficulity
    k = 20 # max number of words to be used
    b = 14 # number of blank spaces
    
    filename = 'folklore_lyrics.txt'
    #filename = 'evermore_lyrics.txt'
    #filename = 'lover_lyrics.txt'
    
    song_titles, song_lyrics = get_songs(filename)
    
    while True:
        song_part, song_part_copy, ran_song = scramble(song_titles, song_lyrics,k,b)
        print()
        print('*******************')
        print()
        print(' '.join(song_part))
        print()
        input('which words are missing?')
        print()
        print('*******************')
        print()
        print(' '.join(song_part_copy))
        print()
        input('what is the song title?')
        print()
        print('*******************')
        print()
        print(ran_song)
        print()
        new_round = input('new song? (yes or no)')
        if new_round == 'no':
            break
    print('Well done! (probably)')

#the_game()

