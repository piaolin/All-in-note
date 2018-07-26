#include<Windows.h>
#include<iostream>
using namespace std;

int main()
{
	SYSTEM_POWER_STATUS a;
	GetSystemPowerStatus(&a);

	if (a.BatteryFlag == 128 || a.BatteryFlag == 255)
		cout << "这是台式电脑" << endl;
	else
		cout << "这是笔记本" << endl;

	system("pause");
	return 0;
}