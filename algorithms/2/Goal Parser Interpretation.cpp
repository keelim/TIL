class Solution {
public:
    string interpret(string command) {
        stack<char> st;
        string result;
        for(auto ele : command){
            if(ele=='G'){
                result+=ele;
                continue;
            }

            if(ele=='('){
                st.push(ele);
                continue;
            }

            if(st.top()=='(' && ele == ')'){
                st.pop();
                result+='o';
                continue;
            }

            if(st.top()=='l'&& ele==')'){
                st.pop();
                st.pop();
                st.pop();
                result+='al';
                continue;
            }

            st.push(ele);
        }
    }

    string interpret(string command) {
        replace(command.begin(), command.end(), "()", "o");
        replace(command.begin(), command.end(), "(al)", "al");
        return command
    }
};