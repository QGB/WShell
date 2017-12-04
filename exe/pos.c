#include <windows.h>
#include <malloc.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
#include <string.h>

void printLastError()
{
    int ic=GetLastError();
	HLOCAL LocalAddress=NULL;
	FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER|FORMAT_MESSAGE_IGNORE_INSERTS|FORMAT_MESSAGE_FROM_SYSTEM,
		NULL,ic,0,(PTSTR)&LocalAddress,0,NULL);
	printf("Error :[%i]  %s",ic, (LPSTR)LocalAddress);
}

typedef HWND (WINAPI *PROCGETCONSOLEWINDOW)();
PROCGETCONSOLEWINDOW GetConsoleWindow;

int main(int ai,char* *as){
    HMODULE hKernel32 = GetModuleHandle("kernel32");
    GetConsoleWindow = (PROCGETCONSOLEWINDOW)GetProcAddress(hKernel32,"GetConsoleWindow");
    HWND  wh=GetConsoleWindow();
    int ix=199,iy=-21;
    if(ai>1){
        ix=atoi(as[1]);
    }
    if(ai>2){
        iy=atoi(as[2]);
//        printf("%i\n",atoi(as[2]));
    }

    ShowWindow(wh,SW_SHOWMAXIMIZED);
    int ir=SetWindowPos(wh,HWND_TOP,ix,iy,555,555,SWP_NOSIZE);
//    printf("%i[%s]",ai,as[0]);

//    HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
//    char *ps="2222222";
//    DWORD chwritten;
//
//    WriteConsole(h, ps, 3, &chwritten, NULL);
//
//
//    printLastError();

//    CONSOLE_SCREEN_BUFFER_INFO screen_info;         //定义窗口缓冲区信息结构体
//    GetConsoleScreenBufferInfo(h, &screen_info);

//
//    for(int i=0;i<3999;i++){
//        printf("%i[%s]<br>",i,0x77c178ac+i);
//    }
//    system("pause");
//    return 2333;
}
