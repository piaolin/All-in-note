#include<iostream>
#include<Windows.h>
#pragma comment(lib, "Urlmon")
using namespace std;

int main(_In_ int _Argc, _In_reads_(_Argc) _Pre_z_ char ** _Argv, _In_z_ char ** _Env)
{
	HRESULT Result;
	Result = URLDownloadToFileA(NULL, "https://the.earth.li/~sgtatham/putty/0.70/w64/putty.exe", "D:\\1.exe", 0, NULL);
	switch (Result)
	{
	case E_OUTOFMEMORY: //ÄÚ´æÒç³ö
		cout << "falut" << endl;
	case S_OK:
		cout << "successful" << endl;
	default:
		break;
	}
	system("pause");
	return 0;
}