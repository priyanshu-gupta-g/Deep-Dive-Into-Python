"""
Binary Types Module
=============================================================================
Contains examples and use cases for Bytes and Bytearray types.
=============================================================================
"""

def demonstrate_binary_types():
    print("\n\n[6] BINARY TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Bytes (bytes)
    # -------------------------------------------------------------------------
    # Use Cases: File I/O, Network Packets, Crypto.
    data_packet = b'\x00\xFF\xA5'
    message_bytes = b"Hello"
    
    print(f"Type: {type(data_packet)}")
    print(f"Examples: {data_packet}")
    print("Real-world Use: Image processing, Network sockets, Cryptography.")

    # -------------------------------------------------------------------------
    # B. Bytearray (bytearray)
    # -------------------------------------------------------------------------
    # Use Cases: Mutable buffers, Stream manipulation.
    mutable_buffer = bytearray(b"Hello")
    mutable_buffer[0] = 74 # 'J'
    
    print(f"\nType: {type(mutable_buffer)}")
    print(f"Examples: {mutable_buffer}")
    print("Real-world Use: Low-level buffering, Binary stream manipulation.")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the difference between `bytes` and `bytearray`?
    A1: `bytes` is immutable (cannot be changed), while `bytearray` is mutable 
        (can be modified in place).

    Q2: How do you convert a string to bytes?
    A2: Use the `.encode()` method on the string (e.g., `"hello".encode('utf-8')`) 
        or the `bytes()` constructor.

    Q3: Why are bytes important in Python?
    A3: They are essential for handling raw binary data, such as image files, 
        network packets, and during serialization/crypto operations where text 
        encodings can be ambiguous.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - BINARY")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_binary_types()
    interview_questions()
