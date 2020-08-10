% constants
set of int: DIGIT = 0..9;
set of int: BYTE = 0..255;

%inputs
int: n; % length of string
array[1..n] of DIGIT: s;

%outputs
array[1..4] of var BYTE: ip_address;

array[1..4] of var 1..n: start; % index of the first digit in each byte
constraint start[1] = 1;
array[1..4] of var 1..n: end;     % index of the last digit in each byte
constraint end[4] = n;
constraint forall(i in 1..3)(start[i+1] == end[i] + 1);
constraint forall(i in 1..3)(start[i] < start[i+1]);
% leading zeros are not allowed
constraint forall(i in 1..4)(s[start[i]] == 0 -> end[i] == start[i]);

constraint forall(i in 1..4)(
  sum([10^j * s[end[i] - j] | j in 0..(end[i] - start[i])]) == ip_address[i]
);

solve satisfy;

output [ join(".", [show(byte) | byte in ip_address]) ];