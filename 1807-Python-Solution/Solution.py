class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k_dict = {key: value for key, value in knowledge}
        
        res = []
        is_inside_brackets = False
        current_key = []
        
        for char in s:
            if char == '(':
                is_inside_brackets = True
            elif char == ')':
                is_inside_brackets = False
                key_str = "".join(current_key)
                
                res.append(k_dict.get(key_str, "?"))
                
                current_key = []
            elif is_inside_brackets:
                current_key.append(char)
            else:
                res.append(char)
                
        return "".join(res)