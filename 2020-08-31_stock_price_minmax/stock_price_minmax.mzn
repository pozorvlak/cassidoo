% inputs
int: n;
set of int: DAY = 1..n;
array[DAY] of int: stock_price;

% decision variables
var DAY: buy;
var DAY: sell;

var int: profit = stock_price[sell] - stock_price[buy];
constraint buy < sell;

solve maximize profit;

output [ "buy on day \(buy), sell on day \(sell)" ];
