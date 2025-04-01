/*
 *  Write a function that takes an array of timestamps (HH:MM) from the same
 *  day and returns the longest gap in minutes between consecutive timestamps.
 *
 * Examples:
 *
 * findLongestTimeGap(['12:00'])
 * 0
 *
 * findLongestTimeGap(['09:00', '11:00'])
 * 120
 *
 * findLongestTimeGap(['14:00', '09:00', '15:00', '10:30'])
 * 210
 *
 * * findLongestTimeGap(['08:00', '10:00', '10:00', '14:00'])
 * 240
 */

#include <string>
#include <vector>
#include <cassert>

using namespace std;

int time_to_minute(string time)
{
        int gap = time.find(":");
        string hour = time.substr(0, gap);
        string minute = time.substr(gap + 1);
        return stoi(hour) * 60 + stoi(minute);
}

int find_longest_time_gap(vector<string> times)
{
        int last = -1;
        int max_diff = 0;
        for (string time : times) {
                int now = time_to_minute(time);
                if (last != -1) {
                        int diff = now - last;
                        if (diff > max_diff) {
                                max_diff = diff;
                        }
                }
                last = now;
        }
        return max_diff;
}

int main(int argc, char* argv[])
{
        assert(find_longest_time_gap({"12:00"}) == 0);
        assert(find_longest_time_gap({"09:00", "11:00"}) == 120);
        assert(find_longest_time_gap({"14:00", "09:00", "15:00", "10:30"}) ==  360);
        assert(find_longest_time_gap({"08:00", "10:00", "10:00", "14:00"}) == 240);
}
