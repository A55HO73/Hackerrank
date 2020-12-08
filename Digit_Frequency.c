#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char str[1001];
    scanf("%[^\n]%*c", str);
    int arr[10] = {0};
    for(int i = 0; i < strlen(str); i++){
        if(str[i] >= '0' && str[i] <= '9')
            arr[str[i] - '0']++;
    }
    for(int i = 0; i < 10; i++)
        printf("%d ", arr[i]);
    printf("\n");
    
    return 0;    

}
