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
array[SONG] of var set of PLAY: plays;

include "globals.mzn";
constraint int_set_channel(playlist, plays);

% every song is played at least once
constraint forall(s in SONG)(card(plays[s]) > 0);

% there's a gap of at least K songs before a song is played again
constraint forall(s in SONG)(
  let { var set of PLAY: ps = plays[s]; } in
  forall(p1 in ps, p2 in ps)(
    p1 == p2 \/ abs(p1 - p2) > K
  )
);

solve satisfy;

output [];