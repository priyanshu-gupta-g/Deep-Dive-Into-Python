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
