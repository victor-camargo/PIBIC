#include <stdio.h>




int main(void){

    unsigned char array[] ={1,2,3,4,5,6};
    unsigned char array2[] = *array;
    int i = 0;
    for(i = 0; i <7; i++){
    	printf("%d",array2[i]);
	}

    return 0;
}
