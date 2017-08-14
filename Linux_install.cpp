#include <cstdlib>
#include <cstdio>
int main()
{
    system("sudo mkdir \"/opt/Gene-Translation\"");
    //Copy files
    system("sudo copy Gene-run.exe \"/opt/Gene-Translation/\"");

    system("sudo copy transcripter.py \"/opt/Gene-Translation/\"");
    system("sudo copy translater.py \"/opt/Gene-Translation/\"");
    //Set EV
    //system("sudo alias Gene-run=/opt/Gene-Translation/Gene-run");
    //printf("copy Gene-run.exe  \"C:\\Program Files\\Gene-Translation\"");
    system("echo down!");
    return 0;
}
