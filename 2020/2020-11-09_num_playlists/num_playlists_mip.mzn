% Your music library contains N songs and your friend wants to listen to L
% songs during your road trip (repeats are allowed). Make a playlist so that
% every song is played at least once, and a song can only be played again only
% if K other songs have been played. Return the number of possible playlists.

int: N; % number of songs
int: L; % length of playlist
int: K; % minimum gap between plays of the same song

set of int: SONG = 1..N;
set of int: PLAY = 1..L;

array[PLAY] of var SONG: playlist;
array[PLAY, SONG] of var bool: plays;

% every slot contains exactly one song
constraint forall(p in PLAY)(sum(s in SONG)(plays[p, s]) = 1);

% every song is played at least once
constraint forall(s in SONG)(sum(p in PLAY)(plays[p, s]) > 0);

% there's a gap of at least K songs before a song is played again
constraint forall(s in SONG)(
  forall(p in 1..L)(sum(i in 0..min(K, L-p))(plays[p+i, s]) <= 1)
);

% output the playlist
constraint forall(p in PLAY)(playlist[p] = sum(s in SONG)(s * plays[p, s]));

% break symmetries
include "globals.mzn";
constraint seq_precede_chain(playlist);

solve satisfy;

output [ "playlist = \(playlist);\n" ]