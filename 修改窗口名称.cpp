#include<iostream>
#include<Windows.h>
using namespace std;

int main()
{
	HWND Win = FindWindowA(NULL, "PuTTY Configuration");
	SetWindowTextA(Win, "Ʈ����");
	FreeConsole();
	return 0;
}