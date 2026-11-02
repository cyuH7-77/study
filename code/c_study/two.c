// #include <stdio.h>
// void butler(void);
// int main(void)
// {
//     printf("I will summon the butler function.\n");
//     butler();
//     printf("Yes. Bring me some tea and writeable DVDs.\n");

//     return 0;
// }
// void butler(void)
// {
//     printf("You rang, sir?\n");
// } 



// #include <stdio.h>
// void br(void);
// void ic(void);
// int main(void)
// {
//     printf("BGrazil, Russia, India, China\n");
//     ic();
//     br();

//     return 0;
// }
// void ic(void)
// {
//     printf("India, China\n");
// }
// void br(void)
// {
//     printf("Brazil, Russia\n");
// }



#include <stdio.h>
void one_three(void);
void two(void);
int main(void)
{
    printf("starting now:\n");
    one_three();
    printf("done!\n");

    return 0;
}
void one_three(void)
{
    printf("one\n");
    two();
}
void two(void)
{
    printf("two\n");
    printf("three\n");
}