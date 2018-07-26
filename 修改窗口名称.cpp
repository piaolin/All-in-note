#include<iostream>
#include<Windows.h>
using namespace std;

int main()
{
	HWND Win = FindWindowA(NULL, "PuTTY Configuration");
	SetWindowTextA(Win, "∆Æ¡„¥Ûµ€");
	FreeConsole();
	return 0;
}