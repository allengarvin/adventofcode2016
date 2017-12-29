#include <stdio.h>

int answer(int initc) {
    int a = 0, c = initc, b = 0, d = 0;

    line0: a = 1;
    line1: b = 1;
    line2: d = 26;
    line3: if( c != 0 ) goto line5;
    line4: if( 1 != 0 ) goto line9;
    line5: c = 7;
    line6: d++;
    line7: c--;
    line8: if( c != 0 ) goto line6;
    line9: c = a;
    line10: a++;
    line11: b--;
    line12: if( b != 0 ) goto line10;
    line13: b = c;
    line14: d--;
    line15: if( d != 0 ) goto line9;
    line16: c = 18;
    line17: d = 11;
    line18: a++;
    line19: d--;
    line20: if( d != 0 ) goto line18;
    line21: c--;
    line22: if( c != 0 ) goto line17;
    return a;
}

int main() {
    printf("Answer 1: %d\n", answer(0));
    printf("Answer 2: %d\n", answer(1));
}
