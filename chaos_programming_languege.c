/*
这是一个语言的解释器
在::后输入一条语句按Enter键即可执行
这个语言有一个虚拟的map（一个数组，其中所有数初始值为0）和一个虚拟指针pointer


初始的时候这个指针指向map数组的第1个数

  0   1   <---下标
---------
| 0 | 0 |...
---------
  ↑


+就是让指针指向的数+1，-就是-1
::++-

  0   1   <---下标
---------
| 1 | 0 |...
---------
  ↑


>就是让指针向右移一位，<是向左移一位
::>+><+++

  0   1   <---下标
---------
| 1 | 4 |...
---------
      ↑



?会输出当前指针指向的数的下标和数的值，格式为：%d -> %d，用于debug
::?
1 -> 0


[]中的指令会一直循环直到指针指向的数的值为0就会退出但只退出一层循环，不会退出所有循环，相当于break


.会输出一个ASCII编码为当前指针指向的数的值的字符（有点绕口哈）


f回让你输入一个file的绝对路径，这个file里面是代码


您可以随便写注释，但注释中不能写这几个字符:<>?.[]-+f
否则就会当作代码（哭笑不得）
建议大家的注释前加上//因为之后还可能修复这个bug


示例
::++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
P
----------------------------------------------我是分割线-------------------------------------------------
::?>?
0 -> 0
1 -> 0
----------------------------------------------我是分割线-------------------------------------------------
::+>++++++<[++++++++>-<]<.
1
----------------------------------------------我是分割线-------------------------------------------------
::++++++++++>+>+>+[+++++++++<++++<+<->>>]>>>+++++++++++++.---.+++++++..+++.<+++.------------.>++++++++.--------.+++.------.--------.<<-.
hello, world
----------------------------------------------我是分割线-------------------------------------------------
::f
filepath>C:\Users\xxxxx\Desktop\hello.txt
hello, world
在这里hello.txt的内容是上一个例子里的代码


此语言借鉴了一个其他的语言（但并不完全相同），网址：https://fatiherikli.github.io/brainfuck-visualizer/
还有就是这个解释器没有报错和检查功能，我的实力不允许
*/
#include<stdio.h>
#define MAX 5000

int loop(char commend[], int* pointer, int* map)
{
    if (*(map + *pointer) == 0)
    {
        return 1;
    }
    int num = 0;
    int isOK = 0;
    while (commend[num] != '\0')
    {
        
        switch (commend[num])
        {
            case '<':{
                (*pointer)--;
                break;
            }
            case '>':{
                (*pointer)++;
                break;
            }
            case '+':{
                (*(map + *pointer))++;
                break;
            }
            case '-':{
                (*(map + *pointer))--;
                break;
            }
            case '.':{
                printf("%c", *(map + *pointer));
                break;
            }
            case '[':{
                char new_commend[MAX];
                int aboutthisnameihavenoidea = 0;
                for (int the_num = num+1;; the_num++)
                {
                    if(commend[the_num] == ']'){
                        new_commend[aboutthisnameihavenoidea] = '\0';
                        while(loop(new_commend, pointer, map) == 0)
                            ;
                        num += aboutthisnameihavenoidea;
                        num += 1;
                        break;
                    }else{
                        new_commend[aboutthisnameihavenoidea] = commend[the_num];
                        aboutthisnameihavenoidea++;
                    }
                }
                break;
            }
            case '?':{
                printf("%d -> %d\n", *pointer, *(map + *pointer));
                break;
            }
        }
        num++;
        if (*(map + *pointer) == 0)
        {
            isOK = 1;
            break;
        }
    }
    return isOK;
}

int main(){
    int map[1000];
    for (int i = 0; i < 1000; i++)
    {
        map[i] = 0;
    }
    int old_pointer = 0;
    while (1)
    {
        char commend[MAX];
        printf("::");
        scanf("%s", commend);
        int* pointer = &old_pointer;
        int num = 0;
        if (commend[0] == 'f')
        {
            char fpath[200];
            printf("filepath>");
            scanf("%s", &fpath);
            FILE* file = fopen(fpath, "r");
            int p = 0;
            while ((commend[p] = getc(file)) != EOF)
            {
                p++;
            }
            fclose(file);
            while (commend[num] != '\0')
            {
                switch (commend[num])
                {
                    case '<':{
                        (*pointer)--;
                        break;
                    }
                    case '>':{
                        (*pointer)++;
                        break;
                    }
                    case '+':{
                        (*(map + *pointer))++;
                        break;
                    }
                    case '-':{
                        (*(map + *pointer))--;
                        break;
                    }
                    case '.':{
                        printf("%c", *(map + *pointer));
                        break;
                    }
                    case '[':{
                        char new_commend[MAX];
                        int aboutthisnameihavenoidea = 0;
                        for (int the_num = num+1;; the_num++)
                        {
                            if(commend[the_num] == ']'){
                                new_commend[aboutthisnameihavenoidea] = '\0';
                                while(loop(new_commend, pointer, map) == 0)
                                    ;
                                num += aboutthisnameihavenoidea;
                                num += 1;
                                break;
                            }else{
                                new_commend[aboutthisnameihavenoidea] = commend[the_num];
                                aboutthisnameihavenoidea++;
                            }
                        }
                        break;
                    }
                    case '?':{
                        printf("%d -> %d\n", *pointer, *(map + *pointer));
                        break;
                    }
                }
                num++;
            }
        }
        else
            while (commend[num] != '\0')
            {
                switch (commend[num])
                {
                    case '<':{
                        (*pointer)--;
                        break;
                    }
                    case '>':{
                        (*pointer)++;
                        break;
                    }
                    case '+':{
                        (*(map + *pointer))++;
                        break;
                    }
                    case '-':{
                        (*(map + *pointer))--;
                        break;
                    }
                    case '.':{
                        printf("%c", *(map + *pointer));
                        break;
                    }
                    case '[':{
                        char new_commend[MAX];
                        int aboutthisnameihavenoidea = 0;
                        for (int the_num = num+1;; the_num++)
                        {
                            if(commend[the_num] == ']'){
                                new_commend[aboutthisnameihavenoidea] = '\0';
                                while(loop(new_commend, pointer, map) == 0)
                                    ;
                                num += aboutthisnameihavenoidea;
                                num += 1;
                                break;
                            }else{
                                new_commend[aboutthisnameihavenoidea] = commend[the_num];
                                aboutthisnameihavenoidea++;
                            }
                        }
                        break;
                    }
                    case '?':{
                        printf("%d -> %d\n", *pointer, *(map + *pointer));
                        break;
                    }
                }
                num++;
            }
    }
        //loop(commend, &pointer, map);
    return 0;
}