#include <cstdlib>
int main()
{
    system("mkdir \"C:\\Program Files\\Gene-Translation\"");
    //Copy files
    system("copy Gene-run.exe \"C:\\Program Files\\Gene-Translation\"");

    system("copy transcripter.py \"C:\\Program Files\\Gene-Translation\"");
    system("copy translater.py \"C:\\Program Files\\Gene-Translation\"");
    //Set EV
    system("set Gene-run=C:\\Program Files\\Gene-Translation\\Gene-run.exe");
   
    system("pause");
    return 0;
}
