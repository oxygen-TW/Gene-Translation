#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

int main(int argc, char *argv[])
{
    if(argc != 3 && strcmp(argv[1],"-h") != 0)
    {
        cout <<"Error 41 -> 參數錯誤，可能遺漏或超過\n";
        exit(41);
    }

    if(strcmp(argv[1],"-m") == 0 || strcmp(argv[1],"-a") == 0 || strcmp(argv[1],"-ma") == 0)
    {
        string cmdt("python transcripter.py ");
        string cmdm(argv[1]);
        string cmdf(argv[2]);
        string cmd = cmdt+" "+cmdf;
        cout<<cmd<<endl;

        if(cmdm == "-m"){
            system(("python transcripter.py "+cmdf).c_str());
            return 0;
        }


        if(cmdm == "-a"){
            system(("python translater.py " + cmdf).c_str());
            return 0;
        }


        if(cmdm == "-ma"){
            system(("python transcripter.py "+cmdf).c_str());
            system(("python translater.py " + cmdf+".mrna").c_str());
            return 0;
        }
    }
    else if(strcmp(argv[1],"-h") == 0)
        cout<<"Gene-run.exe [-mode] [-filename]\nmode:\n -m 僅轉錄 \n -a 僅轉譯\n -ma 轉錄後轉譯\n";

    else
    {
        cout<<"Error 42 -> 參數錯誤，必須是 -m -a -ma\n Gene-run.exe [-mode] [-filename]\nmode:\n -m 僅轉錄 \n -a 僅轉譯\n -ma 轉錄後轉譯\n";
        exit(42);
    }
}
