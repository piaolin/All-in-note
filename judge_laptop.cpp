#include<Windows.h>
#include<iostream>
using namespace std;

int main()
{
	SYSTEM_POWER_STATUS a;
	GetSystemPowerStatus(&a);

	if (a.BatteryFlag == 128 || a.BatteryFlag == 255)
		cout << "����̨ʽ����" << endl;
	else
		cout << "���ǱʼǱ�" << endl;

	system("pause");
	return 0;
}