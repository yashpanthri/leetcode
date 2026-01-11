class Solution {
public:
    int reverse(int x) {
        int rn = 0;

        while (x != 0) {
            int d = x % 10;
            x /= 10;

            // Check overflow BEFORE doing rn = rn*10 + d
            if (rn > INT_MAX / 10 || (rn == INT_MAX / 10 && d > 7)) return 0;
            if (rn < INT_MIN / 10 || (rn == INT_MIN / 10 && d < -8)) return 0;

            rn = rn * 10 + d;
        }

        return rn;
    }
};
