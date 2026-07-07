class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            length = str(len(word))
            encoded_string += length
            encoded_string += '#'
            encoded_string += word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 
            
            n = int(s[i:j])
            inicio = j + 1
            fin = inicio + n
            word = s[inicio: fin]
            decoded_string.append(word)

            i = fin

        return decoded_string

                    

