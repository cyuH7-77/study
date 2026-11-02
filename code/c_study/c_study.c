// #include <stdio.h>

// int main()
// {
//     // printf("是否可以打中文\n");
//     printf("112+434=%d", 112+434);

//     return 0;
// } 


// #include <stdio.h>

// int main()
// {
//     int AMOUNT = 0;
//     int price = 0;

//     printf("请输入金额（元）");
//     scanf("%d", &price);

//     printf("请输入支付的面额（元）");
//     scanf("%d", &AMOUNT);

//     int change = AMOUNT - price;

//     printf("找您%d元\n", change);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int a = 0;
//     int b = 0;

//     scanf("%d%d\n", &a,&b);

//     printf("%d %d\n", a, b);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int a,b,c;
//     a = 1;
//     b = 2;
//     while(b <= 5){
//         a=a*b;
//         b=b+1;
//     }
//     printf("%d",a);
//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int a,b;
//     printf("请输入两个数字：");
//     scanf("%d %d",&a,&b);
//     printf("%d+%d=%d",a,b,a+b);
//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     printf("请分别输入身高的英尺和英寸，如输入\"5 7\"表示5英尺7英寸：");

//     double foot;
//     double inch;
//     scanf("%lf %lf", &foot, &inch);

//     printf("身高是%f米。\n", ((foot + inch / 12.0) * 0.3048));

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     printf("%d\n", 10 / 3);
//     printf("%f\n", 10 / 3.0);
//     printf("%f\n", 10.0 / 3);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     printf("十进制：%d\n", 100);
//     printf("八进制：%o\n", 100);
//     printf("十六进制：%x\n", 100);

//     return 0;
// }



// #include <stdio.h>

// int main()
// {
//     int a = 5;
//     int b = 6;
//     int t;

//     t = a;
//     a = b;
//     b = t;

//     printf("a=%d, b=%d\n", a, b);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int total = 10;
//     int sum = 3;

//     total += 5;
//     printf("%d\n", total);

//     total *= sum + 12;
//     printf("%d\n", total);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int a = 10;

//     printf("%d\n", a++);
//     printf("%d\n", a);
//     printf("%d\n", ++a);
//     printf("%d\n", a);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int hour1, minute1;
//     int hour2, minute2;

//     scanf("%d %d", &hour1, &minute1);
//     scanf("%d %d", &hour2, &minute2);

//     int t1 = hour1 * 60 + minute1;
//     int t2 = hour2 * 60 + minute2;
//     int t = t2 - t1;

//     printf("时间差是%d小时%d分。\n", t / 60, t % 60);

//     return 0;
// }



// #include <stdio.h>

// int main()
// {
//     int price = 0;
//     int bill = 0;

//     printf("请输入金额（元）：");
//     scanf("%d", &price);
//     printf("请输入票面（元）：");
//     scanf("%d", &bill);

//     if (bill >= price) {
//         printf("应该找您%d元。\n", bill - price);
//     } else {
//         printf("您的钱不够。\n");
//     }

//     return 0;
// }



// #include <stdio.h>

// int main()
// {
//     int grade = 0;
//     scanf("%d", &grade);

//     if (grade >= 60) {
//         printf("及格\n");
//     } else {
//         printf("不及格\n");
//     }

//     return 0;
// }



// #include <stdio.h>

// int main()
// {
//     int a = 0, b = 0;
//     int max = 0;

//     scanf("%d %d", &a, &b);

//     if (a > b) {
//         max = a;
//     } else {
//         max = b;
//     }

//     printf("较大的数是%d\n", max);

//     return 0;
// }



// #include <stdio.h>

// int main()
// {
//     int x;
//     int n = 0;

//     scanf("%d", &x);

//     n++;
//     x /= 10;

//     while (x > 0) {
//         n++;
//         x /= 10;
//     }

//     printf("%d\n", n);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int x;
//     scanf("%d", &x);

//     int n = 0;
//     do {
//         x /= 10;
//         n++;
//     } while (x > 0);

//     printf("%d", n);

//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int n = 5;
//     int fact = 1;

//     for (int i = 2; i <= n; i++) {
//         fact *= i;
//     }

//     printf("%d\n", fact);

//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int u = 32;
//     int v = 26;
//     while(v!=0){
//         int temp = u%v;
//         u = v;
//         v = temp;
//     }
//     printf("%d",u);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int a=2;
//     int b=20-6;
//     int c=0;
//     while(a*c!=b){
//         c=c+1;
//     }
//     printf("%d",c);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     printf("请分别输入身高的英尺和英寸");
//     int foot;
//     int inch;

//     scanf("%d %d", &foot, &inch);

//     printf("身高是%f米。\n",
//             ((foot + inch / 12.0)* 0.3048));
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int hour1, minute1;
//     int hour2, minute2;

//     scanf("%d %d", &hour1, &minute1);
//     scanf("%d %d", &hour2, &minute2);

//     int t1 = hour1 * 60 + minute1;
//     int t2 = hour2 * 60 + minute2;

//     int t = t2-t1;
//     printf("时间差是%d小时%d分/", t/60, t%60);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int a,b;
//     scanf("%d %d", &a, &b);
//     double c = (a+b)/2.0;
//     printf("%d和%d的平均值=%f\n", a, b, c);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int a = 5;
//     int b = 6;
//     int t;
//     t=a;
//     a=b;
//     b=t;
//     printf("a=%d,b=%d\n",a,b);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     printf("%d\n",5==3);
//     printf("%d\n",5>3);
//     printf("%d\n",5<=3);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     const int MINOR = 35;

//     int age = 0;

//     printf("请输入你的年龄：");
//     scanf("%d", &age);

//     printf("你的年龄是%d岁。\n", age);

//     if (age < MINOR){
//         printf("年轻是美好的，");
//     }
//     printf("年龄决定了你的精神世界，好好珍惜把。\n");
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int a,b;
//     printf("请输入两个整数：");
//     scanf("%d %d",&a, &b);
//     int max = 0;
//     if (a>b){
//         max = a;
//     }
//     if (b > a){
//         max = b;
//     }
//     printf("大的那个是%d\n", max);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     const double RATE = 8.25;
//     const int STANDARD = 40;
//     double pay = 0.0;
//     int hours;

//     printf("请输入工作的小时数：");
//     scanf("%d",&hours);
//     printf("\n");
//     if (hours > STANDARD)
//         pay = STANDARD * RATE +(hours-STANDARD) * (RATE * 1.5);
//     else
//         pay = hours * RATE;
//     printf("应付工资：%f\n", pay);
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     const int PASS=60;
//     int score;
//     printf("请输入成绩：");
//     scanf("%d", &score);
//     printf("你输入的成绩是%d.\n", score);
//     if (score < PASS){
//         printf("恨意含，这个成绩没有及格。");
//     }
//     else{
//         printf("祝贺你，这个成绩及格了。");
//     }
//     printf("再见\n");
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int x;
//     scanf("%d", &x);
//     int f=0;
//     if (x < 0){
//         f = -1;
//     }else if (x == 0){
//         f = 0;
//     }else {
//         f = 2*x;
//     }
//     printf("%d", f);
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int type;
//     scanf("%d",&type);
    // if (type==1)
    //     printf("你好");
    // else if (type==2)
    //     printf("早上好");
    // else if (type==3)
    //     printf("晚上好");
    // else if (type=4)
    //     printf("再见");
    // else
    //     printf("啊，什么啊？");

//     switch(type){
//         case 1:
//           printf("你好");
//           break;
//         case 2:
//           printf("早上好");
//           break;
//         case 3:
//           printf("晚上好");
//           break;
//         case 4:
//           printf("再见");
//           break;
//         default:
//           printf("啊，什么啊？");
//     }
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int x;
//     int n =1;
//     scanf("%d", &x);
//     if (x > 999){
//         n = 4;
//     }else if (x > 99){
//         n = 3;
//     }else if (x > 9){
//         n = 2;
//     }
//     printf("%d\n", n);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int x;
//     int n = 0;
//     scanf("%d", &x);
//     n++;
//     x /= 10;
//     while (x > 0){
//         n++;
//         x /= 10;
//     }
//     printf("%d\n", n);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int x;
//     int ret = 0;
//     scanf("%d", &x);
//     int t = x;
//     while ( x>1){
//         x /= 2;
//         ret ++;
//     }
//     printf("log2 of %d is %d.", t, ret);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int count =100;
//     while ( count>=0 ){
//           printf("%d\n", count);
//           count --;
//     }
//     printf("发射！\n");
//     return 0;
// }


// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int a = rand();
//     printf("%d\n", a%100);
//     return 0;
// }


// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// int main()
// {
//     srand(time(0));
//     int number = rand()%100+1;
//     int count = 0;
//     int a = 0;
//     printf("ok,you can begin.");
//     do {
//         printf("ok,begin.");
//         scanf("%d", &a);
//         count ++;
//         if (a > number){
//             printf("is so big");
//         }else if (a < number){
//             printf("is so small");
//         }
//     }while (a != number);
//     printf("so good, you are right, you take %d time", count);
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int x;
//     x = 12345;
//     int digit;
//     int ret = 0;
//     while (x> 0){
//         digit = x%10;
//         ret = ret*10 + digit;
//         printf("x%d,digit=%d,ret=%d\n", x, digit, ret);
//         x /= 10;
//     }
//     printf("%d", ret);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int n;

//     scanf("%d", &n);
//     int fact = 1;

//     int i = 1;
//     for (i=1; i <=n; i++ ){
//         fact *= i;
//     }

//     printf("%d!=%d\n", n, fact);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int x;
//     scanf("%d", &x);
//     int i; 
//     int isPrime = 1;
//     for (i=2; i<x;i++){
//         if (x % i == 0){
//             printf("不是素数\n");
//         }
//     }
//     if (isPrime == 1){
//         printf("是素数\n");
//     } else {
//         printf("不是素数\n");
//     }
//     return 0;
   
// }


// #include <stdio.h>
// int main()
// {
//     int n;
//     int i;
//     double sum = 0.0;
//     double sign = 1.0;

//     scanf("%d", &n);
//     for ( i = 1; i<=n; i++);{
//         sum += sign/i;
//         sign = -sign;
//     }
//     printf("f(%d)=%f\n", n, sum);

//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int x;
//     // scanf("%d", &x);
//     x = 13425;
//     do {
//         int d = x % 10;
//         printf("%d", d);
//         if (x > 9){
//             printf(" ");
//         }
//         x /= 10;
//     }while (x > 0);
//     printf("\n");
//     return 0;
// }

// #include <stdio.h>
// int main() {
//     int n=5;
//     for (int i = 1;i<=n;i++){
//         for (int j=0;j<n-i;j++) printf(" ");
//         for (int j = 1; j<=i; j++) printf("%d", j);
//         for (int j = i - 1; j>=1; j--)printf("%d", j);
//         printf("\n");
//     }
//     return 0;
// }



// #include <stdio.h>

// void cheer()
// {
//     printf("c\heer\n");
// }

// int main()
// {
//     // cheer();


//     char str[]="hello world";
//     char a="hello world,i am a student";
//     printf("%s\n", str);
//     printf("%s\n", a);
//     return 0;

    
// // }


// #include <stdio.h>
// int main()
// {
//     // int n;
//     // scanf("%d", &n);
//     // int fact = 1;

//     // int i = 1;
//     // for (i=1; i<=n; i++ ){
//     //     fact *= i;
//     // }
//     // printf("%d!=%d\n", n, fact);
//     // return 0;

//     int a;
//     int b;
//     printf("please input two numbers:");    


//     // int i=0;
//     // int p;
//     // p=(int)(&i);
//     // printf("0x%x\n",p);

//     // scanf("%d",&i);

// }


// #include <stdio.h>
// int main(void)
// {
//     int i = 0;
//     int p;
//     p = &i;
//     printf("0x%c\n", p);
//     printf("%p\n", &i);
//     printf("%lu\n", sizeof(int));
//     printf("%lu\n", sizeof(&i));

//     return 0;  
// }


// #include <stdio.h>
// int main(void)
// {
//     int i = 0;
//     int p;
//     printf("%p\n", &i);
//     printf("%p\n", &p);

//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int a;
//     int *p = &a;
//     printf("请输入一个整数");
//     scanf("%d",p);
//     printf("%d\n", *p);
//     return 0;
// }



// #include <stdio.h>
// int main() 
// {
//     int a = 3, b = 5;
//     int *p1 = &a, *p2 = &b;
//     printf("a=%d, b=%d\n", a, b);
//     int t = *p1;   
//     *p1 = *p2;     
//     *p2 = t;      
//     printf("a=%d, b=%d\n", a, b);
//     return 0;
// }



// #include <stdio.h>
// int main()
// {
//     int a[5] = {1,2,3,4,5};
//     int *p;
//     for (p = a; p < a + 5; p++) {
//         printf("%d ", *p);
//     }
//     printf("\n");
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     char str[] = "fheiuhfefhu";
//     char *p = str;
//     int count = 0;
//      while (*p != '\0') { 
//         count++;
//         p++;              
//     }
//     printf("%d", count);
// }


// #include <stdio.h>
// int main(void)
// {
//     int feet, fathoms;

//     fathoms = 2;
//     feet = 6 * fathoms;
//     printf("There are %d feet in %d fathoms!\n", feet, fathoms);
//     printf("Yes, I said %d feet!\n", 6 * fathoms);

//     return 0;
// }



