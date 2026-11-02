// #include <stdio.h>
// void one(void);
// int main(void)
// {
//     float weight;
//     float value;

//     printf("Are you worth your weight in platinum?\n");
//     printf("Let's check it out.\n");
//     printf("Please enter your weight in pounds:");

//     scanf("%f", &weight);

//     value = 1700.0 * weight * 14.5833;
//     printf("YOur weight in platinum is worth $%.2f.\n", value);
//     printf("You are easily worth that! If platinum prices drop,\n");
//     printf("eat mor eto maintain your value.\n");

//     one();

//     return 0;
// }
// void one(void)
// {
//     int c = getchar();
//     int b = getchar();
//     printf("第一次输入：%d", c);
//     printf("第二次%d",b);
// }



// #include <stdio.h>
// int main(void)
// {
//     int ten = 10;
//     int two = 2;

//     printf("Doing it right :");
//     printf("%d minus %d is %d\n", ten, 2, ten - two);
//     printf("Doing it wrong:");
//     printf("%d minus %d is %d\n", ten);//只给一个参数，会随机打印出存储的数据

//     return 0;
// }



#include <stdio.h>
int main(void)
{
    int x = 100;

    printf("dec = %d; octal = %o; hex = %x\n", x, x, x);
    printf("dec = %d; octal = %#o; hex = %#x\n", x, x, x);

    return 0;
}