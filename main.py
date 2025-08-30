# main.py
from regex_lexer import RegexLexer
from state_lexer import StateMachineLexer

def test_lexer(lexer, name, code):
    print(f"\n{'='*50}")
    print(f"{name} LEXER OUTPUT")
    print(f"{'='*50}")
    
    try:
        tokens = lexer.tokenize()
        for i, token in enumerate(tokens):
            print(f"{i:2d}: {token}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

def main():
    # Sample code to test
    sample_code = """
fn int my_fn(int x, float y) {
    string my_str = "hmm";
    bool my_bool = x == 40;
    return x;
}

// This is a comment
if (x <= 50 && y != 0) {
    float result = x / 2.5;
    string escaped = "Hello\\nWorld\\t!";
}
"""

    # Test with additional Unicode characters (bonus)
    unicode_code = """
fn string greet(string name) {
    return "Hello " + name + "! 👋";
}

int 变量 = 42;  // Chinese variable name
string 🎉 = "celebration";  // Emoji variable
"""

    print("Testing with sample code:")
    print(sample_code)
    
    # Test both lexers
    test_lexer(RegexLexer(sample_code), "REGEX", sample_code)
    test_lexer(StateMachineLexer(sample_code), "STATE MACHINE", sample_code)
    
    print("\n\nTesting with Unicode code (bonus):")
    print(unicode_code)
    
    test_lexer(RegexLexer(unicode_code), "REGEX UNICODE", unicode_code)
    test_lexer(StateMachineLexer(unicode_code), "STATE MACHINE UNICODE", unicode_code)

if __name__ == "__main__":
    main()