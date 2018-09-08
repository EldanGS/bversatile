#ifndef bit_manipulations_h
#define bit_manipulations_h

int leftShift(int x) {
    /* 
        multiple x by 2, which is means add 0 to last bit.
        
        1010 = 2^3 + 2^1 = 10 
        
        1010 << 1
        
        10100 = 2^4 + 2^2 = 20
    */
    return (x << 1);
}

int rightShift(int x) {
    /* 
        divide x by 2, which is means remove last bit.
        
        1011 = 2^3 + 2^1 + 2^0 = 11
        
        1011 >> 1
        
        0101 = 2^2 + 2^0 = 5
    */

    return (x >> 1);
}

bool getBit(int num, int i) {
    /*
        This method is shifts 1 over by i bits, creating a value that looks like 0001000.
        By performing an AND with num, we clear all bits other than the at bit i.

        num = 25 = 11001 = 2^4 + 2^3 + 2^0
        i = 3; (1 << i) = 2^3 = 8
        
        11001
        &
        01000
        =
        01000 = 1 = true
    */

    return (num & (1 << i));
}

int setBit(int num, int i) {
    /*
        setBit shifts 1 over by i bits, creating a value like 0001000.
        By performing an OR with num, only the vakue at bit i will change.

        num = 25 = 11001 = 2^4 + 2^3 + 2^0
        i = 2; (1 << i) = 2^2 = 4
        
        11001
        |
        00100
        =
        11101 = 2^4 + 2^3 + 2^2 + 2^0 = 29
    */

    return (num | (1 << i));
}

int clearBit(int num, int i) {
    /*
        This method operates in almost the reverse of setBit. 
        First, we create a number like 11101111 by creating the reverse of it (00010000) and negating it.
        Then, we perform an AND with num. This will clear the ith bit and leave the remainder unchanged;
        
        Example 1:
        num = 19 = 10011 = 2^4 + 2^1 + 2^0
        i = 2; (1 << i) = 2^2 = 4
        mask = ~(1 << i) = 11011

        10011 = num
        &
        11011 = mask
        =
        10011 = 19
        

        Example 2:
        num = 21 = 10101 = 2^4 + 2^2 + 2^0
        i = 2; (1 << i) = 2^2 = 4
        mask = ~(1 << i) = 11011
        
        10101 = num
        &
        11011 = mask
        =
        10001 = 17 = 2^4 + 2^2 + 2^0 - 2^2 = 21 - 4
    */

    int mask = ~(1 << i);
    return (num & mask);
}

int clearBitsMSBthroughtI(int num, int i) {
    /*
        Example:
        num = 15 = 1101 = 2^3 + 2^2 + 2^0
        i = 2; (1 << i) = 4 = 2^2  
        mask = (1 << i) - 1 = 4 - 1 = 3 = 0011 = 2^1 + 2^0

        1101
        &
        0011
        =
        0001 = 1
    */

    int mask = (1 << i) - 1;
    int (num & mask);
}

int clearBitsMSBthrought0(int num, int i) {
    /*
        Example:
        num = 15 = 1101 = 2^3 + 2^2 + 2^0
        i = 2; (1 << i) = 4 = 2^2  
        mask = (-1 << (i + 1)) = 1'1100

        1101
        &
        1100
        =
        1100 = 14 = 2^3 + 2^2
    */

    int mask = (-1 << (i + 1));
    int (num & mask);
}

int updateBit(int num, int i, bool bitIs1) {
    /*
        To set the ith bit to a value v, we first clear the bit at position i by using a mask that looks like 11101111.
        
        Then, we shift the intended value, v, left by i bits.
        This will create a number with bit i equal to v and all other bits equal to 0.

        Finally, we OR these two numbers, updating the ith bit if v is 1 and leaving it as 0 otherwise.
    */
    int value = bitIs1 ? 1 : 0;
    int mask = ~(1 << i);
    return (num & mask) | (value << i);
}

#endif