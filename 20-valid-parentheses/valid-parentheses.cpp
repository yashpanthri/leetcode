class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (int i = 0; i<s.size(); ++i){
            char ch = s[i];
            if (ch == '('|| ch == '{'|| ch == '['){
                st.push(ch);
            }
            else {
                if(st.empty()){return false;}
                char check_ch = st.top();
                if((check_ch == '(' && ch == ')') || (check_ch == '[' && ch == ']') || (check_ch == '{' && ch == '}')){
                st.pop();}  
                else{
                    return false;
                    }
            }
        }
        return st.empty();
    }
};